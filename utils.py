import time
import os
import json
import random
import requests
import ssl
from typing import Optional
import openai
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


"""
Utility functions
"""




def LabelExtracter(response, **kwargs) ->int:
    """
    Extract the label from the response.
    For isSimpleAns=True(Zeroshot), models answer only contains true or false.
    For other cases, models answer contains more information,
    but the final paragraph is "Final Answer: True" or "Final Answer: False".

    Parameters
    ----------
    response : str, model's answer.
    kwargs : dict, additional parameters
    - answer_form: str. `bool` or `mcq`

    Return
    ------
    label : int, 1=True and 0=False.
    If could not determinte the label, return the response itself for manual evaluation.

    """

    answer_form = kwargs.get("answer_form", "bool")

    #Note: response=null if request failed
    if not response or not isinstance(response, str):
        return "Request failed. Null string is recived. Exclude this data sample."

    # Get the last non-empty line, converting to lowercase
    lines = [line.strip() for line in response.lower().split('\n') if line.strip()]
    if not lines:
        return "Request failed. Null string is recived. Exclude this data sample."

    last_line = lines[-1]

    # Extract answer part after "final answer:" if present
    answer_part = last_line.split("final answer:")[-1].strip() if "final answer:" in last_line else last_line

    # Clean the answer part
    answer_part = answer_part.strip().rstrip('.,;:!? ')

    # Direct true/false check
    if answer_form=="bool":
        if answer_part in ['true', 'yes', '1']:
            return 1
        if answer_part in ['false', 'no', '0']:
            return 0
    else:
        if answer_part in ['a', 'b', 'c', 'd']:
            return answer_part.capitalize()
        else:
            print(f"LabelExtracter: Could not extract MCQ answer from '{answer_part}'")

    return "Request failed. Null string is recived. Exclude this data sample."



def RequestSender(prompt: str,
                 model: str = "gpt-4o",
                 api_key: str = 'sk-',
                 base_url: str = 'https://api.openai.com',
                 max_retries: int = 6,
                 initial_wait: float = 1.0,
                 timeout: float = 60.0) -> str:
    """
    Description
    -----------
    Send request by calling model API with retry mechanism using OpenAI library

    Parameters
    ----------
    prompt : prompt containing the data
    model : model used, gpt-4o by default
    api_key : api credential
    base_url : api proxy base URL
    max_retries : maximum number of retries
    initial_wait : initial wait time between retries (seconds)

    Returns
    -------
    answer : str, answer from model
    """

    # Ensure base_url has a protocol
    if base_url != "null" and not base_url.startswith(('http://', 'https://')):
        base_url = 'https://' + base_url

    client = openai.OpenAI(
        api_key=api_key,
        base_url=base_url,
        timeout=timeout
    )

    # retry
    session = requests.Session()
    retry_strategy = Retry(
        total=max_retries,
        backoff_factor=initial_wait,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["POST"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)


    client.requestssession = session

    for attempt in range(max_retries + 1):
        try:

            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}]
                )

                # Check if response is None before accessing its attributes
                if response is None:
                    return "Request Failed: Received None response"
                # Check if choices list is empty
                if not response.choices:
                    return "Request Failed: No choices in response"
                # Check if message or content is None
                if response.choices[0].message is None or response.choices[0].message.content is None:
                    return "Request Failed: Message or content is None"
                return response.choices[0].message.content.strip()
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e}")
                # Wait and retry
                wait_time = (2 ** attempt) * initial_wait + random.uniform(0, 1)
                if attempt < max_retries:
                    print(f"Waiting {wait_time:.2f} seconds before retrying...")
                    time.sleep(wait_time)
                    continue
                else:
                    return "Request Failed: JSON decode error"

        except (openai.APIError, openai.APIConnectionError,
                openai.RateLimitError, openai.APITimeoutError,
                openai.InternalServerError, requests.exceptions.RequestException,
                json.JSONDecodeError, requests.exceptions.Timeout,
                requests.exceptions.ConnectionError, ssl.SSLError,
                ConnectionResetError, ConnectionAbortedError, ConnectionRefusedError,
                TimeoutError) as e:
            wait_time = (2 ** attempt) * initial_wait + random.uniform(0, 1)

            error_type = type(e).__name__
            if attempt < max_retries:
                print(f"Attempt {attempt + 1}/{max_retries + 1} failed with {error_type}: {str(e)}")
                print(f"Waiting {wait_time:.2f} seconds before retrying...")
                time.sleep(wait_time)
            else:
                print(f"All {max_retries + 1} attempts failed. Last error ({error_type}): {str(e)}")
                return f"Request Failed: {error_type} - {str(e)}"

    return "Request Failed"



def Logger(data:dict, task:str, response:str, predicted_label:int, save_name:str):
    """
    Description
    -----------
    log model's answer for each data entry

    Parameters
    ----------
    data :  an data sample
    task :  the task name, 'projection', 'legality'(Executability in Paper),
                                    'planning', 'goalrecognition'
    save_name :  the name of the jsonl file
    response :  model's answer
    predicted_label :  predicted label extracted from reponse

    Return
    ------
    None, results will be saved directly
    """
    answer = {"problem_id": data["problem_id"], "answer": response,  "predicted_label": predicted_label, "label": data["label"]}

    #save answer and use '{task}-{save_name}-response.jsonl' as file name,
    #and do not need to write task in the save_name
    with open(f'{task}-{save_name}-response.jsonl', 'a', encoding='utf-8') as f:
        f.write(json.dumps(answer, ensure_ascii=False) + '\n')

    print("Log successfully.")


