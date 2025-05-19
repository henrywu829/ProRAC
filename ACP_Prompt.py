#-------------------------------------
#General Prompts
#-------------------------------------
ACTION_SEQUENCE_EXTRACTOR_PROMPT = f"You are required to extract actions from the given question. Your answer must satisfy all the following requirements. First, extract every action from the question like examples above. Second, in your answer, each sentence should contain only one action and sepated by a period. Third, organize all actions into one paragraph without any other content. Besides, don't use any markdown formatting. For example, from \"Is the following sequence of actions \"load the car c13 at location l1 on to the ferry, sail from location l1 to location l0, debark the car c13 from the ferry to location l0,\", you should extract \"load the car c13 at location l1 on to the ferry. sail from location l1 to location l0. debark the car c13 from the ferry to location l0\". Also, you don't need to extract content after choices A B C and D, just actions, not state."


GOAL_EXTRACTOR_PROMPT = f"You are required to think and understand the question above, and then extract goals from the given question. The goal is explicitly stated in the question. If the goal mentioned in the question doesn't explicitly related to objects' states, you should return the initial states of all objects as the goal. Your answer must satisfy all the following requirements. First, don't use any markdown formatting. Second, only answer the goal you extracted without any other content. Third, keep your answer into only one paragraph."


EXECUTABILITY_CHECKER_PROMPT = f"Based on the domain description and examples above, check whether this action is executable at current state. First, think and respond with the format from the example above, including the word choice and paragraph structure. After your analysis, give your final answer in the last paragraph, and the last paragraph should be like \"Final Answer: False(True if executable).\" Besides, don't use any markdown formatting."    
 
 
VALIDATION_CHECKER_PROMPT = f"Based on the domain description, check whether each action in this action sequence is defined in the domain description or not. An action is valid if and only if it is defined in the domain description above. The name of the action may vary slightly in expression as long as they express the same meaning. For example, 'board' and 'embark' can be considered the same action, 'sail' and 'travel by sea' can be considered as the same action. If all actions are valid, please return true. If any action in the action sequence is invalid, return false. Remember, you only need to consider whether each action is defined in the domain description, you don't need to check whether each action is executable or not. Only answer true or false without any other content. Besides, don't use any markdown formatting."
    
    
STATE_CHECKER_PROMPT = f"Above contents include current state and question. Based on the domain description and examples given above, check whether the question matches with the current state. Your answer must satisfy all the following requirements. First, think and respond with the format from the example above, including the word choice and paragraph structure. Second, don't use any markdown formatting. Third, After your analysis, you should tell me your final answer in the last paragraph, and organize the last paragraph with the format: \"Final Answer: True(False if not match)\"."


QUESTION_EXTRACTOR_PROMPT = f"Based on examples above, extract the question from the given content. Your answer should meet all the following conditions: First, extract the question as what exmaples do above, the question you extracted shbould not contain any action. Second, don't use any markdown formatiing. Third, you should only answer the extracted question without any other content in your answer."



#-------------------------------------
#Ferry Prompts
#-------------------------------------
FERRY_DOMAIN_DESCRIPTION = (
    f"[Domain Description]\n"
    f"The ferry domain involves a ferry and many cars. The task is to transport cars from their start to their goal locations, using a ferry. Each location is accessible by ferry from each other location. The cars can be debarked or boarded, and the ferry can carry only one car at a time.\n"
    f"For different objects we use different properties to deccribe its state. For ferry we use: at location l_x, has car c_x on board/empty. For car we use: at location l_x/on the ferry. \n"
    f"Following actions are executable only if all preconditions are met, if any condition are not satisfied, the action is not executable.\n"
    f"A car can be boarded(embark) on to the ferry at location A. This action is executable only if all following preconditions are satisfied: the car is at location A, the ferry is at location A, the ferry is empty.\n"
    f"A car can be debarked from the ferry to location A. This action is executable only if all following preconditions are satisfied: the car is on the ferry, the ferry is at location A.\n"
    f"The ferry can sail/travel from location A to location B. This action is executable only if all following preconditions are satisfied: the ferry is current at location A.\n"
    f"Executing an action will change states of related objects.\n"
    f"A car can be boarded(embark) on to the ferry at location A. This action will result in: the car is not at location A, the car is on the ferry, the ferry is not empty.\n"
    f"A car can be debarked from the ferry to location A. This action will result in: the car is not on the ferry, the car is at location A, the ferry is empty.\n"
    f"The ferry can sail/travel from location A to location B. This action will result in: the ferry is not at location A, the ferry is at location B.\n"
)


INITIAL_STATE_EXTRACTOR_FERRY_PROMPT = (
    f"This is a question related to the ferry domain. You are required to extract the initial state of every objects in this plan, including car and ferry. Your answer must satisfy all the following requirements. First, think and respond with the format from the example above, including the word choice and paragraph structure. Second, each object's state should contain all properties mentioned in the domain description above. Besides, don't use any markdown formatting."
)


INITIAL_STATE_EXTRACTOR_FERRY_EXAMPLE = (
    f"[Examples]\n "
    f"Initial state example 1: This is a ferry domain, where the task is to transport cars from their start to their goal locations, using a ferry. Each location is accessible by ferry from each other location. The cars can be debarked or boarded, and the ferry can carry only one car at a time. There are 2 locations and 20 cars, numbered consecutively. Currently, the ferry is at l1 location and it is empty. The cars are at locations as follows: c7, c11, c2, c16, c14, c19, c5, c4, c12, c17, and c1 are at l1; c13, c8, c6, c18, c0, c3, c9, c10, and c15 are at l0.\n"
    f"Extracted from example 1: \n"
    f"First, we confirm every object involved in the initial state. We can find 20 cars and one ferry here.\n"
    f"Then we extract each object's state.\n"
    f"Currently, the ferry is at l1 location and it is empty. ::: Ferry: at l1, empty.\n"
    f"c7, c11, c2, c16, c14, c19, c5, c4, c12, c17, and c1 are at l1 ::: c7: at l1. c11: at l1. c2: at l1. c16: at l1. c14: at l1. c19: at l1. c5: at l1. c4: at l1. c12: at l1. c17: at l1. c1: at l1.\n"
    f"c13, c8, c6, c18, c0, c3, c9, c10, and c15 are at l0. ::: c13: at l0. c8: at l0. c6: at l0. c18: at l0. c0: at l0. c3: at l0. c9: at l0. c10: at l0. c15: at l0.\n"
    f"Then, we organize all objects' state into a new paragraph as the end of the answer.\n"
    f"Ferry: at l1, empty. c7: at l1. c11: at l1. c2: at l1. c16: at l1. c14: at l1. c19: at l1. c5: at l1. c4: at l1. c12: at l1. c17: at l1. c1: at l1. c13: at l0. c8: at l0. c6: at l0. c18: at l0. c0: at l0. c3: at l0. c9: at l0. c10: at l0. c15: at l0.\n"
    f"-------------------\n"
    f"Initial state example 2: This is a ferry domain, where the task is to transport cars from their start to their goal locations, using a ferry. Each location is accessible by ferry from each other location. The cars can be debarked or boarded, and the ferry can carry only one car at a time. There are 2 locations and 10 cars, numbered consecutively. Currently, the ferry is at l1, with the car c0 on board. The cars are at locations as follows: c6, c3, c9, c1, c8, and c5 are at l0; c4, c7, and c2 are at l1.\n"
    f"Extracted from example 2: \n"
    f"First, we confirm every object involved in the initial state. We can find 10 cars and one ferry here.\n"
    f"Then we extract each object's state.\n"
    f"Currently, the ferry is at l1, with the car c0 on board. ::: Ferry: at l1, has c0 on board. c0: on the ferry.\n"
    f"c6, c3, c9, c1, c8, and c5 are at l0 ::: c6: at l0. c3: at l0. c9: at l0. c1: at l0. c8: at l0. c5: at l0. \n"
    f"c4, c7, and c2 are at l1. ::: c4: at l1. c7: at l1. c2: at l1.\n"
    f"Then, we organize all objects' state into a new paragraph as the end of the answer.\n"
    f"Ferry: at l1, has c0 on board. c0: on the ferry. c6: at l0. c3: at l0. c9: at l0. c1: at l0. c8: at l0. c5: at l0. c4: at l1. c7: at l1. c2: at l1.\n"
    f"-------------------\n"
)


ACTION_SEQUENCE_EXTRACTOR_FERRY_PROMPT = (
    f"[Examples]\n"
    f"Action example 1: Is the following action applicable in this state: travel by sea from location l1 to location l0?\n"
    f"Extracted from example 1: travel by sea from location l1 to location l0.\n"
    f"-------------------\n"
    f"Action example 2: Is the following action applicable in this state: debark the car c1 from the ferry to location l0?\n"
    f"Extracted from example 2: debark the car c1 from the ferry to location l0.\n"
    f"-------------------\n"
)


QUESTION_EXTRACTOR_FERRY_EXAMPLE = (
    f"[Examples]"
    f"Question example 1: Will the fact \"The ferry is empty\" hold after performing the action \"embark the car c0 at location l1 on to the ferry\" in the current state?"
    f"Extracted from example 1: Will the fact \"The ferry is empty\" hold?\n"
    f"-------------------\n"
    f"Question example 2: Will the fact \"Ferry has car c0 on board\" hold after performing the action \"debark car c0 to location l0 from the ferry\" in the current state?\n"
    f"Extracted from example 2: Will the fact \"Ferry has car c0 on board\" hold?\n"
    f"-------------------\n"
    f"Question example 3: Will the fact \"Car c1 is at location l0\" hold after performing the action \"load the car c1 at location l3 on to the ferry\" in the current state?\n"
    f"Extracted from example 3: Will the fact \"Car c1 is at location l0\" hold?\n"
    f"-------------------\n"
)


ACTION_TAKER_FERRY_PROMPT = (
     f"Based on the domain description and examples above, take the action and return the new state of all objects. Your answer must satisfy all the following requirements. First, think and respond like examples above, you are required to return states of all objects(the ferry and cars), including states that are not effected by the action. Second, each object's state must contain all properties mentioned in the domain description above. Third, after your analysis, please return states of all objects into a new paragraph as the end of your answer. Your final paragraph should use the format like: \"c1: on the ferry. c7: at l0.\" Besides, don't use any markdown formatting."
)


ACTION_TAKER_FERRY_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: Ferry: at l1, has c1 on board. c1: on the ferry. c7: at l0. c9: at l0. c8: at l0. c0: at l0. c4: at l0. c6: at l0. c3: at l1. c5: at l1. c2: at l1.\n"
    f"Action 1: sail from location l1 to location l0\n"
    f"Answer 1:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Ferry: at l1, has c1 on board.\n"
    f"Based on the domain description, the ferry can sail/travel from location A to location B. This action will result in: the ferry is not at location A, the ferry is at location B.\n"
    f"the ferry is not at location A, the ferry is at location B. ::: Ferry: at l0, has c1 on board.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into a paragraph as the end of answer.\n"
    f"Ferry: at l0, has c1 on board. c1: on the ferry. c7: at l0. c9: at l0. c8: at l0. c0: at l0. c4: at l0. c6: at l0. c3: at l1. c5: at l1. c2: at l1.\n"
    f"-------------------\n"
    f"Current state example 2: Ferry: at l1, empty. c9: at l0. c8: at l0. c0: at l0. c4: at l0. c3: at l0. c6: at l0. c1: at l1. c7: at l1. c5: at l1. c2: at l1.\n"
    f"Action 2:embark the car c7 at location l1 on to the ferry.\n"
    f"Answer 3:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Ferry: at l1, empty. c7: at l1.\n"
    f"Based on the domain description, a car can be boarded(embark) on to the ferry at location A. This action will result in: the car is not at location A, the car is on the ferry, the ferry is not empty.\n"
    f"the car is not at location A, the car is on the ferry the ferry is not empty. ::: Ferry: at l1, has c7 on board. c7: on the ferry.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into a paragraph as the end of answer.\n"
    f"Ferry: at l1, has c7 on board. c7: on the ferry. c9: at l0. c8: at l0. c0: at l0. c4: at l0. c3: at l0. c6: at l0. c1: at l1. c5: at l1. c2: at l1.\n"
    f"-------------------\n"
    f"Current state example 3: Ferry: at l1, has c1 on board. c1: on the ferry. c0: at l1. c2: at l0.\n"
    f"Action 3:debark c1 from the ferry to l1\n"
    f"Answer 3:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Ferry: at l1, has c1 on board. c1: on the ferry.\n"
    f"Based on the domain description, a car can be debarked from the ferry to location A. This action will result in: the car is not on the ferry, the car is at location A, the ferry is empty.\n"
    f"the car is not on the ferry, the car is at location A, the ferry is empty. ::: Ferry: at l1, empty. c1: at l1.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into a paragraph as the end of answer.\n"
    f"Ferry: at l1, empty. c1: at l1. c0: at l1. c2: at l0.\n"
    f"-------------------\n"

)


EXECUTABILITY_CHECKER_FERRY_EXAMPLE =(
    f"[Examples]\n"
    f"Current state example 1: Ferry: at l1, has c1 on board. c1: on the ferry. c0: at l1. c2: at l0.\n"
    f"Action 1:embark the car c1 at location l1 on to the ferry\n"
    f"Answer 1:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can check whether the action is executable.\n"
    f"Ferry: at l1, has c1 on board. c1: on the ferry.\n"
    f"Based on the domain description, a car can be boarded(embark) on to the ferry at location A. This action is executable only if all following preconditions are satisfied: the car is at location A, the ferry is at location A, the ferry is empty.\n"
    f"the car is at location A, ::: c1: on the ferry. ===> NOT SATISFY\n"
    f"Since not all preconditions are satisfied, this action is not executable.\n"
    f"Final Answer: False."
    f"-------------------\n"
    f"Current state example 2: Ferry: at l1, has c1 on board. c1: on the ferry. c0: at l1. c2: at l0. c3: at l0. c4: at l1. c2: at l1.\n"
    f"Action 2:debark c1 from the ferry to l1\n"
    f"Answer 2:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can check whether the action is executable.\n"
    f"Ferry: at l1, has c1 on board. c1: on the ferry.\n"
    f"Based on the domain description, a car can be debarked from the ferry to location A. This action is executable only if all following preconditions are satisfied: the car is on the ferry, the ferry is at location A.\n"
    f"the car is on the ferry, ::: c1: on the ferry. ===> SATISFY\n"
    f"the ferry is at location A, ::: Ferry: at l1, has c1 on board. ===> SATISFY\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final answer: True.\n"
    f"-------------------\n"
    f"Current state example 3: Ferry: at l1, empty. c1: at l0. c0: at l1. c2: at l0. c3: at l0. c4: at l1. c2: at l1.\n"
    f"Action 3:sail from location l1 to location l0\n"
    f"Answer 3:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can check whether the action is executable.\n"
    f"Ferry: at l1, empty.\n"
    f"Based on the domain description, the ferry can sail/travel from location A to location B. This action is executable only if all following preconditions are satisfied: the ferry is current at location A.\n"
    f"the ferry is current at location A, ::: Ferry: at l1, empty. ===> SATISFY\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final answer: True.\n"
    f"-------------------\n"
)


STATE_CHECKER_FERRY_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: Ferry: at l2, empty. c0: at l0. c1: at l2.\n"
    f"Question 1: Will the fact \"The ferry is empty\" hold?\n"
    f"Answer 1:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. \n"
    f"The ferry is empty ::: Ferry: at l2, empty. ===>SATISFY"
    f"Since all propositions in the question match with the curent state, so the question is true.\n"
    f"Final Answer: True.\n"
    f"-------------------\n"
    f"Current state example 2: Ferry: at l1, empty. c14: at l0. c8: at l0. c15: at l0. c1: at l0. c6: at l0. c17: at l0. c3: at l0. c18: at l0. c10: at l0. c16: at l0. c11: at l0. c0: at l0. c9: at l0. c2: at l0. c5: at l1. c4: at l1. c7: at l1. c12: at l1. c19: at l1. c13: at l1.\n"
    f"Question 2: Car c10 is at location l0 and Car c14 is at location l1.\n"
    f"Answer 2:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. \n"
    f"Car c10 is at location l0 ::: c10: at l0. ===>SATISFY\n"
    f"Car c14 is at location l1 ::: c14: at l0. ===>NOT SATISFY\n"
    f"Since not all propositions in the question match with the curent state, so the question is true.\n"
    f"Final Answer: False.\n"
    f"-------------------\n"
)


TWOSHOTCOT_APP_FERRY_EXAMPLE = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"Initial State: This is a ferry domain, where the task is to transport cars from their start to their goal locations, using a ferry. Each location is accessible by ferry from each other location. The cars can be debarked or boarded, and the ferry can carry only one car at a time. There are 3 locations and 10 cars, numbered consecutively. Currently, the ferry is at l0, with the car c4 on board. The cars are at locations as follows: c0, c1, and c3 are at l1; c2, c5, and c6 are at l2; c7, c8, and c9 are at l0.\n"
    f"Question: Is the following action applicable in this state: board the car c1 onto the ferry at location l0?"
    f"Answer:\n"
    f"Step 1: we find related objects in the current state.\n"
    f"the ferry is at l0, with the car c4 on board. c0, c1, and c3 are at l1\n"
    f"Step 2: we check whether the action is applicable. \n"
    f"A car can be boarded on the ferry only if the car and the ferry are both at the same location, and the ferry is empty. We can see ferry is at l0 and c1 is at l1. So this action is not executable.\n"
    f"Step 3: We return our answer based on previous analysis. \n"
    f"Final Answer: False.\n"
    f"-------------------\n"
    f"(Example 2)\n"
    f"Initial state: This is a ferry domain, where the task is to transport cars from their start to their goal locations, using a ferry. Each location is accessible by ferry from each other location. The cars can be debarked or boarded, and the ferry can carry only one car at a time. There are 4 locations and 20 cars, numbered consecutively. Currently, the ferry is at l1, with the car c5 on board. The cars are at locations as follows: c0, c3, c4, c7, and c8 are at l0; c1, c2, c6, c9, and c10 are at l1; c11, c12, c13, c14, and c15 are at l2; c16, c17, c18, and c19 are at l3."
    f"Question: Which of the following actions will be applicable in this state? A. embark the car c10 at location l1 on to the ferry. B. debark car c5 to location l1 from the ferry. C. embark the car c14 at location l2 on to the ferry. D. debark car c7 to location l0 from the ferry."
    f"Answer:\n"
    f"Step 1: We check each option one by one. \n"
    f"Option A: embark the car c10 at location l1 on to the ferry. A car can be boarded on the ferry only if the car and the ferry are both at the same location, and the ferry is empty. We can see ferry is at l1 and c10 is at l1. However, the ferry is not empty. So this action is not executable.\n"
    f"Option B: debark car c5 to location l1 from the ferry. A car can be debarked from the ferry only if the car is on the ferry and the ferry is at the location. We can see ferry now has c5 on board, the ferry is at l1. So this action is executable.\n"
    f"Step 2: We return our answer based on previous analysis. \n"
    f"Final Answer: B.\n"
    f"-------------------\n"
)


TWOSHOTCOT_PROG_FERRY_EXAMPLE = (
    f"[Examples]\n"
    f"(example 1)\n"
    f"Initial state: This is a ferry domain, where the task is to transport cars from their start to their goal locations, using a ferry. Each location is accessible by ferry from each other location. The cars can be debarked or boarded, and the ferry can carry only one car at a time. There are 4 locations and 4 cars, numbered consecutively. Currently, the ferry is at l1 location and it is carrying car c0. The cars are at locations as follows: c1 and c3 are at l2; c2 is at l3.\n"
    f"Question: Will the fact \"Car c0 is at location l1\" hold after performing the action \"debark car c0 to location l1 from the ferry\" in the current state?\n"
    f"Answer 1:\n"
    f"Step 1: Take the action and get the new state.\n"
    f"Debark car c0 to location l1 from the ferry. After this action, the ferry is empty and c0 is at l1.\n"
    f"Step 2: Check whether the fact hold.\n"
    f"c0 is at l1, so the fact holds.\n"
    f"Step 3: We return our answer based on previous analysis.\n"
    f"Final Answer: True.\n"
    f"-------------------\n"
    f"(example 2)\n"
    f"Initial state: This is a ferry domain, where the task is to transport cars from their start to their goal locations, using a ferry. Each location is accessible by ferry from each other location. The cars can be debarked or boarded, and the ferry can carry only one car at a time. There are 4 locations and 8 cars, numbered consecutively. Currently, the ferry is at l2 location and it is carrying car c5. The cars are at locations as follows: c0, c1, and c2 are at l0; c3 is at l1; c4, c6, and c7 are at l3."
    f"Question: Which of the following facts hold after performing the action \"debark car c5 to location l2 from the ferry\" in the current state? A. Car c4 is on the ferry. B. Car c5 is still on the ferry. C. The ferry is at location l0. D. Car c5 is at location l2."
    f"Step 1: Take the action and get the new state.\n"
    f"debark car c5 to location l2 from the ferry. After this action, the ferry is empty and c5 is at l2.\n"
    f"Step 2: Check each option to find the answer.\n"
    f"Option A: Car c4 is on the ferry. We can see c4 is at l3, so this fact does not hold.\n"
    f"Option B: Car c5 is still on the ferry. We can see c5 is not on the ferry, so this fact does not hold.\n"
    f"Option C: The ferry is at location l0. We can see the ferry is at l2, so this fact does not hold.\n"
    f"Option D: Car c5 is at location l2. We can see c5 is at l2, so this fact holds.\n"
    f"Step 3: We return our answer based on previous analysis.\n"
    f"Final Answer: D.\n"
    f"-------------------\n"
)


TWOSHOTCOT_VAL_FERRY_EXAMPLE = (
    f"[Examples]\n"
    f"(example 1)\n"
    f"Initial state: This is a ferry domain, where the task is to transport cars from their start to their goal locations, using a ferry. Each location is accessible by ferry from each other location. The cars can be debarked or boarded, and the ferry can carry only one car at a time. There are 3 locations and 3 cars, numbered consecutively. Currently, the ferry is at l0 location and it is empty. The cars are at locations as follows: c0 is at l0; c1 is at l1; c2 is at l2. The goal is to reach a state where the following facts hold: Car c0 is at location l2, Car c1 is at location l1, and Car c2 is at location l2.\n"
    f"Question: Is the following sequence of actions \"board the car c0 at the location l0, travel by sea from location l0 to location l2, debark car c0 to location l2 from the ferry\" valid in this problem?"
    f"Answer:\n"
    f"Step 1: Since the question askes the vailidity of the action, we only need to check whether all actions are valid, we don't need to consider whether they are executable or not.\n"
    f"Board, travel, debark, all these actions are valid in the ferry domain. So the action sequence is valid.\n"
    f"Step 2: We return our answer based on previous analysis.\n"
    f"Final Answer: True.\n"
    f"-------------------\n"
    f"(example 2)\n"
    f"Initial state: This is a ferry domain, where the task is to transport cars from their start to their goal locations, using a ferry. Each location is accessible by ferry from each other location. The cars can be debarked or boarded, and the ferry can carry only one car at a time. There are 3 locations and 2 cars, numbered consecutively. Currently, the ferry is at l1 location and it is empty. The cars are at locations as follows: c0 is at l1; c1 is at l2. The goal is to reach a state where the following facts hold: Car c0 is at location l2 and Car c1 is at location l1.\n"
    f"Question: Which of the following claims is true with regard to the following sequence of actions \"embark the car c0 at location l1 on to the ferry, travel by sea from location l1 to location l2, debark the car c0 from the ferry to location l2.\"  A. The sequence is not valid. B. The sequence is a plan. C. The sequence is applicable, but does not achieve the goal. D. The sequence is not applicable."
    f"Answer:\n"
    f"Step 1: Since the question ask whether the action sequence is a plan, we need to take actions to reach the fianl answer, then check the goal.\n"
    f"embark the car c0 at location l1 on to the ferry, after this action, the ferry is at l1, has c0 on board.\n"
    f"travel by sea from location l1 to location l2, after this action, the ferry is at l2.\n"
    f"debark the car c0 from the ferry to location l2, after this action, the c0 is at l2 and the ferry is empty.\n"
    f"Step 2: We check whether the goal is reached.\n"
    f"The goal is to reach a state where the following facts hold: Car c0 is at location l2 and Car c1 is at location l1. We can see c0 is at l2, but c1 is at l2, so the goal is not reached. So this is not a plan.\n"
    f"Final Answer: C.\n"
    f"-------------------\n"
)



#-------------------------------------
#Swap Prompts
#-------------------------------------
SWAP_DOMAIN_DESCRIPTION = (
    f"[Domain Description]\n"
    f"The swap domain involves many agents swapping their roles/items. Each agent can be assigned a single role/item at a time. We use following properties to describe the state of an agent: is assigned item_x/role_x. Besides, an agent can swap role/item with itself, this is also legal.\n"
    f"Following actions are executable only if all preconditions are met, if any condition are not satisfied, the action is not executable.\n"
    f"Agent A with item/role x can swap(trade/switch) role/item with agent B with item/role y. This action is executable only if all following preconditions are satisfied: the agent A is assigned item/role x, the agent B is assigned item/role y. If agent A and agent B are the same agent, then the action is executable only if the item/role x and y are the same.\n"
    f"Executing an action will change states of related objects.\n"
    f"Agent A with item/role x can swap role/item with agent B with item/role y. This action will result in: the agent A is assigned item/role y, the agent B is assigned item/role x.\n"
)


INITIAL_STATE_EXTRACTOR_SWAP_PROMPT = (
    f"This is a question related to the swap domain. You are required to extract the initial state of every agents in this plan. Your answer must satisfy all the following requirements. First, think and respond with the format from the example above, including the word choice and paragraph structure. Second, each object's state should contain all properties mentioned in the domain description above. Besides, don't use any markdown formatting.\n"
)


