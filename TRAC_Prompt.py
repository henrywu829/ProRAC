#----------------------
#General Prompts
#----------------------
QUESTION_EXTRACTOR_PROMPT = f"Based on examples above, extract the question from the given content. Your answer should meet all the following conditions: First, extract the interrogative sentences and the content following the interrogative sentences, as what exmaples do above. If there is an if conditional clause, also extract the content of the if clause. Second, if the interrogative sentence is followed by the state of the objects, extract that as well. Third, do not use any markdown syntax. Fourth, organize the question you extracred in one paragraph. Remember, you only need to extract the questions, not solve them."

EXECUTABILITY_CHECKER_PROMPT = f"Based on the domain description and examples above, check whether this action is executable at current state. First, think and respond with the format from the example above, including the word choice and paragraph structure. After your analysis, give your final answer in the last paragraph, and the last paragraph should be like \"Final Answer: False(True if executable).\" Besides, don't use any markdown formatting."

STATE_CHECKER_PROMPT = f"Above contents include current state and question. Based on the domain description and examples given above, check whether the question matches with the current state. Your answer must satisfy all the following requirements. First, think and respond with the format from the example above, including the word choice and paragraph structure. Second, don't use any markdown formatting. Third, After your analysis, you should tell me your final answer in the last paragraph, and organize the last paragraph with the format: \"Final Answer: True(False if not match)\"."

ACTION_SEQUENCE_EXTRACTOR_PROMPT = f"This is a plan, you are required to think and understand the entire plan, then extract actions from this plan. Your answer must satisfy all the following requirements. First, Each sentence should contain only one action, and it should be a complete sentence that includes the prepositions and other additional structures from the original plan. Second, don't use any comma in each sentence. Third, Your answer does not need to consider actions that appear in interrogative sentences or actions that appear in if-clauses. Fourth, put all sentences into one paragraph. Remember, you are required to only extract actions, you don't need to solve the question. Besides, don't use any markdown formatting."




DOMAIN_DESCRIPTION_BLOCKSWORLD = (
    f"[Domain Description]\n"
    f"In blocksworld, blocks can be put on the table, and blocks can be stacked with each other as soon as they satisfy some conditions.\n"
    f"We use the following properties to describe the state of a block: (1)clear; (2)on the table; (3)on the top of another block.\n"
    f"A block is 'clear' means no any other block is stacked on the top of this block. A block is 'on the table' means the block is put on the table. A block is 'on the top of another block' means this block is stacked directly on the top of the another block.\n"
    f"We have the following actions: (1)Moving a block from the table to another block; (2)Moving a block from another block onto the table. (3)Moving a block from block A to block B\n"
    f"Moving a block from the table to another block must satisfy all the following conditions: the block is clear; the block is on the table; the another block is clear. Moving a block from another block onto the table must satisfy all the following conditions: the block is clear; the block is on the top of the another block. Moving a block from block A to block B must satisfy all the following conditions: the block is on the top of block A; the block is clear; block B is clear.\n"
    f"Taking actions will result in changes in blocks' states. Moving a block from the table to another block will result in: the block is clear; the block is not on the table; the block is on the top of the another block; the another block is not clear. Moving a block from another block onto the table will result in: the block is clear; the another block is clear; the block is on the table; the block is not on the top of any other block. Moving a block from block A to block B will result in: the block is on the top of block B; block B is not clear; block A is clear; the block is clear."
)



INITIAL_STATE_EXTRACTOR_PROMPT = (
    f"This is a question related to the Blocksworld domain. You are required to extract the initial state of every blocks in this plan. Your answer must satisfy all the following requirements. First, think and respond with the format from the example above, including the word choice and paragraph structure. Second, each object's state should contain all properties mentioned in the domain description above. Besides, don't use any markdown formatting."
)




