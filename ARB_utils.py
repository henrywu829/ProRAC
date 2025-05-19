import utils
import ARB_Prompt
import os
import json


DomainMapping ={
    'depots': {'domain_description':ARB_Prompt.DEPOTS_DOMAIN_DESCRIPTION,
               'initial_state_extractor':ARB_Prompt.INITIAL_STATE_EXTRACTOR_DEPOTS_PROMPT,
               'initial_state_extractor_example':ARB_Prompt.INITIAL_STATE_EXTRACTOR_DEPOTS_EXAMPLE,
               'question_extractor_example':ARB_Prompt.QUESTION_EXTRACTOR_DEPOTS_EXAMPLE,
               'action_taker':ARB_Prompt.ACTION_TAKER_DEPOTS_PROMPT,
               'action_taker_example':ARB_Prompt.ACTION_TAKER_DEPOTS_EXAMPLE,
               'executability_checker_example':ARB_Prompt.EXECUTABILITY_CHECKER_DEPOTS_EXAMPLE,
               'state_checker_example':ARB_Prompt.STATE_CHECKER_DEPOTS_EXAMPLE,
                '2ShotCoT_AE_exmaple': ARB_Prompt.TWOSHOTCOT_AE_DEPOTS_EXAMPLE,
                '2ShotCoT_STATE_exmaple': ARB_Prompt.TWOSHOTCOT_STATE_DEPOTS_EXAMPLE,
               },
    'driverlog':{'domain_description':ARB_Prompt.DRIVERLOG_DOMAIN_DESCRIPTION,
               'initial_state_extractor':ARB_Prompt.INITIAL_STATE_EXTRACTOR_DRIVERLOG_PROMPT,
               'initial_state_extractor_example':ARB_Prompt.INITIAL_STATE_EXTRACTOR_DRIVERLOG_EXAMPLE,
               'question_extractor_example':ARB_Prompt.QUESTION_EXTRACTOR_DRIVERLOG_EXAMPLE,
               'action_taker':ARB_Prompt.ACTION_TAKER_DRIVERLOG_PROMPT,
               'action_taker_example':ARB_Prompt.ACTION_TAKER_DRIVERLOG_EXAMPLE,
               'executability_checker_example':ARB_Prompt.EXECUTABILITY_CHECKER_DRIVERLOG_EXAMPLE,
               'state_checker_example':ARB_Prompt.STATE_CHECKER_DRIVERLOG_EXAMPLE,
               '2ShotCoT_AE_exmaple': ARB_Prompt.TWOSHOTCOT_AE_DRIVERLOG_EXAMPLE,
               '2ShotCoT_STATE_exmaple': ARB_Prompt.TWOSHOTCOT_STATE_DRIVERLOG_EXAMPLE,
               },
    'grippers':{'domain_description':ARB_Prompt.GRIPPERS_DOMAIN_DESCRIPTION,
                'initial_state_extractor':ARB_Prompt.INITIAL_STATE_EXTRACTOR_GRIPPERS_PROMPT,
                'initial_state_extractor_example':ARB_Prompt.INITIAL_STATE_EXTRACTOR_GRIPPERS_EXAMPLE,
                'question_extractor_example':ARB_Prompt.QUESTION_EXTRACTOR_GRIPPERS_EXAMPLE,
                'action_taker':ARB_Prompt.ACTION_TAKER_GRIPPERS_PROMPT,
                'action_taker_example':ARB_Prompt.ACTION_TAKER_GRIPPERS_EXAMPLE,
                'executability_checker_example':ARB_Prompt.EXECUTABILITY_CHECKER_GRIPPERS_EXAMPLE,
                'state_checker_example':ARB_Prompt.STATE_CHECKER_GRIPPERS_EXAMPLE,
                '2ShotCoT_AE_exmaple': ARB_Prompt.TWOSHOTCOT_AE_GRIPPERS_EXAMPLE,
                '2ShotCoT_STATE_exmaple': ARB_Prompt.TWOSHOTCOT_STATE_GRIPPERS_EXAMPLE,
                },
    'mystery':{'domain_description':ARB_Prompt.MYSTERY_DOMAIN_DESCRIPTION,
               'initial_state_extractor':ARB_Prompt.INITIAL_STATE_EXTRACTOR_MYSTERY_PROMPT,
               'initial_state_extractor_example':ARB_Prompt.INITIAL_STATE_EXTRACTOR_MYSTERY_EXAMPLE,
               'question_extractor_example':ARB_Prompt.QUESTION_EXTRACTOR_MYSTERY_EXAMPLE,
               'action_taker':ARB_Prompt.ACTION_TAKER_MYSTERY_PROMPT,
               'action_taker_example':ARB_Prompt.ACTION_TAKER_MYSTERY_EXAMPLE,
               'executability_checker_example':ARB_Prompt.EXECUTABILITY_CHECKER_MYSTERY_EXAMPLE,
               'state_checker_example':ARB_Prompt.STATE_CHECKER_MYSTERY_EXAMPLE,
               '2ShotCoT_AE_exmaple': ARB_Prompt.TWOSHOTCOT_AE_MYSTERY_EXAMPLE,
               '2ShotCoT_STATE_exmaple': ARB_Prompt.TWOSHOTCOT_STATE_MYSTERY_EXAMPLE,
               },
    'satellite':{'domain_description':ARB_Prompt.SATELLITE_DOMAIN_DESCRIPTION,
                 'initial_state_extractor':ARB_Prompt.INITIAL_STATE_EXTRACTOR_SATELLITE_PROMPT,
                 'initial_state_extractor_example':ARB_Prompt.INITIAL_STATE_EXTRACTOR_SATELLITE_EXAMPLE,
                 'question_extractor_example':ARB_Prompt.QUESTION_EXTRACTOR_SATELLITE_EXAMPLE,
                 'action_taker':ARB_Prompt.ACTION_TAKER_SATELLITE_PROMPT,
                 'action_taker_example':ARB_Prompt.ACTION_TAKER_SATELLITE_EXAMPLE,
                 'executability_checker_example':ARB_Prompt.EXECUTABILITY_CHECKER_SATELLITE_EXAMPLE,
                 'state_checker_example':ARB_Prompt.STATE_CHECKER_SATELLITE_EXAMPLE,
                 '2ShotCoT_AE_exmaple': ARB_Prompt.TWOSHOTCOT_AE_SATELLITE_EXAMPLE,
                 '2ShotCoT_STATE_exmaple': ARB_Prompt.TWOSHOTCOT_STATE_SATELLITE_EXAMPLE,
                 },
    'visitall':{'domain_description':ARB_Prompt.VISITALL_DOMAIN_DESCRIPTION,
                'initial_state_extractor':ARB_Prompt.INITIAL_STATE_EXTRACTOR_VISITALL_PROMPT,
                'initial_state_extractor_example':ARB_Prompt.INITIAL_STATE_EXTRACTOR_VISITALL_EXAMPLE,
                'question_extractor_example':ARB_Prompt.QUESTION_EXTRACTOR_VISITALL_EXAMPLE,
                'action_taker':ARB_Prompt.ACTION_TAKER_VISITALL_PROMPT,
                'action_taker_example':ARB_Prompt.ACTION_TAKER_VISITALL_EXAMPLE,
                'executability_checker_example':ARB_Prompt.EXECUTABILITY_CHECKER_VISITALL_EXAMPLE,
                'state_checker_example':ARB_Prompt.STATE_CHECKER_VISITALL_EXAMPLE,
                '2ShotCoT_AE_exmaple': ARB_Prompt.TWOSHOTCOT_AE_VISITALL_EXAMPLE,
                '2ShotCoT_STATE_exmaple': ARB_Prompt.TWOSHOTCOT_STATE_VISITALL_EXAMPLE,
                
                },
    'spanner':{'domain_description':ARB_Prompt.SPANNER_DOMAIN_DESCRIPTION,
                'initial_state_extractor':ARB_Prompt.INITIAL_STATE_EXTRACTOR_SPANNER_PROMPT,
                'initial_state_extractor_example':ARB_Prompt.INITIAL_STATE_EXTRACTOR_SPANNER_EXAMPLE,
                'question_extractor_example':ARB_Prompt.QUESTION_EXTRACTOR_SPANNER_EXAMPLE,
                'action_taker':ARB_Prompt.ACTION_TAKER_SPANNER_PROMPT,
                'action_taker_example':ARB_Prompt.ACTION_TAKER_SPANNER_EXAMPLE,
                'executability_checker_example':ARB_Prompt.EXECUTABILITY_CHECKER_SPANNER_EXAMPLE,
                'state_checker_example':ARB_Prompt.STATE_CHECKER_SPANNER_EXAMPLE,
                '2ShotCoT_AE_exmaple': ARB_Prompt.TWOSHOTCOT_AE_SPANNER_EXAMPLE,
                '2ShotCoT_STATE_exmaple': ARB_Prompt.TWOSHOTCOT_STATE_SPANNER_EXAMPLE,
                }
}