ACTION_SEQUENCE_EXTRACTOR_SWAP_PROMPT = (
    f"[Examples]\n"
    f"Action example 1: Is the following action applicable in this state: swap dave:mushroom with alice:valerian?\n"
    f"Extracted from example 1: swap dave:mushroom with alice:valerian.\n"
    f"-------------------\n"
    f"Action example 2: Is the following action applicable in this state: trade ratchet of bob for knead of quentin?\n"
    f"Extracted from example 2: trade ratchet of bob for knead of quentin.\n"
    f"-------------------\n"
    f"Action example 3: Is the following action applicable in this state: swap ted with kevin, valerian for valerian?\n"
    f"Extracted from example 3: swap ted:valerian with kevin:valerian.\n"
    f"-------------------\n"
    f"Action example 4: Is the following action applicable in this state: swap quentin with bob, pliers for pliers?\n"
    f"Extracted from example 4: swap quentin:pliers with bob:pliers.\n"
    f"-------------------\n"
    f"Action example 5: Which fact will hold after performing the action \"trade zebra of michelle for frisbee of zoe\" in the current state?\n"
    f"Extracted from example 5: trade zebra of michelle for frisbee of zoe.\n"
    f"-------------------\n"
)


INITIAL_STATE_EXTRACTOR_SWAP_EXAMPLE = (
    f"[Examples]\n"
    f"Initial state example 1: This is a swap domain where agents are swapping items or roles. Each agent is always assigned a single item/role. The goal is to obtain desired items/roles assigned. There are 7 agents: ted, xena, kevin, bob, dave, heidi, and alice. There are 7 items/roles: leek, parsnip, quince, yam, mushroom, valerian, and ulluco. Currently, kevin is assigned yam, dave is assigned ulluco, bob is assigned parsnip, alice is assigned valerian, ted is assigned leek, heidi is assigned quince, and xena is assigned mushroom.\n"
    f"Extracted from example 1: \n"
    f"First, we confirm every object involved in the initial state. We can find 7 agents and 7 items/roles.\n"
    f"Then we extract each object's state.\n"
    f"kevin is assigned yam, dave is assigned ulluco, bob is assigned parsnip, alice is assigned valerian, ted is assigned leek, heidi is assigned quince, and xena is assigned mushroom. ::: kevin: is assigned yam. dave: is assigned ulluco. bob: is assigned parsnip. alice: is assigned valerian. ted: is assigned leek. heidi: is assigned quince. xena: is assigned mushroom.\n"
    f"Then, we organize all objects' state into a new paragraph as the end of the answer.\n"
    f"kevin: is assigned yam. dave: is assigned ulluco. bob: is assigned parsnip. alice: is assigned valerian. ted: is assigned leek. heidi: is assigned quince. xena: is assigned mushroom.\n"
    f"-------------------\n"
    f"Initial state example 2: This is a swap domain where agents are swapping items or roles. Each agent is always assigned a single item/role. The goal is to obtain desired items/roles assigned. There are 4 agents: zoe, bob, steve, and vic. There are 4 items/roles: book03, book04, book01, and book02. Currently, bob is assigned book01, zoe is assigned book04, vic is assigned book03, and steve is assigned book02. The goal is to reach a state where the following facts hold: bob is assigned book02, vic is assigned book04, steve is assigned book03, and zoe is assigned book01.\n"
    f"Extracted from example 2: \n"
    f"First, we confirm every object involved in the initial state. We can find 4 agents and 4 items/roles.\n"
    f"Then we extract each object's state.\n"
    f"bob is assigned book01, zoe is assigned book04, vic is assigned book03, and steve is assigned book02. ::: bob: is assigned book01. zoe: is assigned book04. vic: is assigned book03. steve: is assigned book02.\n"
    f"Then, we organize all objects' state into a new paragraph as the end of the answer.\n"    
    f"bob: is assigned book01. zoe: is assigned book04. vic: is assigned book03. steve: is assigned book02.\n"
    f"-------------------\n"
)


QUESTION_EXTRACTOR_SWAP_EXAMPLE =(
    f"[Examples]\n"
    f"Question example 1: Will the fact \"vic is assigned knead\" hold after performing the action \"swap bob with vic, ratchet for knead\" in the current state?\n"
    f"Extracted form example 1: Will the fact \"vic is assigned knead\" hold?\n"
    f"-------------------\n"
    f"Question example 2: Will the fact \"kevin is assigned mushroom\" hold after performing the action \"trade leek of dave for mushroom of kevin\" in the current state?\n"
    f"Extracted from example 2: Will the fact \"kevin is assigned mushroom\" hold?\n"
    f"-------------------\n"
)


ACTION_TAKER_SWAP_PROMPT = (
    f"Based on the domain description and examples above, take the action and return the new state of all objects. Your answer must satisfy all the following requirements. First, think and respond like examples above, you are required to return states of all agnets, including states that are not effected by the action. Second, each object's state must contain all properties mentioned in the domain description above. Third, after your analysis, please return states of all objects into a new paragraph as the end of your answer. Your final paragraph should use the format like: \"kevin: is assigned mushroom. ton: is assigned with book2.\" Besides, don't use any markdown formatting."
)


ACTION_TAKER_SWAP_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: bob: is assigned book01. zoe: is assigned book04. vic: is assigned book03. steve: is assigned book02.\n"
    f"Action 1: swap steve:book02 with vic:book03\n"
    f"Answer 1:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"steve: is assigned book02. vic: is assigned book03.\n"
    f"Based on the domain description, agent A with item/role x can swap role/item with agent B with item/role y. This action will result in: the agent A is assigned item/role y, the agent B is assigned item/role x.\n"
    f"the agent A is assigned item/role y, the agent B is assigned item/role x. ::: steve: is assigned book03. vic: is assigned book02.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into a paragraph as the end of answer.\n"
    f"bob: is assigned book01. zoe: is assigned book04. steve: is assigned book03. vic: is assigned book02.\n"
    f"-------------------\n"
)


EXECUTABILITY_CHECKER_SWAP_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: bob: is assigned book01. zoe: is assigned book04. vic: is assigned book03. steve: is assigned book02.\n"
    f"Action 1: swap steve:book02 with vic:book03.\n"
    f"Answer 1:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can check whether the action is executable.\n"
    f"steve: is assigned book02. vic: is assigned book03.\n"
    f"Based on the domain description, agent A with item/role x can swap role/item with agent B with item/role y. This action is executable only if all following preconditions are satisfied: the agent A is assigned item/role x, the agent B is assigned item/role y.\n"
    f"the agent A is assigned item/role x, the agent B is assigned item/role y. ::: steve: is assigned book02. vic: is assigned book03. ===> SATISFY\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final answer: True.\n"
    f"-------------------\n"
    f"Current state example 2: vic: is assigned necklace. heidi: is assigned guitar. zoe: is assigned slinky. michelle: is assigned quadcopter. dave: is assigned iceskates. xena: is assigned whale. carol: is assigned frisbee. alice: is assigned zebra.\n"
    f"Action 2: Trade necklace of carol for zebra of alice.\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can check whether the action is executable.\n"
    f"carol: is assigned frisbee. alice: is assigned zebra.\n"    
    f"Based on the domain description, agent A with item/role x can swap role/item with agent B with item/role y. This action is executable only if all following preconditions are satisfied: the agent A is assigned item/role x, the agent B is assigned item/role y.\n"
    f"the agent A is assigned item/role x, the agent B is assigned item/role y. ::: carol: is assigned frisbee. alice: is assigned zebra.  ===> NOT SATISFY\n"
    f"Since not all preconditions are satisfied, this action is not executable.\n"
    f"Final Answer: False.\n"
    f"-------------------\n"
    f"Current state example 3: liam: is assigned mushroom. vic: is assigned pliers. frank: is assigned nibbler. bob: is assigned sander. xena: is assigned ratchet. quentin: is assigned wrench.\n"
    f"Action 3: swap vic with quentin, wrench for ratchet\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can check whether the action is executable.\n"
    f"vic: is assigned pliers. quentin: is assigned wrench.\n"
    f"Based on the domain description, agent A with item/role x can swap role/item with agent B with item/role y. This action is executable only if all following preconditions are satisfied: the agent A is assigned item/role x, the agent B is assigned item/role y.\n"
    f"the agent A is assigned item/role x, the agent B is assigned item/role y. ::: vic: is assigned pliers. quentin: is assigned wrench.  ===> NOT SATISFY\n"
    f"Since not all preconditions are satisfied, this action is not executable.\n"
    f"Final Answer: False.\n"
    f"-------------------\n"
    f"Current state example 4: bob: is assigned bike. zoe: is assigned book04. vic: is assigned apple. steve: is assigned book02.\n"
    f"Action 4: swap steve:apple with steve:book2\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can check whether the action is executable.\n"
    f"steve: is assigned book02. \n"
    f"Based on the domain description, agent A with item/role x can swap role/item with agent B with item/role y. This action is executable only if all following preconditions are satisfied: the agent A is assigned item/role x, the agent B is assigned item/role y.\n"
    f"the agent A is assigned item/role x, the agent B is assigned item/role y. ::: steve: is assigned book02. steve: is assigned book02.  ===> SATISFY\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final Answer: True.\n"
    f"-------------------\n"
)


STATE_CHECKER_SWAP_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: vic: is assigned necklace. heidi: is assigned guitar. zoe: is assigned slinky. michelle: is assigned quadcopter. dave: is assigned iceskates. xena: is assigned whale. carol: is assigned frisbee. alice: is assigned zebra.\n"
    f"Question 1: Will the fact \"vic is assigned knead\" hold?\n"
    f"Answer 1:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. \n"
    f"vic: is assigned necklace.\n"
    f"vic is assigned knead ::: vic: is assigned necklace. ===> NOT SATISFY\n"
    f"Since there are some propositions in the question doesn't match with the current state, the question is false.\n"
    f"Final Answer: False.\n"
    f"-------------------\n"
    f"Current state example 2: bob: is assigned book01. zoe: is assigned book04. vic: is assigned book03. steve: is assigned book02.\n"
    f"Question 2: Will the fact \"bob is assigned book01\" hold?\n"
    f"Answer 2:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. \n"
    f"bob: is assigned book01.\n"
    f"bob is assigned book01 ::: bob: is assigned book01. ===> SATISFY\n"
    f"Since all propositions in the question match with the curent state, so the question is true.\n"
    f"Final Answer: True.\n"
    f"-------------------\n"
)


TWOSHOTCOT_APP_SWAP_EXAMPLE = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"Initial State: This is a swap domain where agents are swapping items or roles. Each agent is always assigned a single item/role. The goal is to obtain desired items/roles assigned. There are 6 agents: liam, xena, vic, bob, quentin, and frank. There are 6 items/roles: sander, nibbler, pliers, knead, wrench, and ratchet. Currently, vic is assigned knead, bob is assigned nibbler, xena is assigned wrench, frank is assigned ratchet, liam is assigned sander, and quentin is assigned pliers.\n"
    f"Question: Is the following action applicable in this state: swap liam:sander with quentin:pliers?\n"
    f"Answer:\n"
    f"Step 1: we find related objects in the current state.\n"
    f"liam is assigned sander, quentin is assigned pliers.\n"
    f"Step 2: we check whether the action is applicable.\n"
    f"agent A with item/role x can swap role/item with agent B with item/role y. This action is applicable only if all following preconditions are satisfied: the agent A is assigned item/role x, the agent B is assigned item/role y.\n"
    f"the agent A is assigned item/role x, the agent B is assigned item/role y. ::: liam is assigned sander, quentin is assigned pliers.  ===> SATISFY\n"
    f"Since all preconditions are satisfied, this action is applicable.\n"
    f"Step 3: We return our answer based on previous analysis. \n"
    f"Final Answer: True.\n"
    f"-------------------\n"
    f"(Example 2)\n"
    f"Current state: This is a swap domain where agents are swapping items or roles. Each agent is always assigned a single item/role. The goal is to obtain desired items/roles assigned. There are 6 agents: liam, xena, vic, bob, quentin, and frank. There are 6 items/roles: sander, nibbler, pliers, knead, wrench, and ratchet. Currently, vic is assigned knead, bob is assigned nibbler, xena is assigned wrench, frank is assigned ratchet, liam is assigned sander, and quentin is assigned pliers.\n"
    f"Is the following action applicable in this state: swap bob:sander with frank:pliers?\n"
    f"Answer:\n"
    f"Step 1: we find related objects in the current state.\n"
    f"bob is assigned nibbler, frank is assigned ratchet.\n"
    f"Step 2: we check whether the action is applicable.\n"
    f"agent A with item/role x can swap role/item with agent B with item/role y. This action is applicable only if all following preconditions are satisfied: the agent A is assigned item/role x, the agent B is assigned item/role y.\n"
    f"the agent A is assigned item/role x, the agent B is assigned item/role y. ::: bob is assigned nibbler, frank is assigned ratchet.  ===> NOT SATISFY\n"
    f"Since not all preconditions are satisfied, this action is not applicable.\n"
    f"Step 3: We return our answer based on previous analysis. \n"
    f"Final Answer: False.\n"
    f"-------------------\n"
)


TWOSHOTCOT_PROG_SWAP_EXAMPLE = (
    F"[Examples]\n"
    f"(example 1)\n"
    f"Initial state: This is a swap domain where agents are swapping items or roles. Each agent is always assigned a single item/role. The goal is to obtain desired items/roles assigned. There are 8 agents: carol, dave, heidi, vic, alice, michelle, zoe, and xena. There are 8 items/roles: iceskates, slinky, zebra, frisbee, necklace, quadcopter, whale, and guitar. Currently, zoe is assigned iceskates, carol is assigned frisbee, alice is assigned quadcopter, michelle is assigned zebra, dave is assigned slinky, xena is assigned whale, vic is assigned guitar, and heidi is assigned necklace.\n"
    f"Question: Will the fact \"carol is assigned zebra\" hold after performing the action \"trade zebra of michelle for frisbee of carol\" in the current state?\n"
    f"Answer:\n"
    f"Step 1: Take the action and get the new state.\n"
    f"Trade zebra of michelle for frisbee of carol. After taking this action, the michelle is assigned frisbee and the carol is assigned zebra.\n"
    f"Step 2: Check whether the fact hold.\n"
    f"carol is assigned zebra. We can see now the carol is assigned zebra. So this fact is held.\n"
    f"Step 3: We return our answer based on previous analysis.\n"
    f"Final Answer: True.\n"
    f"-------------------\n"
    f"(example 2)\n"
    f"Initial state: This is a swap domain where agents are swapping items or roles. Each agent is always assigned a single item/role. The goal is to obtain desired items/roles assigned. There are 8 agents: zoe, heidi, alice, carol, vic, michelle, dave, and xena. There are 8 items/roles: quadcopter, zebra, frisbee, slinky, necklace, whale, guitar, and iceskates. Currently, alice is assigned whale, xena is assigned slinky, heidi is assigned necklace, carol is assigned zebra, vic is assigned quadcopter, zoe is assigned frisbee, michelle is assigned guitar, and dave is assigned iceskates.\n"
    f"Question: Which of the following facts hold after performing the action \"exchange quadcopter of vic with frisbee of zoe\" in the current state? A.zoe is assigned quadcopter and vic is assigned frisbee. B.zoe is assigned guitar and vic is assigned necklace. C.michelle is assigned quadcopter and vic is assigned guitar. D.zoe is assigned frisbee and vic is assigned quadcopter\n"
    f"Step 1: Take the action and get the new state.\n"
    f"Exchange quadcopter of vic with frisbee of zoe. After taking the action, vic is assigned frisbee and zoe is assigned quadcopter.\n"
    f"Step 2: Check each option to find the answer.\n"
    f"Option A: zoe is assigned quadcopter and vic is assigned frisbee. We can see now the zoe is assigned quadcopter and vic is assigned frisbee. So this option is correct.\n"
    f"Step 3: We return our answer based on previous analysis.\n"
    f"Final Answer: A.\n"
    f"-------------------\n"
)
    

TWOSHOTCOT_VAL_SWAP_EXAMPLE = (
    F"[Examples]\n"
    f"(example 1)\n"
    f"Initial state: This is a swap domain where agents are swapping items or roles. Each agent is always assigned a single item/role. The goal is to obtain desired items/roles assigned. There are 4 agents: zoe, vic, bob, and steve. There are 4 items/roles: book02, book03, book04, and book01. Currently, bob is assigned book01, steve is assigned book02, vic is assigned book03, and zoe is assigned book04. The goal is to reach a state where the following facts hold: vic is assigned book04, zoe is assigned book01, steve is assigned book03, and bob is assigned book02.\n"
    f"Question: Is the following sequence of actions \"exchange book04 of zoe with book02 of steve, exchange book01 of bob with book04 of vic, exchange book03 of vic with book02 of zoe\" applicable in the current state?\n"
    f"Answer:\n"
    f"Step 1: Since the question ask whether the action sequence is applicable, we need to check whether every action is applicable under the current state. If applicable, we take the action and get the new state. If not, we stop and return the final answer.\n"
    f"Action 1: exchange book04 of zoe with book02 of steve. We find related objects in the current state. zoe is assigned book01, steve is assigned book03. agent A with item/role x can swap role/item with agent B with item/role y. This action is applicable only if all following preconditions are satisfied: the agent A is assigned item/role x, the agent B is assigned item/role y. We can see zoe is assigned book01 instead of book4. So this action is not applicable.\n"
    f"Step 2: We return our answer based on previous analysis.\n"
    f"Final Answer: No.\n"
    f"-------------------\n"
    f"(example 2)\n"
    f"Initial state: This is a swap domain where agents are swapping items or roles. Each agent is always assigned a single item/role. The goal is to obtain desired items/roles assigned. There are 7 agents: kevin, alice, dave, heidi, bob, ted, and xena. There are 7 items/roles: ulluco, leek, yam, parsnip, mushroom, valerian, and quince. Currently, heidi is assigned quince, ted is assigned ulluco, dave is assigned valerian, bob is assigned leek, alice is assigned yam, kevin is assigned mushroom, and xena is assigned parsnip. The goal is to reach a state where the following facts hold: heidi is assigned mushroom, ted is assigned leek, bob is assigned parsnip, alice is assigned valerian, dave is assigned ulluco, xena is assigned quince, and kevin is assigned yam.\n"
    f"Question: Which of the following claims is true with regard to the following sequence of actions \"swap kevin with heidi, mushroom for quince; swap kevin with alice, quince for yam; swap alice with dave, quince for valerian; swap dave with ted, quince for ulluco; swap ted with bob, quince for leek; swap bob with xena, quince for parsnip; swap xena with heidi, quince for mushroom\" A. The sequence is a plan. B. The sequence is applicable, but does not achieve the goal. C. The sequence is not valid. D. The sequence is not applicable.\n"
    f"Answer:\n"
    f"Step 1: Since the question ask whether the action sequence is a plan, we need to take actions to reach the fianl answer, then check the goal.\n"
    f"swap kevin with heidi, mushroom for quince. agent A with item/role x can swap role/item with agent B with item/role y. This action is applicable only if all following preconditions are satisfied: the agent A is assigned item/role x, the agent B is assigned item/role y. We can see now kevin is assigned yam is assigned yam, not mushroom. So this action is not applicable.\n"
    f"Step 2: We return our answer based on previous analysis.\n"
    f"Final Answer: D.\n"
    f"-------------------\n"
)


#-------------------------------------
#Logistics Prompts
#-------------------------------------
LOGISTICS_DOMAIN_DESCRIPTION = (
    f"[Domain Description]\n"
    f"The logistics domain involves trucks and airplane transporting packages between locations within cities. Trucks are identified as t_x(t0, t1, t2...). Airplanes are identified as t_x(t1, t2, ...). Packages are identified as p_x(p0, p1, ...). Cities are identified as c_x(c0, c1, ...). Locations are identified as lx-y(l0-0, l0-1, ...) where x means it's in city c_x. A truck and a airplane can contain as many packages as possible. We can think each location has its own airport, so you don't need to worry about whether this location can be used to fly the airplane or not. Besides, we allow trucks and planes transporting in only one city, such as from location A to location A.\n"
    f"Different properties are used to describe states of different objects. For package we use: at location_x/in truck_x/in airplane_x. For truck we use: at location, empty/has package_x in it. For airplane we use: at location, empty/has package_x in it.\n"
    
    f"Following actions are executable only if all preconditions are met, if any condition are not satisfied, the action is not executable.\n"
    f"A package p can be loaded(placed) into a truck at location l. This action is executable only if all following preconditions are satisfied: the package is at location l, the truck is at location l.\n"
    f"A package p can be unloaded(offloaded/removed) from a truck at location l. This action is executable only if all following preconditions are satisfied: the package is in the truck, the truck is at location l.\n"
    f"A package can be loaded(placed) onto a airplane at location l. This action is executable only if all following preconditions are satisfied: the package is at location l, the airplane is at location l.\n"
    f"A package can be unloaded(offloaded/removed) from a airplane at location l. This action is executable only if all following preconditions are satisfied: the package is in the airplane, the airplane is at location l.\n"
    f"A truck can be drivern(navigated) from location lx-y to location lx-z in the same city. This action is executable only if all following preconditions are satisfied: the truck is at location lx-y, location lx-y and lx-z are in the same city.\n"
    f"An airplane can be flew from location lx-i to location ly-j in different cities. This action is executable only if all following preconditions are satisfied: the airplane is at location lx-i, location lx-i and ly-j are in different cities.\n"
    
    f"Executing an action will change states of related objects.\n"
    f"A package p can be loaded(placed) into a truck at location l. This action will result in: the package is not at location l, the package is in the truck.\n"
    f"A package p can be unloaded(offloaded/removed) from a truck at location l. This action will result in: the package is not in the truck, the package is at location l.\n"
    f"A package can be loaded(placed) onto a airplane at location l. This action will result in: the package is not at location l, the package is in the airplane.\n"
    f"A package can be unloaded(offloaded/removed) from a airplane at location l. This action will result in: the package is not onto the airplane, the package is at location l.\n"
    f"A truck can be drivern(navigated) from location lx-y to location lx-z in the same city. This action will result in: the truck is not at location lx-y, the truck is at location lx-z.\n"
    f"An airplane can be flew from location lx-i to location ly-j in different cities. This action will result in: the airplane is not at location lx-i, the airplane is at location ly-j.\n"
   
)


INITIAL_STATE_EXTRACTOR_LOGISTICS_PROMPT = (
    f"This is a question related to the logistics domain. You are required to extract the initial state of every objects in this plan, including package, truck, airplan, location and city. Your answer must satisfy all the following requirements. First, think and respond with the format from the example above, including the word choice and paragraph structure. Second, each object's state should contain all properties mentioned in the domain description above. Besides, don't use any markdown formatting."
)


INITIAL_STATE_EXTRACTOR_LOGISTICS_EXAMPLE = (
    f"[Examples]\n"
    f"Initial state example 1: There are several cities, each containing several locations, some of which are airports. There are also trucks, which can drive within a single city, and airplanes, which can fly between airports. The goal is to get some packages from various locations to various new locations. There are 2 trucks and 1 airplane, as well as 4 packages. There are 6 locations across 2 cities. The locations are in cities as follows: l0-1, l0-2, and l0-0 are in c0; l1-2, l1-1, and l1-0 are in c1. Currently, p1 is at l1-1, a0 is at l0-0, t0 is at l0-2, p2 is at l1-0, t1, p0, and p3 are at l1-2. The goal is to reach a state where the following facts hold: p1 is at l1-2, p3 is at l0-1, p0 is at l0-2, and p2 is at l1-2.\n"
    f"Extracted from example 1:\n"
    f"First, we confirm every object involved in the initial state. We can find 2 trucks, 1 airplane, 4 packages and 6 locations across 2 cities.\n"
    f"Then we extract each object's state.\n"
    f"The locations are in cities as follows: l0-1, l0-2, and l0-0 are in c0; l1-2, l1-1, and l1-0 are in c1. ::: c0: has location l1-2, has locationl1-1, has location l1-0.\n"
    f"Currently, p1 is at l1-1, a0 is at l0-0, t0 is at l0-2, p2 is at l1-0, t1, p0, and p3 are at l1-2.  ::: p1: at l1-1. a0: at l0-0. t0: at l0-2. p2: at l1-0. t1: at l1-2. p0: at l1-2. p3: at l1-2.\n"
    f"Then, we organize all objects' state into a new paragraph as the end of the answer.\n"
    f"c0: has location l0-1, has location l0-2, has location l0-0. c1: has location l1-2, has location l1-1, has location l1-0. p1: at l1-1. a0: at l0-0. t0: at l0-2. p2: at l1-0. t1: at l1-2. p0: at l1-2. p3: at l1-2.\n"
    f"-------------------\n"
    f"Initial state example 2: There are several cities, each containing several locations, some of which are airports. There are also trucks, which can drive within a single city, and airplanes, which can fly between airports. The goal is to get some packages from various locations to various new locations. There are 3 trucks and 1 airplane, as well as 4 packages. There are 9 locations across 3 cities. The locations are in cities as follows: l1-1, l1-0, and l1-2 are in c1; l2-2, l2-1, and l2-0 are in c2; l0-1, l0-2, and l0-0 are in c0. Currently, a0 and p1 are at l2-0, p0 and t2 are at l2-1, t1 is at l1-0, t0 is at l0-1, p2 is in t0, p3 is in t2.\n"
    f"Extracted from example 2:\n"
    f"First, we confirm every object involved in the initial state. We can find 3 trucks, 1 airplane, 4 packages and 9 locations across 3 cities.\n"
    f"Then we extract each object's state.\n"
    f"The locations are in cities as follows: l1-1, l1-0, and l1-2 are in c1; l2-2, l2-1, and l2-0 are in c2; l0-1, l0-2, and l0-0 are in c0. ::: c1: has location l1-1, has location l1-0, has location l1-2. c2: has location l2-2, has location l2-1, has location l2-0. c0: has location l0-1, has location l0-2, has location l0-0.\n"
    f"a0 and p1 are at l2-0, p0 and t2 are at l2-1, t1 is at l1-0, t0 is at l0-1, p2 is in t0, p3 is in t2. ::: a0: at l2-0. p1: at l2-0. p0: at l2-1. t2: at l2-1. t1: at l1-0. t0: at l0-1. p2: in t0. p3: in t2.\n"
    f"Then, we organize all objects' state into a new paragraph as the end of the answer.\n"
    f"c1: has location l1-1, has location l1-0, has location l1-2. c2: has location l2-2, has location l2-1, has location l2-0. c0: has location l0-1, has location l0-2, has location l0-0. a0: at l2-0. p1: at l2-0. p0: at l2-1. t2: at l2-1. t1: at l1-0. t0: at l0-1. p2: in t0. p3: in t2.\n"
    f"-------------------\n"
)