INITIAL_STATE_EXTRACTOR_EXAMPLE = (
    f"[Examples]\n"
    f"Initial state example 1: The red block is on the table. The blue block is on the table. The green block is on the table. The yellow block is on the table. The purple block is on the table. The red block is clear. The blue block is clear. The green block is clear. The yellow block is clear. The purple block is clear.\n"
    f"Extracted from initial state:\n"
    f"First, we confirm every object involved in the initial state. We can find five blocks here.\n"
    f"Then, we extract each object's state.\n"
    f"The red block is on the table. The blue block is on the table. The green block is on the table. The yellow block is on the table. The purple block is on the table. The red block is clear. The blue block is clear. The green block is clear. The yellow block is clear. The purple block is clear. ::: Red block: on the table, clear. Blue block: on the table, clear. Green block: on the table, clear. Yellow block: on the table, clear. Purple block: on the table, clear.\n"
    f"Then we organize all objects states into a new paragraph as the end of answer.\n"
    f"Red block: on the table, clear. Blue block: on the table, clear. Green block: on the table, clear. Yellow block: on the table, clear. Purple block: on the table, clear.\n"
    f"----------------------\n"
    f"Initial state example 2: The cyan block is on top of the black block. The black block is on the table. The teal block is on the table. The beige block is on the table. The red block is on the table. The cyan block is clear. The teal block is clear. The beige block is clear. The red block is clear. The black block is not clear."
    f"Extracted from initial state:\n"
    f"First, we confirm every object involved in the initial state. We can find five blocks here.\n"
    f"Then, we extract each object's state.\n"
    f"The cyan block is on top of the black block. The black block is on the table. The teal block is on the table. The beige block is on the table. The red block is on the table. The cyan block is clear. The teal block is clear. The beige block is clear. The red block is clear. The black block is not clear. ::: Cyan block: on top of the black block, clear. Black block: on the table, not clear. Teal block: on the table, clear. Beige block: on the table, clear. Red block: on the table, clear.\n"
    f"Then we organize all objects states into a new paragraph as the end of answer.\n"
    f"Cyan block: on top of the black block, clear. Black block: on the table, not clear. Teal block: on the table, clear. Beige block: on the table, clear. Red block: on the table, clear.\n"
    f"----------------------\n"
)



ACTION_TAKER_PROMPT = (
    f"Based on the domain description and examples above, take the action and return the new state of all objects. Your answer must satisfy all the following requirements. First, think and respond like examples above, you are required to return states of all blocks, including states that are not effected by the action. Second, each object's state must contain all properties mentioned in the domain description above. Third, after your analysis, please return states of all objects into a new paragraph as the end of your answer. Besides, don't use any markdown formatting.\n"
)



ACTION_TAKER_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: Red block: on the table, clear. Blue block: on the table, clear. Green block: on the table, clear. Yellow block: on the table, clear. Purple block: on the table, clear.\n"
    f"Action 1: Jane moves the red block from the table to the blue block."
    f"Answer 1: \n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Red block: on the table, clear. Blue block: on the table, clear.\n"
    f"Based on the domain description, moving a block from the table to another block will result in: the block is clear; the block is not on the table; the block is on the top of the another block; the another block is not clear.\n"
    f"the block is clear; the block is not on the table; the block is on the top of the another block ::: Red block: on top of the blue block, clear.\n"
    f"the another block is not clear ::: Blue block: on the table, not clear.\n"
    f"Then we return all objects' states into a new paragraph as the end of the answer.\n"
    f"Red block: on top of the blue block, clear. Blue block: on the table, not clear. Green block: on the table, clear. Yellow block: on the table, clear. Purple block: on the table, clear.\n"
    f"----------------------\n"
    f"Current state example 2: Cyan block: on top of the black block, clear. Black block: on the table, not clear. Teal block: on the table, clear. Beige block: on the table, clear. Red block: on the table, clear.\n"
    f"Action 2: Jane moves the cyan block from the black block onto the table.\n"
    f"Answer 2:"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Cyan block: on top of the black block, clear. Black block: on the table, not clear.\n"
    f"Based on the current state and the domain description, moving a block from another block onto the table will result in: the block is clear; the another block is clear; the block is on the table.\n"
    f"the block is clear; the block is on the table. ::: Cyan block: on the table, clear.\n"
    f"the another block is clear ::: Black block: on the table, clear.\n"
    f"Then we return all objects' states into a new paragraph as the end of the answer.\n"
    f"Cyan block: on the table, clear. Black block: on the table, clear. Teal block: on the table, clear. Beige block: on the table, clear. Red block: on the table, clear.\n"
    f"----------------------\n"
)



EXECUTABILITY_CHECKER_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: Red block: on the table, clear. Blue block: on the table, clear. Green block: on the table, clear. Yellow block: on the table, clear. Purple block: on the table, clear.\n"
    f"Action sequence 1: Jane moves the red block from the table to the blue block.\n"
    f"Answer 1:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can check whether the action is executable.\n"
    f"Red block: on the table, clear. Blue block: on the table, clear.\n"
    f"Based on the domain description, moving a block from the table to another block is executable only if all following preconditions are satisfied: the block is on the table; the block is clear; the another block is clear.\n"
    f"the block is on the table, the block is clear ::: Red block: on the table, clear. ===> SATISFY\n"
    f"the another block is clear. ::: Blue block: on the table, clear. ===> SATISFY\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final answer: True.\n"
    f"----------------------\n"
    f"Current state example 2: Cyan block: on top of the black block, clear. Black block: on the table, not clear. Teal block: on the table, clear. Beige block: on the table, clear. Red block: on the table, clear.\n"
    f"Action sequence 2: Jane moves the cyan block from the black block onto the table.\n"
    f"Answer 2:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can check whether the action is executable.\n"
    f"Cyan block: on top of the black block, clear. Black block: on the table, not clear.\n"
    f"Based on the domain description, moving a block from another block onto the table is executable only if all following preconditions are satisfied: the block is clear; the block is on the top of the another block.\n"
    f"the block is clear ::: Cyan block: on top of the black block, clear. ===> SATISFY\n"
    f"the block is on the top of the another block ::: Cyan block: on top of the black block, clear. ===> SATISFY\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final answer: True.\n"
    f"----------------------\n"
)