def DataLoader(file_path) -> list:
    """
    Load data(*.jsonl file) from file_path, convert it into a list.
    """
    with open(file_path, "r", encoding='utf-8') as file:
        dataset = [json.loads(line) for line in file]
    return dataset



def Extractor(extraction_func:str, data_entry: dict, **kwargs) -> str:
    """
    Stage 1: Extract and convert information from data.

    Parameters
    ----------
    extraction_func : str, which function to use for extraction. question_extractor, initial_state_extractor, action_sequence_extractor.
    data_entry : dict, the data entry of from benchmark.
    **kwargs : dict, additional arguments.
    - domain : str, depots, driverlog, grippers, mystery, satellite, spanner, visitall.
    - task : str, action_executability, composite, effects, fluent_tracking, numerical_reasoning, state_tracking.
    - model : LLM model.
    - url : base url from LLM provider.
    - api : api key from LLM provider.

    Returns
    -------
    str : the extracted information(question/initial state extractor).
    list : action sequence(action extractor)
    """
    #Extract initial state from the plan -> str
    if extraction_func == "initial_state_extractor":
        prompt = (
            f"{DomainMapping[kwargs['domain']]['domain_description']}\n\n"
            f"{DomainMapping[kwargs['domain']]['initial_state_extractor_example']}\n"
            f"[Initial State needed to be extracted]{data_entry['initial_state_nl']}\n"
            f"{DomainMapping[kwargs['domain']]['initial_state_extractor']}"
        )
        response = utils.RequestSender(prompt, model=kwargs.get('model', "gpt-4o"), api_key=kwargs.get('api', "null"), base_url=kwargs.get('url', "null"))

        paragraphs = response.strip().split('\n')
        new_state = paragraphs[-1].strip()
        return new_state

    #Extract question from the plan -> str
    elif extraction_func == "question_extractor":
        prompt =(
            f"{DomainMapping[kwargs['domain']]['question_extractor_example']}\n"
            f"[Question needed to be extracted]{data_entry['question']}\n"
            f"{ARB_Prompt.QUESTION_EXTRACTOR_PROMPT}"
        )
        return utils.RequestSender(prompt, model=kwargs.get('model', "gpt-4o"), api_key=kwargs.get('api', "null"), base_url=kwargs.get('url', "null"))

    #Extract action sequence from the plan -> list
    elif extraction_func == "action_sequence_extractor":
        prompt = (
            f"[Plan]"
            f"{data_entry['question']}\n"
            f"{ARB_Prompt.ACTION_SEQUENCE_EXTRACTOR_PROMPT}\n"
            f"You are required to extract {data_entry['plan_length']} actions from the plan."
        )
        response = utils.RequestSender(prompt, model=kwargs.get('model', "gpt-4o"), api_key=kwargs.get('api', "null"), base_url=kwargs.get('url', "null"))

        # Check if the request failed
        if response.startswith("Request Failed"):
            print(f"Warning: Action sequence extraction failed: {response}")
            return []  # Return empty list to indicate failure

        sentences = response.split(".")
        action_sequence = [sent.strip() for sent in sentences if sent.strip()]
        return action_sequence