QUESTION_EXTRACTOR_LOGISTICS_EXAMPLE =(
    f"[Examples]\n"
    f"Question example 1:Will the fact \"p2 is in a0\" hold after performing the action \"fly the airplane a0 from the airport l0-0 to the airport l0-0\" in the current state?\n"
    f"Extracted from example 1: Will the fact \"p2 is in a0\" hold?\n"
    f"-------------------\n"
    f"Question example 2: Will the fact \"a0 is at l1-0\" hold after performing the action \"fly airplane a0 from airport l0-0 to airport l1-0\" in the current state?\n"
    f"Extracted from example 2: Will the fact \"a0 is at l1-0\" hold?\n"
    f"-------------------\n"
    f"Question example 3: Will the fact \"p2 is in t0\" hold after performing the action \"fly the airplane a0 from the airport l0-0 to the airport l0-0\" in the current state?\n"
    f"Extracted from exaple 3: Will the fact \"p2 is in t0\" hold?\n"
    f"-------------------"
)


ACTION_SEQUENCE_EXTRACTOR_LOGISTICS_PROMPT = (
    f"[Examples]\n"
    f"Action example 1: Is the following action applicable in this state: load object p3 into airplane a0 at location l2-0?\n"
    f"Extracted from example 1: load object p3 into airplane a0 at location l2-0.\n"
    f"-------------------\n"
    f"Action example 2: Will the fact \"t1 is at l1-0\" hold after performing the action \"offload the object p2 from the truck t1 at location l1-1\" in the current state?\n"
    f"Extracted from example 2: offload the object p2 from the truck t1 at location l1-1.\n"
    f"-------------------\n"
    f"Action example 3: Will the fact \"p2 is in t0\" hold after performing the action \"fly the airplane a0 from the airport l0-0 to the airport l0-0\" in the current state?\n"
    f"Extracted from example 3: fly the airplane a0 from the airport l0-0 to the airport l0-0.\n"
    f"-------------------\n"
)


ACTION_TAKER_LOGISTICS_PROMPT =(
    f"Based on the domain description and examples above, take the action and return the new state of all objects. Your answer must satisfy all the following requirements. First, think and respond like examples above, you are required to return states of all objects(package, airplane, truck, location and city), including states that are not effected by the action. Second, each object's state must contain all properties mentioned in the domain description above. Third, after your analysis, please return states of all objects into a new paragraph as the end of your answer. Your final paragraph should use the format like: \"c0: has location l0-1, has location l0-2, has location l0-0. a0: at l2-0. p1: at l2-0. p0: at l2-1.\" Besides, don't use any markdown formatting."
)


ACTION_TAKER_LOGISTICS_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: c1: has location l1-1, has location l1-2, has location l1-0. c0: has location l0-0, has location l0-2, has location l0-1. a0: at l1-0. p0: at l1-0.  t1: at l1-0, has p1, has p2. t0: at l0-0, empty. p1: in t1. p2: in t1. p3: in a0.\n"
    f"Action 1: place the object p0 onto the airplane a0 at location l1-0\n"
    f"Answer 1:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"p0: at l1-0. a0: at l1-0.\n"
    f"Based on the domain description, a package p can be loaded(placed) onto a airplane a at location l. This action will result in: the package is not at location l, the package is in the airplane.\n"
    f"the package is not at location l, the package is in the airplane. ::: p0: in a0. a0: at l1-0.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into a paragraph as the end of answer.\n"
    f"c1: has location l1-1, has location l1-2, has location l1-0. c0: has location l0-0, has location l0-2, has location l0-1. a0: at l1-0, has p0 in it, has p3. t1: at l1-0, has p1, has p2. t0: at l0-0, empty. p0: in a0. p1: in t1. p2: in t1. p3: in a0.\n"
    f"-------------------\n"
    f"Current state example 2: c1: has location l1-1, has location l1-2, has location l1-0. c0: has location l0-0, has location l0-2, has location l0-1. a0: at l0-0. p1: at l1-1. t0: at l0-1. t1: at l1-0. p3: in t0. p2: in t0. p0: in a0.\n"
    f"Action 2: fly airplane a0 from airport l0-0 to airport l1-0\n"
    f"Answer 2:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"a0: at l0-0.\n"
    f"Based on the domain description, an airplane a can fly from airport A to airport B. This action will result in: the airplane is not at airport A, the airplane is at airport B.\n"
    f"the airplane is not at airport A, the airplane is at airport B. ::: a0: at l1-0.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into a paragraph as the end of answer.\n"
    f"c1: has location l1-1, has location l1-2, has location l1-0. c0: has location l0-0, has location l0-2, has location l0-1. a0: at l1-0. p1: at l1-1. t0: at l0-1. t1: at l1-0. p3: in t0. p2: in t0. p0: in a0.\n"
    f"-------------------\n"
    f"Current state example 3: c0: has location l0-1, has location l0-2, has location l0-0. c1: has location l1-1, has location l1-0. c2: has location l2-1, has location l2-2, has location l2-0. a0: at l0-0. t0: at l0-1. t1: at l0-1. t2: at l1-0. a1: at l2-0. p4: at l0-1. p2: at l2-1. p0: in t2. p1: at l1-1. p3: in a1.\n"
    f"Action 3: load object p4 into truck t1 at location l0-1.\n"
    f"Answer 3:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"t1: at l0-0. p4: at l0-1.\n"
    f"Based on the domain description, a package p can be loaded(placed) into a truck at location l. This action will result in: the package is not at location l, the package is in the truck.\n"
    f"the package is not at location l, the package is in the truck. ::: p4: in t1. t1: at l0-1, has p4.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into a paragraph as the end of answer.\n"
    f"c0: has location l0-1, has location l0-2, has location l0-0. c1: has location l1-1, has location l1-0. c2: has location l2-1, has location l2-2, has location l2-0. a0: at l0-0. t0: at l0-1. t1: at l0-1, has p4. t2: at l1-0. a1: at l2-0. p4: in t1. p2: at l2-1. p0: in t2. p1: at l1-1. p3: in a1.\n"
    f"-------------------\n"
)



EXECUTABILITY_CHECKER_LOGISTICS_EXAMPLE = (
    f"[Examples]"
    f"Current state example 1: c0: has location l0-1, has location l0-2, has location l0-0. c1: has location l1-1, has location l1-0. c2: has location l2-1, has location l2-2, has location l2-0. a0: at l0-0. t0: at l0-1. t1: at l0-1, has p4. t2: at l1-0. a1: at l2-0. p4: in t1. p2: at l2-1. p0: in t2. p1: at l1-1. p3: in a1.\n"
    f"Action 1: fly the airplane a0 from airport l0-0 to airport l0-2.\n"
    f"Answer 1:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can check whether the action is executable.\n"
    f"a0: at l0-0.\n"
    f"Based on the domain description, An airplane can be flew from location lx-i to location ly-j in different cities. This action is executable only if all following preconditions are satisfied: the airplane is at location lx-i, location lx-i and ly-j are in different cities.\n"
    f"the airplane is at airport A, ::: a0: at l0-0. ===> SATISFY\n"
    f"location lx-i and ly-j are in different cities. ::: a0: at l0-0. c0: has location l0-1, has location l0-2, has location l0-0. ===> NOT SATISFY\n"
    f"Since not all preconditions are satisfied, this action is not executable.\n"
    f"Final answer: False.\n"
    f"-------------------\n"
    f"Current state example 2: c1: has location l1-1, has location l1-0, has location l1-2. c2: has location l2-2, has location l2-1, has location l2-0. c0: has location l0-1, has location l0-2, has location l0-0. a0: at l2-0. p1: at l2-0. p0: at l2-1. t2: at l2-0. t1: at l1-0. t0: at l0-1. p2: in t0. p3: in t2.\n"
    f"Action 2: load object p1 into truck t2 at location l2-0\n"
    f"Answer 2:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can check whether the action is executable.\n"
    f"t2: at l2-0. p1: at l2-0.\n"
    f"Based on the domain description, A package p can be loaded(placed) into a truck at location l. This action is executable only if all following preconditions are satisfied: the package is at location l, the truck is at location l.\n"
    f"the package is at location l, ::: p1: at l2-0. ===> SATISFY\n"
    f"the truck is at location l, ::: t2: at l2-0. ===> SATISFY\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final answer: True.\n"
    f"-------------------\n"
)



STATE_CHECKER_LOGISTICS_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: c1: has location l1-1, has location l1-2, has location l1-0. c0: has location l0-0, has location l0-2, has location l0-1. a0: at l1-0. p0: at l1-0.  t1: at l1-0, has p1, has p2. t0: at l0-0, empty. p1: in t1. p2: in t1. p3: in a0.\n"
    f"Question 1: Will the fact \"p0 is in a0\" hold?\n"
    f"Answer 1:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. \n"
    f"p0 is in a0 ::: p0: at l1-0. ===>NOT SATISFY\n"
    f"Since not all propositions are true, so the answer is false.\n"
    f"Final Answer: False.\n"
    f"-------------------\n"
    f"Current state example 2: c1: has location l1-1, has location l1-2, has location l1-0. c0: has location l0-0, has location l0-2, has location l0-1. a0: at l1-0. p0: at l1-0.  t1: at l1-0, has p1, has p2. t0: at l0-0, empty. p1: in t1. p2: in t1. p3: in a0.\n"
    f"Question 2: Will the fact \"p0 is at l1-0\" hold?\n"
    f"Answer 2:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. \n"
    f"p0 is at l1-0 ::: p0: at l1-0. ===>SATISFY\n"
    f"Since all propositions in the question match with the curent state, so the question is true.\n"
    f"Final Answer: True.\n"
    f"-------------------\n"
)


TWOSHOTCOT_APP_LOGISTICS_EXAMPLE = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"Initial State: There are several cities, each containing several locations, some of which are airports. There are also trucks, which can drive within a single city, and airplanes, which can fly between airports. The goal is to get some packages from various locations to various new locations. There are 3 trucks and 1 airplane, as well as 5 packages. There are 9 locations across 3 cities. The locations are in cities as follows: l1-1, l1-0, and l1-2 are in c1; l2-2, l2-1, and l2-0 are in c2; l0-1, l0-2, and l0-0 are in c0. Currently, a0, p1, and p3 are at l2-0, t1 is at l1-1, p4 is at l1-0, t2 is at l2-1, t0 is at l0-0, p0 and p2 are in a0.\n"
    f"Question: Is the following action applicable in this state: drive the truck t1 in city c1 from location l1-1 to location l1-0?\n"
    f"Answer:\n"
    f"Step 1: we find related objects in the current state.\n"
    f"t1 is at l1-1.\n"
    f"Step 2: we check whether the action is applicable.\n"
    f"A truck can be drivern(navigated) from location lx-y to location lx-z in the same city. This action is executable only if all following preconditions are satisfied: the truck is at location lx-y, location lx-y and lx-z are in the same city. We can see t1 is at l1-1, l1-1 and l1-0 are in the same city. So this action is applicable.\n"
    f"Step 3: We return our answer based on previous analysis. \n"
    f"Final Answer: True.\n"
    f"-------------------\n"
    f"(Example 2)\n"
    f"Initial State: There are several cities, each containing several locations, some of which are airports. There are also trucks, which can drive within a single city, and airplanes, which can fly between airports. The goal is to get some packages from various locations to various new locations. There are 3 trucks and 1 airplane, as well as 5 packages. There are 9 locations across 3 cities. The locations are in cities as follows: l2-1, l2-2, and l2-0 are in c2; l1-0, l1-1, and l1-2 are in c1; l0-2, l0-0, and l0-1 are in c0. Currently, t0 and p4 are at l0-2, a0 is at l1-2, p0 and p3 are at l2-2, t2 is at l2-1, p2 is in a0, bob is at l1-1, and t1 is at l1-1.\n"
    f"Question: Which of the following actions will be applicable in this state? A. unload object p2 from airplane a0 at location l1-2. B. drive the truck t1 in city c1 from location l1-1 to location l1-0. C. offload the object p3 from the truck t2 at location l2-1. D. offload the object p4 from the truck t0 at location l0-2.\n"
    f"Answer:\n"
    f"Step 1: We check each option one by one. \n"
    f"Option A: unload object p2 from airplane a0 at location l1-2. A object can be unload from the airplane at location x only if the airplane has the package and the airplane is at location x. We can see p2 is in a0, a0 is at l1-2. So this action is executable.\n"
    f"Step 3: We return our answer based on previous analysis. \n"
    f"Final Answer: A.\n"
    f"-------------------\n"
)


TWOSHOTCOT_PROG_LOGISTICS_EXAMPLE = (
    f"[Examples]\n"
    f"(example 1)\n"
    f"Initial state: There are several cities, each containing several locations, some of which are airports. There are also trucks, which can drive within a single city, and airplanes, which can fly between airports. The goal is to get some packages from various locations to various new locations. There are 3 trucks and 1 airplane, as well as 5 packages. There are 9 locations across 3 cities. The locations are in cities as follows: l1-1, l1-2, and l1-0 are in c1; l0-0, l0-2, and l0-1 are in c0; l2-2, l2-1, and l2-0 are in c2. Currently, a0, p4, and t1 are at l1-0, t2 is at l2-2, t0 is at l0-1, p1, p3, and p0 are in a0, p2 is in t0.\n"
    f"Question: Will the fact \"p3 is at l1-0\" hold after performing the action \"offload the object p3 from the airplane a0 at location l1-0\" in the current state?\n"
    f"Step 1: Take the action and get the new state.\n"
    f"offload the object p3 from the airplane a0 at location l1-0. After taking this action, p3 is at l1-0.\n"
    f"Step 2: Check whether the fact hold.\n"
    f"p3 is at l1-0. We can see now p3 is at l1-0. So this fact is held.\n"
    f"Step 3: We return our answer based on previous analysis.\n"
    f"Final Answer: True.\n"
    f"-------------------\n"
    f"(example 2)\n"
    f"Initial state: There are several cities, each containing several locations, some of which are airports. There are also trucks, which can drive within a single city, and airplanes, which can fly between airports. The goal is to get some packages from various locations to various new locations. There are 5 trucks and 1 airplane, as well as 4 packages. There are 15 locations across 5 cities. The locations are in cities as follows: l2-2, l2-1, and l2-0 are in c2; l4-2, l4-1, and l4-0 are in c4; l0-1, l0-0, and l0-2 are in c0; l3-0, l3-1, and l3-2 are in c3; l1-0, l1-1, and l1-2 are in c1. Currently, t2 and p2 are at l2-1, t0 is at l0-2, p1 is at l1-1, t3 is at l3-2, t4 and a0 are at l0-0, t1 is at l4-2, p3 and p0 are in a0.\n"
    f"Question: Which of the following facts hold after performing the action \"fly the airplane a0 from airport l0-0 to airport l2-0\" in the current state? A. a0 is at l4-2. B. p0 is at l0-0. C. a0 is at l2-0. D. t0 is at l2-0.\n"
    f"Step 1: Take the action and get the new state.\n"
    f"fly the airplane a0 from airport l0-0 to airport l2-0. After taking this action, a0 is at l2-0.\n"
    f"Step 2: Check each option to find the answer.\n"
    f"Option A: a0 is at l4-2. We can see a0 is at l0-0, so this option is false.\n"
    f"Option B: p0 is at l0-0. We can see p0 are in a0, so this option is false.\n"
    f"Option C: a0 is at l2-0. We can see a0 is at l2-0, so this option is true.\n"
    f"Step 3: We return our answer based on previous analysis.\n"
    f"Final Answer: C.\n"
    f"-------------------\n"
)


TWOSHOTCOT_VAL_LOGISTICS_EXAMPLE = (
    F"[Examples]\n"
    f"(example 1)\n"
    f"Initial state: There are several cities, each containing several locations, some of which are airports. There are also trucks, which can drive within a single city, and airplanes, which can fly between airports. The goal is to get some packages from various locations to various new locations. There are 2 trucks and 1 airplane, as well as 4 packages. There are 6 locations across 2 cities. The locations are in cities as follows: l0-0, l0-1, and l0-2 are in c0; l1-0, l1-1, and l1-2 are in c1. Currently, t0 and p1 are at l0-1, t1 is at l1-2, p0 and a0 are at l1-0, p2 and p3 are at l0-2. The goal is to reach a state where the following facts hold: p0 is at l0-0, p1 is at l0-0, p2 is at l0-0, and p3 is at l0-0.\n"  
    f"Question: Is the following sequence of actions \"load the object p0 from location l1-0 into the airplane a0, fly airplane a0 from airport l1-0 to airport l0-1, offload the object p0 from the airplane a0 at location l0-1, place the object p0 into the truck t0 at location l0-1\" applicable in the current state?\n"
    f"Answer:\n"
    f"Step 1: Since the question askes whether the action sequencece is applicable or not. We check every action one by one. If applicable, we take the action and get the new state. If not, return false.\n"
    f"Action 1: load the object p0 from location l1-0 into the airplane a0. A package can be loaded(placed) onto a airplane at location l. This action is executable only if all following preconditions are satisfied: the package is at location l, the airplane is at location l. We can see both p0 and a0 are both at l1-0, so this action is applicable.\n"
    f"Action 2: fly airplane a0 from airport l1-0 to airport l0-1. An airplane can be flew from location lx-i to location ly-j in different cities. This action is executable only if all following preconditions are satisfied: the airplane is at location lx-i, location lx-i and ly-j are in different cities. We can see a0 is at l1-0, l1-0 and l0-1 are in different cities, so this action is applicable.\n"
    f"Action 3: offload the object p0 from the airplane a0 at location l0-1. A package can be unloaded(offloaded/removed) from a airplane at location l. This action is executable only if all following preconditions are satisfied: the package is in the airplane, the airplane is at location l. We can see p0 is in a0, a0 is at l0-1, so this action is applicable.\n"
    f"Action 4: place the object p0 into the truck t0 at location l0-1. A package can be loaded(placed) into a truck at location l. This action is executable only if all following preconditions are satisfied: the package is at location l, the truck is at location l. We can see p0 is at l0-1, t0 is at l0-1, so this action is applicable.\n"
    f"Step 2: We return our answer based on previous analysis. \n"
    f"Since all actions in the action sequence is applicable, so the action sequence is applicable.\n"
    f"Final Answer: True.\n"
    f"-------------------\n"
    f"(example 2)\n"
    f"Initial state: There are several cities, each containing several locations, some of which are airports. There are also trucks, which can drive within a single city, and airplanes, which can fly between airports. The goal is to get some packages from various locations to various new locations. There are 3 trucks and 1 airplane, as well as 5 packages. There are 9 locations across 3 cities. The locations are in cities as follows: l0-2, l0-0, and l0-1 are in c0; l2-0, l2-1, and l2-2 are in c2; l1-0, l1-1, and l1-2 are in c1. Currently, p0, t0, and a0 are at l0-0, p1 and p3 are at l2-0, t2 is at l2-1, p4 is at l1-0, t1 is at l1-1, p2 is at l0-1. The goal is to reach a state where the following facts hold: p0 is at l1-2, and p4 is at l0-0.\n"
    f"Question: Which of the following claims is true with regard to the following sequence of actions \"place the object p0 onto the airplane a0 at location l0-0\"  A. The sequence is not valid. B. The sequence is a plan. C. The sequence is not applicable. D. The sequence is applicable, but does not achieve the goal.\n"
    f"Answer:\n"
    f"Step 1: Since the question ask whether the action sequence is a plan, we need to take actions to reach the fianl answer, then check the goal. \n"
    f"Action 1: place the object p0 onto the airplane a0 at location l0-0. A package can be loaded(placed) onto a airplane at location l. This action is executable only if all following preconditions are satisfied: the package is at location l, the airplane is at location l. We can see p0 is at l0-0, a0 is at l0-0, so this action is applicable.\n"
    f"Since all actions are applicable, so the action sequence is applicable. Then we check whether the action sequence reach the goal. The goal is to reach a state where the following facts hold: p0 is at l1-2, and p4 is at l0-0. We can see after taking the action, p0 is at l0-0, so the goal is not reached. So the action sequence is applicable, but does not achieve the goal.\n"
    f"Step 2: We return our answer based on previous analysis. \n"
    f"Final Answer: D.\n"
    f"-------------------\n"
)


#-------------------------------------
#Rovers Prompts
#-------------------------------------
ROVERS_DOMAIN_DESCRIPTION = (
    f"[Domain Description]\n"
    f"The Rovers domain involves rovers, cameras, landers, stores, and objectives. In this domain, rovers navigate through waypoints, collect samples or take images, and then send the data to a lander(lander general). A rover's location can be changed, the lander's location is fixed. The lander is used to receive data from rovers. Cameras are equipped on rovers, and can be used to take images of objectives in supported modes. Cameras should be calibrated in specific waypoint with specific objectives before it can be used to take images. Stores on rovers are used to store samples including rock sample and soil sample, each store can only store one sample.\n"
    f"For different objects in the domains we use different properties to describer their states.\n"
    f"For rovers we use: at waypoint_x, equipped for imaging(or rock analysis, soil analysis), has camera_x on board, has store_x, store_x is empty/has soil(or rock) sample, available/unavailable, has image of objective_x in mode_x, has soil(or rock) data from waypoint_x, can traverse from waypoint A to waypoint B.\n"
    f"For camera we use: is equipped on rover_x, calibrated/not calibrated, use objective_x as calibration target, support mode_x.\n"
    f"For lander(lander general) we use: at waypoint_x, has rock data(or soil data) communicated from waypoint_x, has image of objective_x in mode_x.\n"
    f"For store we use: on rover_x, has rock(or soil) sample, is empty/full.\n"
    f"For waypoint we use: has visuality of waypoint_x, has visuality of objective_x, has rock sample(or soil sample).\n"
    f"Following actions are executable only if all preconditions are met, if any condition are not satisfied, the action is not executable.\n"
    f"A rover can navigate(traverse) from waypoint A to waypoint B. This action is executable only if all following preconditions are satisfied: the rover is at waypoint A, the rover can traverse from A to B, the rover is available, waypoint B is visible for waypoint A.\n"
    f"A rover can sample rock(or soil) at waypoint A and store it in store X. This action is executable only if all following preconditions are satisfied: the rover is at waypoint A, store X is on the rover, store X is empty, waypoint A has rock sample(or soil sample), the rover is available, the rover is equipped for rock(or soil) analysis.\n"
    f"A rover can drop the rock(or soil) sample in store X. This action is executable only if all following preconditions are satisfied: store X is on the rover, store X has rock(or soil) sample(store X is not empty), the rover is available.\n"
    f"A camera on the rover can be calibrated/adjusted for objective X at waypoint A. This action is executable only if all following preconditions are satisfied: the rover is at waypoint A, waypoint A has the visuality of the objective X, the camera is equipped on the rover, the camera can be calibrated using objective X(X is the calibration target).\n"
    f"A rover can take an image of objective X in mode Y from waypoint A. This action is executable only if all following preconditions are satisfied: the rover is at waypoint A, the rover is available, the rover is equipped for imaging, the camera is equipped on the rover, the camera supports mode Y, the camera is calibrated, objective X is visible from waypoint A.\n" 
    f"A rover can communicate(transmit) data at waypoint waypoint X to the lander general at waypoint waypoint Y through waypoint X. The data can be image of objective, soil data or rock data. This action is executable only if all following preconditions are satisfied: the rover is at waypoint X, the rover is available, the lander general is at waypoint Y, waypoint X has visuality of waypoint Y, the rover has the data.\n"
    f"Executing an action will change states of related objects.\n"
    f"A rover can navigate(traverse) from waypoint A to waypoint B. This action will result in: the rover is not at waypoint A, the rover is at waypoint B.\n"
    f"A rover can sample rock(or soil) at waypoint A and store it in store X. This action will result in: store X has rock sample(or soil sample), store X is not empty(store X is full), the rover has rock(or soil) data analyzed at waypoint A.\n"
    f"A rover can drop the rock(or soil) sample in store X at waypoint A. This action will result in: store X doesn't have rock(or soil) sample, store X is empty, waypoint A has rock(or soil) sample.\n"
    f"A camera on the rover can be calibrated/adjusted for objective X at waypoint A. This action will result in: the camera is calibrated.\n"
    f"A rover can communicate(transmit) data at waypoint waypoint X to the lander general at waypoint waypoint Y through waypoint X. This action will result in: the lander general has the data."
)

INITIAL_STATE_EXTRACTOR_ROVERS_PROMPT = (
    f"This is a question related to the rovers domain. You are required to extract the initial state of every objects in this plan, including rovers, stores, lander, cameras, objectives and waypoints. Your answer must satisfy all the following requirements. First, think and respond with the format from the example above, including the word choice and paragraph structure. Second, each object's state should contain all properties mentioned in the domain description above. Besides, don't use any markdown formatting."
)