STATE_CHECKER_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: Cyan block: on top of the black block, clear. Black block: on the table, not clear. Teal block: on the table, clear. Beige block: on the table, clear. Red block: on the table, clear.\n"
    f"Question 1: The teal block is on top of the beige block.\n"
    f"Answer 1:"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. \n"
    f"Teal block: on the table, clear. Beige block: on the table, clear. Red block: on the table, clear.\n"
    f"The teal block is on top of the beige block ::: Teal block: on the table, clear. ===> NOT SATISFY\n"
    f"Since not all propositions in the question match with the curent state, so the question is true.\n"
    f"Final Answer: False.\n"
    f"----------------------\n"
    f"Current state example 2: Cyan block: on the table, clear. Black block: on the table, clear. Teal block: on the table, clear. Beige block: on the table, clear. Red block: on the table, clear.\n"
    f"Question 2: The red block is on the table.\n"
    f"Answer 2:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. \n"
    f"Red block: on the table, clear.\n"
    f"The red block is on the table ::: Red block: on the table, clear. ===> SATISFY\n"
    f"Since all propositions in the question match with the curent state, so the question is true.\n"
    f"Final Answer: True.\n"
    f"----------------------\n"
)



   


TWOSHOTCOT_EXAMPLE_PR = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"Current state: The cyan block is on top of the black block. The black block is on the table. The teal block is on the table. The beige block is on the table. The red block is on the table. The cyan block is clear. The teal block is clear. The beige block is clear. The red block is clear. The black block is not clear.\n"
    f"Action Sequence: Jame moves the teal block from the table to the beige block. Jane moves the cyan block from the black block onto the table.\n"
    f"Query: The teal block is on top of the cyan block. The beige block is on the table.\n"
    f"Question: After taking the action sequence based on the current state, whether the query is true of false?\n"
    f"Answer: \n"
    f"Step 1: we take each action in the action sequence to reach the final state.\n"
    f"After taking the action 'Jame moves the teal block from the table to the beige block', the teal block is on top of the beige block. Then, after taking the action 'Jane moves the cyan block from the black block onto the table.', the cyan block is on the table and the balck block is clear.\n"
    f"Step 2: we check whether the query is true or false.\n" 
    f"The teal block is on top of the cyan block. The beige block is on the table. We can see the teal block is on top of the beige block. So the query is false.\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final Answer: True"
    f"------------\n"
    f"(Example 2)\n"
    f"Current state: The blue block is on the table. The green block is on top of the blue block. The yellow block is on the table. The pink block is on the table. The gray block is on the table. The green block is clear. The yellow block is clear. The pink block is clear. The gray block is clear. The blue block is not clear.\n"
    f"Action sequence: Jane moves the yellow block from the table to the pink block. Jane moves the gray block from the table to the yellow block. Jane moves the green block from the blue block to the gray block.\n"
    f"Query: The green block is on top of the gray block. The pink block is not on top of the green block.\n"
    f"Question: After taking the action sequence based on the current state, whether the query is true of false?\n"
    f"Answer:\n"
    f"Step 1: we take each action in the action sequence to reach the final state.\n"
    f"After taking the action 'Jane moves the yellow block from the table to the pink block', the yellow block is on top of the pink block, and the pink block is no longer clear.\n"
    f"Then, after taking the action 'Jane moves the gray block from the table to the yellow block', the gray block is on top of the yellow block, and the yellow block is no longer clear.\n"
    f"Finally, after taking the action 'Jane moves the green block from the blue block to the gray block', the green block is on top of the gray block, and the blue block becomes clear.\n"
    f"Step 2: we check whether the query is true or false.\n"
    f"The green block is on top of the gray block. The pink block is not on top of the green block.\n"
    f"We can see from the final state that the green block is on top of the gray block, and the pink block is at the bottom of a separate stack, so both parts of the query are true.\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final Answer: True\n"
    f"------------\n"
)




