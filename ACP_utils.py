import utils
import ACP_Prompt
import os
import json
import utils
import re



DomainMapping ={
    'ferry': {
        'domain_description': ACP_Prompt.FERRY_DOMAIN_DESCRIPTION,
        'initial_state_extractor': ACP_Prompt.INITIAL_STATE_EXTRACTOR_FERRY_PROMPT,
        'initial_state_extractor_example': ACP_Prompt.INITIAL_STATE_EXTRACTOR_FERRY_EXAMPLE,
        'question_extractor_example': ACP_Prompt.QUESTION_EXTRACTOR_FERRY_EXAMPLE,
        'action_sequence_extractor_example': ACP_Prompt.ACTION_SEQUENCE_EXTRACTOR_FERRY_PROMPT,
        'action_taker': ACP_Prompt.ACTION_TAKER_FERRY_PROMPT,
        'action_taker_example': ACP_Prompt.ACTION_TAKER_FERRY_EXAMPLE,
        'executability_checker_example': ACP_Prompt.EXECUTABILITY_CHECKER_FERRY_EXAMPLE,
        'state_checker_example': ACP_Prompt.STATE_CHECKER_FERRY_EXAMPLE,
        '2ShotCoT_app_exmaple': ACP_Prompt.TWOSHOTCOT_APP_FERRY_EXAMPLE,
        '2ShotCoT_prog_exmaple': ACP_Prompt.TWOSHOTCOT_PROG_FERRY_EXAMPLE,
        '2ShotCoT_val_exmaple': ACP_Prompt.TWOSHOTCOT_VAL_FERRY_EXAMPLE,
    },
    'swap': {
        'domain_description': ACP_Prompt.SWAP_DOMAIN_DESCRIPTION,
        'initial_state_extractor': ACP_Prompt.INITIAL_STATE_EXTRACTOR_SWAP_PROMPT,
        'initial_state_extractor_example': ACP_Prompt.INITIAL_STATE_EXTRACTOR_SWAP_EXAMPLE,
        'question_extractor_example': ACP_Prompt.QUESTION_EXTRACTOR_SWAP_EXAMPLE,
        'action_sequence_extractor_example': ACP_Prompt.ACTION_SEQUENCE_EXTRACTOR_SWAP_PROMPT,
        'action_taker': ACP_Prompt.ACTION_TAKER_SWAP_PROMPT,
        'action_taker_example': ACP_Prompt.ACTION_TAKER_SWAP_EXAMPLE,
        'executability_checker_example': ACP_Prompt.EXECUTABILITY_CHECKER_SWAP_EXAMPLE,
        'state_checker_example': ACP_Prompt.STATE_CHECKER_SWAP_EXAMPLE,
        '2ShotCoT_app_exmaple': ACP_Prompt.TWOSHOTCOT_APP_SWAP_EXAMPLE,
        '2ShotCoT_prog_exmaple': ACP_Prompt.TWOSHOTCOT_PROG_SWAP_EXAMPLE,
        '2ShotCoT_val_exmaple': ACP_Prompt.TWOSHOTCOT_VAL_SWAP_EXAMPLE,
    },
    'logistics': {
        'domain_description': ACP_Prompt.LOGISTICS_DOMAIN_DESCRIPTION,
        'initial_state_extractor': ACP_Prompt.INITIAL_STATE_EXTRACTOR_LOGISTICS_PROMPT,
        'initial_state_extractor_example': ACP_Prompt.INITIAL_STATE_EXTRACTOR_LOGISTICS_EXAMPLE,
        'question_extractor_example': ACP_Prompt.QUESTION_EXTRACTOR_LOGISTICS_EXAMPLE,
        'action_sequence_extractor_example': ACP_Prompt.ACTION_SEQUENCE_EXTRACTOR_LOGISTICS_PROMPT,
        'action_taker': ACP_Prompt.ACTION_TAKER_LOGISTICS_PROMPT,
        'action_taker_example': ACP_Prompt.ACTION_TAKER_LOGISTICS_EXAMPLE,
        'executability_checker_example': ACP_Prompt.EXECUTABILITY_CHECKER_LOGISTICS_EXAMPLE,
        'state_checker_example': ACP_Prompt.STATE_CHECKER_LOGISTICS_EXAMPLE,
        '2ShotCoT_app_exmaple': ACP_Prompt.TWOSHOTCOT_APP_LOGISTICS_EXAMPLE,
        '2ShotCoT_prog_exmaple': ACP_Prompt.TWOSHOTCOT_PROG_LOGISTICS_EXAMPLE,
        '2ShotCoT_val_exmaple': ACP_Prompt.TWOSHOTCOT_VAL_LOGISTICS_EXAMPLE,
    },
    'rovers': {
        'domain_description': ACP_Prompt.ROVERS_DOMAIN_DESCRIPTION,
        'initial_state_extractor': ACP_Prompt.INITIAL_STATE_EXTRACTOR_ROVERS_PROMPT,
        'initial_state_extractor_example': ACP_Prompt.INITIAL_STATE_EXTRACTOR_ROVERS_EXAMPLE,
        'question_extractor_example': ACP_Prompt.QUESTION_EXTRACTOR_ROVERS_EXAMPLE,
        'action_sequence_extractor_example': ACP_Prompt.ACTION_SEQUENCE_EXTRACTOR_ROVERS_PROMPT,
        'action_taker': ACP_Prompt.ACTION_TAKER_ROVERS_PROMPT,
        'action_taker_example': ACP_Prompt.ACTION_TAKER_ROVERS_EXAMPLE,
        'executability_checker_example': ACP_Prompt.EXECUTABILITY_CHECKER_ROVERS_EXAMPLE,
        'state_checker_example': ACP_Prompt.STATE_CHECKER_ROVERS_EXAMPLE,
        '2ShotCoT_app_exmaple': ACP_Prompt.TWOSHOTCOT_APP_LOGISTICS_EXAMPLE,
        '2ShotCoT_prog_exmaple': ACP_Prompt.TWOSHOTCOT_PROG_LOGISTICS_EXAMPLE,
        '2ShotCoT_val_exmaple': ACP_Prompt.TWOSHOTCOT_VAL_LOGISTICS_EXAMPLE,
    },
    'floortile':{
        'domain_description': ACP_Prompt.FLOORTILE_DOMAIN_DESCRIPTION,
        'initial_state_extractor': ACP_Prompt.INITIAL_STATE_EXTRACTOR_FLOORTILE_PROMPT,
        'initial_state_extractor_example': ACP_Prompt.INITIAL_STATE_EXTRACTOR_FLOORTILE_EXAMPLE,
        'question_extractor_example': ACP_Prompt.QUESTION_EXTRACTOR_FLOORTILE_EXAMPLE,
        'action_sequence_extractor_example': ACP_Prompt.ACTION_SEQUENCE_EXTRACTOR_FLOORTILE_PROMPT,
        'action_taker': ACP_Prompt.ACTION_TAKER_FLOORTILE_PROMPT,
        'action_taker_example': ACP_Prompt.ACTION_TAKER_FLOORTILE_EXAMPLE,
        'executability_checker_example': ACP_Prompt.EXECUTABILITY_CHECKER_FLOORTILE_EXAMPLE,
        'state_checker_example': ACP_Prompt.STATE_CHECKER_FLOORTILE_EXAMPLE,
        '2ShotCoT_app_exmaple': ACP_Prompt.TWOSHOTCOT_APP_FLOORTILE_EXAMPLE,
        '2ShotCoT_prog_exmaple': ACP_Prompt.TWOSHOTCOT_PROG_FLOORTILE_EXAMPLE,
        '2ShotCoT_val_exmaple': ACP_Prompt.TWOSHOTCOT_VAL_FLOORTILE_EXAMPLE,
    },
    'goldminer':{
        'domain_description': ACP_Prompt.GOLDMINER_DOMAIN_DESCRIPTION,
        'initial_state_extractor': ACP_Prompt.INITIAL_STATE_EXTRACTOR_GOLDMINER_PROMPT,
        'initial_state_extractor_example': ACP_Prompt.INITIAL_STATE_EXTRACTOR_GOLDMINER_EXAMPLE,
        'question_extractor_example': ACP_Prompt.QUESTION_EXTRACTOR_GOLDMINER_EXAMPLE,
        'action_sequence_extractor_example': ACP_Prompt.ACTION_SEQUENCE_EXTRACTOR_GOLDMINER_PROMPT,
        'action_taker': ACP_Prompt.ACTION_TAKER_GOLDMINER_PROMPT,
        'action_taker_example': ACP_Prompt.ACTION_TAKER_GOLDMINER_EXAMPLE,
        'executability_checker_example': ACP_Prompt.EXECUTABILITY_CHECKER_GOLDMINER_EXAMPLE,
        'state_checker_example': ACP_Prompt.STATE_CHECKER_GOLDMINER_EXAMPLE,
        '2ShotCoT_app_exmaple': ACP_Prompt.TWOSHOTCOT_APP_GOLDMINER_EXAMPLE,
        '2ShotCoT_prog_exmaple': ACP_Prompt.TWOSHOTCOT_PROG_GOLDMINER_EXAMPLE,
        '2ShotCoT_val_exmaple': ACP_Prompt.TWOSHOTCOT_VAL_GOLDMINER_EXAMPLE,
    },
}