INITIAL_STATE_EXTRACTOR_ROVERS_EXAMPLE = (
    f"[Examples]\n"
    f"Initial state example 1: This is a Rovers domain where rovers must navigate between waypoints gathering data and transmitting it back to a lander. Rovers cannot navigate to all waypoints and this makes particular routes impassable to some of the rovers. Data transmission is also constrained by the visibility of the lander from the waypoints. There are2 rovers,4 waypoints,2 stores, 2 cameras, 4 objectives numbered consecutively. Further, there is 1 lander and 3 modes for the camera namely colour, high resolution, and low resolution.Rover(s) rover0 and rover1 are equipped for soil analysis. Rover(s) rover0 is equipped for rock analysis. Rover(s) rover0 and rover1 are equipped for imaging. Rover rover1 has store store1. Rover rover0 has store store0. Rover rover0 has camera0 on board. Rover rover1 has camera1 on board. Camera camera1 can be calibrated on objective2. Camera camera0 can be calibrated on objective1. Camera camera1 supports high_res. Camera camera0 supports colour and low_res. Rover rover1 can traverse from waypoint2 to waypoint1, waypoint0 to waypoint2, waypoint1 to waypoint3. Rover rover0 can traverse from waypoint0 to waypoint2, waypoint1 to waypoint0, waypoint2 to waypoint3. Waypoint(s) are visible from waypoint0: waypoint2. Waypoint(s) are visible from waypoint1: waypoint3and waypoint2. Waypoint(s) are visible from waypoint2: waypoint1 and waypoint0. Waypoint(s) are visible from waypoint3: waypoint1. Objective objective2 is visible from waypoint1. Objective objective1 is visible from waypoint2. Objective objective0 is visible from waypoint3. Objective objective3 is visible from waypoint0. Lander general is at waypoint waypoint2. Currently, Rover rover0 is at waypoint2. Rover rover1 is at waypoint1. Rocks can be sampled at the following location(s): waypoint1, waypoint3. Soil can be sampled at the following location(s): waypoint0, waypoint2. Rovers rover1 and rover0 are available. Camera camera0 is calibrated. Store store1 is empty. Store store0 is full.\n"
    f"Extracted from example 1:\n"
    f"First, we confirm every object involved in the initial state. We can find 2 rovers, 1 lander, 4 waypoints, 2 stores, 2 cameras, 4 objectives numbered consecutively.\n"
    f"Then we extract each object's state.\n"
    f"Rover(s) rover0 and rover1 are equipped for soil analysis. Rover(s) rover0 is equipped for rock analysis. Rover(s) rover0 and rover1 are equipped for imaging. Rover rover1 has store store1. Rover rover0 has store store0. Rover rover0 has camera0 on board. Rover rover1 has camera1 on board. Currently, Rover rover0 is at waypoint2. Rover rover1 is at waypoint1. Rover rover1 can traverse from waypoint2 to waypoint1, waypoint0 to waypoint2, waypoint1 to waypoint3. Rover rover0 can traverse from waypoint0 to waypoint2, waypoint1 to waypoint0, waypoint2 to waypoint3. Rovers rover1 and rover0 are available. Lander general is at waypoint waypoint2::: Rover0: at waypoint2, available, equipped for soil analysis, equipped for rock analysis, equipped for imaging, has store0, has camera0 on board, can traverse from waypoint0 to waypoint2, can traverse from waypoint1 to waypoint0, can traverse from waypoint2 to waypoint3. Rover1: at waypoint2, available, equipped for soil analysis, equipped for imaging, has store1, has camera1 on board, can traverse from waypoint2 to waypoint1, can traverse from waypoint0 to waypoint2, can traverse from waypoint1 to waypoint3. Lander: at waypoint2.\n"
    f"Rover rover0 has camera0 on board. Rover rover1 has camera1 on board. Camera camera1 can be calibrated on objective2. Camera camera0 can be calibrated on objective1. Camera camera1 supports high_res. Camera camera0 supports colour and low_res. Camera camera0 is calibrated. Store store1 is empty. Store store0 is full. ::: Camera0: is equipped on rover0, is calibrated, use objective1 as calibration target, supports colour, supports low_res. Camera1: is equipped on rover1, use objective2 as calibration target, support high_res. Store0: on rover0, is full. Store1: on rover1, is empty.\n"
    f"Waypoint(s) are visible from waypoint0: waypoint2. Waypoint(s) are visible from waypoint1: waypoint3and waypoint2. Waypoint(s) are visible from waypoint2: waypoint1 and waypoint0. Waypoint(s) are visible from waypoint3: waypoint1. Objective objective2 is visible from waypoint1. Objective objective1 is visible from waypoint2. Objective objective0 is visible from waypoint3. Objective objective3 is visible from waypoint0. Rocks can be sampled at the following location(s): waypoint1, waypoint3. Soil can be sampled at the following location(s): waypoint0, waypoint2. ::: Waypoint0: has visuality of waypoint2, has visuality of objective3, has soil sample. Waypoint1: has visuality of waypoint3, has visuality of waypoint2, has visuality of objective2, has rock sample. Waypoint2: has visuality of waypoint1, has visuality of waypoint0, has visuality of objective1, has soil sample. Waypoint3: has visuality of waypoint1, has visuality of objective0, has rock sample.\n"
    f"Then, we organize all objects' state into a new paragraph as the end of the answer.\n"
    f"Rover0: at waypoint2, available, equipped for soil analysis, equipped for rock analysis, equipped for imaging, has store0, has camera0 on board, can traverse from waypoint0 to waypoint2, can traverse from waypoint1 to waypoint0, can traverse from waypoint2 to waypoint3. Rover1: at waypoint2, available, equipped for soil analysis, equipped for imaging, has store1, has camera1 on board, can traverse from waypoint2 to waypoint1, can traverse from waypoint0 to waypoint2, can traverse from waypoint1 to waypoint3. Lander: at waypoint2. Camera0: is equipped on rover0, is calibrated, use objective1 as calibration target, supports colour, supports low_res. Camera1: is equipped on rover1, use objective2 as calibration target, support high_res. Store0: on rover0, is full. Store1: on rover1, is empty. Waypoint0: has visuality of waypoint2, has visuality of objective3, has soil sample. Waypoint1: has visuality of waypoint3, has visuality of waypoint2, has visuality of objective2, has rock sample. Waypoint2: has visuality of waypoint1, has visuality of waypoint0, has visuality of objective1, has soil sample. Waypoint3: has visuality of waypoint1, has visuality of objective0, has rock sample.\n"
    f"-------------------\n"
    f"Initial state example 2: This is a Rovers domain where rovers must navigate between waypoints gathering data and transmitting it back to a lander. Rovers cannot navigate to all waypoints and this makes particular routes impassable to some of the rovers. Data transmission is also constrained by the visibility of the lander from the waypoints. There are 3 rovers, 3 waypoints, 3 stores, 2 cameras, 3 objectives numbered consecutively. Further, there is 1 lander and 3 modes for the camera namely colour, high resolution, and low resolution. Rover(s) rover0 and rover2 are equipped for soil analysis. Rover(s) rover1 is equipped for rock analysis. Rover(s) rover0 and rover1 are equipped for imaging. Rover rover2 has store store2. Rover rover1 has store store1. Rover rover0 has store store0. Rover rover0 has camera0 on board. Rover rover1 has camera1 on board. Camera camera1 can be calibrated on objective0. Camera camera0 can be calibrated on objective2. Camera camera1 supports colour. Camera camera0 supports high_res. Rover rover1 can traverse from waypoint1 to waypoint0, waypoint0 to waypoint2. Rover rover0 can traverse from waypoint0 to waypoint2, waypoint2 to waypoint1. Rover rover2 can traverse from waypoint1 to waypoint2, waypoint0 to waypoint1. Waypoint(s) are visible from waypoint0: waypoint2. Waypoint(s) are visible from waypoint1: waypoint0. Waypoint(s) are visible from waypoint2: waypoint1. Objective objective2 is visible from waypoint1. Objective objective1 is visible from waypoint2. Objective objective0 is visible from waypoint0. Lander general is at waypoint waypoint0. Currently, Rover rover0 is at waypoint1. Rover rover1 is at waypoint0. Rover rover2 is at waypoint2. Rocks can be sampled at the following location(s): waypoint0. Soil can be sampled at the following location(s): waypoint1, waypoint2. Rovers rover0, rover1 and rover2 are available. Rover rover1 has rock analyzed in waypoint0. Store store0 and store1 are empty. Store store2 is full.\n"
    f"First, we confirm every object involved in the initial state. We can find 3 rovers, 1 lander, 3 waypoints, 3 stores, 2 cameras, 3 objectives numbered consecutively.\n"
    f"Then we extract each object's state.\n"
    f"Rover(s) rover0 and rover2 are equipped for soil analysis. Rover(s) rover1 is equipped for rock analysis. Rover(s) rover0 and rover1 are equipped for imaging. Rover rover2 has store store2. Rover rover1 has store store1. Rover rover0 has store store0. Rover rover0 has camera0 on board. Rover rover1 has camera1 on board. Currently, Rover rover0 is at waypoint1. Rover rover1 is at waypoint0. Rover rover2 is at waypoint2. Rover rover1 can traverse from waypoint1 to waypoint0, waypoint0 to waypoint2. Rover rover0 can traverse from waypoint0 to waypoint2, waypoint2 to waypoint1. Rover rover2 can traverse from waypoint1 to waypoint2, waypoint0 to waypoint1. Rovers rover0, rover1 and rover2 are available. Lander general is at waypoint waypoint0. ::: Rover0: at waypoint1, available, equipped for soil analysis, equipped for imaging, has store0, has camera0 on board, can traverse from waypoint0 to waypoint2, can traverse from waypoint2 to waypoint1. Rover1: at waypoint0, available, equipped for rock analysis, equipped for imaging, has store1, has camera1 on board, can traverse from waypoint1 to waypoint0, can traverse from waypoint0 to waypoint2. Rover2: at waypoint2, available, equipped for soil analysis, has store2, can traverse from waypoint1 to waypoint2, can traverse from waypoint0 to waypoint1. Lander: at waypoint0.\n"
    f"Rover rover0 has camera0 on board. Rover rover1 has camera1 on board. Camera camera1 can be calibrated on objective0. Camera camera0 can be calibrated on objective2. Camera camera1 supports colour. Camera camera0 supports high_res. Store store0 and store1 are empty. Store store2 is full. Rover rover1 has rock analyzed in waypoint0. ::: Camera0: is equipped on rover0, use objective2 as calibration target, supports high_res. Camera1: is equipped on rover1, use objective0 as calibration target, supports colour. Store0: on rover0, is empty. Store1: on rover1, is empty. Store2: on rover2, is full.\n"
    f"Waypoint(s) are visible from waypoint0: waypoint2. Waypoint(s) are visible from waypoint1: waypoint0. Waypoint(s) are visible from waypoint2: waypoint1. Objective objective2 is visible from waypoint1. Objective objective1 is visible from waypoint2. Objective objective0 is visible from waypoint0. Rocks can be sampled at the following location(s): waypoint0. Soil can be sampled at the following location(s): waypoint1, waypoint2. ::: Waypoint0: has visuality of waypoint2, has visuality of objective0, has rock sample. Waypoint1: has visuality of waypoint0, has visuality of objective2, has soil sample. Waypoint2: has visuality of waypoint1, has visuality of objective1, has soil sample.\n"
    f"Rover0: at waypoint1, available, equipped for soil analysis, equipped for imaging, has store0, has camera0 on board, can traverse from waypoint0 to waypoint2, can traverse from waypoint2 to waypoint1. Rover1: at waypoint0, available, equipped for rock analysis, equipped for imaging, has store1, has camera1 on board, can traverse from waypoint1 to waypoint0, can traverse from waypoint0 to waypoint2, has rock analyzed in waypoint0. Rover2: at waypoint2, available, equipped for soil analysis, has store2, can traverse from waypoint1 to waypoint2, can traverse from waypoint0 to waypoint1. Lander: at waypoint0. Camera0: is equipped on rover0, use objective2 as calibration target, supports high_res. Camera1: is equipped on rover1, use objective0 as calibration target, supports colour. Store0: on rover0, is empty. Store1: on rover1, is empty. Store2: on rover2, is full. Waypoint0: has visuality of waypoint2, has visuality of objective0, has rock sample. Waypoint1: has visuality of waypoint0, has visuality of objective2, has soil sample. Waypoint2: has visuality of waypoint1, has visuality of objective1, has soil sample.\n"
    f"-------------------\n"
)  


QUESTION_EXTRACTOR_ROVERS_EXAMPLE = (
    F"[Examples]\n"
    f"Question example 1: Will the fact \"Store(s) store0 and store1 are full\" hold after performing the action \"navigate rover rover1 from waypoint waypoint2 to waypoint waypoint0\" in the current state?\n"
    f"Extracted from example 1: Will the fact \"Store(s) store0 and store1 are full\" hold?\n"
    f"-------------------\n"
    f"Question example 2: Will the fact \"Rover rover1 has camera2 on board\" hold after performing the action \"calibrate camera camera2 on objective objective1 for rover rover1 at waypoint waypoint2\" in the current state?\n"
    f"Extracted from example 2: Will the fact \"Rover rover1 has camera2 on board\" hold?\n"
    f"-------------------\n"
    f"Question example 3: Will the fact \"Rover rover1 is at waypoint2\" hold after performing the action \"navigate rover rover1 from waypoint waypoint2 to waypoint waypoint1\" in the current state?\n"
    f"xtracted from example 3: Will the fact \"Rover rover1 is at waypoint2\" hold?\n"
    f"-------------------\n"
)

ACTION_SEQUENCE_EXTRACTOR_ROVERS_PROMPT = (
    f"[Examples]\n"
    f"Action example 1: Is the following action applicable in this state: collect a sample from the waypoint waypoint2 using the rover rover0 and store it in the store store0?\n"
    f"Extracted from example 1: collect a sample from the waypoint waypoint2 using the rover rover0 and store it in the store store0.\n"
    f"-------------------\n"
    f"Action example 2: Is the following action applicable in this state: navigate rover rover0 from waypoint waypoint2 to waypoint waypoint1?\n"
    f"Extracted from example 2: navigate rover rover0 from waypoint waypoint2 to waypoint waypoint1.\n"
    f"-------------------\n"
    f"Action example 3: Is the following applicable in this state: navigate rover rover0 from waypoint waypoint1 to waypoint waypoint0, sample the soil at waypoint waypoint0 using the rover rover0, then store it in the storage unit store0, transmit soil data from rover rover1 at waypoint waypoint0 to the lander general at waypoint waypoint3, regarding the soil analysis of waypoint waypoint0?\n"
    f"Extracted from example 3: Navigate rover rover0 from waypoint waypoint1 to waypoint waypoint0. Sample the soil at waypoint waypoint0 using the rover rover0 then store it in the storage unit store0. Transmit soil data from rover rover1 at waypoint waypoint0 to the lander general at waypoint waypoint3 regarding the soil analysis of waypoint waypoint0.\n"
    f"-------------------\n"
)


ACTION_TAKER_ROVERS_PROMPT = (
   f"Based on the domain description and examples above, take the action and return the new state of all objects. Your answer must satisfy all the following requirements. First, think and respond like examples above, you are required to return states of all objects, including states that are not effected by the action. Second, each object's state must contain all properties mentioned in the domain description above. Third, after your analysis, please return states of all objects into a new paragraph as the end of your answer. Besides, don't use any markdown formatting."
)



ACTION_TAKER_ROVERS_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: Rover0: at waypoint1, available, equipped for soil analysis, equipped for imaging, has store0, has camera0 on board, can traverse from waypoint0 to waypoint2, can traverse from waypoint2 to waypoint1. Rover1: at waypoint0, available, equipped for rock analysis, equipped for imaging, has store1, has camera1 on board, can traverse from waypoint1 to waypoint0, can traverse from waypoint0 to waypoint2, has rock analyzed in waypoint0. Rover2: at waypoint2, available, equipped for soil analysis, has store2, can traverse from waypoint1 to waypoint2, can traverse from waypoint0 to waypoint1. Lander: at waypoint0. Camera0: is equipped on rover0, use objective2 as calibration target, supports high_res. Camera1: is equipped on rover1, use objective0 as calibration target, supports colour. Store0: on rover0, is empty. Store1: on rover1, is empty. Store2: on rover2, is full. Waypoint0: has visuality of waypoint2, has visuality of objective0, has rock sample. Waypoint1: has visuality of waypoint0, has visuality of objective2, has soil sample. Waypoint2: has visuality of waypoint1, has visuality of objective1, has soil sample.\n"
    f"Action 1: Collect a sample from the waypoint waypoint0 using the rover rover1and store it in the store store1.\n"
    f"Answer 1:"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Waypoint0: has visuality of waypoint2, has visuality of objective0, has rock sample. Rover1: at waypoint0, available, equipped for rock analysis, equipped for imaging, has store1, has camera1 on board, can traverse from waypoint1 to waypoint0, can traverse from waypoint0 to waypoint2, has rock analyzed in waypoint0. Store1: on rover1, is empty.\n"
    f"Based on the domain description, A rover can sample rock(or soil) at waypoint A and store it in store X. This action will result in: store X has rock sample(or soil sample), store X is not empty(store X is full), the rover has rock(or soil) data analyzed at waypoint A.\n"
    f"store X has rock sample(or soil sample), store X is not empty(store X is full) ::: Store1: on rover1, has rock sample, is full.\n"
    f"the rover has rock(or soil) data analyzed at waypoint A ::: Rover1: at waypoint0, available, equipped for rock analysis, equipped for imaging, has store1, has camera1 on board, can traverse from waypoint1 to waypoint0, can traverse from waypoint0 to waypoint2, has rock analyzed in waypoint0.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into a new paragraph.\n"
    f"Rover0: at waypoint1, available, equipped for soil analysis, equipped for imaging, has store0, has camera0 on board, can traverse from waypoint0 to waypoint2, can traverse from waypoint2 to waypoint1. Rover1: at waypoint0, available, equipped for rock analysis, equipped for imaging, has store1, has camera1 on board, can traverse from waypoint1 to waypoint0, can traverse from waypoint0 to waypoint2, has rock analyzed in waypoint0. Rover2: at waypoint2, available, equipped for soil analysis, has store2, can traverse from waypoint1 to waypoint2, can traverse from waypoint0 to waypoint1. Lander: at waypoint0. Camera0: is equipped on rover0, use objective2 as calibration target, supports high_res. Camera1: is equipped on rover1, use objective0 as calibration target, supports colour. Store0: on rover0, is empty. Store1: on rover1, has rock sample, is full. Store2: on rover2, is full. Waypoint0: has visuality of waypoint2, has visuality of objective0, has rock sample. Waypoint1: has visuality of waypoint0, has visuality of objective2, has soil sample. Waypoint2: has visuality of waypoint1, has visuality of objective1, has soil sample.\n"
    f"-------------------\n"
    f"Current state example 2: Rover0: at waypoint1, available, equipped for soil analysis, equipped for imaging, has store0, has camera0 on board, can traverse from waypoint0 to waypoint2, can traverse from waypoint2 to waypoint1. Rover1: at waypoint0, available, equipped for rock analysis, equipped for imaging, has store1, has camera1 on board, can traverse from waypoint1 to waypoint0, can traverse from waypoint0 to waypoint2, has rock analyzed in waypoint0. Rover2: at waypoint2, available, equipped for soil analysis, has store2, can traverse from waypoint1 to waypoint2, can traverse from waypoint0 to waypoint1. Lander: at waypoint0. Camera0: is equipped on rover0, use objective2 as calibration target, supports high_res. Camera1: is equipped on rover1, use objective0 as calibration target, supports colour. Store0: on rover0, is empty. Store1: on rover1, is full. Store2: on rover2, is full. Waypoint0: has visuality of waypoint2, has visuality of objective0, has rock sample. Waypoint1: has visuality of waypoint0, has visuality of objective2, has soil sample. Waypoint2: has visuality of waypoint1, has visuality of objective1, has soil sample.\n"
    f"Action 2: Navigate the rover rover0 from waypoint waypoint1 to waypoint waypoint0?\n"
    f"Answer 2:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Rover0: at waypoint1, available, equipped for soil analysis, equipped for imaging, has store0, has camera0 on board, can traverse from waypoint0 to waypoint2, can traverse from waypoint2 to waypoint1. Waypoint1: has visuality of waypoint0, has visuality of objective2, has soil sample. Waypoint0: has visuality of waypoint2, has visuality of objective0, has rock sample.\n"
    f"Based on the domain description, A rover can navigate(traverse) from waypoint A to waypoint B. This action will result in: the rover is not at waypoint A, the rover is at waypoint B.\n"
    f"the rover is not at waypoint A, the rover is at waypoint B ::: Rover0: at waypoint0, available, equipped for soil analysis, equipped for imaging, has store0, has camera0 on board, can traverse from waypoint0 to waypoint2, can traverse from waypoint2 to waypoint1.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into a new paragraph.\n"
    f"Rover0: at waypoint0, available, equipped for soil analysis, equipped for imaging, has store0, has camera0 on board, can traverse from waypoint0 to waypoint2, can traverse from waypoint2 to waypoint1. Rover1: at waypoint0, available, equipped for rock analysis, equipped for imaging, has store1, has camera1 on board, can traverse from waypoint1 to waypoint0, can traverse from waypoint0 to waypoint2, has rock analyzed in waypoint0. Rover2: at waypoint2, available, equipped for soil analysis, has store2, can traverse from waypoint1 to waypoint2, can traverse from waypoint0 to waypoint1. Lander: at waypoint0. Camera0: is equipped on rover0, use objective2 as calibration target, supports high_res. Camera1: is equipped on rover1, use objective0 as calibration target, supports colour. Store0: on rover0, is empty. Store1: on rover1, is full. Store2: on rover2, is full. Waypoint0: has visuality of waypoint2, has visuality of objective0, has rock sample. Waypoint1: has visuality of waypoint0, has visuality of objective2, has soil sample. Waypoint2: has visuality of waypoint1, has visuality of objective1, has soil sample.\n"
    f"-------------------\n"
)


EXECUTABILITY_CHECKER_ROVERS_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: Rover0: at waypoint1, available, equipped for soil analysis, equipped for imaging, has store0, has camera0 on board, can traverse from waypoint0 to waypoint2, can traverse from waypoint2 to waypoint1. Rover1: at waypoint0, available, equipped for rock analysis, equipped for imaging, has store1, has camera1 on board, can traverse from waypoint1 to waypoint0, can traverse from waypoint0 to waypoint2, has rock analyzed in waypoint0. Rover2: at waypoint2, available, equipped for soil analysis, has store2, can traverse from waypoint1 to waypoint2, can traverse from waypoint0 to waypoint1. Lander: at waypoint0. Camera0: is equipped on rover0, use objective2 as calibration target, supports high_res. Camera1: is equipped on rover1, use objective0 as calibration target, supports colour. Store0: on rover0, is empty. Store1: on rover1, is full. Store2: on rover2, is full. Waypoint0: has visuality of waypoint2, has visuality of objective0, has rock sample. Waypoint1: has visuality of waypoint0, has visuality of objective2, has soil sample. Waypoint2: has visuality of waypoint1, has visuality of objective1, has soil sample.\n"
    f"Action 1: Navigate the rover rover0 from waypoint waypoint1 to waypoint waypoint2\n"
    f"Answer 1:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can check whether the action is executable.\n"
    f"Rover0: at waypoint1, available, equipped for soil analysis, equipped for imaging, has store0, has camera0 on board, can traverse from waypoint0 to waypoint2, can traverse from waypoint2 to waypoint1. Waypoint1: has visuality of waypoint0, has visuality of objective2, has soil sample. Waypoint2: has visuality of waypoint1, has visuality of objective1, has soil sample.\n"
    f"Based on the domain description, A rover can navigate(traverse) from waypoint A to waypoint B. This action is executable only if all following preconditions are satisfied: the rover is at waypoint A, the rover can traverse from A to B, the rover is available, waypoint B is visible for waypoint A.\n"
    f"the rover is at waypoint A, ::: Rover0: at waypoint1, available, equipped for soil analysis, equipped for imaging, has store0, has camera0 on board, can traverse from waypoint0 to waypoint2, can traverse from waypoint2 to waypoint1. ===> SATISFY\n"
    f"the rover can traverse from A to B, ::: Rover0: at waypoint1, available, equipped for soil analysis, equipped for imaging, has store0, has camera0 on board, can traverse from waypoint0 to waypoint2, can traverse from waypoint2 to waypoint1. ===> NOT SATISFY\n"
    f"Since not all preconditions are satisfied, this action is not executable.\n"
    f"Final answer: False.\n" 
    f"------------------\n"  
    f"Current state example 2: Rover0: at waypoint1, available, equipped for soil analysis, equipped for imaging, has store0, has camera0 on board, can traverse from waypoint0 to waypoint2, can traverse from waypoint2 to waypoint1. Rover1: at waypoint0, available, equipped for rock analysis, equipped for imaging, has store1, has camera1 on board, can traverse from waypoint1 to waypoint0, can traverse from waypoint0 to waypoint2, has rock analyzed in waypoint0. Rover2: at waypoint2, available, equipped for soil analysis, has store2, can traverse from waypoint1 to waypoint2, can traverse from waypoint0 to waypoint1. Lander: at waypoint0, has soil data, has objective0's image in colour. Camera0: is equipped on rover0, use objective2 as calibration target, supports high_res. Camera1: is equipped on rover1, use objective0 as calibration target, supports colour. Store0: on rover0, is empty. Store1: on rover1, is full. Store2: on rover2, is full. Waypoint0: has visuality of waypoint2, has visuality of objective0, has rock sample. Waypoint1: has visuality of waypoint0, has visuality of objective2, has soil sample. Waypoint2: has visuality of waypoint1, has visuality of objective1, has soil sample.\n"
    f"Action 2: sample the rock at waypoint waypoint1 with rover rover1 and store it in store store1\n"
    f"Answer 2:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can check whether the action is executable.\n"
    f"Rover1: at waypoint0, available, equipped for rock analysis, equipped for imaging, has store1, has camera1 on board, can traverse from waypoint1 to waypoint0, can traverse from waypoint0 to waypoint2, has rock analyzed in waypoint0. Waypoint1: has visuality of waypoint0, has visuality of objective2, has soil sample. Store1: on rover1, is full.\n"
    f"Based on the domain description, A rover can sample rock(or soil) at waypoint A and store it in store X. This action is executable only if all following preconditions are satisfied: the rover is at waypoint A, store X is on the rover, store X is empty, waypoint A has rock sample(or soil sample), the rover is available, the rover is equipped for rock(or soil) analysis.\n"
    f"the rover is at waypoint A ::: Rover1: at waypoint0, available, equipped for rock analysis, equipped for imaging, has store1, has camera1 on board, can traverse from waypoint1 to waypoint0, can traverse from waypoint0 to waypoint2, has rock analyzed in waypoint0. ===> NOT SATISFY\n"
    f"Since not all preconditions are satisfied, this action is not executable.\n"
    f"Final answer: False.\n"
    f"-------------------\n"
)