TWOSHOTCOT_EXAMPLE_EXE = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"Current state: The red block is on the table. The blue block is on the table. The green block is on top of the red block. The yellow block is on the table. The green block is clear. The blue block is clear. The yellow block is clear. The red block is not clear. The purple block is clear. The purple block is on the table.\n"
    f"Action sequence: Jane moves the blue block from the table to the yellow block.\n"
    f"Check whether all actions in the action sequence is executable or not.\n"
    f"Answer:\n"
    f"Step 1: We check whether every action is executable or not. If executable, we take the action and get the new state. If not, we stop and return the final answer.\n "
    f"Action 1 is Jane moves the blue block from the table to the yellow block. Based on the domain description, Moving a block from the table to another block must satisfy all the following conditions: the block is clear; the block is on the table; the another block is clear. We can see the blue block is on the table and clear, and the yellow block is also clear. So this action is executable.\n"
    f"Step 2: If all actions in the action sequence is executable, the answer is true, otherwise false.\n"
    f"Since all actions can be executed, the answer is true.\n"
    f"Final answer: True.\n"
    f"------------\n"
    f"(Example 2)\n"
    f"Current state: The white block is on top of the black block. The black block is on the table. The orange block is on the table. The gray block is on the table. The blue block is clear. The white block is clear. The orange block is clear. The gray block is clear. The black block is not clear.\n"
    f"Action sequence: Jane moves the blue block from the orange block to the gray block. Jane moves the white block from the black block to the blue block.\n"
    f"Check whether all actions in the action sequence is executable or not.\n"
    f"Answer:\n"
    f"Step 1: We check whether every action is executable or not. If executable, we take the action and get the new state. If not, we stop and return the final answer.\n "
    f"Action 1 is Jane moves the blue block from the orange block to the gray block. Based on the domain description, moving a block from another block to a target block must satisfy: the source block is clear; the source block is on another block; the target block is clear. But from the current state, the blue block is not on the orange block — it is not on any block. So this action is not executable.\n"
    f"Step 2: If all actions in the action sequence is executable, the answer is true, otherwise false.\n"
    f"Since the first action cannot be executed, we stop and the answer is false.\n"
    f"Final answer: False.\n"
    f"------------\n"
)





TWOSHOTCOT_EXAMPLE_PV = (
    f"[Examples]\n"
    f"(Example1)\n"
    f"Current State: The red block is clear. The green block is clear. The green block is on the table. The orange block is clear. The red block is on the table. The yellow block is on the table. The yellow block is clear. The gray block is on the table. The gray block is clear. The orange block is on the table.\n"
    f"Action sequence: Jane moves the green block from the table to the red block.\n"
    f"Goal: the red block is not on top of the gray block and the yellow block is not on top of the orange block.\n"
    f"Take every action in the action sequence, check whether the action sequence can reach the state that satisfies the goal.\n"
    f"Answer:\n"
    f"Step 1: We take every action in the action sequence, and get the final state.\n"
    f"After taking the action 'Jane moves the green block from the table to the red block', the green block is on top of the red block, and the red block is no longer clear.\n"
    f"Step 2: We check whether the final state can satisfy the query.\n"
    f"the red block is not on top of the gray block and the yellow block is not on top of the orange block. We can see the red block is on the table and not clear, so the red block is not on top of the gray block. Besides, the we can see the yellow block is on the table and the orange block is also on the table, so the yellow block is not on top of the orange block."
    f"Since all propositions in the goal are true, so the goal is true.\n"
    f"Final answer: True.\n"
    f"------------\n"
    f"(Example 2)\n"
    f"Current state: The black block is clear. The white block is on the table. The white block is clear. The cyan block is clear. The black block is on the table. The brown block is on the table. The cyan block is on the table. The pink block is on the table. The pink block is clear. The brown block is clear.\n"
    f"Action sequence: Jane moves the brown block from the table to the cyan block. Jane moves the white block from the table to the black block.\n"
    f"Query: the white block is not on top of the black block and the cyan block is not on top of the brown block.\n"
    f"Answer:\n"
     f"Step 1: We take every action in the action sequence, and get the final state.\n"
    f"After taking the action 'Jane moves the brown block from the table to the cyan block', the brown block is on top of the cyan block. Then, after taking the action 'Jane moves the white block from the table to the black block', the white block is on top of the black block.\n"
    f"Step 2: We check whether the final state can satisfy the query.\n"
    f"The white block is not on top of the black block and the cyan block is not on top of the brown block. However, in the final state, the white block is on top of the black block, and the brown block is on top of the cyan block. So both propositions in the goal are false.\n"
    f"Since the goal is not satisfied, the answer is false.\n"
    f"Final answer: False.\n"
    f"------------\n"
)