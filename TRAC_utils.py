import time
import os
import json
import utils
import TRAC_Prompt

def DataLoader(file_path) -> list:
    """
    Load data(*.jsonl file) from file_path, convert it into a list.
    """
    with open(file_path, "r", encoding='utf-8') as file:
        dataset = [json.loads(line) for line in file]
    return dataset



def Extractor(data_entry: dict, extraction_func: str, task:str, **kwargs) -> str:
    """
    Stage 1: Extract and convert information from data.

    Parameters
    ----------
    data_entry : dict, the data entry of from benchmark.
    extraction_func : str, which function to use for extraction. `question_extractor`, `initial_state_extractor`, `action_sequence_extractor`, `goal_extractor`.
    task :  the task name, Projection, PlanVerification, Executability
    **kwargs : dict, additional arguments.
    - model : LLM model.
    - url : base url from LLM provider.
    - api : api key from LLM provider.

    Returns
    -------
    str : the extracted information(question/initial state extractor).
    list : action sequence(action extractor)
    """
    if extraction_func == "question_extractor":
       if task=="Projection":
           return data_entry["query"]
       elif task=="Executability":
           return "N/A"
       else:
           return data_entry['goal']

    elif extraction_func == "action_sequence_extractor":
        if task=="Projection":
            actions = data_entry['action_sequence']
            return [sentence.strip() for sentence in actions.split('.') if sentence.strip()]
        else:
            actions = data_entry['query']
            return [sentence.strip() for sentence in actions.split('.') if sentence.strip()]
        
    elif extraction_func=="initial_state_extractor":
        prompt = (
            f"{TRAC_Prompt.INITIAL_STATE_EXTRACTOR_EXAMPLE}\n"
            f"[Initial State needed to be extracted]{data_entry['state']}\n"
            f"{TRAC_Prompt.INITIAL_STATE_EXTRACTOR_PROMPT}"
        )
        response = utils.RequestSender(prompt, model=kwargs.get('model', "gpt-4o"), api_key=kwargs.get('api', "null"), base_url=kwargs.get('url', "null"))
        paragraphs = response.strip().split('\n')
        new_state = paragraphs[-1].strip()
        return new_state

    else:
        return data_entry['goal']
        