STATE_CHECKER_ROVERS_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: Rover0: at waypoint0, available, equipped for soil analysis, equipped for imaging, has store0, has camera1 on board, can traverse from waypoint0 to waypoint2, can traverse from waypoint2 to waypoint1. Rover1: at waypoint2, available, equipped for rock analysis, equipped for imaging, has store1, has camera0 on board, can traverse from waypoint2 to waypoint0, can traverse from waypoint2 to waypoint1, has rock analyzed in waypoint2. Rover2: at waypoint1, available, equipped for soil analysis, has store2, can traverse from waypoint1 to waypoint2, can traverse from waypoint1 to waypoint0. Lander: at waypoint2, has rock data, has objective2's image in high_res. Camera0: is equipped on rover1, use objective1 as calibration target, supports high_res. Camera1: is equipped on rover0, use objective2 as calibration target, supports colour. Store0: on rover0, is full. Store1: on rover1, is empty. Store2: on rover2, is full. Waypoint0: has visuality of waypoint1, has visuality of objective2, has rock sample. Waypoint1: has visuality of waypoint0, has visuality of objective1, has soil sample. Waypoint2: has visuality of waypoint0, has visuality of objective0, has soil sample.\n"
    f"Question 1: Will the fact \"Store(s) store0 and store1 are full\" hold?\n"
    f"Answer 1:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false.\n"
    f"Store(s) store0 and store1 are full ::: Store0: on rover0, is full. Store1: on rover1, is empty. ===> NOT SATISFY\n"
    f"Since there are some propositions in the question doesn't match with the current state, the question is false.\n"
    f"Final answer: False.\n"
    f"-------------------\n"
    f"Current state example 2: Rover0: at waypoint2, available, equipped for soil analysis, equipped for imaging, has store0, has camera0 on board, can traverse from waypoint2 to waypoint0, can traverse from waypoint0 to waypoint1. Rover1: at waypoint1, available, equipped for rock analysis, equipped for imaging, has store1, has camera1 on board, can traverse from waypoint1 to waypoint0, can traverse from waypoint1 to waypoint2, has rock analyzed in waypoint1. Rover2: at waypoint0, available, equipped for soil analysis, has store2, can traverse from waypoint0 to waypoint2, can traverse from waypoint0 to waypoint1. Lander: at waypoint1, has soil data, has objective1's image in colour. Camera0: is equipped on rover0, use objective0 as calibration target, supports high_res. Camera1: is equipped on rover1, use objective1 as calibration target, supports colour. Store0: on rover0, is empty. Store1: on rover1, is full. Store2: on rover2, is full. Waypoint0: has visuality of waypoint1, has visuality of objective1, has rock sample. Waypoint1: has visuality of waypoint2, has visuality of objective0, has soil sample. Waypoint2: has visuality of waypoint0, has visuality of objective2, has soil sample.\n"
    f"Question 2: Will the fact \"Objective0 is visible from rover1's current location\" hold?\n"     
    f"Answer 2:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false.\n"
    f"Objective1 is visible from rover1's current location ::: Rover1: at waypoint1, available, equipped for rock analysis, equipped for imaging, has store1, has camera1 on board, can traverse from waypoint1 to waypoint0, can traverse from waypoint1 to waypoint2, has rock analyzed in waypoint1. Waypoint1: has visuality of waypoint2, has visuality of objective0, has soil sample. ===> SATISFY\n"
    f"Since all propositions in the question match with the current state, the question is true.\n"
    f"Final answer: True.\n"
    f"-------------------\n"
)



TWOSHOTCOT_APP_ROVERS_EXAMPLE = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"Initial State: This is a Rovers domain where rovers must navigate between waypoints gathering data and transmitting it back to a lander. Rovers cannot navigate to all waypoints and this makes particular routes impassable to some of the rovers. Data transmission is also constrained by the visibility of the lander from the waypoints. There are 2 rovers, 3 waypoints, 2 stores, 3 cameras, 3 objectives numbered consecutively. Further, there is 1 lander and 3 modes for the camera namely colour, high resolution, and low resolution. Rover(s) rover0 and rover1 are equipped for soil analysis. Rover(s) rover1 is equipped for rock analysis. Rover(s) rover0 and rover1 are equipped for imaging. Rover rover1 has store store1. Rover rover0 has store store0. Rover rover0 has camera0 and camera1 on board. Rover rover1 has camera2 on board. Camera camera1 can be calibrated on objective0. Camera camera0 can be calibrated on objective1. Camera camera2 can be calibrated on objective0. Camera camera2 supports high_res and colour. Camera camera0 supports colour. Camera camera1 supports low_res. Rover rover1 can traverse from waypoint2 to waypoint1, waypoint0 to waypoint2, waypoint2 to waypoint0, waypoint1 to waypoint2. Rover rover0 can traverse from waypoint0 to waypoint2, waypoint1 to waypoint0, waypoint0 to waypoint1, waypoint2 to waypoint0. Waypoint(s) are visible from waypoint0: waypoint2 and waypoint1. Waypoint(s) are visible from waypoint1: waypoint2 and waypoint0. Waypoint(s) are visible from waypoint2: waypoint1 and waypoint0. Objective objective1 is visible from waypoint2. Objective objective2 is visible from waypoint1. Objective objective0 is visible from waypoint1 and waypoint0. Lander general is at waypoint waypoint1. Currently, Rover rover1 is at waypoint0. Rover rover0 is at waypoint0. Soil can be sampled at the following location(s): waypoint0. Rovers rover1 and rover0 are available. Rock data was communicated from waypoint waypoint0; Rover rover1 has rock analyzed in waypoint waypoint0. Rover rover1 has its camera camera2 calibrated. Store(s) store0 is empty. Store(s) store1 is full.\n"
    f"Question: Is the following action applicable in this state: calibrate the camera camera0 on rover rover0 for the objective objective1 at the waypoint waypoint0?\n"
    f"Answer:\n"
    f"Step 1: we find related objects in the current state.\n"
    f"Rover rover0 is at waypoint0. Camera camera0 can be calibrated on objective1. Objective objective1 is visible from waypoint2.\n"
    f"Step 2: we check whether the action is applicable.\n"
    f"A camera on the rover can be calibrated/adjusted for objective X at waypoint A. This action is executable only if all following preconditions are satisfied: the rover is at waypoint A, waypoint A has the visuality of the objective X, the camera is equipped on the rover, the camera can be calibrated using objective X(X is the calibration target). We can see rover0 is at waypoint. However, objective1 is visible from waypoint2. So this action is not applicable.\n"
    f"Step 3: We return our answer based on previous analysis. \n"
    f"Final Answer: False.\n"
    f"-------------------\n"
    f"(Example 2)\n"
    f"Initial state: This is a Rovers domain where rovers must navigate between waypoints gathering data and transmitting it back to a lander. Rovers cannot navigate to all waypoints and this makes particular routes impassable to some of the rovers. Data transmission is also constrained by the visibility of the lander from the waypoints. There are 2 rovers, 3 waypoints, 2 stores, 3 cameras, 3 objectives numbered consecutively. Further, there is 1 lander and 3 modes for the camera namely colour, high resolution, and low resolution. Rover(s) rover0 and rover1 are equipped for soil analysis. Rover(s) rover1 is equipped for rock analysis. Rover(s) rover0 and rover1 are equipped for imaging. Rover rover1 has store store1. Rover rover0 has store store0. Rover rover1 has camera2 on board. Rover rover0 has camera1 and camera0 on board. Camera camera0 can be calibrated on objective1. Camera camera2 can be calibrated on objective0. Camera camera1 can be calibrated on objective0. Camera camera2 supports colour and high_res. Camera camera0 supports colour. Camera camera1 supports low_res. Rover rover0 can traverse from waypoint0 to waypoint2, waypoint2 to waypoint0, waypoint1 to waypoint0, waypoint0 to waypoint1. Rover rover1 can traverse from waypoint2 to waypoint1, waypoint0 to waypoint2, waypoint1 to waypoint2, waypoint2 to waypoint0. Waypoint(s) are visible from waypoint0: waypoint2 and waypoint1. Waypoint(s) are visible from waypoint1: waypoint2 and waypoint0. Waypoint(s) are visible from waypoint2: waypoint0 and waypoint1. Objective objective1 is visible from waypoint2. Objective objective0 is visible from waypoint1 and waypoint0. Objective objective2 is visible from waypoint1. Lander general is at waypoint waypoint1. Currently, Rover rover1 is at waypoint0. Lander general is at waypoint waypoint1. Rover rover0 is at waypoint0. Rocks can be sampled at the following location(s): waypoint0. Rovers rover1 and rover0 are available. Rover rover0 has soil analyzed in waypoint waypoint0. Store(s) store1 is empty. Store(s) store0 is full. Rover rover1 has its camera camera2 calibrated. Rover rover1 has the image data of objective objective0 in mode high_res.\n"
    f"Question: Which of the following actions will be applicable in this state? A. calibrate the camera camera1 on rover rover0 for the objective objective2 at the waypoint waypoint2. B. calibrate the camera camera0 on rover rover0 for the objective objective1 at the waypoint waypoint0. C. communicate the rock data from rover rover1 at waypoint waypoint0 to lander general at waypoint waypoint1 using rock analysis of waypoint waypoint1. D. communicate the image data of objective objective0 in mode high_res from rover rover1 at waypoint waypoint0 to lander general at waypoint waypoint1.\n"
    f"Answer:\n"
    f"Step 1: We check each option one by one. \n"
    f"Option A: calibrate the camera camera1 on rover rover0 for the objective objective2 at the waypoint waypoint2. A camera on the rover can be calibrated/adjusted for objective X at waypoint A. This action is executable only if all following preconditions are satisfied: the rover is at waypoint A, waypoint A has the visuality of the objective X, the camera is equipped on the rover, the camera can be calibrated using objective X(X is the calibration target). We can see rover0 is at waypoint0. So this action is not applicable.\n"
    f"Option B: calibrate the camera camera0 on rover rover0 for the objective objective1 at the waypoint waypoint0. A camera on the rover can be calibrated/adjusted for objective X at waypoint A. This action is executable only if all following preconditions are satisfied: the rover is at waypoint A, waypoint A has the visuality of the objective X, the camera is equipped on the rover, the camera can be calibrated using objective X(X is the calibration target). We can see rover0 is at waypoint0, objective1 is visible from waypoint0, camera0 is equipped on rover0. However, objective1 is visible from waypoint2. So this action is not applicable.\n"
    f"Option C: communicate the rock data from rover rover1 at waypoint waypoint0 to lander general at waypoint waypoint1 using rock analysis of waypoint waypoint1. A rover can communicate(transmit) data at waypoint waypoint X to the lander general at waypoint waypoint Y through waypoint X. The data can be image of objective, soil data or rock data. This action is executable only if all following preconditions are satisfied: the rover is at waypoint X, the rover is available, the lander general is at waypoint Y, waypoint X has visuality of waypoint Y, the rover has the data. We can see rover1 does not has rock data, so this action is not applicable.\n"
    f"Option D: communicate the image data of objective objective0 in mode high_res from rover rover1 at waypoint waypoint0 to lander general at waypoint waypoint1. A rover can communicate(transmit) data at waypoint waypoint X to the lander general at waypoint waypoint Y through waypoint X. The data can be image of objective, soil data or rock data. This action is executable only if all following preconditions are satisfied: the rover is at waypoint X, the rover is available, the lander general is at waypoint Y, waypoint X has visuality of waypoint Y, the rover has the data. We can see rover1 is at waypoint0, waypoint0 has visuality of waypoint1, rover1 has the image data of objective objective0 in mode high_res, the lander general is at waypoint1. So this action is applicable.\n"
    f"Step 3: We return our answer based on previous analysis. \n"
    f"Final Answer: D.\n"
    f"-------------------\n"
)


TWOSHOTCOT_PROG_ROVERS_EXAMPLE = (
    F"[Examples]\n"
    f"(example 1)\n"
    f"Initial state: This is a Rovers domain where rovers must navigate between waypoints gathering data and transmitting it back to a lander. Rovers cannot navigate to all waypoints and this makes particular routes impassable to some of the rovers. Data transmission is also constrained by the visibility of the lander from the waypoints. There are 2 rovers, 3 waypoints, 2 stores, 3 cameras, 3 objectives numbered consecutively. Further, there is 1 lander and 3 modes for the camera namely colour, high resolution, and low resolution. Rover(s) rover0 and rover1 are equipped for soil analysis. Rover(s) rover1 is equipped for rock analysis. Rover(s) rover0 and rover1 are equipped for imaging. Rover rover1 has store store1. Rover rover0 has store store0. Rover rover0 has camera0 and camera1 on board. Rover rover1 has camera2 on board. Camera camera0 can be calibrated on objective1. Camera camera1 can be calibrated on objective0. Camera camera2 can be calibrated on objective0. Camera camera0 supports colour. Camera camera1 supports low_res. Camera camera2 supports high_res and colour. Rover rover0 can traverse from waypoint2 to waypoint0, waypoint1 to waypoint0, waypoint0 to waypoint1, waypoint0 to waypoint2. Rover rover1 can traverse from waypoint2 to waypoint0, waypoint1 to waypoint2, waypoint2 to waypoint1, waypoint0 to waypoint2. Waypoint(s) are visible from waypoint2: waypoint0 and waypoint1. Waypoint(s) are visible from waypoint0: waypoint1 and waypoint2. Waypoint(s) are visible from waypoint1: waypoint0 and waypoint2. Objective objective1 is visible from waypoint2. Objective objective0 is visible from waypoint0 and waypoint1. Objective objective2 is visible from waypoint1. Lander general is at waypoint waypoint1. Currently, Rover rover0 is at waypoint0. Rover rover1 is at waypoint0. Rover rover0 has soil analyzed in waypoint waypoint0. Rover rover1 has rock analyzed in waypoint waypoint0. Rover rover0 has image objective1 in mode colour. Rovers rover0 and rover1 are available. Store(s) store0 is full. Store(s) store1 is empty.\n"
    f"Question: Will the fact \"Store store0 is empty\" hold after performing the action \"communicate the image data of objective objective1 in mode colour from rover rover0 at waypoint waypoint0 to lander general at waypoint waypoint1\" in the current state?\n"
    f"Answer 1:\n"
    f"Step 1: Take the action and get the new state.\n"
    f"communicate the image data of objective objective1 in mode colour from rover rover0 at waypoint waypoint0 to lander general at waypoint waypoint1. Atfer this action, the lander general has the image data of objective objective1 in mode colour.\n"
    f"Step 2: Check whether the fact hold.\n"
    f"Store store0 is empty. We can see store0 is still empty, so this fact is held.\n"
    f"Step 3: We return our answer based on previous analysis.\n"
    f"Final Answer: True.\n"
    f"-------------------\n"
    f"(Example 2)\n"
    f"Initial state: This is a Rovers domain where rovers must navigate between waypoints gathering data and transmitting it back to a lander. Rovers cannot navigate to all waypoints and this makes particular routes impassable to some of the rovers. Data transmission is also constrained by the visibility of the lander from the waypoints. There are 2 rovers, 5 waypoints, 2 stores, 3 cameras, and 2 objectives. There is 1 lander and 3 camera modes: colour, high resolution, and low resolution. Rover(s) rover0 and rover1 are equipped for rock analysis. Rover(s) rover0 is equipped for imaging. Rover rover0 has store store0 and rover1 has store store1. Rover rover0 has camera0 and camera1. Rover rover1 has camera2. Camera camera0 supports high_res and colour. Camera camera1 supports low_res. Camera camera2 supports colour. Camera camera0 can be calibrated on objective0. Camera camera1 can be calibrated on objective1. Camera camera2 can be calibrated on objective1. Rover rover0 can traverse from waypoint0 to waypoint1, waypoint1 to waypoint0, waypoint0 to waypoint2, waypoint2 to waypoint0. Rover rover1 can traverse from waypoint3 to waypoint4, waypoint4 to waypoint3. Waypoint(s) are visible from waypoint0: waypoint1 and waypoint2. Waypoint(s) are visible from waypoint2: waypoint0. Waypoint(s) are visible from waypoint4: waypoint3. Objective objective0 is visible from waypoint2. Objective objective1 is visible from waypoint4. Lander general is at waypoint waypoint1. Currently, rover rover0 is at waypoint0 and rover rover1 is at waypoint4. Rover rover0 is available. Rover rover1 is available. Store store0 is full. Store store1 is empty. Rover rover0 has image objective0 in mode colour. Camera camera0 on rover rover0 is calibrated.\n"
    f"Question: Which of the following facts will hold after performing the action \"drop store store0 of rover rover0\" in the current state? A.Store(s) store0 is full. B.Store(s) store0 is empty. C.Rover rover1 is at waypoint0. D.Camera camera1 on rover rover0 is calibrated.\n"
    f"Step 1: Take the action and get the new state.\n"
    f"drop store store0 of rover rover0. After this action, store0 is empty.\n"
    f"Step 2: Check each option to find the answer.\n"
    f"Option A: A.Store(s) store0 is full. We can see store0 is empty. So this option is false.\n"
    f"Option B: Store(s) store0 is empty. We can see store0 is empty. So this option is true.\n"
    f"Step 3: We return our answer based on previous analysis.\n"
    f"Final Answer: B.\n"
    f"-------------------\n"
)


TWOSHOTCOT_VAL_ROVERS_EXAMPLE = (
    f"[Examples]\n"
    f"(example 1)\n"
    f"Initial state: This is a Rovers domain where rovers must navigate between waypoints gathering data and transmitting it back to a lander. Rovers cannot navigate to all waypoints and this makes particular routes impassable to some of the rovers. Data transmission is also constrained by the visibility of the lander from the waypoints. There are 2 rovers, 7 waypoints, 2 stores, 3 cameras, 2 objectives numbered consecutively. Further, there is 1 lander and 3 modes for the camera namely colour, high resolution, and low resolution.  No rovers are equipped for soil analysis. Rover(s) rover0 and rover1 are equipped for rock analysis. Rover(s) rover0 and rover1 are equipped for imaging. Rover rover1 has store store1. Rover rover0 has store store0. Rover rover0 has camera2 on board. Rover rover1 has camera1 and camera0 on board. Camera camera1 can be calibrated on objective0. Camera camera2 can be calibrated on objective1. Camera camera0 can be calibrated on objective1. Camera camera0 supports high_res and low_res and colour. Camera camera2 supports colour and low_res. Camera camera1 supports colour. Rover rover0 can traverse from waypoint0 to waypoint5, waypoint6 to waypoint5, waypoint1 to waypoint5, waypoint2 to waypoint5, waypoint5 to waypoint1, waypoint5 to waypoint6, waypoint5 to waypoint2, waypoint3 to waypoint0, waypoint4 to waypoint5, waypoint5 to waypoint4, waypoint5 to waypoint0, waypoint0 to waypoint3. Rover rover1 can traverse from waypoint2 to waypoint4, waypoint0 to waypoint6, waypoint6 to waypoint0, waypoint0 to waypoint2, waypoint5 to waypoint0, waypoint0 to waypoint3, waypoint2 to waypoint0, waypoint0 to waypoint5, waypoint1 to waypoint6, waypoint6 to waypoint1, waypoint3 to waypoint0, waypoint4 to waypoint2. Waypoint(s) are visible from waypoint5: waypoint6, waypoint1, waypoint4, waypoint3, waypoint0, and waypoint2. Waypoint(s) are visible from waypoint4: waypoint2, waypoint5, waypoint1, waypoint6, and waypoint3. Waypoint(s) are visible from waypoint0: waypoint3, waypoint2, waypoint5, and waypoint6. Waypoint(s) are visible from waypoint1: waypoint4, waypoint3, waypoint6, waypoint2, and waypoint5. Waypoint(s) are visible from waypoint6: waypoint4, waypoint3, waypoint0, waypoint5, and waypoint1. Waypoint(s) are visible from waypoint2: waypoint4, waypoint3, waypoint0, waypoint5, and waypoint1. Waypoint(s) are visible from waypoint3: waypoint4, waypoint0, waypoint2, waypoint5, waypoint1, and waypoint6. Objective objective1 is visible from waypoint0, waypoint5, waypoint4, and waypoint2. Objective objective0 is visible from waypoint0. Lander general is at waypoint waypoint3.  Currently, Rover rover1 is at waypoint0. Rover rover0 is at waypoint5. Rocks can be sampled at the following location(s): waypoint6, waypoint5, waypoint3, waypoint2, and waypoint4. Soil can be sampled at the following location(s): waypoint6, waypoint1, waypoint3, and waypoint4. Rovers rover0 and rover1 are available. Store(s) store1 and store0 are empty. The goal is to reach a state where the following facts hold: Rock data was communicated from waypoint waypoint4;, and Image objective1 was communicated in mode high_res.\n"
    f"Question: Is the following sequence of actions \"move the rover rover1 from waypoint waypoint0 to waypoint waypoint2, sample rock at waypoint waypoint2 with rover rover1 and store in store store1\" applicable in the current state?\n"
    f"Answer:\n"
    f"Step 1: Since the question askes whether the action sequence is applicable. So we check each actions precondtions, if applicable, we take the action and get the new state. If not, the action sequence is not applicable.\n"
    f"Action 1: move the rover rover1 from waypoint waypoint0 to waypoint waypoint2. This action is executable only if all following preconditions are satisfied: the rover is at waypoint0, the rover is available. We can see rover1 is at waypoint0, rover1 is available. So this action is executable. After this action, rover1 is at waypoint2.\n"
    f"Action 2: sample rock at waypoint waypoint2 with rover rover1 and store in store store1. This action is executable only if all following preconditions are satisfied: the rover is at waypoint2, the rover is available, store1 is on rover1, store1 is empty, waypoint2 has rock sample, the rover is equipped for rock analysis. We can see rover1 is at waypoint2, rover1 is available, store1 is on rover1, store1 is empty, waypoint2 has rock sample, rover1 is equipped for rock analysis. So this action is executable. After this action, store1 is full.\n"
    f"Step 2: Return the answer based on the analysis.\n"
    f"Final Answer: True.\n"
    f"-------------------\n"
    f"(example 2)\n"
    f"Initial state: This is a Rovers domain where rovers must navigate between waypoints gathering data and transmitting it back to a lander. Rovers cannot navigate to all waypoints and this makes particular routes impassable to some of the rovers. Data transmission is also constrained by the visibility of the lander from the waypoints. There are 2 rovers, 5 waypoints, 2 stores, 2 cameras, 2 objectives numbered consecutively. Further, there is 1 lander and 3 modes for the camera namely colour, high resolution, and low resolution.  Rover(s) rover0 and rover1 are equipped for soil analysis. Rover(s) rover1 is equipped for rock analysis. Rover(s) rover0 and rover1 are equipped for imaging. Rover rover0 has store store0. Rover rover1 has store store1. Rover rover0 has camera0 on board. Rover rover1 has camera1 on board. Camera camera1 can be calibrated on objective0. Camera camera0 can be calibrated on objective0. Camera camera1 supports colour and low_res. Camera camera0 supports colour and low_res. Rover rover0 can traverse from waypoint4 to waypoint1, waypoint0 to waypoint1, waypoint1 to waypoint0, waypoint1 to waypoint4. Rover rover1 can traverse from waypoint0 to waypoint2, waypoint1 to waypoint2, waypoint2 to waypoint1, waypoint2 to waypoint0. Waypoint(s) are visible from waypoint2: waypoint3, waypoint0, and waypoint1. Waypoint(s) are visible from waypoint1: waypoint4, waypoint2, and waypoint0. Waypoint(s) are visible from waypoint0: waypoint4, waypoint2, waypoint1, and waypoint3. Waypoint(s) are visible from waypoint3: waypoint0 and waypoint2. Waypoint(s) are visible from waypoint4: waypoint0 and waypoint1. Objective objective0 is visible from waypoint1 and waypoint2. Objective objective1 is visible from waypoint4. Lander general is at waypoint waypoint3.  Currently, Rover rover0 is at waypoint0. Rover rover1 is at waypoint2. Rocks can be sampled at the following location(s): waypoint0 and waypoint1. Soil can be sampled at the following location(s): waypoint0. Rovers rover0 and rover1 are available. Store(s) store0 and store1 are empty. The goal is to reach a state where the following facts hold: Image objective0 was communicated in mode colour, Image objective1 was communicated in mode low_res, Rock data was communicated from waypoint waypoint0;, Rock data was communicated from waypoint waypoint1;, Soil data was communicated from waypoint waypoint0;, and Image objective0 was communicated in mode low_res.\n"
    f"Question: Which of the following claims is true with regard to the following sequence of actions: \"navigate the rover rover1 from waypoint waypoint2 to waypoint waypoint0\"? A.The sequence is not applicable. B.The sequence is applicable, but does not achieve the goal. C.The sequence is not valid. D.The sequence is a plan\n"
    f"Answer:\n"
    f"Step 1: Since the question ask whether the action sequence is a plan, we need to take actions to reach the fianl answer, then check the goal.\n"
    f"Action 1: navigate the rover rover1 from waypoint waypoint2 to waypoint waypoint0. A rover can navigate(traverse) from waypoint A to waypoint B. This action is executable only if all following preconditions are satisfied: the rover is at waypoint A, the rover can traverse from A to B, the rover is available, waypoint B is visible for waypoint A. We can see rover1 is at waypoint2, rover1 can traverse from waypoint2 to waypoint0, rover1 is available, waypoint0 is visible for waypoint2. So this action is executable. After this action, rover1 is at waypoint0. So the action is applicable. After taking this action, rover1 is at waypoint0.\n"
    f"Step 2: We check whether the goal is reached.\n"
    f"The goal is to reach a state where the following facts hold: Image objective0 was communicated in mode colour, Image objective1 was communicated in mode low_res, Rock data was communicated from waypoint waypoint0;, Rock data was communicated from waypoint waypoint1;, Soil data was communicated from waypoint waypoint0;, and Image objective0 was communicated in mode low_res. We can see after taking the action, none of the goal is reached. So the action sequence is applicable, but does not achieve the goal.\n"
    f"Step 3: We return our answer based on previous analysis.\n"
    f"Final Answer: B.\n"
    f"-------------------\n"
)