def Checker(checker_func:str, current_state:str, domain:str, **kwargs) ->list:
    """
    State 2 and 3: ExecutabiliryChecker(state+action) or StateChecker(state+question) based on the current state.

    Parameters
    ----------
    checker_func : str. The function to be used. `executability_checker` or `state_checker`.
    current_state : str. The current state of the objects.
    domain: str, depots, driverlog, grippers, mystery, satellite, spanner, visitall.
    **kwargs: dict, additional arguments.
    - action : str. The action to be checked.
    - question : str. The question to be checked.
    - model : str, LLM model.
    - url : base url from LLM provider.
    - api : api key from LLM provider.

    Returns
    -------
    [label, response] : 1=executable/match and 0=not executable/match. Response is the generated response from LLM.

    """

    if checker_func == "executability_checker":
        prompt = (
            f"{DomainMapping[domain]['domain_description']}\n"
            f"{DomainMapping[domain]['executability_checker_example']}\n"
            f"[current state]{current_state}\n"
            f"[Action needed to be checked]{kwargs['action']}\n"
            f"{ARB_Prompt.EXECUTABILITY_CHECKER_PROMPT}"
        )
    elif checker_func == "state_checker":
        prompt = (
            f"{DomainMapping[domain]['domain_description']}\n"
            f"{DomainMapping[domain]['state_checker_example']}\n"
            f"[current state]{current_state}\n"
            f"[Question]{kwargs['question']}\n"
            f"{ARB_Prompt.STATE_CHECKER_PROMPT}"
        )

    response = utils.RequestSender(prompt, model=kwargs.get('model', "gpt-4o"), api_key=kwargs.get('api', "null"), base_url=kwargs.get('url', "null"))
    label = utils.LabelExtracter(response)
    return [label, response]