def Checker(checker_func:str, current_state:str, **kwargs) ->list:
    """
    State 2 and 3: ExecutabiliryChecker(state+action) or StateChecker(state+question) based on the current state.

    Parameters
    ----------
    checker_func : str. The function to be used. `executability_checker`, `state_checker`
    current_state : str. The current state of the objects.
    **kwargs: dict. additional arguments.
    - action : str/list. The action to be checked.
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
            f"{TRAC_Prompt.DOMAIN_DESCRIPTION_BLOCKSWORLD}\n"
            f"{TRAC_Prompt.EXECUTABILITY_CHECKER_EXAMPLE}\n"
            f"[current state]{current_state}\n"
            f"[Action needed to be checked]{kwargs['action']}\n"
            f"{TRAC_Prompt.EXECUTABILITY_CHECKER_PROMPT}"
        )
    elif checker_func == "state_checker":
        prompt = (
            f"{TRAC_Prompt.DOMAIN_DESCRIPTION_BLOCKSWORLD}\n"
            f"{TRAC_Prompt.STATE_CHECKER_EXAMPLE}\n"
            f"[current state]{current_state}\n" #Progressed state Sn
            f"[Question]{kwargs['question']}\n"
            f"{TRAC_Prompt.STATE_CHECKER_PROMPT}"
        )

    response = utils.RequestSender(prompt, model=kwargs.get('model', "gpt-4o"), api_key=kwargs.get('api', "null"), base_url=kwargs.get('url', "null"))
    label = utils.LabelExtracter(response)
    return [label, response]



def ActionTaker(current_state, action, **kwargs):
    """
    Stage 2: Progression, take action and return new state.

    Parameters
    ----------
    current_state : str. The current state of the objects.
    action : str
    **kwargs: dict, additional arguments.
    - model : LLM model.
    - url : base url from LLM provider.
    - api : api key from LLM provider.

    Returns
    -------
    new_state : str. New state from progression.
    """
    prompt =(
        f"{TRAC_Prompt.DOMAIN_DESCRIPTION_BLOCKSWORLD}\n"
        f"{TRAC_Prompt.ACTION_TAKER_EXAMPLE}\n"
        f"[Current State]{current_state}\n"
        f"[Action]{action}\n"
        f"{TRAC_Prompt.ACTION_TAKER_PROMPT}\n"
    )
    response = utils.RequestSender(prompt, model=kwargs.get('model', "gpt-4o"), api_key=kwargs.get('api', "null"), base_url=kwargs.get('url', "null"))

    #extract final answer as predicted label("Final Answer: yes/no")
    paragraphs = response.strip().split('\n')
    new_state = paragraphs[-1].strip()
    return new_state




def Action_Executability_Progression(data_entry: dict, task: str, save_name: str, **kwargs) -> int:
    """
    Progression for executability task.
    """
    #Stage 1: extraction
    states = []
    current_state = Extractor("initial_state_extractor", data_entry,  model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
    action_sequence = Extractor("action_sequence_extractor", data_entry, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))

    # Check if action sequence extraction failed
    if not action_sequence:
        print(f"Warning: Action sequence extraction failed for problem_id: {data_entry.get('problem_id', 'unknown')}")
        return 0  # Return 0 to indicate failure

    question = Extractor("question_extractor", data_entry,  model=kwargs.get('model', "gpt-4o"))
    states.append(current_state)
    action_taken = 0

    #Stage 2: Progress
    for action in action_sequence:
        checker_result = Checker('executability_checker', current_state, action=action, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
        if not checker_result[0]: #label=0 -> this action is not executable
            states.append(f"{checker_result[1]}")
            ProgressionLogger(data_entry, action_sequence, states, 0, save_name, task="Executability", question=question, action_taken=action_taken)
            return 0
        current_state = ActionTaker(current_state, action,  model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
        states.append(current_state)
        action_taken += 1

    #Stage 3: Querying
    ProgressionLogger(data_entry, action_sequence, states, 1, save_name, task="Executability", question=question, action_taken=action_taken, state_checker_response=checker_result[1])
    return 1



def State_Progression(data_entry: dict, task: str, save_name: str, **kwargs) -> int:
    """
    Progression for `Projection` and `Plan Verification`
    """
    # Stage 1: Extraction
    states = []
    current_state = Extractor("initial_state_extractor", data_entry, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
    action_sequence = Extractor("action_sequence_extractor", data_entry, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))

    # Check if action sequence extraction failed
    if not action_sequence:
        print(f"Warning: Action sequence extraction failed for problem_id: {data_entry.get('problem_id', 'unknown')}")
        return 0  # Return 0 to indicate failure

    question = Extractor("question_extractor", data_entry, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
    states.append(current_state)
    action_taken = 0

    # Stage 2: Progress
    for action in action_sequence:
        current_state = ActionTaker(current_state, action, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
        states.append(current_state)
        action_taken += 1

    # Stage 3: Querying
    checker_result = Checker('state_checker', current_state,  question=question, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
    ProgressionLogger(data_entry, action_sequence, states, checker_result[0], save_name, task=data_entry['question_category'], question=question, action_taken=action_taken, state_checker_response=checker_result[1])
    return checker_result[0]



def Progression(data_entry: dict, task: str, save_name: str, **kwargs) -> int:
    """
    Progress based on action and current state.
    If progression is successful, return 1, otherwise return 0.

    Parameters
    ----------
    data_entry : dict. The data entry of from benchmark.
    task : str. `Executability`, `PlanVerification` and `Projection`
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
        "Executability": Action_Executability_Progression,
        "PlanVerification": State_Progression,
        "Projection": State_Progression
    }

    if task not in task_functions:
        raise ValueError(f"Unsupported task: {task}")

    return task_functions[task](data_entry, save_name, **kwargs)






def ProgressionLogger(data_entry:dict, task:str, response:str, predicted_label:int, save_name:str):
    """
    Description
    -----------
    log model's answer for each data entry

    Parameters
    ----------
    data_entry :  an data sample
    task :  the task name, Projection, PlanVerification, Executability
    save_name :  the name of the jsonl file
    response :  model's answer
    predicted_label :  predicted label extracted from reponse

    Return
    ------
    None, results will be saved directly
    """
    answer = {"problem_id": data_entry["problem_id"], "task": task, "answer": response,  "predicted_label": predicted_label, "label": data_entry["label"]}

    #save answer and use '{task}-{save_name}-response.jsonl' as file name,
    #and do not need to write task in the save_name
    with open(f'{save_name}-{task}-response.jsonl', 'a', encoding='utf-8') as f:
        f.write(json.dumps(answer, ensure_ascii=False) + '\n')