#-------------------------------------
#Floortile Prompts
#-------------------------------------
FLOORTILE_DOMAIN_DESCRIPTION =(
    f"[Domain Description]\n"
    f"The floortile involves robots and a n-lines * m-columns grid made up of tiles, and tiles in the grid are numbered in a column-major order (bottom to top, then left to right). The robot can hold a color at a time, but it can change to any available color. The tile can be painted with a color(black and white), and the cell color must alternated with each other. Once the tile is painted, the robot can not stand on it. Besides, a robot can only paint a tile which is above or down from the tile the robot is standing at.\n"
    f"We use different color to describe different objects. For robot we use: at tile_x, holding color_x. For tile we use: is to the right(or left, above, down) of tile_8, painted with color_x, clear, has robot_x standing on it. \n"
    f"Following actions are executable only if all preconditions are met, if any condition are not satisfied, the action is not executable.\n"
    f"A robot can move(navigate) from tile A to tile B. This action is executable only if all following preconditions are satisfied: the robot is currently at tile A, tile A and B are adjacent, tile B is clear.\n"
    f"A robot can paint(apply) tile X with the color from tile Y. This action is executable only if all following preconditions are satisfied: the robot is currently at tile Y, tile Y is above or downward from tile X, the robot is holding the color, tile X is clear.\n"
    f"A robot can alter(change) the color from color A to color B. This action is executable only if all following preconditions are satisfied: the robot is currently holding color A, color B is different from color A.\n"
    f"Executing an action will change states of related objects.\n"
    f"A robot can move(navigate) from tile A to tile B. This action will result in: the robot is not at tile A, the robot is currently at tile B, tile A is clear, tile B is not clear, tile B has the robot standing on it.\n"
    f"A robot can paint(apply) tile X with the color from tile Y. This action will result in: tile X is painted with color, tile X is not clear.\n"
    f"A robot can alter(change) the color from color A to color B. This action will result in: the robot is holding color B.\n"
)


INITIAL_STATE_EXTRACTOR_FLOORTILE_PROMPT = (
    f"This is a question related to the floortilefloortile domain. You are required to extract the initial state of every object in this plan, including robots and tiles. Your answer must satisfy all the following requirements. First, think and respond with the format from the example above, including the word choice and paragraph structure. Second, each object's state should contain all properties mentioned in the domain description above. Besides, don't use any markdown formatting."

)

INITIAL_STATE_EXTRACTOR_FLOORTILE_EXAMPLE = (
    f"[Examples]\n"
    f"Initial state example 1: A set of robots use different colors to paint patterns in floor tiles. The robots can move around the floor tiles in four directions (up, down, left and right). Robots paint with one color at a time, but can change their spray guns to any available color. However, robots can only paint the tile that is in front (up) and behind (down) them, and once a tile has been painted no robot can stand on it. Robots need to paint a grid with black and white, where the cell color is alternated always. There are 9 tiles and 2 robots. The tiles locations are: tile_8 is to the right of tile_7, tile_6 is to the right of tile_5, tile_3 is to the right of tile_2, tile_2 is to the right of tile_1, tile_9 is to the right of tile_8, and tile_5 is to the right of tile_4. Further, tile_4 is down from tile_7, tile_5 is down from tile_8, tile_2 is down from tile_5, tile_3 is down from tile_6, tile_6 is down from tile_9, and tile_1 is down from tile_4. Currently, robot robot1 is at tile_3 and holding color white and robot robot2 is at tile_2 and holding color white; tile_5, tile_4, tile_6, and tile_1 are clear; tile_9 is painted black, tile_8 is painted white, and tile_7 is painted black.\n"
    f"Extracted from exampl 1:\n"
    f"First, we confirm every object involved in the initial state. We can find 9 tiles and 2 robots, numbered consecutively.\n"
    f"Then we extract each object's state.\n"
    f"The tiles locations are: tile_8 is to the right of tile_7, tile_6 is to the right of tile_5, tile_3 is to the right of tile_2, tile_2 is to the right of tile_1, tile_9 is to the right of tile_8, and tile_5 is to the right of tile_4. Further, tile_4 is down from tile_7, tile_5 is down from tile_8, tile_2 is down from tile_5, tile_3 is down from tile_6, tile_6 is down from tile_9, and tile_1 is down from tile_4. ::: Tile_8: is to the right of tile_7. Tile_6: is to the right of tile_5, is down from tile_9. Tile_3: is to the right of tile_2, is down from tile_6. Tile_2: is to the right of tile_1, is down from tile_5. Tile_9: is to the right of tile_8. Tile_5: is to the right of tile_4. Tile_4: is down from tile_7. Tile_5: is down from tile_8. Tile_1: is down from tile_4.\n"
    f"Currently, robot robot1 is at tile_3 and holding color white and robot robot2 is at tile_2 and holding color white. ::: Robot1: at tile_3, holding white color. Robot2: at tile_2, holding color white.\n"
    f"tile_5, tile_4, tile_6, and tile_1 are clear; tile_9 is painted black, tile_8 is painted white, and tile_7 is painted black. ::: Tile_5: is clear, is down from tile_8. Tile_4: is clear, is down from tile_7. Tile_6: is clear, is to the right of tile_5, is down from tile_9. Tile_1: is clear, is down from tile_4. Tile_9: is painted black, is to the right of tile_8. Tile_8: is painted white, is to the right of tile_7. Tile_7: is painted black.\n"
    f"Then, we organize all objects states into a new paragraph as the end of answer.\n"
    f"Tile_8: is to the right of tile_7. Tile_6: is to the right of tile_5, is down from tile_9. Tile_3: is to the right of tile_2, is down from tile_6. Tile_2: is to the right of tile_1, is down from tile_5. Tile_9: is to the right of tile_8. Tile_5: is to the right of tile_4. Tile_4: is down from tile_7. Tile_5: is down from tile_8. Tile_1: is down from tile_4. Robot1: at tile_3, holding white color. Robot2: at tile_2, holding color white. Tile_5: is clear, is down from tile_8. Tile_4: is clear, is down from tile_7. Tile_6: is clear, is to the right of tile_5, is down from tile_9. Tile_1: is clear, is down from tile_4. Tile_9: is painted black, is to the right of tile_8. Tile_8: is painted white, is to the right of tile_7. Tile_7: is painted black.\n"
    f"-------------------\n"
    f"Initial state example 2: A set of robots use different colors to paint patterns in floor tiles. The robots can move around the floor tiles in four directions (up, down, left and right). Robots paint with one color at a time, but can change their spray guns to any available color. However, robots can only paint the tile that is in front (up) and behind (down) them, and once a tile has been painted no robot can stand on it. Robots need to paint a grid with black and white, where the cell color is alternated always. There are 20 tiles and 2 robots. The tiles locations are: tile_2 is up from tile_1, tile_3 is up from tile_2, tile_4 is up from tile_3, tile_6 is up from tile_5, tile_7 is up from tile_6, tile_8 is up from tile_7, tile_10 is up from tile_9, tile_11 is up from tile_10, tile_12 is up from tile_11, tile_14 is up from tile_13, tile_15 is up from tile_14, tile_16 is up from tile_15, tile_18 is up from tile_17, tile_19 is up from tile_18, tile_20 is up from tile_19, tile_5 is to the right of tile_1, tile_6 is to the right of tile_2, tile_7 is to the right of tile_3, tile_8 is to the right of tile_4, tile_9 is to the right of tile_5, tile_10 is to the right of tile_6, tile_11 is to the right of tile_7, tile_12 is to the right of tile_8, tile_13 is to the right of tile_9, tile_14 is to the right of tile_10, tile_15 is to the right of tile_11, tile_16 is to the right of tile_12, tile_17 is to the right of tile_13, tile_18 is to the right of tile_14, tile_19 is to the right of tile_15, tile_20 is to the right of tile_16. Currently, robot robot1 is at tile_10 and holding color white and robot robot2 is at tile_15 and holding color black; tile_5, tile_6, tile_7, and tile_18 are clear; tile_8 is painted black, tile_11 is painted white, and tile_13 is painted white.\n"
    f"Extracted from example 2: \n"
    f"First, we confirm every object involved in the initial state. We can find 20 tiles and 2 robots, numbered consecutively.\n"
    f"Then we extract each object's state.\n"
    f"The tiles locations are: tile_2 is up from tile_1, tile_3 is up from tile_2, tile_4 is up from tile_3, tile_6 is up from tile_5, tile_7 is up from tile_6, tile_8 is up from tile_7, tile_10 is up from tile_9, tile_11 is up from tile_10, tile_12 is up from tile_11, tile_14 is up from tile_13, tile_15 is up from tile_14, tile_16 is up from tile_15, tile_18 is up from tile_17, tile_19 is up from tile_18, tile_20 is up from tile_19, tile_5 is to the right of tile_1, tile_6 is to the right of tile_2, tile_7 is to the right of tile_3, tile_8 is to the right of tile_4, tile_9 is to the right of tile_5, tile_10 is to the right of tile_6, tile_11 is to the right of tile_7, tile_12 is to the right of tile_8, tile_13 is to the right of tile_9, tile_14 is to the right of tile_10, tile_15 is to the right of tile_11, tile_16 is to the right of tile_12, tile_17 is to the right of tile_13, tile_18 is to the right of tile_14, tile_19 is to the right of tile_15, tile_20 is to the right of tile_16. ::: Tile_2: is up from tile_1. Tile_3: is up from tile_2. Tile_4: is up from tile_3. Tile_6: is up from tile_5. Tile_7: is up from tile_6. Tile_8: is up from tile_7. Tile_10: is up from tile_9. Tile_11: is up from tile_10. Tile_12: is up from tile_11. Tile_14: is up from tile_13. Tile_15: is up from tile_14. Tile_16: is up from tile_15. Tile_18: is up from tile_17. Tile_19: is up from tile_18. Tile_20: is up from tile_19. Tile_5: is to the right of tile_1. Tile_6: is to the right of tile_2. Tile_7: is to the right of tile_3. Tile_8: is to the right of tile_4. Tile_9: is to the right of tile_5. Tile_10: is to the right of tile_6. Tile_11: is to the right of tile_7. Tile_12: is to the right of tile_8. Tile_13: is to the right of tile_9. Tile_14: is to the right of tile_10. Tile_15: is to the right of tile_11. Tile_16: is to the right of tile_12. Tile_17: is to the right of tile_13. Tile_18: is to the right of tile_14. Tile_19: is to the right of tile_15. Tile_20: is to the right of tile_16.\n"
    f"Currently, robot robot1 is at tile_10 and holding color white and robot robot2 is at tile_15 and holding color black. ::: Robot1: at tile_10, holding white color. Robot2: at tile_15, holding black color.\n"
    f"tile_5, tile_6, tile_7, and tile_18 are clear; tile_8 is painted black, tile_11 is painted white, and tile_13 is painted white. ::: Tile_5: is clear, is to the right of tile_1. Tile_6: is clear, is to the right of tile_2, is up from tile_5. Tile_7: is clear, is to the right of tile_3, is up from tile_6. Tile_18: is clear, is to the right of tile_14, is up from tile_17. Tile_8: is painted black, is to the right of tile_4, is up from tile_7. Tile_11: is painted white, is to the right of tile_7, is up from tile_10. Tile_13: is painted white, is to the right of tile_9.\n"
    f"Then, we organize all objects states into a new paragraph as the end of answer.\n"
    f"Tile_2: is up from tile_1. Tile_3: is up from tile_2. Tile_4: is up from tile_3. Tile_6: is up from tile_5. Tile_7: is up from tile_6. Tile_8: is up from tile_7. Tile_10: is up from tile_9. Tile_11: is up from tile_10. Tile_12: is up from tile_11. Tile_14: is up from tile_13. Tile_15: is up from tile_14. Tile_16: is up from tile_15. Tile_18: is up from tile_17. Tile_19: is up from tile_18. Tile_20: is up from tile_19. Tile_5: is to the right of tile_1. Tile_6: is to the right of tile_2. Tile_7: is to the right of tile_3. Tile_8: is to the right of tile_4. Tile_9: is to the right of tile_5. Tile_10: is to the right of tile_6. Tile_11: is to the right of tile_7. Tile_12: is to the right of tile_8. Tile_13: is to the right of tile_9. Tile_14: is to the right of tile_10. Tile_15: is to the right of tile_11. Tile_16: is to the right of tile_12. Tile_17: is to the right of tile_13. Tile_18: is to the right of tile_14. Tile_19: is to the right of tile_15. Tile_20: is to the right of tile_16. Robot1: at tile_10, holding white color. Robot2: at tile_15, holding black color. Tile_5: is clear, is to the right of tile_1. Tile_6: is clear, is to the right of tile_2, is up from tile_5. Tile_7: is clear, is to the right of tile_3, is up from tile_6. Tile_18: is clear, is to the right of tile_14, is up from tile_17. Tile_8: is painted black, is to the right of tile_4, is up from tile_7. Tile_11: is painted white, is to the right of tile_7, is up from tile_10. Tile_13: is painted white, is to the right of tile_9.\n"
    f"-------------------\n"
)


QUESTION_EXTRACTOR_FLOORTILE_EXAMPLE = (
    f"[Examples]\n"
    f"Question example 1: Will the fact \"tile_5 is clear\" hold after performing the action \"move the robot robot1 from tile tile_1 to the up tile tile_4\" in the current state?\n"
    f"Extracted from example 1: Will the fact \"tile_5 is clear\" hold\n"
    f"-------------------\n"
    f"Question example 2: Will the fact \"tile_7 is clear\" hold after performing the action \"move the robot robot1 from tile tile_4 to the right tile tile_5\" in the current state?\n"
    f"Extracted from example 2: Will the fact \"tile_7 is clear\" hold\n"
    f"-------------------\n"
    f"Question example 3: Will the fact \"tile_2 is clear\" hold after performing the action \"move the robot robot1 from tile tile_6 to the left tile tile_5\" in the current state?\n"
    f"Extracted from example 3: Will the fact \"tile_2 is clear\" hold \n"
)


ACTION_SEQUENCE_EXTRACTOR_FLOORTILE_PROMPT = (
    f"[Examples]\n"
    f"Action example 1: Is the following action applicable in this state: apply color black to tile tile_5 which is below tile tile_11 using robot robot1?\n"
    f"Extracted from example 1: apply color black to tile tile_5 which is below tile tile_11 using robot robot1.\n"
    f"-------------------\n"
    f"Action examplee 2: Is the following action applicable in this state: apply color white to tile tile_12 which is to the right of tile tile_11 using robot robot1?\n"
    f"Extracted from example 2: apply color white to tile tile_12 which is to the right of tile tile_11 using robot robot1.\n"
    f"-------------------\n"
    f"Action examplee 3: Is the following sequence of actions \"move the robot robot1 up from tile tile_3 to tile tile_6, use robot robot1 to paint the tile tile_9 above tile tile_6 with the color white, move robot robot2 from tile tile_5 to the tile on its left tile_4, use robot robot2 to paint the tile tile_7 above tile tile_4 with the color black\" applicable in the current state?"
    f"Extracted from example 3: move the robot robot1 up from tile tile_3 to tile tile_6. use robot robot1 to paint the tile tile_9 above tile tile_6 with the color white.  move robot robot2 from tile tile_5 to the tile on its left tile_4. use robot robot2 to paint the tile tile_7 above tile tile_4 with the color black.\n"
    f"-------------------\n"
)


ACTION_TAKER_FLOORTILE_PROMPT = (
    f"Based on the domain description and examples above, take the action and return the new state of all objects. Your answer must satisfy all the following requirements. First, think and respond like examples above, you are required to return states of all objects(robots and tiles), including states that are not effected by the action. Second, each object's state must contain all properties mentioned in the domain description above. Third, after your analysis, please return states of all objects into a new paragraph as the end of your answer. Your final paragraph should use the format like: \"Robot2: at tile_7, holding black color. Tile_1: is clear, is down from tile_4.\" Besides, don't use any markdown formatting."
)


ACTION_TAKER_FLOORTILE_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: Tile_11: is to the right of tile_10. Tile_5: is to the right of tile_4, is down from tile_8. Tile_3: is to the right of tile_2, is down from tile_6. Tile_8: is to the right of tile_7, is down from tile_11. Tile_12: is to the right of tile_11. Tile_9: is to the right of tile_8, is down from tile_12. Tile_6: is to the right of tile_5, is down from tile_9. Tile_2: is to the right of tile_1, is down from tile_5. Tile_1: is down from tile_4. Tile_4: is down from tile_7. Tile_7: is down from tile_10. Robot1: at tile_4, holding white color. Robot2: at tile_7, holding black color. Tile_1: is clear, is down from tile_4. Tile_2: is clear, is to the right of tile_1, is down from tile_5. Tile_3: is clear, is to the right of tile_2, is down from tile_6. Tile_5: is clear, is to the right of tile_4, is down from tile_8. Tile_8: is clear, is to the right of tile_7, is down from tile_11. Tile_10: is painted black, is to the right of tile_11. Tile_11: is painted white, is to the right of tile_10. Tile_6: is painted white, is to the right of tile_5, is down from tile_9. Tile_12: is painted black, is to the right of tile_11.\n"
    f"Action 1: Move the robot robot1 from tile tile_4 to the right tile tile_5.\n"
    f"Answer 1:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Robot1: at tile_4, holding white color. Tile_4: is down from tile_7. Tile_5: is clear, is to the right of tile_4, is down from tile_8.\n"
    f"Based on the domain description, a robot can move(navigate) from tile A to tile B. This action will result in: the robot is not at tile A, the robot is currently at tile B, tile A is clear, tile B is not clear. \n"
    f"the robot is not at tile A, the robot is currently at tile B, tile A is clear, tile B is not clear. ::: Robot1: at tile_5, holding white color. Tile_4: is clear, is down from tile_7. Tile_5: is not clear, is to the right of tile_4, is down from tile_8.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into a new paragraph.\n"
    f"Tile_11: is to the right of tile_10. Tile_5: is to the right of tile_4, is down from tile_8. Tile_3: is to the right of tile_2, is down from tile_6. Tile_8: is to the right of tile_7, is down from tile_11. Tile_12: is to the right of tile_11. Tile_9: is to the right of tile_8, is down from tile_12. Tile_6: is to the right of tile_5, is down from tile_9. Tile_2: is to the right of tile_1, is down from tile_5. Tile_1: is down from tile_4. Tile_4: is down from tile_7. Tile_7: is down from tile_10. Robot1: at tile_5, holding white color. Robot2: at tile_7, holding black color. Tile_1: is clear, is down from tile_4. Tile_2: is clear, is to the right of tile_1, is down from tile_5. Tile_3: is clear, is to the right of tile_2, is down from tile_6. Tile_5: is clear, is to the right of tile_4, is down from tile_8. Tile_8: is clear, is to the right of tile_7, is down from tile_11. Tile_10: is painted black, is to the right of tile_11. Tile_11: is painted white, is to the right of tile_10. Tile_6: is painted white, is to the right of tile_5, is down from tile_9. Tile_12: is painted black, is to the right of tile_11.\n"
    f"Action 1: Move the robot robot1 from tile tile_4 to the right tile tile_5.\n"
    f"-------------------\n"
    f"Current state example 2: Tile_11: is to the right of tile_10. Tile_5: is to the right of tile_4, is down from tile_8. Tile_3: is to the right of tile_2, is down from tile_6. Tile_8: is to the right of tile_7, is down from tile_11. Tile_12: is to the right of tile_11. Tile_9: is to the right of tile_8. Tile_6: is to the right of tile_5, is down from tile_9. Tile_2: is to the right of tile_1, is down from tile_5. Tile_4: is down from tile_7. Tile_7: is down from tile_10. Tile_1: is down from tile_4. Robot1: at tile_5, holding black color. Robot2: at tile_11, holding white color. Tile_1: is clear, is down from tile_4. Tile_2: is clear, is to the right of tile_1, is down from tile_5. Tile_3: is clear, is to the right of tile_2, is down from tile_6. Tile_4: is clear, is down from tile_7. Tile_6: is clear, is to the right of tile_5, is down from tile_9. Tile_8: is clear, is to the right of tile_7, is down from tile_11. Tile_10: is painted white, is to the right of tile_11. Tile_9: is painted black, is to the right of tile_8, is down from tile_12. Tile_12: is painted black, is to the right of tile_11. Tile_7: is painted white, is down from tile_10.\n"
    f"Action 2: paint tile_8 with color white by robot robot2 from tile tile_11.\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Robot2: at tile_11, holding white color. Tile_8: is to the right of tile_7, is down from tile_11.\n"    
    f"Based on the domain description, a robot can paint tile X with the color from tile Y. This action will result in: tile X is painted with color, tile X is not clear.\n"
    f"tile X is painted with color, tile X is not clear. ::: Tile_8: is painted white, is to the right of tile_7, is down from tile_11.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into a new paragraph.\n"
    f"Tile_11: is to the right of tile_10. Tile_5: is to the right of tile_4, is down from tile_8. Tile_3: is to the right of tile_2, is down from tile_6. Tile_8: is to the right of tile_7, is down from tile_11. Tile_12: is to the right of tile_11. Tile_9: is to the right of tile_8. Tile_6: is to the right of tile_5, is down from tile_9. Tile_2: is to the right of tile_1, is down from tile_5. Tile_4: is down from tile_7. Tile_7: is down from tile_10. Tile_1: is down from tile_4. Robot1: at tile_5, holding black color. Robot2: at tile_11, holding white color. Tile_1: is clear, is down from tile_4. Tile_2: is clear, is to the right of tile_1, is down from tile_5. Tile_3: is clear, is to the right of tile_2, is down from tile_6. Tile_4: is clear, is down from tile_7. Tile_6: is clear, is to the right of tile_5, is down from tile_9. Tile_8: is painted white, is to the right of tile_7, is down from tile_11. Tile_10: is painted white, is to the right of tile_11. Tile_9: is painted black, is to the right of tile_8, is down from tile_12. Tile_12: is painted black, is to the right of tile_11. Tile_7: is painted white, is down from tile_10.\n"
    f"-------------------\n"
)

EXECUTABILITY_CHECKER_FLOORTILE_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: Tile_17: is to the right of tile_16, is down from tile_23. Tile_20: is to the right of tile_19. Tile_22: is to the right of tile_21. Tile_16: is to the right of tile_15, is down from tile_22. Tile_12: is to the right of tile_11, is down from tile_18. Tile_21: is to the right of tile_20. Tile_11: is to the right of tile_10, is down from tile_17. Tile_10: is to the right of tile_9, is down from tile_16, is clear. Tile_9: is to the right of tile_8, is down from tile_15, is clear. Tile_15: is to the right of tile_14, is down from tile_21. Tile_2: is to the right of tile_1, is down from tile_8. Tile_9: is to the right of tile_8. Tile_6: is to the right of tile_5, is down from tile_12. Tile_24: is to the right of tile_23. Tile_23: is to the right of tile_22. Tile_3: is to the right of tile_2, is down from tile_9, is clear. Tile_5: is to the right of tile_4, is down from tile_11, is clear. Tile_18: is to the right of tile_17, is down from tile_24, is painted black. Tile_13: is down from tile_19, is clear. Tile_14: is down from tile_20, is painted white. Tile_7: is down from tile_13, is clear. Tile_1: is down from tile_7, is clear. Tile_8: is painted black. Robot1: at tile_11, holding black color. Robot2: at tile_24, holding white color. Tile_19: is painted white, is to the right of tile_18. Tile_22: is painted black, is to the right of tile_21. Tile_6: is clear, is to the right of tile_5. Tile_10: is clear, is to the right of tile_9. Tile_1: is clear, is down from tile_7. Tile_17: is clear, is to the right of tile_16. Tile_13: is clear, is down from tile_19. Tile_5: is clear, is to the right of tile_4. Tile_9: is clear, is to the right of tile_8. Tile_7: is clear, is down from tile_13. Tile_16: is clear, is to the right of tile_15. Tile_3: is clear, is to the right of tile_2.\n"
    f"Action 1: apply color white to tile tile_12 which is to the right of tile tile_11 using robot robot1.\n"
    f"Answer 1:"
    f"Based on the current state and the domain description, we first find states of related objects, then we can check whether the action is executable.\n"
    f"Robot1: at tile_11, holding black color. Tile_12: is to the right of tile_11, is down from tile_18.\n"
    f"Based on the domain description, a robot can paint(apply) tile X with the color from tile Y. This action is executable only if all following preconditions are satisfied: the robot is currently at tile Y, tile Y is above or downward from tile X, the robot is holding the color, tile X is clear.\n"
    f"the robot is currently at tile Y ::: Robot1: at tile_11, holding black color. ===> SATISFY\n"
    f"tile Y is above or downward from tile X ::: Tile_12: is to the right of tile_11 ===> NOT SATISFY\n"
    f"Since not all preconditions are satisfied, this action is not executable.\n"
    f"Final answer: False.\n"
    f"-------------------\n"
    f"Current state example 2: Tile_17: is to the right of tile_16, is down from tile_23. Tile_20: is to the right of tile_19. Tile_22: is to the right of tile_21. Tile_16: is to the right of tile_15, is down from tile_22. Tile_12: is to the right of tile_11, is down from tile_18. Tile_21: is to the right of tile_20. Tile_11: is to the right of tile_10, is down from tile_17. Tile_10: is to the right of tile_9, is down from tile_16. Tile_15: is to the right of tile_14, is down from tile_21. Tile_2: is to the right of tile_1, is down from tile_8. Tile_9: is to the right of tile_8, is down from tile_15. Tile_6: is to the right of tile_5, is down from tile_12. Tile_24: is to the right of tile_23. Tile_23: is to the right of tile_22. Tile_3: is to the right of tile_2, is down from tile_9. Tile_5: is to the right of tile_4, is down from tile_11. Tile_18: is to the right of tile_17, is down from tile_24. Tile_13: is down from tile_19. Tile_7: is down from tile_13. Tile_1: is down from tile_7. Tile_4: is down from tile_10. Tile_8: is painted black, is to the right of tile_7. Tile_19: is painted white. Tile_14: is painted white, is down from tile_20. Tile_22: is painted black. Tile_6: is clear, is to the right of tile_5, is down from tile_12. Tile_10: is clear, is to the right of tile_9, is down from tile_16. Tile_1: is clear. Tile_17: is clear, is to the right of tile_16, is down from tile_23. Tile_13: is clear. Tile_5: is clear, is to the right of tile_4, is down from tile_11. Tile_9: is clear, is to the right of tile_8, is down from tile_15. Tile_7: is clear. Tile_16: is clear, is to the right of tile_15, is down from tile_22. Tile_3: is clear, is to the right of tile_2, is down from tile_9. Robot1: at tile_11, holding black color. Robot2: at tile_24, holding white color.\n"
    f"Action 2: apply color black to tile tile_5 which is below tile tile_11 using robot robot1.\n"
    f"Answer 2:"
    f"Based on the current state and the domain description, we first find states of related objects, then we can check whether the action is executable.\n"
    f"Robot1: at tile_11, holding black color. Tile_5: is clear, is to the right of tile_4, is down from tile_11.\n"
    f"Based on the domain description, a robot can paint(apply) tile X with the color from tile Y. This action is executable only if all following preconditions are satisfied: the robot is currently at tile Y, tile Y is above or downward from tile X, the robot is holding the color, tile X is clear.\n"
    f"the robot is currently at tile Y ::: Robot1: at tile_11, holding black color. ===> SATISFY\n"
    f"tile Y is above or downward from tile X ::: Tile_5: is clear, is to the right of tile_4, is down from tile_11. ===> SATISFY\n"
    f"the robot is holding the color ::: Robot1: at tile_11, holding black color. ===> SATISFY\n"
    f"tile X is clear ::: Tile_5: is clear, is to the right of tile_4, is down from tile_11. ===> SATISFY\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final answer: True.\n"
    f"-------------------\n"
)