def ActionTaker(current_state, action, domain, **kwargs):
    """
    Stage 2: Progression, take action and return new state.

    Parameters
    ----------
    current_state : str. The current state of the objects.
    action : str
    domain : str, depots, driverlog, grippers, mystery, satellite, spanner, visitall.
    **kwargs: dict, additional arguments.
    - model : LLM model.
    - url : base url from LLM provider.
    - api : api key from LLM provider.

    Returns
    -------
    new_state : str. New state from progression.
    """
    prompt =(
        f"{DomainMapping[domain]['domain_description']}\n"
        f"{DomainMapping[domain]['action_taker_example']}\n"
        f"[Current State]{current_state}\n"
        f"[Action]{action}\n"
        f"{DomainMapping[domain]['action_taker']}"

    )
    response = utils.RequestSender(prompt, model=kwargs.get('model', "gpt-4o"), api_key=kwargs.get('api', "null"), base_url=kwargs.get('url', "null"))

    #extract final answer as predicted label("Final Answer: True/False")
    paragraphs = response.strip().split('\n')
    new_state = paragraphs[-1].strip()
    return new_state



def Action_Executability_Progression(data_entry: dict, domain: str, save_name: str, **kwargs) -> int:
    """
    Progression for action executability task.
    """
    #Stage 1: extraction
    states = []
    current_state = Extractor("initial_state_extractor", data_entry, domain=domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
    action_sequence = Extractor("action_sequence_extractor", data_entry, domain=domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))

    # Check if action sequence extraction failed
    if not action_sequence:
        print(f"Warning: Action sequence extraction failed for problem_id: {data_entry.get('problem_id', 'unknown')}")
        return 0  # Return 0 to indicate failure

    question = Extractor("question_extractor", data_entry, domain=domain, model=kwargs.get('model', "gpt-4o"))
    states.append(current_state)
    action_taken = 0
    executability_flag = 1

    #Stage 2: Progress
    for action in action_sequence:
        checker_result = Checker('executability_checker', current_state, domain, action=action, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
        if not checker_result[0]: #label=0 -> this action is not executable
            executability_flag = 0
            states.append(f"{checker_result[1]}")
            ProgressionLogger(data_entry, action_sequence, states, 0, save_name, domain=domain, task="action_executability", question=question, action_taken=action_taken)
            return 0
        current_state = ActionTaker(current_state, action, domain, model=kwargs.get('model', "gpt-4o"))
        states.append(current_state)
        action_taken += 1

    #Stage 3: Querying
    answer = int(len(states) == len(action_sequence) + 1) #the entire action sequence is executable
    ProgressionLogger(data_entry, action_sequence, states, answer, save_name, domain=domain, task="action_executability", question=question, action_taken=action_taken, state_checker_response=checker_result[1])
    return 1



def State_Progression(data_entry: dict, domain: str, save_name: str, **kwargs) -> int:
    """
    Progression for effects, fluent tracking and state tracking.
    """
    # Stage 1: Extraction
    states = []
    current_state = Extractor("initial_state_extractor", data_entry, domain=domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
    action_sequence = Extractor("action_sequence_extractor", data_entry, domain=domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))

    # Check if action sequence extraction failed
    if not action_sequence:
        print(f"Warning: Action sequence extraction failed for problem_id: {data_entry.get('problem_id', 'unknown')}")
        return 0  # Return 0 to indicate failure

    question = Extractor("question_extractor", data_entry, domain=domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
    states.append(current_state)
    action_taken = 0

    # Stage 2: Progress
    for action in action_sequence:
        current_state = ActionTaker(current_state, action, domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
        states.append(current_state)
        action_taken += 1

    # Stage 3: Querying
    checker_result = Checker('state_checker', current_state, domain, question=question, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
    ProgressionLogger(data_entry, action_sequence, states, checker_result[0], save_name, domain=domain, task=data_entry['question_category'], question=question, action_taken=action_taken, state_checker_response=checker_result[1])
    return checker_result[0]



def Complex_Reasoing_Progression(data_entry: dict, domain: str, save_name: str, **kwargs) -> int:
    """
    Progression for numerical and composite tasks.
    """
    # Stage 1: Extraction
    states = []
    current_state = Extractor("initial_state_extractor", data_entry, domain=domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
    action_sequence = Extractor("action_sequence_extractor", data_entry, domain=domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))

    # Check if action sequence extraction failed
    if not action_sequence:
        print(f"Warning: Action sequence extraction failed for problem_id: {data_entry.get('problem_id', 'unknown')}")
        return 0  # Return 0 to indicate failure

    question = Extractor("question_extractor", data_entry, domain=domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
    states.append(current_state)
    action_taken = 0
    executability_flag = 1

    # Stage 2: Progress
    for action in action_sequence:
        checker_result = Checker('executability_checker', current_state, domain, action=action, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
        if not checker_result[0]:  # if not executable
            executability_flag = 0
            states.append(f"{checker_result[1]}")
            ProgressionLogger(data_entry, action_sequence, states, checker_result[0], save_name, domain=domain, task=data_entry['question_category'], question=question, action_taken=action_taken)
            return checker_result[0]
        current_state = ActionTaker(current_state, action, domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
        states.append(current_state)
        action_taken += 1

    # Stage 3: Querying
    checker_result = Checker('state_checker', current_state, domain, question=question, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
    ProgressionLogger(data_entry, action_sequence, states, checker_result[0], save_name, domain=domain, task="composite", question=question, action_taken=action_taken, state_checker_response=checker_result[1])
    return checker_result[0]




def Progression(data_entry: dict, domain: str, task: str, save_name: str, **kwargs) -> int:
    """
    Progress based on action and current state.
    If progression is successful, return 1, otherwise return 0.

    Parameters
    ----------
    data_entry : dict. The data entry of from benchmark.
    domain : str. depots, driverlog, grippers, mystery, satellite, spanner, visitall.
    task : str. action_executability, effects, fluent_tracking, state_tracking, numerical_reasoning, composite.
    save_name : str. The name for the log file.
    **kwargs: Additional arguments
    - model : LLM model.    
    - url : base url from LLM provider.
    - api : api key from LLM provider.

    Returns
    -------
    answer : int, 1=true, 0=false.
    """

    task_functions = {
        "action_executability": Action_Executability_Progression,
        "effects": State_Progression,
        "fluent_tracking": State_Progression,
        "state_tracking": State_Progression,
        "composite": Complex_Reasoing_Progression,
        "numerical_reasoning": Complex_Reasoing_Progression

    }

    if task not in task_functions:
        raise ValueError(f"Unsupported task: {task}")

    return task_functions[task](data_entry, domain, save_name, **kwargs)




def ProgressionLogger(data_entry: dict, action_sequence: list, states: list, answer: int, save_name: str, **kwargs):
    """
    Log progression data into a jsonl file.

    Parameters
    ----------
    data_entry : dict. The data entry.
    action_sequence : list. The sequence of actions.
    states : list. The list of states, from S0 to Sn.
    answer : int. Final answer from LLM.
    save_name : str. The name for the log file.
    **kwargs: Additional arguments
    - domain : str. depots, driverlog, grippers, mystery, satellite, spanner, visitall.
    - question : str. Question extracted from the plan.
    - task : str. action_executability, composite, effects, fluent_tracking, numerical_reasoning, state_tracking.
    - action_taken: int. how many actions are executed
    - model : LLM model.
    """
    log_data = {
        "question_id": data_entry["question_id"],
        "domain": kwargs.get('domain', None),
        "question": kwargs['question'],
        "initial_state": states[0],
        "action_sequence": action_sequence,
        "state_progression": states[1:],
        "action_taken": kwargs.get('action_taken', None),
        "state_checker_response" : kwargs.get('state_checker_response', 'N/A for AE task'),
        "answer": answer,
        "label":data_entry['answer']
    }

    filename = f"{save_name}-{kwargs['domain']}-{kwargs['task']}-response.jsonl"
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(log_data, ensure_ascii=False) + '\n')
    else:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_data, ensure_ascii=False) + '\n')



def BaselineEvaluation(data_entry:dict, domain, save_name:str, mode="0Shot", model="gpt-4o", **kwargs) -> int:
    """
    0Shot, 0Shot-CoT and 2Shot-CoT as baseline evaliation for benchmark

    Parameters
    ----------
    data_entry : dict. The data entry of from benchmark.
    domain : str. depots, driverlog, mystery, grippers, satellite, spanner, visitall.

    save_name : str. The name for the log file.
    model : str. LLM model used.
    mode : str. `0Shot`, `0Shot-CoT` or `2ShotCoT`.
    **kwargs: Additional arguments
    - base_url : str. The base URL for the API.
    - api_key : str. The API key.
    - task : str. `action_executability` or `state_tracking` or `fluent_tracking` or `effects`.

    Returns
    -------
    llm_label : int, 1=True and 0=False.
    """
    task_mapping={"action_executability": "2ShotCoT_AE_exmaple", "state_tracking":"2ShotCoT_STATE_exmaple", "fluent_tracking":"2ShotCoT_STATE_exmaple", "effects":"2ShotCoT_STATE_exmaple"}

    if mode == '0Shot':
        prompt = (
            f"[Initial state]{data_entry['initial_state_nl']}\n"
            f"[Question]{data_entry['question']}\n"
            f"Answer the question based on the initial state, after your answer, return your final verdict in the last paragraph of your answer. The last paragraph should be like 'Final Answer: True/False'. Besides, don't use any markdown formatting in your answer."
        )

    elif mode == '0Shot-CoT':
        prompt = (
            f"[Initial state]{data_entry['initial_state_nl']}\n"
            f"[Question]{data_entry['question']}\n"
            f"Let's think step by step."
            f"Answer the question based on the initial state, after your answer, return your final verdict in the last paragraph of your answer. The last paragraph should be like 'Final Answer: True/False'. Besides, don't use any markdown formatting in your answer.\n"
        )
    else:
        prompt = (
            f"{DomainMapping[domain][task_mapping[kwargs.get('task', "null")]]}"
            f"[Initial state]{data_entry['initial_state_nl']}\n"
            f"[Question]{data_entry['question']}\n"
            f"Let's think step by step."
            f"Answer the question based on the initial state, after your answer, return your final verdict in the last paragraph of your answer. The last paragraph should be like 'Final Answer: True/False'. Besides, don't use any markdown formatting in your answer.\n"
        )

    # Add timeout parameter and increase max_retries for more reliability
    response = utils.RequestSender(
        prompt,
        model=model,
        base_url=kwargs.get('base_url', 'null'),
        api_key=kwargs.get('api_key', 'null'),
        max_retries=8,  # Increase retries
        timeout=90.0  # Longer timeout
    )

    # Check if the request failed
    if response.startswith("Request Failed"):
        print(f"Warning: API request failed with message: {response}")
        # Log the failure but don't count it in accuracy calculations
        BaselineLogger(data_entry, response, None, save_name, domain=data_entry['domain_name'], task=data_entry['question_category'], mode=mode)
        return None  # Return None to indicate failure

    # Extract label from successful response
    llm_label = utils.LabelExtracter(response)

    # Log the result
    BaselineLogger(data_entry, response, llm_label, save_name, domain=data_entry['domain_name'], task=data_entry['question_category'], mode=mode)

    return llm_label



def BaselineLogger(data_entry, answer, llm_label, save_name, **kwargs) -> None:
    """
    Log baseline evaluation a data entry into a jsonl file.

    Parameters
    ----------
    data_entry : dict. Evaluated data
    answer : int. The final answer from LLM.
    llm_label : int. The predicted label from LLM, extracted from answer.
    save_name : str. The name for the log file.
    **kwargs: Additional arguments
    - domain : str. depots, driverlog, grippers, mystery, satellite, spanner, visitall.
    - task : str. action_executability, composite, effects, fluent_tracking, numerical_reasoning, state_tracking.
    - mode : str. '0Shot' or '0Shot-CoT'.

    """

    log_data = {
        "question_id": data_entry["question_id"],
        "domain": data_entry["domain_name"],
        "question": data_entry["question"],
        "answer": answer,
        "llm_label": llm_label,
        "label":data_entry['answer']
    }

    filename = f"{save_name}-{kwargs['domain']}-{kwargs['task']}-{kwargs['mode']}-response.jsonl"
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(log_data, ensure_ascii=False) + '\n')
    else:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_data, ensure_ascii=False) + '\n')