def BaselineEvaluation(data_entry: dict, task: str, mode:str, save_name: str, **kwargs) -> int:
    """
    0Shot, 0Shot-CoT ans 2Shot-CoT as baseline evaliation for benchmark

    Parameters
    ----------
    data_entry : dict. The data entry of from benchmark.
    task : str. Projection, Executability, PlanVerification.
    mode : str. `0shot`, `0Shot-CoT` or `2Shot-CoT`
    save_name : str. The name for the log file.
    **kwargs: Additional arguments
    - model : LLM used
    - url : base url from LLM provider.
    - api : api key from LLM provider.

    Returns
    -------
    For bool task returns llm_label : int, 1=True and 0=False.
    For mcq task returns llm_label : str, A/B/C/D.
    """

    base_prompt = ()
    example = ()

    #BASE PROMPT
    if task=="Projection":
        base_prompt = (
            f"[Initial state]{data_entry['state']}\n"
            f"[Action Sequence]{data_entry['action_sequence']}\n"
            f"[Question]{data_entry['query']}\n"
            f"Based on the initial state, take actions in the action sequence and get the final state. Then, check whether the query match with the final state. After your analysis, return your final answer into a new paragraph as the end of your answer. The last paragraph should be like 'Final Answer: True/False'. Besides, don't use any markdown formatting in your answer.\n"
        )
        example = (
            f"{TRAC_Prompt.TWOSHOTCOT_EXAMPLE_PR}\n"
        )
    elif task=="Executability":
        base_prompt = (
            f"[Initial state]{data_entry['state']}\n"
            f"[Action Sequence]{data_entry['query']}\n"
            f"Based on the initial state, check whether all actions in the action sequence is executable or not. After your analysis, return your final answer into a new paragraph as the end of your answer. The last paragraph should be like 'Final Answer: True/False'. Besides, don't use any markdown formatting in your answer.\n"
        )
        example = (
            f"{TRAC_Prompt.TWOSHOTCOT_EXAMPLE_EXE}\n"
        )
    elif task=="PlanVerification":
        base_prompt=(
            f"[Initial state]{data_entry['state']}\n"
            f"[Action Sequence]{data_entry['query']}\n"
            f"[Goal]{data_entry['goal']}\n"
            f"Based on the initial state, take actions in the action sequence and check whether this action sequence can reach the goal or not. After your analysis, return your final answer into a new paragraph as the end of your answer. The last paragraph should be like 'Final Answer: True/False'. Besides, don't use any markdown formatting in your answer.\n"
        )
        example = (
            f"{TRAC_Prompt.TWOSHOTCOT_EXAMPLE_PV}\n"
        )

    #PROMPT
    if mode=="0shot":
        prompt = base_prompt
    elif mode=="0Shot-CoT":
        prompt = (
            f"{base_prompt}"
            f"Let's think step by step."
        )
    else:
        prompt = (
            f"{example}\n"
            f"{base_prompt}\n"
            f"Let's think like examples above and solve this problem step by step."
        )

    #GET LLM ANSWER
    response = utils.RequestSender(prompt, model=kwargs.get("model", "null"), api_key=kwargs.get('api', "null"), base_url=kwargs.get('url', "null"))
    llm_label = utils.LabelExtracter(response)

    BaselineLogger(data_entry, response, llm_label, save_name, task, mode=mode)

    return llm_label



def BaselineLogger(data_entry, answer, llm_label, save_name, task, **kwargs) -> None:
    """
    Log baseline evaluation a data entry into a jsonl file.

    Parameters
    ----------
    data_entry : dict. Evaluated data
    answer : int. The final answer from LLM.
    llm_label : int. The predicted label from LLM, extracted from answer.
    save_name : str. The name for the log file.
    task : str. Projection, Legality, PlanVerification.
    **kwargs: Additional arguments
    - mode : str. '0Shot', '0Shot-CoT' or '2Shot-CoT'.
    """

    log_data = {
        "question_id": data_entry["problem_id"],
        "answer": answer,
        "llm_label": llm_label,
        "label":data_entry['label']
    }

    filename = f"{save_name}-{task}-{kwargs['mode']}-response.jsonl"

    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(log_data, ensure_ascii=False) + '\n')
    else:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_data, ensure_ascii=False) + '\n')