STATE_CHECKER_FLOORTILE_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: Tile_13: is to the right of tile_12, is down from tile_18. Tile_5: is to the right of tile_4, is down from tile_10. Tile_15: is to the right of tile_14, is down from tile_20. Tile_3: is to the right of tile_2, is down from tile_8. Tile_19: is to the right of tile_18. Tile_10: is to the right of tile_9, is down from tile_15. Tile_8: is to the right of tile_7, is down from tile_13. Tile_7: is to the right of tile_6, is down from tile_12. Tile_12: is to the right of tile_11, is down from tile_17. Tile_14: is to the right of tile_13, is down from tile_19. Tile_4: is to the right of tile_3, is down from tile_9. Tile_18: is to the right of tile_17. Tile_9: is to the right of tile_8, is down from tile_14. Tile_20: is to the right of tile_19. Tile_2: is to the right of tile_1, is down from tile_7. Tile_17: is to the right of tile_16. Tile_11: is down from tile_16. Tile_6: is down from tile_11. Tile_1: is down from tile_6. Robot1: at tile_3, holding black color. Robot2: at tile_9, holding color white. Tile_4: is clear, is to the right of tile_3, is down from tile_9. Tile_7: is clear, is to the right of tile_6, is down from tile_12. Tile_3: not clear, has robot 1 standing on it, is to the right of tile_2, is down from tile_8. Tile_13: is clear, is to the right of tile_12, is down from tile_18. Tile_5: is clear, is to the right of tile_4, is down from tile_10. Tile_11: is clear, is down from tile_16. Tile_14: is clear, is to the right of tile_13, is down from tile_19. Tile_8: is clear, is to the right of tile_7, is down from tile_13. Tile_1: is painted white, is down from tile_6. Tile_6: is painted black, is down from tile_11. Tile_12: is painted black, is to the right of tile_11, is down from tile_17. Tile_10: is painted white, is to the right of tile_9, is down from tile_15. Tile_15: is painted black, is to the right of tile_14, is down from tile_20.\n"
    f"Question 1: Will the fact \"tile_3 is clear\" hold.\n"
    f"Answer 1: \n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false.\n"
    f"Tile_3: not clear, has robot 1 standing on it, is to the right of tile_2, is down from tile_8."
    f"Will the fact \"tile_3 is clear\" ::: Tile_3: not clear, has robot 1 standing on it, is to the right of tile_2, is down from tile_8. ===> NOT MATCH\n"
    f"Since not all propositions are true, so the answer is false.\n"
    f"Final Answer: False.\n"   
    f"-------------------\n"
    f"Current state example 2: Tile_13: is to the right of tile_12, is down from tile_18. Tile_5: is to the right of tile_4, is down from tile_10. Tile_15: is to the right of tile_14, is down from tile_20. Tile_3: is to the right of tile_2, is down from tile_8. Tile_19: is to the right of tile_18. Tile_10: is to the right of tile_9, is down from tile_15. Tile_8: is to the right of tile_7, is down from tile_13. Tile_7: is to the right of tile_6, is down from tile_12. Tile_12: is to the right of tile_11, is down from tile_17. Tile_14: is to the right of tile_13, is down from tile_19. Tile_4: is to the right of tile_3, is down from tile_9. Tile_18: is to the right of tile_17. Tile_9: is to the right of tile_8, is down from tile_14. Tile_20: is to the right of tile_19. Tile_2: is to the right of tile_1, is down from tile_7. Tile_17: is to the right of tile_16. Tile_11: is down from tile_16. Tile_6: is down from tile_11. Tile_1: is down from tile_6. Robot2: at tile_3, holding black color. Robot1: at tile_4, holding white color. Tile_5: is clear, is to the right of tile_4, is down from tile_10. Tile_9: is clear, is to the right of tile_8, is down from tile_14. Tile_2: is clear, is to the right of tile_1, is down from tile_7. Tile_1: is clear, is down from tile_6. Tile_14: is clear, is to the right of tile_13, is down from tile_19. Tile_13: is clear, is to the right of tile_12, is down from tile_18. Tile_8: is clear, is to the right of tile_7, is down from tile_13. Tile_17: is clear, is to the right of tile_16. Tile_6: is painted black, is to the right of tile_11, is down from tile_11. Tile_10: is painted white, is to the right of tile_9, is down from tile_15. Tile_12: is painted black, is to the right of tile_11, is down from tile_17. Tile_7: is painted white, is to the right of tile_6, is down from tile_12. Tile_15: is painted black, is to the right of tile_14, is down from tile_20. Tile_20: is painted white, is to the right of tile_19.\n"
    f"Question 2: Will the fact \"tile_7 is painted with white color.\""
    f"Answer 2: \n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false.\n"
    f"Tile_7: is painted white, is to the right of tile_6, is down from tile_12.\n"
    f"Will the fact \"tile_7 is painted with white color.\" ::: Tile_7: is painted white, is to the right of tile_6, is down from tile_12. ===> SATISFY\n"
    f"Since all propositions are true, so the answer is true.\n"
    f"Final Answer: True.\n"
    f"-------------------\n"
)


TWOSHOTCOT_APP_FLOORTILE_EXAMPLE = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"Initial State: A set of robots use different colors to paint patterns in floor tiles. The robots can move around the floor tiles in four directions (up, down, left and right). Robots paint with one color at a time, but can change their spray guns to any available color. However, robots can only paint the tile that is in front (up) and behind (down) them, and once a tile has been painted no robot can stand on it. Robots need to paint a grid with black and white, where the cell color is alternated always. There are 24 tiles and 2 robots. The tiles locations are: tile_17 is to the right of tile_16, tile_8 is to the right of tile_7, tile_20 is to the right of tile_19, tile_22 is to the right of tile_21, tile_16 is to the right of tile_15, tile_12 is to the right of tile_11, tile_21 is to the right of tile_20, tile_11 is to the right of tile_10, tile_4 is to the right of tile_3, tile_10 is to the right of tile_9, tile_15 is to the right of tile_14, tile_2 is to the right of tile_1, tile_9 is to the right of tile_8, tile_6 is to the right of tile_5, tile_24 is to the right of tile_23, tile_23 is to the right of tile_22, tile_14 is to the right of tile_13, tile_3 is to the right of tile_2, tile_5 is to the right of tile_4, and tile_18 is to the right of tile_17. Further, tile_13 is down from tile_19, tile_10 is down from tile_16, tile_17 is down from tile_23, tile_12 is down from tile_18, tile_5 is down from tile_11, tile_1 is down from tile_7, tile_2 is down from tile_8, tile_9 is down from tile_15, tile_16 is down from tile_22, tile_11 is down from tile_17, tile_6 is down from tile_12, tile_18 is down from tile_24, tile_8 is down from tile_14, tile_4 is down from tile_10, tile_7 is down from tile_13, tile_15 is down from tile_21, tile_3 is down from tile_9, and tile_14 is down from tile_20. Currently, robot robot1 is at tile_2 and holding color white and robot robot2 is at tile_18 and holding color black; tile_5, tile_4, tile_12, tile_8, tile_13, tile_21, tile_11, tile_17, tile_9, tile_10, tile_6, tile_15, tile_23, tile_1, tile_16, tile_3, and tile_7 are clear; tile_20 is painted black, tile_19 is painted white, tile_24 is painted black, tile_14 is painted white, and tile_22 is painted black.\n"
    f"Question: Is the following action applicable in this state: apply color white to tile tile_1 which is below tile tile_7 using robot robot1?\n"
    f"Answer:\n"
    f"Step 1: We find related objects in the current state."
    f"robot robot1 is at tile_2 and holding color white. tile_7 is down from tile_13. tile_1 is down from tile_7. "
    f"Step 2: we check whether the action is applicable. \n"
    f"A robot can paint(apply) tile X with the color from tile Y. This action is executable only if all following preconditions are satisfied: the robot is currently at tile Y, tile Y is above or downward from tile X, the robot is holding the color, tile X is clear. We can see now robot1 is at tile_2, not tile_7, so this action is not executable.\n"
    f"Step 3: We return our answer based on previous analysis. \n"
    f"Final Answer: False.\n"
    f"-------------------\n"
    f"(Example 2)\n"
    f"Initial state: A set of robots use different colors to paint patterns in floor tiles. The robots can move around the floor tiles in four directions (up, down, left and right). Robots paint with one color at a time, but can change their spray guns to any available color. However, robots can only paint the tile that is in front (up) and behind (down) them, and once a tile has been painted no robot can stand on it. Robots need to paint a grid with black and white, where the cell color is alternated always. There are 12 tiles and 2 robots. The tiles locations are: tile_2 is to the right of tile_1, tile_3 is to the right of tile_2, tile_5 is to the right of tile_4, tile_6 is to the right of tile_5, tile_8 is to the right of tile_7, tile_9 is to the right of tile_8, tile_4 is down from tile_1, tile_5 is down from tile_2, tile_6 is down from tile_3, tile_7 is down from tile_4, tile_8 is down from tile_5, tile_9 is down from tile_6, tile_10 is down from tile_7, tile_11 is down from tile_8, and tile_12 is down from tile_9. Currently, robot robot1 is at tile_5 and holding color white and robot robot2 is at tile_8 and holding color black; tile_1, tile_2, tile_3, tile_4, tile_6, and tile_9 are clear; tile_10 is painted black, tile_7 is painted white, tile_11 is painted black, and tile_12 is painted white.\n"
    f"Question: Which of the following actions will be applicable in this state? A.move the robot robot1 from tile tile_5 to the right tile tile_6. B.use robot robot2 to paint the tile tile_5 above the tile tile_8 with the color black. C.paint tile tile_12 down from tile tile_9 with color white using robot robot1. D.use robot robot2 to paint the tile tile_10 down from tile tile_7 with the color black.\n"
    f"Answer:\n"
    f"Step 1: We check each option one by one. \n"
    "Option A: move the robot robot1 from tile tile_5 to the right tile tile_6. A robot can move(navigate) from tile A to tile B. This action is executable only if all following preconditions are satisfied: the robot is currently at tile A, tile A and B are adjacent, tile B is clear. We can see robot1 is at tile_5, tile_5 and tile_6 are adjacent, tile_6 is clear. So this action is executable.\n"
    f"Step 2: We return our answer based on previous analysis. \n"
    f"Final Answer: A.\n"
    f"-------------------\n"
)


TWOSHOTCOT_PROG_FLOORTILE_EXAMPLE = (
    f"[Examples]\n"
    f"(example 1)\n"
    f"Initial state: A set of robots use different colors to paint patterns in floor tiles. The robots can move around the floor tiles in four directions (up, down, left and right). Robots paint with one color at a time, but can change their spray guns to any available color. However, robots can only paint the tile that is in front (up) and behind (down) them, and once a tile has been painted no robot can stand on it. Robots need to paint a grid with black and white, where the cell color is alternated always. There are 12 tiles and 2 robots. The tiles locations are: tile_2 is to the right of tile_1, tile_3 is to the right of tile_2, tile_5 is to the right of tile_4, tile_6 is to the right of tile_5, tile_8 is to the right of tile_7, tile_9 is to the right of tile_8, tile_4 is down from tile_1, tile_5 is down from tile_2, tile_6 is down from tile_3, tile_7 is down from tile_4, tile_8 is down from tile_5, tile_9 is down from tile_6. Currently, robot robot1 is at tile_5 and holding color white, and robot robot2 is at tile_8 and holding color black; tile_1, tile_2, tile_3, tile_4, tile_6, tile_7, and tile_9 are clear; tile_10 is painted white, tile_11 is painted black, and tile_12 is painted white.\n"
    f"Question: Will the fact \"Tile tile_5 is clear\" hold after performing the action \"move robot robot1 down from tile tile_5 to tile tile_8\" in the current state?\n"
    f"Answer 1:\n"
    f"Step 1: Take the action and get the new state.\n"
    f"move robot robot1 down from tile tile_5 to tile tile_8. After this action, robot1 is at tile_8.\n"
    f"Step 2: Check whether the fact hold.\n"
    f"Tile tile_5 is clear. We can see tile_5 is clear. So this fact is held.\n"
    f"Step 3: We return our answer based on previous analysis.\n"
    f"Final Answer: True.\n"
    f"-------------------\n"
    f"(example 2)\n"
    f"Initial state: A set of robots use different colors to paint patterns in floor tiles. The robots can move around the floor tiles in four directions (up, down, left and right). Robots paint with one color at a time, but can change their spray guns to any available color. However, robots can only paint the tile that is in front (up) and behind (down) them, and once a tile has been painted no robot can stand on it. Robots need to paint a grid with black and white, where the cell color is alternated always. There are 2 robots and 12 tiles. The tiles locations are: tile_2 is to the right of tile_1, tile_3 is to the right of tile_2, tile_5 is to the right of tile_4, tile_6 is to the right of tile_5, tile_8 is to the right of tile_7, tile_9 is to the right of tile_8, tile_11 is to the right of tile_10, tile_12 is to the right of tile_11, tile_4 is down from tile_1, tile_5 is down from tile_2, tile_6 is down from tile_3, tile_7 is down from tile_4, tile_8 is down from tile_5, tile_9 is down from tile_6, tile_10 is down from tile_7, tile_11 is down from tile_8, tile_12 is down from tile_9. Currently, robot robot1 is at tile_4 and holding color black, and robot robot2 is at tile_11 and holding color white; tile_1, tile_2, tile_3, tile_5, tile_6, tile_7, tile_8, tile_9, and tile_10 are clear; tile_12 is painted black.\n"
    f"Question: Which of the following facts hold after performing the action \"alter the color of the robot robot1 from color black to color white\" in the current state?  A.Robot robot1 is holding white paint and tile_7 is painted white. B.Tile tile_4 is painted black and robot robot1 is holding white paint. C.Robot robot1 is holding white paint. D.Robot robot1 is holding black paint.\n"
    f"Step 1: Take the action and get the new state.\n"
    f"alter the color of the robot robot1 from color black to color white. After this action, robot1 is holding white paint.\n"
    f"Step 2: Check each option to find the answer.\n"
    f"Option A: Robot robot1 is holding white paint and tile_7 is painted white. We can see robot1 is holding white paint, but tile_7 is clear. So this option is false.\n"
    f"Option B: Tile tile_4 is painted black and robot robot1 is holding white paint. We can see robot1 is holding white paint, but tile_4 is clear. So this option is false.\n"
    f"Option C: Robot robot1 is holding white paint. We can see robot1 is holding white paint. So this option is true.\n"
    f"Step 3: We return our answer based on previous analysis.\n"
    f"Final Answer: C.\n"
    f"-------------------\n"
)


TWOSHOTCOT_VAL_FLOORTILE_EXAMPLE = (
    f"[Examples]\n"
    f"(example 1)\n"
    f"Initial state: A set of robots use different colors to paint patterns in floor tiles. The robots can move around the floor tiles in four directions (up, down, left and right). Robots paint with one color at a time, but can change their spray guns to any available color. However, robots can only paint the tile that is in front (up) and behind (down) them, and once a tile has been painted no robot can stand on it. Robots need to paint a grid with black and white, where the cell color is alternated always. There are 3 robots and 12 tiles. The tiles locations are: tile_2 is to the right of tile_1, tile_3 is to the right of tile_2, tile_5 is to the right of tile_4, tile_6 is to the right of tile_5, tile_8 is to the right of tile_7, tile_9 is to the right of tile_8, tile_11 is to the right of tile_10, tile_12 is to the right of tile_11, tile_4 is down from tile_1, tile_5 is down from tile_2, tile_6 is down from tile_3, tile_7 is down from tile_4, tile_8 is down from tile_5, tile_9 is down from tile_6, tile_10 is down from tile_7, tile_11 is down from tile_8, tile_12 is down from tile_9. Currently, robot robot1 is at tile_5 and holding color black, robot robot2 is at tile_8 and holding color white, and robot robot3 is at tile_12 and holding color black. tile_1, tile_2, tile_3, tile_4, tile_6, tile_7, tile_9, tile_10, tile_11 are clear; tile_12 is painted white. The goal is robot1 is at tile_2 and tile_5 is painted black\n"
    f"Question: Is the following sequence of actions \"move robot robot1 up from tile tile_5 to tile tile_2, apply color black to tile tile_5 down from tile tile_2 using robot robot1\" a plan for the current state?\n"
    f"Answer:\n"
    f"Step 1: Since the question ask whether the action sequence is a plan, we need to take actions to reach the fianl answer, then check the goal.\n"
    f"move robot robot1 up from tile tile_5 to tile tile_2. After this action, robot1 is at tile_2. Then, apply color black to tile tile_5 down from tile tile_2 using robot robot1. After this action, tile_5 is painted black.\n"
    f"Step 2: Check whether the goal is reached.\n"
    f"The goal is robot1 is at tile_2 and tile_5 is painted black. We can see now robot1 is at tile_2 and tile_5 is painted black. The goal is reached, so this is a plan.\n"
    f"Final Answer: True.\n"
    f"-------------------\n"
    f"(example 2)\n"
    f"Initial state: A set of robots use different colors to paint patterns in floor tiles. The robots can move around the floor tiles in four directions (up, down, left and right). Robots paint with one color at a time, but can change their spray guns to any available color. However, robots can only paint the tile that is in front (up) and behind (down) them, and once a tile has been painted no robot can stand on it. Robots need to paint a grid with black and white, where the cell color is alternated always. There are 12 tiles and 2 robots. The tiles locations are: tile_2 is to the right of tile_1, tile_3 is to the right of tile_2, tile_5 is to the right of tile_4, tile_6 is to the right of tile_5, tile_8 is to the right of tile_7, tile_9 is to the right of tile_8, tile_11 is to the right of tile_10, tile_12 is to the right of tile_11. Further, tile_4 is down from tile_1, tile_5 is down from tile_2, tile_6 is down from tile_3, tile_7 is down from tile_4, tile_8 is down from tile_5, tile_9 is down from tile_6, tile_10 is down from tile_7, tile_11 is down from tile_8, tile_12 is down from tile_9. Currently, robot robot1 is at tile_5 and holding color white, robot robot2 is at tile_8 and holding color black; tile_1, tile_2, tile_3, tile_4, tile_6, tile_7, tile_9, tile_10, tile_11, and tile_12 are clear; tile_5 is painted black. The goal is Robot robot1 is at tile_6 and tile_5 is painted white.\n"
    f"Question: Is the following sequence of actions applicable in the current state: \"move the robot robot1 from tile tile_5 to tile tile_6 to the right\" and does it achieve the goal? A.The sequence is applicable, but does not achieve the goal. B.The sequence is a plan. C.The sequence is not valid. D.The sequence is not applicable.\n"
    f"Answer:\n"
    f"Step 1: Since the question ask whether the action sequence is a plan, we need to take actions to reach the fianl answer, then check the goal.\n"
    f"move the robot robot1 from tile tile_5 to tile tile_6 to the right. A robot can move(navigate) from tile A to tile B. This action is executable only if all following preconditions are satisfied: the robot is currently at tile A, tile A and B are adjacent, tile B is clear. We can see robot robot1 is at tile_5, tile_6 is to the right of tile_5 and tile_6 is clear. So this action is executable. After this action, robot1 is at tile_6.\n"
    f"Step 2: We check whether the goal is reached.\n"
    f"The goal is Robot robot1 is at tile_6 and tile_5 is painted white. We can see robot1 is now at tile_6. However, the tile_5 is painted black. So the goal is not reached.\n"
    f"Step 3: Return the answer based on the analysis.\n"
    f"Final Answer: A.\n"
    f"-------------------\n"
)




#-------------------------------------
#Goldminer Prompts
#-------------------------------------
GOLDMINER_DOMAIN_DESCRIPTION = (
    f"[Domain Description]\n"
    f"The Goldminer domain involves a robot moving in a grid that cells are connected to their neighbors. Each cell in the grid are named as fi-jf, and location fi-jf's adjacent cells have the same i or j(for example, f0_1f is connected to f0_0f because their x-axis values are both 0). The robot can move to adjacent(neighbouring) cells, but can not move to cells that are not adjacent. Also, the robot can not move to cells that are blocked by rock(hard rock) or soft rock. The robot can use the laser or bomb to clear rock(hard rock) and soft soft to clear the way. The robot can pick up the laser, bomb or gold, but it can only pick up one of them at a time. The laser can be used to clear rock(hard rock) or soft rock, but the bomb can by only used to clear soft rock and can not be used to clear rock(hard rock). The bomb supply is unlitmited but there is only one laser. Once a bomb is picked, it cannot be placed back. It can only be detonated at connected location that have soft rock. However, the laser can be put down without using.\n"
    f"Different properties are used to describe states of different objects. For robot we use: at fi-fj, holding laser/bomb/gold/nothing. For each cell we use: has rock/soft rock/gold/laser/bomb supply, clear(has nothing). For gold(or laser) we use: at location fi-jf/held by the robot. For bomb we use: supplying at fi-jf.\n"
    f"Following actions are executable only if all preconditions are met, if any condition are not satisfied, the action is not executable.\n"    
    f"A robot can move(travel) from from location fa-bf to location fc-df. This action is executable only if all following preconditions are satisfied: the robot is currently at fa-bf, fa-bf and fc-df are adjacent, fc-df has no rocks or soft rocks.\n"
    f"A robot can pick up laser(or gold) at location fi-jf. This action is executable only if all following preconditions are satisfied: the robot is currently at fi-jf, fi-jf has laser(or gold), the robot is holding nothing.\n"
    f"A robot can put down laser(or gold) at location fi-jf. This action is executable only if all following preconditions are satisfied: the robot is currently at fi-jf, the robot is holding laser(or gold).\n"
    f"A robot can aim(direct/fire) the laser from location fa-bf to location fc-df. This action is executable only if all following preconditions are satisfied: the robot is at location fa-bf, the robot is holding laser, fa-bf and fc-df are adjacent, location fc_df has rock(hard rock) or soft rock.\n"
    f"A robot can pick up(retrieve) a bomb at fi-jf. This action is executable only if all following preconditions are satisfied: the robot is currently at fi-jf, fi-jf has bomb supply, the robot is holding nothing.\n"
    f"A robot can detonate(trigger) a bomb at location fa-bf connected to location fc-df. This action is executable only if all following preconditions are satisfied: the robot is at location fa-bf, the robot is holding a bomb, fa-bf and fc-df are adjacent, location fc-df has soft rock(must be soft rock).\n"
    f"Executing an action will change states of related objects.\n"
    f"A robot can move(travel) from from location fa-bf to location fc-df. This action will result in: the robot is at location fc-df.\n"
    f"A robot can pick up laser(or gold) at location fi-jf. This action will result in: the robot is holding laser(or gold), fi-jf does not have laser(or gold).\n"
    f"A robot can put down laser(or gold) at location fi-jf. This action will result in: the robot is holding nothing, fi-jf has laser(or gold).\n"
    f"A robot can aim(direct/fire) the laser from location fa-bf to location fc-df. This action will result in: the location fc-df does not have any rock(clear).\n"
    f"A robot can pick up(retrieve) a bomb at fi-jf. This action will result in: the robot is holding a bomb.\n"
    f"A robot can detonate(trigger) a bomb at location fa-bf connected to location fc-df. This action will result in: the location fc-df does not have soft rock, the robot is holding nothing(the robot is not holding the bomb).\n"
)

INITIAL_STATE_EXTRACTOR_GOLDMINER_PROMPT = (
   f"This is a question related to the Goldminer domain. You are required to extract the initial state of every objects in this plan, including robot, laser, bomb, and n*m locations. Your answer must satisfy all the following requirements. First, think and respond with the format from the example above, including the word choice and paragraph structure. Second, each object's state should contain all properties mentioned in the domain description above. Besides, don't use any markdown formatting."
)