def DataLoader(file_path) -> list:
    """
    Load data(*.jsonl file) from file_path, convert it into a list.
    """
    with open(file_path, "r", encoding='utf-8') as file:
        dataset = [json.loads(line) for line in file]
    return dataset




def Extractor(extraction_func:str, data_entry: dict, answer_form:str, task:str, **kwargs) -> str:
    """
    Stage 1: Extract and convert information from data.

    Parameters
    ----------
    extraction_func : str, which function to use for extraction. question_extractor, initial_state_extractor, action_sequence_extractor, goal_extractor.
    data_entry : dict, the data entry of from benchmark.
    answer_form: str. bool or mcq.
    - task: str. For app, the action sequence comes from `choice["text"]`. For prog and val, the action is extracted from `question` key
    **kwargs : dict, additional arguments.
    - domain : str, alfworld, ferry, floortile, goldminer, logistics, rovers, swap.
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
            f"[Initial State needed to be extracted]{data_entry['context']}\n"
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
            f"{ACP_Prompt.QUESTION_EXTRACTOR_PROMPT}"
        )
        return utils.RequestSender(prompt, model=kwargs.get('model', "gpt-4o"), api_key=kwargs.get('api', "null"), base_url=kwargs.get('url', "null"))

    #Goal extractor
    elif extraction_func == "goal_extractor":
        prompt = (
            f"[Question needed to be extracted]{data_entry['context']}\n"
            f"{ACP_Prompt.GOAL_EXTRACTOR_PROMPT}\n"
        )
        return utils.RequestSender(prompt, model=kwargs.get('model', "gpt-4o"), api_key=kwargs.get('api', "null"), base_url=kwargs.get('url', "null"))

    #Action sequence extractor
    else:
        if answer_form == "bool":
            prompt = (
                f"[Plan] "
                f"{DomainMapping[kwargs['domain']]['action_sequence_extractor_example']}\n"
                f"{data_entry['question']}\n"
                f"{ACP_Prompt.ACTION_SEQUENCE_EXTRACTOR_PROMPT}\n"
            )
            response = utils.RequestSender(prompt, model=kwargs.get('model', "gpt-4o"), api_key=kwargs.get('api', "null"), base_url=kwargs.get('url', "null"))
            sentences = response.split(".")
            action_sequence = [sent.strip() for sent in sentences if sent.strip()]
            return action_sequence
        elif answer_form == "mcq" and task=="Applicability":
            return data_entry["choices"]["text"]
        elif answer_form == "mcq":
            prompt = (
                f"[Plan] "
                f"{DomainMapping[kwargs['domain']]['action_sequence_extractor_example']}\n"
                f"{data_entry['question']}\n"
                f"{ACP_Prompt.ACTION_SEQUENCE_EXTRACTOR_PROMPT}\n"
            )
            response = utils.RequestSender(prompt, model=kwargs.get('model', "gpt-4o"), api_key=kwargs.get('api', "null"), base_url=kwargs.get('url', "null"))
            sentences = response.split(".")
            action_sequence = [sent.strip() for sent in sentences if sent.strip()]
            return action_sequence




def Checker(checker_func:str, current_state:str, domain:str, **kwargs) ->list:
    """
    State 2 and 3: ExecutabiliryChecker(state+action) or StateChecker(state+question) based on the current state.

    Parameters
    ----------
    checker_func : str. The function to be used. `executability_checker`, `state_checker`, `valid_checker`
    current_state : str. The current state of the objects.
    domain: str, alfworld, ferry, floortile, goldminer, logistics, rovers, swap.
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
            f"{DomainMapping[domain]['domain_description']}\n"
            f"{DomainMapping[domain]['executability_checker_example']}\n"
            f"[current state]{current_state}\n"
            f"[Action needed to be checked]{kwargs['action']}\n"
            f"{ACP_Prompt.EXECUTABILITY_CHECKER_PROMPT}"
        )
    elif checker_func == "state_checker":
        prompt = (
            f"{DomainMapping[domain]['domain_description']}\n"
            f"{DomainMapping[domain]['state_checker_example']}\n"
            f"[current state]{current_state}\n" #Progressed state Sn
            f"[Question]{kwargs['question']}\n"
            f"{ACP_Prompt.STATE_CHECKER_PROMPT}"
        )
    elif checker_func == "valid_checker":
        prompt = (
            f"{DomainMapping[domain]['domain_description']}\n"
            f"[Actions needed to be checked]{kwargs['action']}\n"
            f"{ACP_Prompt.VALIDATION_CHECKER_PROMPT}"
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
    domain : str, alfworld, ferry, floortile, goldminer, logistics, rovers, swap.
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

    #extract final answer as predicted label("Final Answer: yes/no")
    paragraphs = response.strip().split('\n')
    new_state = paragraphs[-1].strip()
    return new_state



def Executability_Progression(data_entry: dict, domain: str, task: str, answer_form:str, save_name: str, **kwargs) -> int:
    """
    Progression for applicability task.

    Returns
    -------
    For bool: int, 1=true and 0=false
    For MCQ: int, i=0->A, i=1->B, i=2->C, i=3->D.
    """
    #Stage 1: extraction
    answer_mapping = {0:"A", 1:"B", 2:"C", 3:"D", 999:"N/A"}
    current_state = Extractor("initial_state_extractor", data_entry, answer_form, task, domain=domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
    action_sequence = Extractor("action_sequence_extractor", data_entry, answer_form, task, domain=domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
    executability_flag = [0,0,0,0]
    action_taken=0
    states=[]
    states.append(current_state)


    #Stage 2: Progress
    if answer_form =="bool":
        for action in action_sequence:
            checker_result =  Checker("executability_checker", current_state, domain, action=action, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
            if  not checker_result[0]: #if this action is not executable
                current_state = ActionTaker(current_state, action, domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
                states.append(current_state)
                ProgressionLogger(data_entry, action_sequence, states, checker_result[0], save_name, domain=domain, task=task, question="N/A", action_taken=action_taken, state_checker_response=checker_result[1], answer_form=answer_form)
                return checker_result[0]
            current_state = ActionTaker(current_state, action, domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
            states.append(current_state)
            action_taken += 1
        ProgressionLogger(data_entry, action_sequence, states, 1, save_name, domain=domain, task=task, question="N/A for APP task", action_taken=len(action_sequence), state_checker_response="ALL actions are executable", answer_form=answer_form)
        return 1

    elif answer_form =="mcq":
        i=0
        for act in action_sequence:
            checker_result = Checker("executability_checker", current_state, domain, action=act, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
            executability_flag[i]=checker_result[0]
            states.append(f"{checker_result[1]}")
            action_taken += 1
            if executability_flag[i]==1:
                ProgressionLogger(data_entry, action_sequence, states, answer_mapping[i], save_name, domain=domain, task=task, question="N/A", action_taken=action_taken, state_checker_response=checker_result[1], answer_form=answer_form)
                return i
            i+=1

        # If no action is executable, return the first option (0) as default, even though it is impossible.
        print(f"Warning: No executable action found for question ID {data_entry['id']}. Defaulting to first option.")
        ProgressionLogger(data_entry, action_sequence, states, answer_mapping[0], save_name, domain=domain, task=task, question="N/A", action_taken=4, state_checker_response="No executable action found", answer_form=answer_form)
        return 0




def Validation_Progression(data_entry: dict, domain: str,task: str, answer_form:str, save_name: str, **kwargs) -> int:
    """
    Progression for validation task.
    """
    
    # Stage 1: Extraction
    states = []
    current_state = Extractor("initial_state_extractor", data_entry, answer_form, task, domain=domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
    action_sequence = Extractor("action_sequence_extractor", data_entry, answer_form, task, domain=domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
    goal = Extractor("goal_extractor", data_entry, answer_form, task, domain=domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
    states.append(current_state)
    action_taken = 0
    answer_mapping = {0:"A", 1:"B", 2:"C", 3:"D", 999:"N/A"}
    val_subtask = Val_task_identifier(data_entry, answer_form)
    valid_result = None
    executable_result = None
    
    if answer_form == "bool":
        #check whether all actions are valid
        valid_result = Checker("valid_checker", current_state, domain, action=str(action_sequence), model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
        if valid_result[0]==0: 
            states.append(f"{valid_result[1]}")
            ProgressionLogger(data_entry, action_sequence, states, 0, save_name, domain=domain, task=task, question=goal, action_taken=action_taken, answer_form=answer_form, state_checker_response=valid_result[1])
            return 0
        #Stage 2: Progress
        else:    
            for action in action_sequence:
                #check whether this action is executable
                executable_result = Checker('executability_checker', current_state, domain, action=action, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
                if executable_result[0]==0:
                    states.append(f"{executable_result[1]}")
                    ProgressionLogger(data_entry, action_sequence, states, 0, save_name, domain=domain, task=task, question=goal, action_taken=action_taken, answer_form=answer_form, state_checker_response=executable_result[1])
                    return 0
                current_state = ActionTaker(current_state, action, domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
                states.append(current_state)
                action_taken += 1
            # Stage 3: Querying
            checker_result = Checker('state_checker', current_state, domain, question=goal, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null")) # A plan or not
            ProgressionLogger(data_entry, action_sequence, states, checker_result[0], save_name, domain=domain, task=task, question=goal, action_taken=len(action_sequence), state_checker_response=checker_result[1], answer_form=answer_form)
            return checker_result[0]

    elif answer_form == "mcq":
        valid_result = Checker("valid_checker", current_state, domain, action=str(action_sequence), model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
        if valid_result[0]==0: 
            states.append(f"{valid_result[1]}")
            answer_number = data_entry["choices"]["text"].index("The sequence is not valid")
            ProgressionLogger(data_entry, action_sequence, states, data_entry["choices"]["label"][answer_number], save_name, domain=domain, task=task, question=goal, action_taken=action_taken, answer_form=answer_form, state_checker_response=valid_result[1])
            return answer_number
        else:
            for action in action_sequence:
                executable_result = Checker('executability_checker', current_state, domain, action=action, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
                # not executable 
                if executable_result[0]==0: 
                    executable_flag = 0
                    states.append(f"{executable_result[1]}")
                    answer_number = data_entry["choices"]["text"].index("The sequence is not applicable")
                    ProgressionLogger(data_entry, action_sequence, states, data_entry["choices"]["label"][answer_number], save_name, domain=domain, task=task, question=goal, action_taken=action_taken, answer_form=answer_form, state_checker_response=executable_result[1])
                    return answer_number
                current_state = ActionTaker(current_state, action, domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
                states.append(current_state)
                action_taken += 1
            # Stage 3: Querying
            checker_result = Checker('state_checker', current_state, domain, question=goal, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
            if checker_result[0]: #the action sequence is a plan
                answer_number = data_entry["choices"]["text"].index("The sequence is a plan")
            else: #the action sequence is applicable, but does not achieve the goal
                answer_number = data_entry["choices"]["text"].index("The sequence is applicable, but does not achieve the goal")
            ProgressionLogger(data_entry, action_sequence, states, data_entry["choices"]["label"][answer_number], save_name, domain=domain, task=task, question=goal, action_taken=action_taken, state_checker_response=checker_result[1], answer_form=answer_form)
            return answer_number




def State_Progression(data_entry: dict, domain: str, task: str, answer_form:str, save_name: str, **kwargs):
    """
    Progression for progression task.

    Returns
    -------
    For bool: int, 1=true and 0=false
    For MCQ: int, i=0->A, i=1->B, i=2->C, i=3->D.
    """

    #Step 1: Preprocess
    states = []
    current_state = Extractor("initial_state_extractor", data_entry, answer_form, task, domain=domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
    action_sequence = Extractor("action_sequence_extractor", data_entry, answer_form, task, domain=domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
    action_taken = 0
    answer_mapping = {0:"A", 1:"B", 2:"C", 3:"D", 999:"N/A"}

    if answer_form == "bool":
        #Step 1: Preprocess
        question = Extractor("question_extractor", data_entry, answer_form, task, domain=domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))

        #Step 2: Progress
        current_state = ActionTaker(current_state, action_sequence[0], domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
        states.append(current_state)
        action_taken += 1

        #Setp 3: Querying
        checker_result = Checker('state_checker', current_state, domain, question=question, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
        ProgressionLogger(data_entry, action_sequence, states, checker_result[0], save_name, domain=domain, task=task, question=question, action_taken=action_taken, state_checker_response=checker_result[1], answer_form=answer_form)
        return checker_result[0]

    elif answer_form =="mcq":
        #Step 1: Preprocess
        i=0
        question = data_entry["choices"]["text"]
        cheker_flag = [0,0,0,0]

        #Step 2: Progression
        current_state = ActionTaker(current_state, action_sequence[0], domain, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
        states.append(current_state)
        action_taken += 1

        #Step 3: Querying
        for q in question:
            checker_result = Checker('state_checker', current_state, domain, question=q, model=kwargs.get('model', "gpt-4o"), url=kwargs.get('url', "null"), api=kwargs.get('api', "null"))
            cheker_flag[i]=checker_result[0]
            if cheker_flag[i]==1:
                ProgressionLogger(data_entry, action_sequence, states, answer_mapping[i], save_name, domain=domain, task=task, question=question, action_taken=action_taken, state_checker_response=checker_result[1], answer_form=answer_form)
                return i
            i+=1

        # If no choice matches, return 999 a
        # This ensures we always return a valid integer
        print(f"Warning: No matching choice found for question ID {data_entry['id']}. That indicates error")
        ProgressionLogger(data_entry, action_sequence, states, 999, save_name, domain=domain, task=task, question=question, action_taken=action_taken, state_checker_response="No matching choice found", answer_form=answer_form)
        return 0


def Progression(data_entry: dict, domain: str, task: str, answer_form:str, save_name: str, **kwargs) -> int:
    """
    Progress based on action and current state.
    If progression is successful, return 1, otherwise return 0.

    Parameters
    ----------
    data_entry : dict. The data entry of from benchmark.
    domain : str. ferry, swap, alfworld, logistics, rovers, goldminer, floortile,
    task : str. Applicability, Progression, Validation.
    answer_form : bool or mcq.
    save_name : str. The name for the log file.
    **kwargs : Additional arguments
    - model : LLM model.
    - url : base url from LLM provider.
    - api : api key from LLM provider.

    Returns
    -------
    For bool:
    - answer : int, 1=true, 0=false.
    For mcq:
    - choice number : int. 0=A, 1=B, 2=C, 3=D.
    """

    task_functions = {
        "Applicability": Executability_Progression,
        "Progression": State_Progression,
        "Validation": Validation_Progression,
    }

    if task not in task_functions:
        raise ValueError(f"Unsupported task: {task}")

    return task_functions[task](data_entry, domain, task, answer_form, save_name, **kwargs)



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
    - task : str. Applicability, Progression, Validation.
    - state_checker_response : str. The checker response from LLM.
    - action_taken: int. how many actions are executed
    -answer_form : str. bool or mcq.
    """

    log_data = {
        "question_id": data_entry["id"],
        "domain": kwargs.get('domain', None),
        "question": kwargs['question'],
        "initial_state": states[0],
        "action_sequence": action_sequence,
        "state_progression": states[1:],
        "action_taken": kwargs.get('action_taken', None),
        "state_checker_response" : kwargs.get('state_checker_response', 'NO STATE IS ENTERED'),
        "answer": answer,
        "label":data_entry['answer']
    }

    filename = f"{save_name}-{kwargs['domain']}-{kwargs['task']}-{kwargs['answer_form']}-response.jsonl"
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(log_data, ensure_ascii=False) + '\n')
    else:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_data, ensure_ascii=False) + '\n')




def BaselineEvaluation(data_entry: dict, domain: str, task: str, mode:str, answer_form:str, save_name: str, **kwargs) -> int:
    """
    0Shot, 0Shot-CoT ans 2Shot-CoT as baseline evaliation for benchmark

    Parameters
    ----------
    data_entry : dict. The data entry of from benchmark.
    domain : str. ferry, swap, logistics, rovers, goldminer, floortile, alfworld.
    task : str. Applicability, Progression, Validation.
    mode : str. `0shot`, `0Shot-CoT` or `2Shot-CoT`
    answer_form : str. bool or mcq.
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
    task_mapping={"Applicability": "2ShotCoT_app_exmaple", "Progression":"2ShotCoT_prog_exmaple", "Validation":"2ShotCoT_val_exmaple"}

    if mode=="0shot":
        prompt = (
            f"[Initial state]{data_entry['context']}\n"
            f"[Question]{data_entry['question']}\n"
            f"Answer the question based on the initial state. After your answer, return your final answer into a new paragraph as the end of your answer. The last paragraph should be like 'Final Answer: True/False'('Final Answer: A/B/C/D' for multiple choice questions). Besides, don't use any markdown formatting in your answer."
        )
    elif mode=="0Shot-CoT":
        prompt = (
            f"[Initial state]{data_entry['context']}\n"
            f"[Question]{data_entry['question']}\n"
            f"Answer the question based on the initial state. After your answer, return your final answer into a new paragraph as the end of your answer. The last paragraph should be like 'Final Answer: True/False'('Final Answer: A/B/C/D' for multiple choice questions). Besides, don't use any markdown formatting in your answer.\n"
            f"Let's think step by step."
        )
    else:
        prompt = (
            f"{DomainMapping[domain][task_mapping[task]]}\n"
            f"[Initial state]{data_entry['context']}\n"
            f"[Question]{data_entry['question']}\n"
            f"Based on the initial state, answer the question. Let's think step by step as examples above. After your answer, return your final answer into a new paragraph as the end of your answer. The last paragraph should be like 'Final Answer: True/False'('Final Answer: A/B/C/D' for multiple choice questions). Besides, don't use any markdown formatting in your answer."
        )

    #GET LLM ANSWER
    response = utils.RequestSender(prompt, model=kwargs.get("model", "null"), api_key=kwargs.get('api', "null"), base_url=kwargs.get('url', "null"))
    llm_label = utils.LabelExtracter(response, answer_form=answer_form)

    BaselineLogger(data_entry, response, llm_label, save_name, task, answer_form, domain=domain, mode=mode)

    return llm_label



def BaselineLogger(data_entry, answer, llm_label, save_name, task, answer_form, **kwargs) -> None:
    """
    Log baseline evaluation a data entry into a jsonl file.

    Parameters
    ----------
    data_entry : dict. Evaluated data
    answer : int. The final answer from LLM.
    llm_label : int. The predicted label from LLM, extracted from answer.
    save_name : str. The name for the log file.
    task : str. Applicability, Progression, Validation.
    answer_form : str. bool or mcq.
    **kwargs: Additional arguments
    - domain : str. depots, driverlog, grippers, mystery, satellite, spanner, visitall.
    - mode : str. '0Shot', '0Shot-CoT' or '2Shot-CoT'.
    """

    log_data = {
        "question_id": data_entry["id"],
        "domain": kwargs.get("domain", None),
        "question": data_entry["question"],
        "answer": answer,
        "llm_label": llm_label,
        "label":data_entry['answer']
    }

    filename = f"{save_name}-{kwargs['domain']}-{task}-{answer_form}-{kwargs['mode']}-response.jsonl"
  
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(log_data, ensure_ascii=False) + '\n')
    else:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_data, ensure_ascii=False) + '\n')




def Val_task_identifier(data_entry, answer_form):
    """
    Confirm the subtask in validation task. Returns plan, applicable, or valid.
    """
    if answer_form == "bool":
        question_str=data_entry["question"]
    else:
        question_str=data_entry["query"]

    end_quote_pos = question_str.rfind('"')

    if end_quote_pos != -1:
        suffix = question_str[end_quote_pos+1:]

        plan_match = re.search(r'\bplan\b', suffix.lower())
        applicable_match = re.search(r'\bapplicable\b', suffix.lower())
        valid_match = re.search(r'\bvalid\b', suffix.lower())
        goal_match = re.search(r'\bgoal\b', suffix.lower())

        if plan_match or goal_match:
            return "plan"
        elif applicable_match:
            return "applicable"
        elif valid_match:
            return "valid"

    plan_match = re.search(r'\bplan\b', question_str.lower())
    applicable_match = re.search(r'\bapplicable\b', question_str.lower())
    valid_match = re.search(r'\bvalid\b', question_str.lower())
    goal_match = re.search(r'\bgoal\b', question_str.lower())


    if plan_match or goal_match:
        return "plan"
    elif applicable_match:
        return "applicable"
    elif valid_match:
        return "valid"

    return "plan"