INITIAL_STATE_EXTRACTOR_GOLDMINER_EXAMPLE = (
     f"[Examples]\n"
    f"Initial state example 1: A robotic arm is in a grid and can only move to locations that are connected to its current location. The 3x4 grid locations may have gold, hard rocks, or soft rocks. Rocks cannot be moved. The robotic arm can pick up laser or bomb. Only one item can be picked at a time. There is one laser in the grid that can be used to clear rocks. Robotic arm can fire laser at a location from a connected location. The locations are of the form fi-jf (e.g., f3-2f or f0-1f). The grid cells are connected to their neighbors (e.g., f1-2f is connected to the four neighbors f0-2f, f2-2f, f1-1f, and f1-3f). If a bomb is picked, it cannot be placed back. It can only be detonated at connected location that have soft rock. Bomb supply is available at f0-0f location. Currently, the robot is at position f1-1f and is holding laser. The following locations have hard rock: f1-2f. The location f1-2f is connected to f1-1f.\n"
    f"Extracted from example 1:\n"
    f"First, we confirm every object involved in the initial state. We can find this is a 3x4 grid.\n"
    f"Then we extract each object's state.\n"
    f"Bomb supply is available at f0-0f location. ::: f0_0f: has bomb supply."
    f"the robot is at position f1-1f and is holding laser. ::: Robot: at f1-1f, holding laser.\n"
    f"the following locations have hard rock: f1-2f. ::: f1-2f: has rock.\n"
    f"The 3x4 grid locations may have gold, hard rocks, or soft rocks. ::: f0-1f: has nothing. f0-2f: has nothing. f0-3f: has nothing. f1-0f: has nothing. f1-3f: has nothing. f2-0f: has nothing. f2-1f: has nothing. f2-2f: has nothing. f2-3f: has nothing.\n"
    f"Then, we organize all objects' state into a new paragraph as the end of the answer.\n"
    f"f0-0f: has bomb supply. f1-2f: has rock. Robot: at f1-1f, holding laser. f0-1f: has nothing. f0-2f: has nothing. f0-3f: has nothing. f1-0f: has nothing. f1-3f: has nothing. f2-0f: has nothing. f2-1f: has nothing. f2-2f: has nothing. f2-3f: has nothing. \n"
    f"-------------------\n"
    f"Initial state example 2: A robotic arm is in a grid and can only move to locations that are connected to its current location. The 4x4 grid locations may have gold, hard rocks, or soft rocks. Rocks cannot be moved. The robotic arm can pick up laser or bomb. Only one item can be picked at a time. There is one laser in the grid that can be used to clear rocks. Robotic arm can fire laser at a location from a connected location. The locations are of the form fi-jf (e.g., f3-2f or f0-1f). The grid cells are connected to their neighbors (e.g., f2-2f is connected to f1-2f, f3-2f, f2-1f, and f2-3f). If a bomb is picked, it cannot be placed back. It can only be detonated at connected location that have soft rock. Bomb supply is available at f0-0f location. Currently, the robot is at position f2-2f and is holding laser. The following locations have hard rock: f3-2f. The following locations have soft rock: f1-2f.\n"
    f"Extracted from example 2:"
    f"First, we confirm every object involved in the initial state. We can find this is a 4*4 grid.\n"
    f"Then we extract each object's state.\n"
    f"Bomb supply is available at f0-0f location. ::: f0_0f: has bomb supply.\n"
    f"the robot is at position f2-2f and is holding laser. ::: Robot: at f2-2f, holding laser.\n"
    f"the following locations have hard rock: f3-2f. ::: f3-2f: has rock.\n"
    f"The following locations have soft rock: f1-2f. ::: f1-2f: has soft rock.\n"
    f"The 4x4 grid locations may have gold, hard rocks, or soft rocks. ::: f0-1f: has nothing. f0-2f: has nothing. f0-3f: has nothing. f1-0f: has nothing. f1-1f: has nothing. f1-3f: has nothing. f2-0f: has nothing. f2-1f: has nothing. f2-3f: has nothing. f3-0f: has nothing. f3-1f: has nothing. f3-3f: has nothing.\n"
    f"Then, we organize all objects' state into a new paragraph as the end of the answer.\n"
    f"f0_0f: has bomb supply. Robot: at f2-2f, holding laser. f3-2f: has rock. f1-2f: has soft rock. f0-1f: has nothing. f0-2f: has nothing. f0-3f: has nothing. f1-0f: has nothing. f1-1f: has nothing. f1-3f: has nothing. f2-0f: has nothing. f2-1f: has nothing. f2-3f: has nothing. f3-0f: has nothing. f3-1f: has nothing. f3-3f: has nothing.\n"
    f"-------------------\n"
)

QUESTION_EXTRACTOR_GOLDMINER_EXAMPLE = (
    f"[Examples]\n"
    f"Question example 1: Will the fact \"Location(s) f3-2f is clear\" hold after performing the action \"fire laser from location f2-2f to location f3-2f\" in the current state?\n"
    f"Extracte from example 1: Will the fact \"Location(s) f3-2f is clear\" hold?\n"
    f"-------------------\n"
    f"Question example 2: Will the fact \"Soft rock at f2-1f\" hold after performing the action \"move from location f2-0f to location f2-1f\" in the current state?\n"
    f"Extracte from example 2: Will the fact \"Soft rock at f2-1f\" hold?\n"
    f"-------------------\n"
    f"Question example 3: Will the fact \"Location(s) f2-2f is clear\" hold after performing the action \"detonate bomb at location f2-2f connected to f1-2f\" in the current state?\n"
    f"Extracte from example 3: Will the fact \"Location(s) f2-2f is clear\" hold?\n"
    f"-------------------\n"
)

ACTION_SEQUENCE_EXTRACTOR_GOLDMINER_PROMPT = (
    f"[Examples]\n"
    f"Action example 1: Is the following sequence of actions applicable in this state: move from location f1-1f to location f2-1f, move from location f2-1f to location f2-2f?\n"
    f"Extracted from example 1: Move from location f1-1f to location f2-1f. Move from location f2-1f to location f2-2f.\n"
    f"-------------------\n"
    f"Action example 2: Is the following action applicable in this state: aim the laser from location f0-2f to location f1-2f?\n"
    f"Extracted from example 2: Aim the laser from location f0-2f to location f1-2f?.\n"
    f"-------------------\n"
    f"Action example 3: Is the following action applicable in this state: pick up the laser at location f0-1f?\n"
    f"Extracted from example 3: Pick up the laser at location f0-1f.\n"
    f"-------------------\n"
)

ACTION_TAKER_GOLDMINER_PROMPT = (
    f"Based on the domain description and examples above, take the action and return the new state of all objects. Your answer must satisfy all the following requirements. First, think and respond like examples above, you are required to return states of all objects(robot, laser, bomb and locations), including states that are not effected by the action. Second, each object's state must contain all properties mentioned in the domain description above. Third, after your analysis, please return states of all objects into a new paragraph as the end of your answer. Your final paragraph should use the format like: \"f0_0f: has bomb supply. Robot: at f2-2f, holding laser.\" Besides, don't use any markdown formatting.\n"
)

ACTION_TAKER_GOLDMINER_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: f0-0f: has bomb supply. Robot: at f2-2f, holding laser. f1-4f: has rock. f1-1f: has rock. f1-2f: has rock. f2-3f: has soft rock. f0-4f: has soft rock. f2-1f: has soft rock. f2-4f: has soft rock. f1-3f: has soft rock. Gold: at location f0-4f. f0-1f: has nothing. f0-2f: has nothing. f0-3f: has nothing. f1-0f: has nothing. f2-0f: has nothing. f2-2f: has nothing.\n"
    f"Action 1: Fire laser from location f2-2f to location f1-2f.\n"
    f"Answer 1:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Robot: at f2-2f, holding laser. f1-2f: has rock.\n"
    f"Based on the domain description, A robot can aim(direct/fire) the laser from location fa-bf to location fc-df. This action will result in: the location fc-df does not have any rock(clear)."
    f"the location fc-df does not have any rock(clear). ::: f1-2f: has nothing.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into a paragraph as the end of answer.\n"
    f"f0-0f: has bomb supply. Robot: at f2-2f, holding laser. f1-4f: has rock. f1-1f: has rock. f1-2f: has nothing. f2-3f: has soft rock. f0-4f: has soft rock. f2-1f: has soft rock. f2-4f: has soft rock. f1-3f: has soft rock. Gold: at location f0-4f. f0-1f: has nothing. f0-2f: has nothing. f0-3f: has nothing. f1-0f: has nothing. f2-0f: has nothing. f2-2f: has nothing."
    f"-------------------\n"
    f"Current state example 2: f0-0f: has bomb supply. Robot: at f1-1f, holding bomb. f1-2f: has soft rock; f2-1f: has soft rock; f2-2f: has soft rock. f0-3f: has rock; f1-3f: has rock. f2-3f: has gold. f3-0f: has laser. f0-1f: has nothing. f0-2f: has nothing. f1-0f: has nothing. f2-0f: has nothing. f3-1f: has nothing. f3-2f: has nothing. f3-3f: has nothing.\n"
    f"Action 2: Detonate the bomb at location f1-2f connected to location f1-1f.\n"
    f"Answer 2:\n"    
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Robot: at f1-1f, holding bomb. f1-2f: has soft rock.\n"
    f"A robot can detonate(trigger) a bomb at location fa-bf connected to location fc-df. This action will result in: the location fc-df does not have soft rock, the robot is holding nothing(the robot is not holding the bomb).\n"
    f" the location fc-df does not have soft rock ::: f1-2f: has nothing.\n"
    f"the robot is holding nothing(the robot is not holding the bomb). ::: Robot: at f1-1f, holding nothing.\n"
    f"-------------------\n"
)

EXECUTABILITY_CHECKER_GOLDMINER_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: f0-0f: has bomb supply. Robot: at f2-2f, holding bomb. f1-2f: has rock. f2-1f: has rock. f3-2f: has soft rock. f3-3f: has soft rock. f2-3f: has soft rock. Gold: at location f3-3f. Laser: at location f0-0f. f0-1f: has nothing. f0-2f: has nothing. f0-3f: has nothing. f1-0f: has nothing. f1-1f: has nothing. f1-3f: has nothing. f2-0f: has nothing. f3-0f: has nothing. f3-1f: has nothing.\n" 
    f"Action 1: Move to location f2-1f from location f2-2f.\n"
    f"Answer 1:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can check whether the action is executable.\n"
    f"Robot: at f2-2f, holding bomb. f2-1f: has rock.\n"
    f"Based on the domain description, A robot can move(travel) from from location fa-bf to location fc-df. This action is executable only if all following preconditions are satisfied: the robot is currently at fa-bf, fa-bf and fc-df are adjacent, fc-df is clear.\n"
    f"the robot is currently at fa-bf ::: Robot: at f2-2f, holding bomb. ===> SATISFY\n"
    f"fa-bf and fc-df are adjacent ::: f2-2f is connected to f2-1f. ===> SATISFY\n"
    f"fc-df is clear ::: f2-1f: has rock. ===> NOT SATISFY\n"
    f"Since not all preconditions are satisfied, this action is not executable.\n"
    f"-------------------\n"
    f"Current state example 2: f0-0f: has bomb supply, has laser. Robot: at f0-0f, holding bomb. f1-1f: has rock. f3-3f: has rock, has gold. f3-2f: has soft rock. f2-3f: has soft rock. f0-1f: has nothing. f0-2f: has nothing. f0-3f: has nothing. f1-0f: has nothing. f1-2f: has nothing. f1-3f: has nothing. f2-0f: has nothing. f2-1f: has nothing. f2-2f: has nothing. f3-0f: has nothing. f3-1f: has nothing.\n"
    f"Action 2: Move to location f2-3f from location f0-0f.\n"
    f"Answer 2:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can check whether the action is executable.\n"
    f"Robot: at f0-0f, holding bomb. f2-3f: has soft rock.\n"
    f"Based on the domain description, A robot can move(travel) from from location fa-bf to location fc-df. This action is executable only if all following preconditions are satisfied: the robot is currently at fa-bf, fa-bf and fc-df are adjacent, fc-df is clear.\n"
    f"the robot is currently at fa-bf ::: Robot: at f0-0f, holding bomb. ===> SATISFY\n"
    f"fa-bf and fc-df are adjacent ::: f0-0f is not connected to f2-3f. ===> NOT SATISFY\n"
    f"Since not all preconditions are satisfied, so this action is not executable.\n"
    f"Final answer: False.\n"
    f"-------------------\n"
)



STATE_CHECKER_GOLDMINER_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: f0-0f: has bomb supply. Robot: at f1-2f, holding nothing. f2-3f: has soft rock. f1-3f: has soft rock, has gold. f1-1f: has soft rock. f0-1f: has laser. f0-2f: has nothing. f0-3f: has nothing. f1-0f: has nothing. f2-0f: has nothing. f2-1f: has nothing. f2-2f: has nothing.\n"
    f"Question 1: Will the fact \"Soft rock at f1-3f\" hold?\n"
    f"Answer 1:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false.\n"
    f"Soft rock at f1-3f ::: f1-3f: has soft rock, has gold. ===>SATISFY\n"
    f"Since all propositions in the question match with the curent state, so the question is true.\n"
    f"Final Answer: True.\n"
    f"-------------------\n"
    f"Current state example 2: f0-0f: has bomb supply. Robot: at f0-0f, holding bomb. f1-0f: has nothing. f1-3f: has gold. f0-1f: has laser. f0-2f: has nothing. f0-3f: has nothing. f1-1f: has nothing. f1-2f: has nothing. f2-0f: has nothing. f2-1f: has nothing. f2-2f: has nothing. f2-3f: has nothing.\n"
    f"Question 2: Will the fact \"Soft rock at f1-0f\" hold?\n"
    f"Answer 2:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false.\n"
    f"Soft rock at f1-0f ::: f1-0f: has nothing. ===> NOT SATISFY\n"
    f"Since not all propositions are true, so the answer is false.\n"
    f"Final Answer: False.\n"
    f"-------------------\n"
)


TWOSHOTCOT_APP_GOLDMINER_EXAMPLE = (
    f"[Examples]\n"
    f"(Example1)\n"
    f"Initial State: A robotic arm is in a grid and can only move to locations that are connected to its current location. The 4x4 grid locations may have gold, hard rocks, or soft rocks. Rocks cannot be moved. The robotic arm can pick up laser or bomb. Only one item can be picked at a time. There is one laser is the grid that can be used to clear rocks. Robotic arm can fire laser at a location from a connected location. The locations are of the form fi-jf (e.g., f3-2f or f0-1f). The grid cells are connected to their neighbors (e.g., f2-2f is connected to f1-2f, f3-2f, f2-1f, and f2-3f). If a bomb is picked, it cannot be placed back. It can only be detonated at connected location that have soft rock. Bomb supply is available at f0-0f location. Currently, the robot is at position f2-2f and is holding a bomb. The following locations have hard rock: f1-2f, f2-1f. The following locations have soft rock: f3-2f, f3-3f, f2-3f. The gold is at f3-3f location. The laser is at f0-0f location.\n"
    f"Question: Is the following action applicable in this state: move to location f2-1f from location f2-2f?\n"
    f"Answer:\n"
    f"Step 1: we find related objects in the current state.\n"
    f"the robot is at position f2-2f and is holding a bomb.\n"
    f"Step 2: we check whether the action is applicable.\n"
    f"The following locations have hard rock: f1-2f, f2-1f.\n"
    f"A robot can move(travel) from from location fa-bf to location fc-df. This action is executable only if all following preconditions are satisfied: the robot is currently at fa-bf, fa-bf and fc-df are adjacent, fc-df is clear. We can see the f2-1f has rock, so this action is not executable.\n"
    f"Step 3: We return our answer based on previous analysis. \n"
    f"Final Answer: False.\n"
    f"-------------------\n"
    f"(Example2)\n"
    f"Initial State: A robotic arm is in a grid and can only move to locations that are connected to its current location. The 3x4 grid locations may have gold, hard rocks, or soft rocks. Rocks cannot be moved. The robotic arm can pick up laser or bomb. Only one item can be picked at a time. There is one laser is the grid that can be used to clear rocks. Robotic arm can fire laser at a location from a connected location. The locations are of the form fi-jf (e.g., f3-2f or f0-1f). The grid cells are connected to their neighbors (e.g., f1-2f is connected to the four neighbors f0-2f, f2-2f, f1-1f, and f1-3f). If a bomb is picked, it cannot be placed back. It can only be detonated at connected location that have soft rock. Bomb supply is available at f0-0f location. Currently, the robot is at position f2-1f and is holding a bomb. The following locations have soft rock: f0-3f, f2-2f, f1-3f, f2-3f, f1-2f. The gold is at f0-3f location. The laser is at f0-0f location.\n"
    f"Question: Is the following action applicable in this state: detonate the bomb from location f2-1f to location f2-2f?\n"
    f"Answer:\n"
    f"Step 1: we find related objects in the current state.\n"
    f"the robot is at position f2-1f and is holding a bomb. The following locations have soft rock: f0-3f, f2-2f, f1-3f, f2-3f, f1-2f.\n"
    f"Step 2: we check whether the action is applicable.\n"
    f"A robot can detonate(trigger) a bomb at location fa-bf connected to location fc-df. This action is executable only if all following preconditions are satisfied: the robot is at location fa-bf, the robot is holding a bomb, fa-bf and fc-df are adjacent, location fc-df has soft rock(must be soft rock).\n"
    f"Executing an action will change states of related objects."
    f"the robot is at location fa-bf, the robot is holding a bomb ::: the robot is at position f2-1f and is holding a bomb. ===> SATISFY\n"
    f"fa-bf and fc-df are adjacent, location fc-df has soft rock(must be soft rock). ::: f2-1f is connected to f2-2f, f2-2f has soft rock. ===> SATISFY\n"
    f"Step 3: We return our answer based on previous analysis. \n"
    f"Final Answer: True.\n"
    f"-------------------\n"
)


TWOSHOTCOT_PROG_GOLDMINER_EXAMPLE = (
    f"[Examples]\n"
    f"(example 1)\n"
    f"Initial state: A robotic arm is in a grid and can only move to locations that are connected to its current location. The 3x5 grid locations may have gold, hard rocks, or soft rocks. Rocks cannot be moved. The robotic arm can pick up laser or bomb. Only one item can be picked at a time. There is one laser is the grid that can be used to clear rocks. Robotic arm can fire laser at a location from a connected location. The locations are of the form fi-jf (e.g., f3-2f or f0-1f). The grid cells are connected to their neighbors (e.g., f1-2f is connected to the four neighbors f0-2f, f2-2f, f1-1f, and f1-3f). If a bomb is picked, it cannot be placed back. It can only be detonated at connected location that have soft rock. Bomb supply is available at f0-0f location. Currently, the robot is at position f0-1f and is holding a laser. The following locations have hard rock: f1-4f, f1-1f, and f1-3f. The following locations have soft rock: f1-2f, f2-3f, f0-4f, f2-1f, f2-4f, and f2-2f. The gold is at f0-4f location.\n"
    f"Question: Will the fact \"The robot is at position f2-3f\" hold after performing the action \"move to location f0-0f from location f0-1f\" in the current state?\n"
    f"Step 1: Take the action and get the new state.\n"
    f"move to location f0-0f from location f0-1f. After this action, the robot is at f0-0f.\n"
    f"Step 2: Check whether the fact hold.\n"
    f"The robot is at position f2-3f. We can see the robot is at f0-0f, not f2-3f. So this fact is not held.\n"
    f"Step 3: We return our answer based on previous analysis.\n"
    f"Final Answer: False.\n"
    f"-------------------\n"
    f"(example 2)\n"
    f"Initial state: A robotic arm is in a grid and can only move to locations that are connected to its current location. The 4x4 grid locations may have gold, hard rocks, or soft rocks. Rocks cannot be moved. The robotic arm can pick up laser or bomb. Only one item can be picked at a time. There is one laser in the grid that can be used to clear rocks. Robotic arm can fire laser at a location from a connected location. The locations are of the form fi-jf (e.g., f3-2f or f0-1f). The grid cells are connected to their neighbors (e.g., f1-2f is connected to the four neighbors f0-2f, f2-2f, f1-1f, and f1-3f). If a bomb is picked, it cannot be placed back. It can only be detonated at connected location that have soft rock. Bomb supply is available at f0-0f location. Currently, the robot is at position f1-2f and is holding a laser. The following locations have hard rock: f2-2f. The following locations have soft rock: f0-3f, f2-3f. The gold is at f0-3f location. The laser is at f0-0f location.\n"  
    f"Question: Will the fact \"Location f2-2f is clear\" hold after performing the action \"fire laser from location f1-2f to location f2-2f\" in the current state?\n"
    f"Step 1: Take the action and get the new state.\n"
    f"fire laser from location f1-2f to location f2-2f. After taking the action, f1-2f has nothing.\n"
    f"Step 2: Check whether the fact hold.\n"
    f"Location f2-2f is clear. We can see f1-2f has nothing. So this fact is hold.\n"
    f"Step 3: We return our answer based on previous analysis.\n"
    f"Final Answer: True.\n"
    f"-------------------\n"
)


TWOSHOTCOT_VAL_GOLDMINER_EXAMPLE = (
    F"[Examples]\n"
    f"(example 1)\n"
    f"Initial state: A robotic arm is in a grid and can only move to locations that are connected to its current location. The 3x4 grid locations may have gold, hard rocks, or soft rocks. Rocks cannot be moved. The robotic arm can pick up laser or bomb. Only one item can be picked at a time. There is one laser is the grid that can be used to clear rocks. Robotic arm can fire laser at a location from a connected location. The locations are of the form fi-jf (e.g., f3-2f or f0-1f). The grid cells are connected to their neighbors (e.g., f1-2f is connected to the four neighbors f0-2f, f2-2f, f1-1f, and f1-3f).  If a bomb is picked, it cannot be placed back. It can only be detonated at connected location that have soft rock. Bomb supply is available at f0-0f location.  Currently, the robot is at position f2-0f and its arm is empty. The following locations have hard rock: f1-1f and f0-2f. The following locations have soft rock: f0-3f, f1-2f, f2-2f, f2-1f, f2-3f, f1-3f, and f0-1f. The gold is at f0-3f location. The laser is at f0-0f location. The goal is to reach a state where the following facts hold: The robot is holding gold.\n"    
    f"Question: Is the following sequence of actions \"move from loc f2-0f to loc f1-0f, move from loc f1-0f to loc f0-0f, pick up the laser at loc f0-0f, move from loc f0-0f to loc f0-1f, aim the laser from loc f0-1f to loc f0-2f\" a plan for the current state?\n"
    f"Step 1: We check whether each action is executable. If executable, take the action and return the new state, otherwise return false.\n"
    f"move from loc f2-0f to loc f1-0f, after this action the robot is at f1-0f. move from loc f1-0f to loc f0-0f, after this action the robot is at f0-0f. pick up the laser at loc f0-0f, after this action the robot is holding a laser. move from loc f0-0f to loc f0-1f, after this action the robot is at f0-1f. aim the laser from loc f0-1f to loc f0-2f, after this action f0-2f is clear.\n"
    f"Step 2: We check whether the goal is reached.\n"
    f"The goal is to reach a state where the following facts hold: The robot is holding gold. We can see the robot is not holding gold. So the goal is not reached.\n"
    f"Step 3: We return our answer based on previous analysis.\n"
    f"Final Answer: False.\n"
    f"-------------------\n"
    f"(example 2)\n"
    f"Initial state: A robotic arm is in a grid and can only move to locations that are connected to its current location. The 3x4 grid locations may have gold, hard rocks, or soft rocks. Rocks cannot be moved. The robotic arm can pick up laser or bomb. Only one item can be picked at a time. There is one laser is the grid that can be used to clear rocks. Robotic arm can fire laser at a location from a connected location. The locations are of the form fi-jf (e.g., f3-2f or f0-1f). The grid cells are connected to their neighbors (e.g., f1-2f is connected to the four neighbors f0-2f, f2-2f, f1-1f, and f1-3f).  If a bomb is picked, it cannot be placed back. It can only be detonated at connected location that have soft rock. Bomb supply is available at f0-0f location.  Currently, the robot is at position f1-0f and its arm is empty. The following locations have hard rock: f0-2f, f2-1f. The following locations have soft rock: f1-1f, f1-2f, f2-2f, f2-3f, and f1-3f. The gold is at f1-3f location. The laser is at f0-0f location. The goal is to reach a state where the following facts hold: The robot is holding gold.\n"
    f"Question: Which of the following claims is true with regard to the following sequence of actions \"move to location f0-0f from location f1-0f, pick up laser at loc f0-0f, move to location f0-1f from location f0-0f, fire laser from loc f0-1f to loc f0-2f, move to location f0-2f from location f0-1f. A. The sequence is not valid. B. The sequence is a plan. C. The sequence is applicable, but does not achieve the goal. D. The sequence is not applicable.\n"
    f"Answer:\n"
    f"Step 1: Since the question ask whether the action sequence is a plan, we need to take actions to reach the fianl answer, then check the goal.\n"
    f"move to location f0-0f from location f1-0f. After this action, the robot is at f0-0f.\n"
    f"pick up laser at loc f0-0f. After this action, the robot is holding a laser.\n"
    f"move to location f0-1f from location f0-0f. After this action, the robot is at f0-1f.\n"
    f"fire laser from loc f0-1f to loc f0-2f. After this action, f0-2f is clear.\n"
    f"move to location f0-2f from location f0-1f. After this action, the robot isat f0-2f.\n"
    f"Step 2: Then we check whether the action sequence reaches the goal.\n"
    f"The goal is to reach a state where the following facts hold: The robot is holding gold. We can see the robot is not holding the gold. So this action sequence can not reach the goal.\n"
    f"Step 3: We return our answer based on previous analysis. \n"
    f"Final Answer: C.\n"   
    f"-------------------\n"
)




#-------------------------------------
#Alfworld Prompts
#-------------------------------------
ALFWORLD_DOMAIN_DESCRIPTION= (
    
)

INITIAL_STATE_EXTRACTOR_ALFWORLD_PROMPT = ( )


INITIAL_STATE_EXTRACTOR_ALFWORLD_EXAMPLE = ()


QUESTION_EXTRACTOR_ALFWORLD_EXAMPLE = ()


ACTION_SEQUENCE_EXTRACTOR_ALFWORLD_PROMPT = ()


ACTION_TAKER_ALFWORLD_PROMPT = ()


ACTION_TAKER_ALFWORLD_EXAMPLE = ()


EXECUTABILITY_CHECKER_ALFWORLD_EXAMPLE = ()


STATE_CHECKER_ALFWORLD_EXAMPLE = ()


TWOSHOTCOT_APP_ALFWORLD_EXAMPLE = (
    
)


TWOSHOTCOT_PROG_ALFWORLD_EXAMPLE = ()


TWOSHOTCOT_VAL_ALFWORLD_EXAMPLE = ()



