#----------------------
#General Prompts
#----------------------
QUESTION_EXTRACTOR_PROMPT = f"Based on examples above, extract the question from the given content. Your answer should meet all the following conditions: First, extract the interrogative sentences and the content following the interrogative sentences, as what exmaples do above. If there is an if conditional clause, also extract the content of the if clause. Second, if the interrogative sentence is followed by the state of the objects, extract that as well. Third, do not use any markdown syntax. Fourth, organize the question you extracred in one paragraph. Remember, you only need to extract the questions, not solve them."

EXECUTABILITY_CHECKER_PROMPT = f"Based on the domain description and examples above, check whether this action is executable at current state. First, think and respond with the format from the example above, including the word choice and paragraph structure. After your analysis, give your final answer in the last paragraph, and the last paragraph should be like \"Final Answer: False(True if executable).\" Besides, don't use any markdown formatting."
    
STATE_CHECKER_PROMPT = f"Above contents include current state and question. Based on the domain description and examples given above, check whether the question matches with the current state. Your answer must satisfy all the following requirements. First, think and respond with the format from the example above, including the word choice and paragraph structure. Second, don't use any markdown formatting. Third, After your analysis, you should tell me your final answer in the last paragraph, and organize the last paragraph with the format: \"Final Answer: True(False if not match)\"."

ACTION_SEQUENCE_EXTRACTOR_PROMPT = f"This is a plan, you are required to think and understand the entire plan, then extract actions from this plan. Your answer must satisfy all the following requirements. First, Each sentence should contain only one action, and it should be a complete sentence that includes the prepositions and other additional structures from the original plan. Second, don't use any comma in each sentence. Third, Your answer does not need to consider actions that appear in interrogative sentences or actions that appear in if-clauses. Fourth, put all sentences into one paragraph. Remember, you are required to only extract actions, you don't need to solve the question. Besides, don't use any markdown formatting."



#----------------------
#DEPOTS Domain
#----------------------
DEPOTS_DOMAIN_DESCRIPTION = (
    f"[Domain Description]\n"
    f"Depots domain involves elements such as truck, crate, pallet, distributor, and depot. Hoist and pallet have fixed locations, which can either be at the depot or at the distributor. The location of the crate and truck are not fixed. Crate can be put on a pallet, or put on the top of another crate, or be held by a hoist, or be loaded into a truck. The hoist can only hold one crate at a time. We don't consider crate's stack constraint while it is in the truck.\n"
    
    f"Different properties are used to describe current states of different objects. For crate we use: at depot/distributor_X, has crate_X on top of it/clear, on top of crate_X/pallet_X, in truck_X, held by hoist_X. For hoist we use: at depot/distributor_X, available(free)/unavailable, holding crate_X. For pallet we use: at depot/distributor, has crate_x on it/clear. For truck we use: at depot/distributor_X, has crate_X in it/has no crate in it.\n"
    
    f"Following actions are executable only if all preconditions are met, if any condition are not satisfied, the action is not executable.\n"
    
    f"A truck can 'drive' from location A to location B. Location can be a depot or distributor. This action is executable only if all following preconditions are satisfied: truck is currently at location A.\n"
    
    f"A hoist can 'lift' a crate from pallet_x/crate_x at the location. This action is executable if all following preconditions are satisfied: the hoist and the crate are both at the same location, the hoist is available, the crate is on the top of pallet_x/crate_x, the crate is clear.\n"
    
    f"A hoist can 'drop' a crate on pallet_x/crate_x at the location. This action is executable if all following preconditions are satisfied: the hoist and pallet_x/crate_x are both at the same location, pallet_x/crate_x is clear, the hoist is holding the crate.\n"
    
    f"A hoist can 'load' a crate into a truck at the location. This action is executable if all following preconditions are satisfied: the hoist and the truck are at the same location, the hoist is holding the crate.\n"
    
    f"A hoist can 'unload' a crate from a truck at the location. This action is executable if all following preconditions are satisfied: the hoist and the truck are at the same location, the hoist is available, the crate is on the truck.\n"
    
    f"Executing an action will change states of related objects.\n"
    
    f"A truck can 'drive' from location A to location B. This action will result in: the truck is at location B.\n"
    
    f"A hoist can 'lift' a crate from pallet_x/crate_x at the location. This action will result in: the crate is not at the location, the hoist is holding the crate, the hoist is not available, the crate is not clear, pallet_x/crate_x is clear, the crate is not on top of pallet_x/crate_x.\n"
    
    f"A hoist can 'drop' a crate on pallet_x/crate_x at the location. This action will result in: the hoist is available, the hoist is not holding the crate, the crate is at the location, the crate is clear, the crate is on top of pallet_x/crate_x, pallet_x/crate_x is not clear.\n"
    
    f"A hoist can 'load' a crate into a truck at the location. This action will result in: the hoist is available, the hoist is not holding the crate, the crate is in the truck.\n"
    
    f"A hoist can 'unload' a crate from a truck at the location. This action will result in: the hoist is holding the crate, the hoist is unavailable, the crate is not in the truck.\n"
)


INITIAL_STATE_EXTRACTOR_DEPOTS_PROMPT = f"This is a question related to the deopts domain. You are required to extract the initial state of every objects in this plan, including trucks, crates, pallets and hoists. Your answer must satisfy all the following requirements. First, think and respond with the format from the example above, including the word choice and paragraph structure. Second, each object's state should contain all properties mentioned in the domain description above. Besides, don't use any markdown formatting."


INITIAL_STATE_EXTRACTOR_DEPOTS_EXAMPLE = (
    f"[Examples]\n"
    f"Initial state example 1: Crate0 can be found located at distributor0, crate0 is clear of any crates, crate0 is on pallet3, crate1 has crate2 on it, crate1 is on top of pallet2, crate3 is at depot2, crate3 is clear, crate3 is on crate2, depot0 is where hoist0 is located, depot1 is where truck1 is located, depot2 is where crate1 is located, depot2 is where crate2 is located, distributor0 is where hoist3 is located, distributor1 is where hoist4 is located, distributor1 is where pallet4 is located, hoist0 is available for work, hoist1 can be found located at depot1, hoist1 is available, hoist2 is available, hoist2 is located at depot2, hoist3 is accessible, hoist4 is available for work, hoist5 is available, hoist5 is located at distributor2, pallet0 is clear, pallet0 is located at depot0, pallet1 is clear, pallet1 is located at depot1, pallet2 can be found located at depot2, pallet3 is located at distributor0, pallet4 is clear of any crates, pallet5 is clear of any crates, pallet5 is located at distributor2, truck0 is at distributor0 and truck2 can be found located at depot0. \n"
    f"Extracted from initial state example 1:\n"
    f"In order to extract initial states of objects, we first need to confirm how many objects are mentioned in the initial state.\n"
    
    f"We can find following objects in the intial state description: crate0, crate1, crate2, crate3, hoist0, hoist1, hoist2, hoist3, hoist4, hoist5, pallet0, pallet1, pallet2, pallet3, pallet4, pallet5, truck0, truck1, truck2.\n"
    
    f"Then, we find all descriptions related to an object, and organize then into the required format. Repeat this process until all objects' states are extracted, and each object's state contains all related properties.\n"

    f"Crate0 can be found located at distributor0, crate0 is clear of any crates, crate0 is on pallet3, ::: Crate0: at distributor0, clear, on top of pallet3. \n"
    f"crate1 has crate2 on it, crate1 is on top of pallet2, depot2 is where crate1 is located, depot2 is where crate2 is located, crate3 is at depot2, crate3 is clear, crate3 is on crate2,  ::: Crate1: at depot2, on top of pallet2, has crate2 on it. Crate2: at depot2, on top of crate1, has crate3 on it. Crate3: at depot2, on top of crate2, clear. \n"
    f"depot0 is where hoist0 is located, hoist0 is available for work ::: Hoist0: at depot0, available.\n"
    f"hoist1 can be found located at depot1, hoist1 is available, ::: Hoist1: at depot1, available.\n"
    f"hoist2 is available, hoist2 is located at depot2, ::: Hoist2: at depot2, available.\n"
    f"distributor0 is where hoist3 is located, hoist3 is accessible ::: Hoist3: at distributor0, available.\n"
    f"distributor1 is where hoist4 is located, hoist4 is available for work, ::: Hoist4: at distributor1, available.\n"
    f"hoist5 is available, hoist5 is located at distributor2, ::: Hoist5: at distributor2, available.\n"
    f"truck0 is at distributor0 ::: Truck0: at distributor0, has no crate in it.\n"
    f"depot1 is where truck1 is located, ::: Truck1: at depot1, has no crate in it.\n"
    f"truck2 can be found located at depot0. ::: Truck2: at depot0, has no crate in it.\n"
    f"pallet0 is clear, pallet0 is located at depot0, ::: pallet0: at depot0, clear.\n"
    f"pallet1 is clear, pallet1 is located at depot1, ::: pallet1: at depot1, clear.\n"
    f"pallet2 can be found located at depot2, crate1 is on top of pallet2 ::: pallet2: at depot2, has crate1 on it.\n"
    f"pallet3 is located at distributor0, crate0 is on pallet3, ::: pallet3: at distributor0, has crate0 on it.\n"
    f"pallet4 is clear of any crates, distributor1 is where pallet4 is located, ::: pallet4: distributor1, clear.\n"
    f"pallet5 is clear of any crates, pallet5 is located at distributor2, ::: pallet5: distributor2, clear.\n"


    f"After extracting all objects' state, organize the answer into a new paragraph as the end of answer.\n"
    f"Crate0: at distributor0, clear, on top of pallet3. Crate1: at depot2, on top of pallet2, has crate2 on it. Crate2: at depot2, on top of crate1, has crate3 on it. Crate3: at depot2, on top of crate2, clear. Hoist0: at depot0, available. Hoist1: at depot1, available. Hoist2: at depot2, available. Hoist3: at distributor0, available. Hoist4: at distributor1, available. Hoist5: at distributor2, available. Truck0: at distributor0, has no crate in it. Truck1: at depot1, has no crate in it. Truck2: at depot0, has no crate in it. pallet0: at depot0, clear. pallet1: at depot1, clear. pallet2: at depot2, has crate1 on it. pallet3: at distributor0, has crate0 on it. pallet4: distributor1, clear. pallet5: distributor2, clear.\n"
    f"----------------"
)


QUESTION_EXTRACTOR_DEPOTS_EXAMPLE = (
    f"[Examples]\n"
    
    f"Plan example 1: Given the initial condition, the following actions are performed: from depot0, truck2 is driven to depot2, hoist2 lifts crate3 from crate2 at depot2, crate3 is loaded by hoist2 into truck2 at depot2, hoist2 lifts crate2 from crate1 at depot2, at depot2, hoist2 loads crate2 into truck2, crate1 is lifted from pallet2 at depot2 by hoist2, at depot2, hoist2 loads crate1 into truck2, from depot2, truck2 is driven to distributor0, crate0 is lifted from pallet3 at distributor0 by hoist3 and at distributor0, hoist3 loads crate0 into truck2 to reach the current state. In this state, if at distributor0, hoist3 unloads crate1 from truck2, is it True or False that hoist3 is not accessible?\n"
    
    f"Question extracted from plan example 1: In this state, if at distributor0, hoist3 unloads crate1 from truck2, is it True or False that hoist3 is not accessible?\n"
    
    f"------------\n"
    
    f"Plan example 2:  Given the initial condition, the following actions are performed: crate2 is lifted from pallet0 at depot0 by hoist0, crate2 is loaded by hoist0 into truck2 at depot0, truck2 is driven from depot0 to distributor1, hoist2 lifts crate1 from pallet2 at depot2, crate1 is loaded by hoist2 into truck0 at depot2, truck0 is driven from depot2 to distributor0, crate1 is unloaded by hoist3 from truck0 at distributor0, hoist3 drops crate1 on pallet3 at distributor0, hoist4 lifts crate0 from pallet4 at distributor1, at distributor1, hoist4 loads crate0 into truck2, crate3 is lifted from pallet5 at distributor2 by hoist5, at distributor2, hoist5 loads crate3 into truck1, from distributor2, truck1 is driven to distributor1, hoist4 unloads crate3 from truck1 at distributor1, at distributor1, hoist4 drops crate3 on pallet4, at distributor1, hoist4 unloads crate2 from truck2, from distributor1, truck2 is driven to depot1, crate0 is unloaded by hoist1 from truck2 at depot1 and crate0 is dropped on pallet1 at depot1 by hoist1 to reach the current state. In this state, are all of the following valid properties of the state (both with and without negations)? crate0 is clear of any crates, crate0 is not at distributor1, crate0 is not in truck2, crate0 is not inside truck0, crate0 is not located at depot0, crate0 is not located at depot2, crate0 is not located at distributor0, crate0 is not located at distributor2, crate0 is not on crate0, crate0 is not on crate2, crate0 is not on pallet0, crate0 is not on pallet2, crate0 is not on pallet4, crate0 is not on top of pallet5, crate0 is on top of pallet1, crate1 can be found located at distributor0, crate1 cannot be found located at depot0, crate1 does not have crate0 on it, crate1 is clear of any crates, crate1 is not at depot1, crate1 is not in truck2, crate1 is not located at depot2, crate1 is not located at distributor1, crate1 is not on crate0, crate1 is not on crate1, crate1 is not on crate2, crate1 is not on pallet4, crate1 is not on top of crate3, crate1 is on top of pallet3, crate2 cannot be found located at distributor1, crate2 cannot be found located at distributor2, crate2 is not at distributor0, crate2 is not clear, crate2 is not in truck2, crate2 is not inside truck0, crate2 is not located at depot0, crate2 is not located at depot1, crate2 is not located at depot2, crate2 is not on crate0, crate2 is not on crate1, crate2 is not on crate2, crate2 is not on pallet0, crate2 is not on pallet1, crate2 is not on pallet2, crate2 is not on pallet3, crate2 is not on pallet4, crate2 is not on top of crate3, crate2 is not on top of pallet5, crate3 cannot be found located at distributor0, crate3 does not have crate0 on it, crate3 does not have crate3 on it, crate3 is clear of any crates, crate3 is located at distributor1, crate3 is not at distributor2, crate3 is not in truck0, crate3 is not inside truck1, crate3 is not located at depot0, crate3 is not located at depot1, crate3 is not on crate0, crate3 is not on crate2, crate3 is not on top of crate1, crate3 is not on top of pallet2, crate3 is not on top of pallet3, crate3 is on pallet4, depot0 is where hoist0 is located, depot0 is where hoist1 is not located, depot0 is where hoist3 is not located, depot0 is where hoist4 is not located, depot0 is where pallet1 is not located, depot0 is where pallet4 is not located, depot0 is where truck0 is not located, depot0 is where truck2 is not located, depot1 is where crate0 is located, depot1 is where hoist3 is not located, depot1 is where hoist4 is not located, depot1 is where hoist5 is not located, depot1 is where pallet2 is not located, depot1 is where pallet4 is not located, depot1 is where pallet5 is not located, depot1 is where truck1 is not located, depot2 is where crate3 is not located, depot2 is where hoist1 is not located, depot2 is where hoist2 is located, depot2 is where hoist3 is not located, depot2 is where hoist5 is not located, depot2 is where truck0 is not located, distributor0 is where pallet5 is not located, distributor0 is where truck2 is not located, distributor1 is where hoist0 is not located, distributor1 is where hoist5 is not located, distributor1 is where pallet2 is not located, distributor2 is where crate1 is not located, distributor2 is where hoist1 is not located, hoist0 is accessible, hoist0 is not at depot2, hoist0 is not at distributor0, hoist0 is not at distributor2, hoist0 is not elevating crate2, hoist0 is not lifting crate0, hoist0 is not located at depot1, hoist0 is not raising crate1, hoist0 is not raising crate3, hoist1 can be found located at depot1, hoist1 cannot be found located at distributor1, hoist1 is available for work, hoist1 is not elevating crate0, hoist1 is not elevating crate1, hoist1 is not located at distributor0, hoist1 is not raising crate2, hoist1 is not raising crate3, hoist2 is available, hoist2 is not at depot1, hoist2 is not at distributor1, hoist2 is not lifting crate2, hoist2 is not located at depot0, hoist2 is not located at distributor0, hoist2 is not located at distributor2, hoist2 is not raising crate0, hoist2 is not raising crate1, hoist2 is not raising crate3, hoist3 is accessible, hoist3 is located at distributor0, hoist3 is not at distributor2, hoist3 is not elevating crate2, hoist3 is not lifting crate3, hoist3 is not located at distributor1, hoist3 is not raising crate0, hoist3 is not raising crate1, hoist4 can be found located at distributor1, hoist4 cannot be found located at distributor0, hoist4 is lifting crate2, hoist4 is not available for work, hoist4 is not elevating crate3, hoist4 is not lifting crate1, hoist4 is not located at depot2, hoist4 is not located at distributor2, hoist4 is not raising crate0, hoist5 cannot be found located at depot0, hoist5 cannot be found located at distributor0, hoist5 is at distributor2, hoist5 is available, hoist5 is not lifting crate1, hoist5 is not lifting crate2, hoist5 is not raising crate0, hoist5 is not raising crate3, pallet0 can be found located at depot0, pallet0 cannot be found located at depot2, pallet0 cannot be found located at distributor0, pallet0 cannot be found located at distributor2, pallet0 does not have crate1 on it, pallet0 does not have crate3 on it, pallet0 is clear, pallet0 is not at depot1, pallet0 is not located at distributor1, pallet1 can be found located at depot1, pallet1 cannot be found located at depot2, pallet1 cannot be found located at distributor2, pallet1 does not have crate1 on it, pallet1 does not have crate3 on it, pallet1 is not at distributor1, pallet1 is not clear of any crates, pallet1 is not located at distributor0, pallet2 can be found located at depot2, pallet2 cannot be found located at distributor2, pallet2 does not have crate1 on it, pallet2 is clear of any crates, pallet2 is not at depot0, pallet2 is not at distributor0, pallet3 can be found located at distributor0, pallet3 cannot be found located at depot0, pallet3 cannot be found located at depot1, pallet3 does not have crate0 on it, pallet3 is not at depot2, pallet3 is not at distributor1, pallet3 is not at distributor2, pallet3 is not clear of any crates, pallet4 can be found located at distributor1, pallet4 cannot be found located at depot2, pallet4 cannot be found located at distributor0, pallet4 is not at distributor2, pallet4 is not clear of any crates, pallet5 can be found located at distributor2, pallet5 cannot be found located at depot0, pallet5 cannot be found located at depot2, pallet5 cannot be found located at distributor1, pallet5 does not have crate1 on it, pallet5 does not have crate3 on it, pallet5 is clear of any crates, truck0 cannot be found located at distributor1, truck0 does not contain crate1, truck0 is located at distributor0, truck0 is not at distributor2, truck0 is not located at depot1, truck1 cannot be found located at depot0, truck1 cannot be found located at depot2, truck1 cannot be found located at distributor0, truck1 cannot be found located at distributor2, truck1 does not contain crate0, truck1 does not contain crate1, truck1 does not contain crate2, truck1 is located at distributor1, truck2 does not contain crate3, truck2 is located at depot1, truck2 is not at distributor1, truck2 is not at distributor2 and truck2 is not located at depot2. Respond with True or False.\n"
    
    f"Question extracted from plan example 2: In this state, are all of the following valid properties of the state (both with and without negations)? crate0 is clear of any crates, crate0 is not at distributor1, crate0 is not in truck2, crate0 is not inside truck0, crate0 is not located at depot0, crate0 is not located at depot2, crate0 is not located at distributor0, crate0 is not located at distributor2, crate0 is not on crate0, crate0 is not on crate2, crate0 is not on pallet0, crate0 is not on pallet2, crate0 is not on pallet4, crate0 is not on top of pallet5, crate0 is on top of pallet1, crate1 can be found located at distributor0, crate1 cannot be found located at depot0, crate1 does not have crate0 on it, crate1 is clear of any crates, crate1 is not at depot1, crate1 is not in truck2, crate1 is not located at depot2, crate1 is not located at distributor1, crate1 is not on crate0, crate1 is not on crate1, crate1 is not on crate2, crate1 is not on pallet4, crate1 is not on top of crate3, crate1 is on top of pallet3, crate2 cannot be found located at distributor1, crate2 cannot be found located at distributor2, crate2 is not at distributor0, crate2 is not clear, crate2 is not in truck2, crate2 is not inside truck0, crate2 is not located at depot0, crate2 is not located at depot1, crate2 is not located at depot2, crate2 is not on crate0, crate2 is not on crate1, crate2 is not on crate2, crate2 is not on pallet0, crate2 is not on pallet1, crate2 is not on pallet2, crate2 is not on pallet3, crate2 is not on pallet4, crate2 is not on top of crate3, crate2 is not on top of pallet5, crate3 cannot be found located at distributor0, crate3 does not have crate0 on it, crate3 does not have crate3 on it, crate3 is clear of any crates, crate3 is located at distributor1, crate3 is not at distributor2, crate3 is not in truck0, crate3 is not inside truck1, crate3 is not located at depot0, crate3 is not located at depot1, crate3 is not on crate0, crate3 is not on crate2, crate3 is not on top of crate1, crate3 is not on top of pallet2, crate3 is not on top of pallet3, crate3 is on pallet4, depot0 is where hoist0 is located, depot0 is where hoist1 is not located, depot0 is where hoist3 is not located, depot0 is where hoist4 is not located, depot0 is where pallet1 is not located, depot0 is where pallet4 is not located, depot0 is where truck0 is not located, depot0 is where truck2 is not located, depot1 is where crate0 is located, depot1 is where hoist3 is not located, depot1 is where hoist4 is not located, depot1 is where hoist5 is not located, depot1 is where pallet2 is not located, depot1 is where pallet4 is not located, depot1 is where pallet5 is not located, depot1 is where truck1 is not located, depot2 is where crate3 is not located, depot2 is where hoist1 is not located, depot2 is where hoist2 is located, depot2 is where hoist3 is not located, depot2 is where hoist5 is not located, depot2 is where truck0 is not located, distributor0 is where pallet5 is not located, distributor0 is where truck2 is not located, distributor1 is where hoist0 is not located, distributor1 is where hoist5 is not located, distributor1 is where pallet2 is not located, distributor2 is where crate1 is not located, distributor2 is where hoist1 is not located, hoist0 is accessible, hoist0 is not at depot2, hoist0 is not at distributor0, hoist0 is not at distributor2, hoist0 is not elevating crate2, hoist0 is not lifting crate0, hoist0 is not located at depot1, hoist0 is not raising crate1, hoist0 is not raising crate3, hoist1 can be found located at depot1, hoist1 cannot be found located at distributor1, hoist1 is available for work, hoist1 is not elevating crate0, hoist1 is not elevating crate1, hoist1 is not located at distributor0, hoist1 is not raising crate2, hoist1 is not raising crate3, hoist2 is available, hoist2 is not at depot1, hoist2 is not at distributor1, hoist2 is not lifting crate2, hoist2 is not located at depot0, hoist2 is not located at distributor0, hoist2 is not located at distributor2, hoist2 is not raising crate0, hoist2 is not raising crate1, hoist2 is not raising crate3, hoist3 is accessible, hoist3 is located at distributor0, hoist3 is not at distributor2, hoist3 is not elevating crate2, hoist3 is not lifting crate3, hoist3 is not located at distributor1, hoist3 is not raising crate0, hoist3 is not raising crate1, hoist4 can be found located at distributor1, hoist4 cannot be found located at distributor0, hoist4 is lifting crate2, hoist4 is not available for work, hoist4 is not elevating crate3, hoist4 is not lifting crate1, hoist4 is not located at depot2, hoist4 is not located at distributor2, hoist4 is not raising crate0, hoist5 cannot be found located at depot0, hoist5 cannot be found located at distributor0, hoist5 is at distributor2, hoist5 is available, hoist5 is not lifting crate1, hoist5 is not lifting crate2, hoist5 is not raising crate0, hoist5 is not raising crate3, pallet0 can be found located at depot0, pallet0 cannot be found located at depot2, pallet0 cannot be found located at distributor0, pallet0 cannot be found located at distributor2, pallet0 does not have crate1 on it, pallet0 does not have crate3 on it, pallet0 is clear, pallet0 is not at depot1, pallet0 is not located at distributor1, pallet1 can be found located at depot1, pallet1 cannot be found located at depot2, pallet1 cannot be found located at distributor2, pallet1 does not have crate1 on it, pallet1 does not have crate3 on it, pallet1 is not at distributor1, pallet1 is not clear of any crates, pallet1 is not located at distributor0, pallet2 can be found located at depot2, pallet2 cannot be found located at distributor2, pallet2 does not have crate1 on it, pallet2 is clear of any crates, pallet2 is not at depot0, pallet2 is not at distributor0, pallet3 can be found located at distributor0, pallet3 cannot be found located at depot0, pallet3 cannot be found located at depot1, pallet3 does not have crate0 on it, pallet3 is not at depot2, pallet3 is not at distributor1, pallet3 is not at distributor2, pallet3 is not clear of any crates, pallet4 can be found located at distributor1, pallet4 cannot be found located at depot2, pallet4 cannot be found located at distributor0, pallet4 is not at distributor2, pallet4 is not clear of any crates, pallet5 can be found located at distributor2, pallet5 cannot be found located at depot0, pallet5 cannot be found located at depot2, pallet5 cannot be found located at distributor1, pallet5 does not have crate1 on it, pallet5 does not have crate3 on it, pallet5 is clear of any crates, truck0 cannot be found located at distributor1, truck0 does not contain crate1, truck0 is located at distributor0, truck0 is not at distributor2, truck0 is not located at depot1, truck1 cannot be found located at depot0, truck1 cannot be found located at depot2, truck1 cannot be found located at distributor0, truck1 cannot be found located at distributor2, truck1 does not contain crate0, truck1 does not contain crate1, truck1 does not contain crate2, truck1 is located at distributor1, truck2 does not contain crate3, truck2 is located at depot1, truck2 is not at distributor1, truck2 is not at distributor2 and truck2 is not located at depot2. Respond with True or False.\n"
    
    f"------------\n"
    
    f"Plan example 3: Given the initial condition, the following actions are performed: at depot0, hoist0 lifts crate2 off pallet0, hoist0 loads crate2 into truck2 at depot0, truck2 is driven to distributor1 from depot0, crate1 is lifted from pallet2 at depot2 by hoist2, at depot2, hoist2 loads crate1 into truck0, truck0 is driven to distributor0 from depot2, at distributor0, hoist3 unloads crate1 from truck0, at distributor0, hoist3 drops crate1 on pallet3, hoist4 lifts crate0 from pallet4 at distributor1, hoist4 loads crate0 into truck2 at distributor1, crate3 is lifted from pallet5 at distributor2 by hoist5, crate3 is loaded by hoist5 into truck1 at distributor2, from distributor2, truck1 is driven to distributor1, hoist4 unloads crate3 from truck1 at distributor1, hoist4 drops crate3 on pallet4 at distributor1, crate2 is unloaded by hoist4 from truck2 at distributor1, truck2 is driven to depot1 from distributor1, crate0 is unloaded by hoist1 from truck2 at depot1 and at depot1, hoist1 drops crate0 on pallet1 to reach the current state. In this state, is it True or False that hoist4 is elevating crate2?\n"
    
    f"Question extracted from plan example 3: In this state, is it True or False that hoist4 is elevating crate2?\n"
    
    f"------------\n"
)


ACTION_TAKER_DEPOTS_PROMPT = f"Based on the domain description and examples above, take the action and return the new state of all objects. Your answer must satisfy all the following requirements. First, think and respond like examples above, you are required to return states of all objects, including states that are not effected by the action. Second, each object's state must contain all properties mentioned in the domain description above. Third, after your analysis, please return states of all objects in the final paragraph with the format: \"Crate0: at depot0, clear. Crate1: at depot1, on pallet1, unobstructed.\" Besides, don't use any markdown formatting, and keep states of all objects in one paragraph without any content."


ACTION_TAKER_DEPOTS_EXAMPLE = (
    f"[Examples]"
    f"Current state exmaple 1: Crate0: at distributor0, clear, on top of pallet3. Crate1: at depot2, on top of pallet2, has crate2 on it. Crate2: at depot2, on top of crate1, has crate3 on it. Crate3: at depot2, on top of crate2, clear. Hoist0: at depot0, available. Hoist1: at depot1, available. Hoist2: at depot2, available. Hoist3: at distributor0, available. Hoist4: at distributor1, available. Hoist5: at distributor2, available. Truck0: at distributor0, has no crate in it. Truck1: at depot1, has no crate in it. Truck2: at depot0, has no crate in it. pallet0: at depot0, clear. pallet1: at depot1, clear. pallet2: at depot2, has crate1 on it. pallet3: at distributor0, has crate0 on it. pallet4: distributor1, clear. pallet5: distributor2, clear.\n"
    
    f"Action 1: Crate0 is lifted from pallet3 at distributor0 by hoist3.\n"
    
    f"Answer 1:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Crate0: at distributor0, clear, on top of pallet3. Pallet3: at distributor0, has crate0 on it. Hoist3: at distributor0, available.\n"
    f"Based on the domain description, A hoist can 'lift' a crate from pallet_x/crate_x at the location. This action will result in: the crate is not at the location, the hoist is holding the crate, the hoist is not available, the crate is not clear, pallet_x/crate_x is clear, the crate is not on top of pallet_x/crate_x. \n"
    f"the crate is not at the location, the crate is not clear, the hoist is holding the crate ::: Crate0: not clear, held by hoist3.\n"
    f"the hoist is holding the crate, the hoist is not available ::: Hoist3: at distributor0, unavailable, holding crate0.\n"
    f"pallet_x/crate_x is clear, the crate is not on top of pallet_x/crate_x ::: Pallet3: at distributor0, clear.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action, and organize them into a new paragraph as the end of answer.\n"
    f"Crate0: not clear, held by hoist3. Crate1: at depot2, on top of pallet2, has crate2 on it. Crate2: at depot2, on top of crate1, has crate3 on it. Crate3: at depot2, on top of crate2, clear. Hoist0: at depot0, available. Hoist1: at depot1, available. Hoist2: at depot2, available. Hoist3: at distributor0, unavailable, holding crate0. Hoist4: at distributor1, available. Hoist5: at distributor2, available. Truck0: at distributor0, has no crate in it. Truck1: at depot1, has no crate in it. Truck2: at depot0, has no crate in it. pallet0: at depot0, clear. pallet1: at depot1, clear. pallet2: at depot2, has crate1 on it. Pallet3: at distributor0, clear. pallet4: distributor1, clear. pallet5: distributor2, clear.\n"
    f"—————\n"
)


EXECUTABILITY_CHECKER_DEPOTS_EXAMPLE = (
    f"Current state example 1: Crate0: at distributor0, clear, on top of pallet3. Crate1: at depot2, on top of pallet2, has crate2 on it. Crate2: at depot2, on top of crate1, has crate3 on it. Crate3: at depot2, on top of crate2, clear. Hoist0: at depot0, available. Hoist1: at depot1, available. Hoist2: at depot2, available. Hoist3: at distributor0, available. Hoist4: at distributor1, available. Hoist5: at distributor2, available. Truck0: at distributor0, has no crate in it. Truck1: at depot1, has no crate in it. Truck2: at depot0, has no crate in it. pallet0: at depot0, clear. pallet1: at depot1, clear. pallet2: at depot2, has crate1 on it. pallet3: at distributor0, has crate0 on it. pallet4: distributor1, clear. pallet5: distributor2, clear.\n"
    f"Action 1: Hoist2 lifts crate3 from crate2 at depot2.\n"
    f"Answer 1:\n"
    f"In order to check whether this action is executable or not, we first need to find states of objects related to this action, then check whether all preconditions of this action are satisfied.\n"
    f"Hoist2: at depot2, available. Crate3: at depot2, on top of crate2, clear. Crate2: at depot2, on top of crate1, has crate3 on it.\n"
    f"Based on the domain description, a hoist can 'lift' a crate from pallet_x/crate_x at the location. This action is executable if all following preconditions are satisfied: the hoist and the crate are both at the same location, the hoist is available, the crate is on the top of pallet_x/crate_x, the crate is clear.\n"
    f"the hoist and the crate are both at the same location, the hoist is available ::: Hoist2: at depot2, available. Crate3: at depot2, on top of crate2, clear. ===> SATISFY\n"
    f"the crate is on the top of pallet_x/crate_x, the crate is clear. ::: Crate3: at depot2, on top of crate2, clear. Crate2: at depot2, on top of crate1, has crate3 on it. ===> SATISFY\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final answer: True.\n"
    f"——————\n"
    
)


STATE_CHECKER_DEPOTS_EXAMPLE = (
    f"[Example1]\n"
    f"Current state example 1: Crate0: at distributor2, clear, on top of pallet6. Crate1: at depot3, on top of pallet3, clear. Crate2: at depot0, clear, on top of pallet0. Crate3: at distributor1, clear, on top of pallet5. Hoist0: at depot0, available. Hoist1: at depot1, available. Hoist2: at depot2, available. Hoist3: at depot3, available. Hoist4: at distributor0, available. Hoist5: at distributor1, available. Hoist6: at distributor2, available. Pallet0: at depot0, has crate2 on it. Pallet1: at depot1, clear. Pallet2: at depot2, clear. Pallet3: at depot3, has crate1 on it. Pallet4: at distributor0, clear. Pallet5: at distributor1, has crate3 on it. Pallet6: at distributor2, has crate0 on it. Truck0: at depot1, has no crate on it. Truck1: at distributor0, has no crate on it. Truck2: at depot1, has no crate on it.\n"
    f"Question 1: In this state, are all of the following valid properties of the state that do not involve negations? crate0 is at distributor2, crate0 is clear of any crates, crate0 is on top of pallet6, crate1 is at depot3, crate1 is clear of any crates, crate1 is on pallet3, crate2 is at depot0, crate2 is clear of any crates, crate2 is on top of pallet0, crate3 can be found located at distributor1, crate3 is clear of any crates, crate3 is on pallet5, depot1 is where pallet1 is located, distributor0 is where pallet4 is located, distributor2 is where hoist6 is located, hoist0 can be found located at depot0, hoist0 is accessible, hoist1 is accessible, hoist1 is located at depot1, hoist2 can be found located at depot2, hoist2 is available, hoist3 can be found located at depot3, hoist3 is available for work, hoist4 is accessible, hoist4 is at distributor0, hoist5 is at distributor1, hoist5 is available for work, hoist6 is available, pallet0 is at depot0, pallet1 is clear of any crates, pallet2 is clear, pallet2 is located at depot2, pallet3 is located at depot3, pallet4 is clear of any crates, pallet5 can be found located at distributor1, pallet6 is at distributor2, truck0 can be found located at depot0, truck1 is located at distributor0 and truck2 can be found located at depot0. Respond with True or False.\n"
    f"Answer 1:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. If there is any action needed to take in the question, we should first take the action and return all objects states, including those states that are not affected by the action. \n"
    f"crate0 is at distributor2, crate0 is clear of any crates, crate0 is on top of pallet6  :::  Crate0: at distributor2, clear, on top of pallet6.   ===> MATCH\n"
    f"crate1 is at depot3, crate1 is clear of any crates, crate1 is on pallet3  :::  Crate1: at depot3, on top of pallet3, clear.   ===> MATCH\n"
    f"crate2 is at depot0, crate2 is clear of any crates, crate2 is on top of pallet0  ::: Crate2: at depot0, clear, on top of pallet0.   ===> MATCH\n"
    f"crate3 can be found located at distributor1, crate3 is clear of any crates, crate3 is on pallet5  :::  Crate3: at distributor1, clear, on top of pallet5.     ===> MATCH\n"
    f"depot1 is where pallet1 is located.  :::  Pallet1: at depot1, clear.     ===> MATCH\n"
    f"distributor0 is where pallet4 is located,  :::  Pallet4: at distributor0, clear.     ===> MATCH\n"
    f"distributor2 is where hoist6 is located,  :::  Hoist6: at distributor2, available.     ===> MATCH\n"
    f"hoist0 can be found located at depot0, hoist0 is accessible,  :::  Hoist0: at depot0, available.    ===> MATCH\n"
    f"hoist1 is accessible, hoist1 is located at depot1, ::: Hoist1: at depot1, available. ===> MATCH\n"
    f"hoist2 can be found located at depot2, hoist2 is available,  ::: Hoist2: at depot2, available. ===> MATCH\n"
    f"hoist3 can be found located at depot3, hoist3 is available for work, ::: Hoist3: at depot3, available. ===> MATCH\n"
    f"hoist4 is accessible, hoist4 is at distributor0, ::: Hoist4: at distributor0, available. ===> MATCH\n"
    f"hoist5 is at distributor1, hoist5 is available for work, ::: Hoist5: at distributor1, available. ===> MATCH\n"
    f"hoist6 is available, ::: Hoist6: at distributor2, available.  ===> MATCH\n"
    f"pallet0 is at depot0, ::: Pallet0: at depot0, has crate2 on it. ===> MATCH\n"
    f"pallet1 is clear of any crates, ::: Pallet1: at depot1, clear. ===> MATCH\n"
    f"pallet2 is clear, pallet2 is located at depot2, ::: Pallet2: at depot2, clear. ===> MATCH\n"
    f"pallet3 is located at depot3, :::  Pallet3: at depot3, has crate1 on it.  ===> MATCH\n"
    f"pallet4 is clear of any crates, ::: Pallet4: at distributor0, clear. ===> MATCH\n"
    f"pallet5 can be found located at distributor1, :::Pallet5: at distributor1, has crate3 on it. ===> MATCH\n"
    f"pallet6 is at distributor2, ::: Pallet6: at distributor2, has crate0 on it. ===> MATCH\n"
    f"truck0 can be found located at depot0, ::: Truck0: at depot1, has no crate on it. ===> NOT MATCH\n"
    f"Since truck0's state in the question doesn't match with the current state, the question is false.\n"
    f"Final Answer: False.\n"
    
    f"------------\n"
    
    f"Current state example 2: Crate0: at distributor0, clear, on top of pallet3. Crate1: at depot2, on top of pallet2, has crate2 on it. Crate2: at depot2, on top of crate1, has crate3 on it. Crate3: at depot2, on top of crate2, clear. Hoist0: at depot0, available. Hoist1: at depot1, available. Hoist2: at depot2, available. Hoist3: at distributor0, available. Hoist4: at distributor1, available. Hoist5: at distributor2, available. Truck0: at distributor0, has no crate in it. Truck1: at depot1, has no crate in it. Truck2: at depot0, has no crate in it. pallet0: at depot0, clear. pallet1: at depot1, clear. pallet2: at depot2, has crate1 on it. pallet3: at distributor0, has crate0 on it. pallet4: distributor1, clear. pallet5: distributor2, clear.\n"
    f"Question 2 : In this state, if hoist3 lift crate0 at distributor0 to reach the current state. Are following properties true or false? Crate0 is held by hoist3 and truck0 is at distributor0?\n"
    f"Answer 2:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. If there is any action needed to take in the question, we should first take the action and return all objects states, including those states that are not affected by the action. \n"
    f"Because the question contains one action, we should first take the action and get new states of all objects. After taking the action, we should return states of all objects, including states that are not effected by the action.\n"
    f"The action is 'if hoist3 lift crate0 at distributor0'. Based on the domain description, this action is executable. After executing this action, the sates of all objects are: Crate0: at distributor0, not clear, held by hoist3. Crate1: at depot2, on top of pallet2, has crate2 on it. Crate2: at depot2, on top of crate1, has crate3 on it. Crate3: at depot2, on top of crate2, clear. Hoist0: at depot0, available. Hoist1: at depot1, available. Hoist2: at depot2, available. Hoist3: at distributor0, holding crate0, unavailable. Hoist4: at distributor1, available. Hoist5: at distributor2, available. Truck0: at distributor0, has no crate in it. Truck1: at depot1, has no crate in it. Truck2: at depot0, has no crate in it. Pallet0: at depot0, clear. Pallet1: at depot1, clear. Pallet2: at depot2, has crate1 on it. Pallet3: at distributor0, clear. Pallet4: distributor1, clear. Pallet5: distributor2, clear. \n"
    f"Then, we compare each proposition in the question one by one.\n"
    f"Crate0 is held by hoist3 ::: Crate0: at distributor0, not clear, held by hoist3. ===> MATCH\n"
    f"truck0 is at distributor0 ::: Truck0: at distributor0, has no crate in it. ===> MATCH\n"
    f"Since all propositions match with the current state, the question is true.\n"
    f"Final Answer: True.\n"
    f"——————\n"
)


TWOSHOTCOT_AE_DEPOTS_EXAMPLE = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"Current state: Crate0 is at depot0, on pallet0, and clear. Crate1 is at depot2, on pallet2, and clear. Crate2 is at depot1, on pallet1, and not clear (crate3 on top). Crate3 is at depot1, on crate2, and clear. Hoist0 is at depot0 and available. Hoist1 is at depot1 and available. Hoist2 is at depot2 and available. Pallet0 is at depot0 and has crate0. Pallet1 is at depot1 and has crate2 (with crate3 on top). Pallet2 is at depot2 and has crate1. Truck0 is at depot2. Truck1 is at depot1.\n"
    f"Question: Given the initial condition, the following action is planned to be performed: at depot2, hoist2 lifts crate1 from pallet2. Is it possible to execute it, True or False?\n"
    f"Answer: \n"
    f"Step 1: we can confirm whether this action is executable or not by checking the initial state.\n"
    f"A hoist can lift a crate from a pallet only if following preconditions are satisfied: the hoist is available, the crate is clear, and the crate is on the pallet. We can see Hoist2 is at depot2 and available,  Crate1 is at depot2, on pallet2, and clear. So this action is executable.\n"
    f"Step 2: we return the final answer based on the checking result.\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final Answer: True\n"
    f"---------------\n"
    f"(Example 2)\n"
    f"current state: Crate0 is at depot0, on pallet0, and clear. Crate1 is at depot2, on pallet2, and clear. Crate2 is at depot1, on pallet1, but not clear due to crate3 on top. Crate3 is at depot1, on crate2, and clear. Hoist0 is at depot0 and available. Hoist1 is at depot1 and available. Hoist2 is at depot2 and available. Pallet0 is at depot0 and has crate0. Pallet1 is at depot1 and has crate2 with crate3 on top. Pallet2 is at depot2 and has crate1. Truck0 is at depot1. Truck1 is at depot0.\n"
    f"Question: Given the initial condition, the following action is planned to be performed: at depot1, hoist1 lifts crate2 from pallet1. Is it possible to execute it, True or False?\n"
    f"Answer: \n"
    f"Step 1: we can confirm whether this action is executable or not by checking the initial state.\n"
    f"A hoist can lift a crate from a pallet only if the following preconditions are satisfied: the hoist is available, the crate is clear, and the crate is on the pallet.  We can see Hoist1 is at depot1 and available. Crate2 is at depot1, on pallet1, but it is not clear because Crate3 is on top of it. So, this action is **not executable\n"
    f"Step 2: we return the final answer based on the checking result.\n"
    f"Since one or more preconditions are violated (specifically, the crate is not clear), the action cannot be performed.\n" 
    f"Final Answer: False.\n"
    f"---------------\n"
)


TWOSHOTCOT_STATE_DEPOTS_EXAMPLE = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"Current state: Crate0 is on top of pallet5, crate1 is at distributor2, crate1 is clear of any crates, crate1 is on top of crate0, crate2 is clear of any crates, crate2 is located at depot0, crate2 is on pallet0, crate3 is clear, crate3 is located at depot2, depot1 is where truck1 is located, distributor0 is where hoist3 is located, distributor1 is where pallet4 is located, distributor2 is where crate0 is located, distributor2 is where pallet5 is located, hoist0 is at depot0, hoist0 is available for work, hoist1 can be found located at depot1, hoist1 is available for work, hoist2 is available, hoist2 is located at depot2, hoist3 is accessible, hoist4 is available for work, hoist4 is located at distributor1, hoist5 is available, hoist5 is located at distributor2, hoist6 is available, hoist6 is located at distributor3, pallet0 is located at depot0, pallet1 can be found located at depot1, pallet1 is clear, pallet2 has crate3 on it, pallet2 is at depot2, pallet3 can be found located at distributor0, pallet3 is clear of any crates, pallet4 is clear, pallet6 is clear, pallet6 is located at distributor3, truck0 is located at distributor2 and truck2 is located at depot2.\n"
    f"Question: Given the initial condition, the following action is performed: truck2 is driven to depot1 from depot2. In this state, if at depot1, hoist1 lifts crate3 off pallet2, is it True or False that crate3 is no longer at depot1, crate3 is no longer on pallet2, and hoist1 is lifting crate3?\n"
    f"Answer: \n"
    f"Step 1: We first execute the action and get the new state.\n"
    f"After taking the action truck2 is driven to depot1 from depot2, the truck is at depot1. If at depot1, hoist1 lifts crate3 off pallet2, crate3 is no longer at depot1, crate3 is no longer on pallet2, and hoist1 is lifting crate3.\n"
    f"Step 2: Then, we compare the state and the question and get the answer.\n"
    f"is it True or False that crate3 is no longer at depot1, crate3 is no longer on pallet2, and hoist1 is lifting crate3? We can see crate is being lifted by hoist1, and crate3 is not at depot1, crate3 is not on pallet2.\n"
    f"So the question is true\n"
    f"Final Answer: True.\n"
    f"---------------\n"
    f"(Example 2)\n"
    f"Current state: Crate0 is on top of pallet5, crate1 is at distributor2, crate1 is clear of any crates, crate1 is on top of crate0, crate2 is clear of any crates, crate2 is located at depot0, crate2 is on pallet0, crate3 is clear, crate3 is located at depot2, depot1 is where truck1 is located, distributor0 is where hoist3 is located, distributor1 is where pallet4 is located, distributor2 is where crate0 is located, distributor2 is where pallet5 is located, hoist0 is at depot0, hoist0 is available for work, hoist1 can be found located at depot1, hoist1 is available for work, hoist2 is available, hoist2 is located at depot2, hoist3 is accessible, hoist4 is available for work, hoist4 is located at distributor1, hoist5 is available, hoist5 is located at distributor2, hoist6 is available, hoist6 is located at distributor3, pallet0 is located at depot0, pallet1 can be found located at depot1, pallet1 is clear, pallet2 has crate3 on it, pallet2 is at depot2, pallet3 can be found located at distributor0, pallet3 is clear of any crates, pallet4 is clear, pallet6 is clear, pallet6 is located at distributor3, truck0 is located at distributor2 and truck2 is located at depot2.\n"
    f"Question: Given the initial condition, the following action is performed: truck0 is driven to distributor2 from depot1. In this state, if at distributor2, hoist5 lifts crate1 off pallet5, is it True or False that crate1 is no longer at distributor2, truck0 is at depot0?\n"
    f"Answer: \n"
    f"Step 1: We first execute the action and get the new state.\n"
    f"After taking the action truck0 is driven to distributor2 from depot1, truck0 is at distributor2. If at distributor2, hoist5 lifts crate1 off pallet5, the crate1 is held by hoist5, and crate1 is not on pallet5. \n"
    f"Step 2: Then, we compare the state and the question and get the answer.\n"
    f"crate1 is no longer at distributor2, truck0 is at depot0? We can see crate1 is being held by hoist5, so crate1 is not at distributor2, and truck0 is at distributor2, not depot0\n"
    f"So the question is false.\n"
    f"Final Answer: False."
    f"---------------\n"
)



#----------------------------------------
#Drivelog Domain
#----------------------------------------
DRIVERLOG_DOMAIN_DESCRIPTION = (
    f"[Domain Description]\n"
    f"The Drivelog domain involves driver, truck, package, and location. Driver, package and truck's locations can be changed but the links/paths between two locations are fixed. A truck can carry more than one packages at a time, a driver can only drive one truck at a time. There are two types of connections between locations: links, which can only be used by driving a truck, and paths, which can only be used by a driver walking on foot.\n"

    f"Different properties are used to describe current states of different objects. For package we use: at location_x/in truck_x. For truck we use: at location_x, has package_x in it/has no package in it, driven by driver_x/has no driver on it. For driver we use: at location_x/driving truck_x.\n"

    f"Following actions are executable only if all preconditions are met, if any condition are not satisfied, the action is not executable.\n"

    f"A package can be loaded into a truck at the location. This action is executable only if all following preconditions are satisfied: the truck and the package are both at the location.\n"
    
    f"A package can be unloaded from a truck at the location. This action is executable only if all following preconditions are satisfied: the truck is at the location, the package is in the truck.\n"
    
    f"A driver can board a truck at the location. This action is executable only if all following preconditions are satisfied: the truck and the driver at both at the location, the truck has no driver on it.\n"
    
    f"A driver can disembark a truck at the location. This action is executable only if all following preconditions are satisfied: the truck is at the location, the driver is driving the truck.\n"
    
    f"A driver can drive a truck from location A to location B. This action is executable only if all following preconditions are satisfied: the truck is at the location, the truck has driver on it(the driver is driving the truck), there is a link betweenlocation A and B.\n"
    
    f"A driver can walk from location A to location B. This action is executable only if all following preconditions are satisfied: the driver is at location A, there is path between location A and B.\n"
    
    f"Executing an action will change states of related objects.\n"

    f"A package can be loaded into a truck at the location. This action will result in: the package is not at the location, the package is in the truck.\n"
    
    f"A package can be unloaded from a truck at the location. This action will result in: the package is not in the truck, the package is at the location.\n"
    
    f"A driver can board a truck at the location. This action will result in: the driver is not at the location, the driver is drving the truck, the truck has the driver on it.\n"
    
    f"A driver can disembark a truck at the location. This action will result in: the driver is at the location, the truck has no driver on it.\n"
    
    f"A driver can drive a truck from location A to location B. This action will result in: the truck is at location B(the truck is not at location A).\n"
    
    f"A driver can walk from location A to location B. This action will result in: the driver is at location B(the driver is not at location A).\n"

)


INITIAL_STATE_EXTRACTOR_DRIVERLOG_PROMPT = f"This is initial states of all objects of drivelog domain, you are required to extract states of all objects, including driver, truck, package and connectivity(link and path) between locations. Your answer must satisfy all the following requirements. First, think and respond with the format from the example above, including the word choice and paragraph structure. Second, each object's state should contain all properties mentioned in the domain description above. Besides, don't use any markdown formatting."


INITIAL_STATE_EXTRACTOR_DRIVERLOG_EXAMPLE = (
    f"[Examples]\n"
    f"Initial state exmaple 1: Driver1 is at location s1, driver2 is present at location s3, driver3 is present at location s3, locations p0_1 and s1 have a path between them, locations p1_2 and s2 have a path between them, locations p3_0 and s3 have a path between them, locations s0 and p0_1 have a path between them, locations s0 and s1 have a link between them, locations s0 and s3 have a link between them, locations s1 and p1_2 have a path between them, locations s1 and s2 have a link between them, locations s3 and s0 have a link between them, locations s3 and s1 have a link between them, package1 is currently at location s3, package2 is present at location s2, package3 is currently at location s2, package4 is currently at location s1, there exists a link between the locations s0 and s2, there exists a link between the locations s1 and s3, there exists a link between the locations s2 and s1, there exists a path between the locations p1_2 and s1, there exists a path between the locations p1_3 and s3, there exists a path between the locations s2 and p1_2, there is a link between location s1 and location s0, there is a link between location s2 and location s0, there is a path between location p0_1 and location s0, there is a path between location p1_3 and location s1, there is a path between location p2_0 and location s0, there is a path between location p2_0 and location s2, there is a path between location p3_0 and location s0, there is a path between location s0 and location p2_0, there is a path between location s0 and location p3_0, there is a path between location s1 and location p0_1, there is a path between location s1 and location p1_3, there is a path between location s2 and location p2_0, there is a path between location s3 and location p1_3, there is a path between location s3 and location p3_0, truck1 is currently at location s0, truck1 is empty, truck2 contains nothing, truck2 is at location s3, truck3 contains nothing and truck3 is present at location s0.\n"
    f"Answer 1:\n"
    f"In order to extract initial states of objects, we first need to confirm how many objects and how many locations are mentioned in the initial state.\n"
    f"We can find following objects in the intial state description: driver1, driver2, package1, package2, package3, package4, truck1, truck2. truck3. We can find following locations in the intial state description: p0_1, p1_2, p1_3, p2_0, p4_0, s0, s1, s2, s3.\n"
    f"Then, we find all descriptions related to an object, and organize then into the required format. Repeat this process until all objects' states are extracted, and each object's state contains all related properties.\n"
    
    f"Driver1 is at location s1, driver2 is present at location s3,driver3 is present at location s3, ::: Driver1: at s1. Driver2: at s3. Driver3: at s3.\n"
    f"package1 is currently at location s3,  package2 is present at location s2,  package3 is currently at location s2,  package4 is currently at location s1, ::: Package1: at s3, Package2: at s2, Package3: at s2, Package4: at s1.\n"
    f"truck1 is currently at location s0, truck1 is empty, truck2 contains nothing, truck2 is at location s3, truck3 contains nothing and truck3 is present at location s0.\",  ::: Truck1: at s0, has no driver on it, has no package in it. Truck2: at s3, has no driver on it, has no package in it. Truck3: at s0, has no driver on it, has no package in it.\n"
    f"locations p0_1 and s1 have a path between them, there is a path between location p0_1 and location s0,  ::: p0_1: has a path with s0, has a path with s1.\n"
    f"locations p1_2 and s2 have a path between them, there exists a path between the locations p1_2 and s1 ::: p1_2: has a path with s1, has a path with s2.\n"
    f"there exists a path between the locations p1_3 and s3, there is a path between location p1_3 and location s1 ::: p1_3: has a path with s1, has a path with s3.\n"
    f"there is a path between location p2_0 and location s0, there is a path between location p2_0 and location s2, ::: p2_0: has a path with s0, has a path with s2.\n"
    f"locations p3_0 and s3 have a path between them, there is a path between location p3_0 and location s0, ::: p3_0: has a path with s0, has a path with s3.\n"
    f"locations s0 and p0_1 have a path between them,  there is a path between location s0 and location p2_0, there is a path between location s0 and location p3_0, locations s0 and s1 have a link between them, there is a link between location s2 and location s0, locations s0 and s3 have a link between them, ::: s0: has a path with p0_1, has a path with p2_0, has a path with p3_0, has a link with s1, has a link with s2, has a link with s3.\n"
    f"there is a path between location s1 and location p0_1, locations s1 and p1_2 have a path between them, there is a path between location s1 and location p1_3, there is a link between location s1 and location s0, locations s1 and s2 have a link between them, there exists a link between the locations s1 and s3, ::: s1: has a path with p0_1, has a path with p1_2, has a path with p1_3, has a link with s0, has a link with s2, has a link with s3.\n"
    f"there exists a path between the locations s2 and p1_2, there is a path between location s2 and location p2_0, there exists a link between the locations s2 and s1, there is a link between location s2 and location s0. ::: s2: has a path with p1_2, has a path with p2_0, has a link with s0, has a link with s1.\n"
    f"there is a path between location s3 and location p1_3, there is a path between location s3 and location p3_0, locations s3 and s0 have a link between them, locations s3 and s1 have a link between them, ::: s3: has a path with p1_3, has a path with p3_0, has a link with s0, has a link with s1.\n"
    
    f"After extracting all objects' state, organize all objects' states  into a new paragraph as the end of answer.\n"
    f"Driver1: at s1. Driver2: at s3. Driver3: at s3. Package1: at s3, Package2: at s2, Package3: at s2, Package4: at s1. Truck1: at s0, has no driver on it, has no package on it. Truck2: at s3, has no driver on it, has no package on it. Truck3: at s0, has no driver on it, has no package on it. p0_1: has a path with s0, has a path with s1. p1_2: has a path with s1, has a path with s2. p1_3: has a path with s1, has a path with s3. p2_0: has a path with s0, has a path with s2. p3_0: has a path with s0, has a path with s3. s0: has a path with p0_1, has a path with p2_0, has a path with p3_0, has a link with s1, has a link with s2, has a link with s3. s1: has a path with p0_1, has a path with p1_2, has a path with p1_3, has a link with s0, has a link with s2, has a link with s3. s2: has a path with p1_2, has a path with p2_0, has a link with s0, has a link with s1. s3: has a path with p1_3, has a path with p3_0, has a link with s0, has a link with s1. \n"
    f"------------"
)


QUESTION_EXTRACTOR_DRIVERLOG_EXAMPLE = (
    f"[Examples]\n"
    f"Plan1: Given the initial condition, the following actions are performed: truck1 is boarded by driver3 at location s0, truck1 is loaded with package3 at location s0, at location s0, package1 is loaded in truck1, driver3 drives truck1 from location s0 to location s3, package1 is unloaded from truck1 at location s3, driver3 drives truck1 from location s3 to location s1, driver3 disembarks from truck1 at location s1, at location s1, package3 is unloaded in truck1, package2 is loaded in truck2 at location s2 and driver1 walks to location p3_0 from location s3 to reach the current state. In this state, if driver1 walks from location p3_0 to location s0, is it True or False that package2 is not in truck1?\n"

    f"Question extracted from plan1: In this state, if driver1 walks from location p3_0 to location s0, is it True or False that package2 is not in truck1?\n"

    f"Plan2: Given the initial condition, the following actions are performed: driver1 walks to location p4_3 from location s3, driver1 walks to location s4 from location p4_3, driver1 walks to location p4_1 from location s4, driver1 walks from location p4_1 to location s1, at location s1, driver1 boards truck1, driver1 drives truck1 to location s0 from location s1, package4 is loaded in truck1 at location s0, driver1 drives truck1 to location s2 from location s0, truck1 is loaded with package2 at location s2, package1 is loaded in truck1 at location s2, truck1 is driven from location s2 to s3 by driver1, at location s3, package3 is loaded in truck1, truck1 is unloaded with package1 at location s3, driver1 drives truck1 from location s3 to location s4, at location s4, package4 is unloaded in truck1, truck1 is unloaded with package3 at location s4, package2 is unloaded from truck1 at location s4, driver1 drives truck1 to location s1 from location s4 and driver1 disembarks from truck1 at location s1 to reach the current state. In this state, are all of the following valid properties of the state that do not involve negations? driver1 is at location s1, driver2 is present at location s4, driver3 is present at location s3, locations p4_0 and s4 have a path between them, locations p4_1 and s4 have a path between them, locations s0 and p4_0 have a path between them, locations s0 and s1 have a link between them, locations s0 and s4 have a link between them, locations s0 and s5 have a link between them, locations s1 and s2 have a link between them, locations s2 and p5_2 have a path between them, locations s2 and s0 have a link between them, locations s2 and s3 have a link between them, locations s3 and s4 have a link between them, locations s4 and s1 have a link between them, locations s4 and s3 have a link between them, locations s5 and p0_5 have a path between them, package1 is present at location s3, package2 is currently at location s4, package3 is currently at location s4, package4 is currently at location s4, there exists a link between the locations s0 and s2, there exists a link between the locations s1 and s0, there exists a link between the locations s1 and s4, there exists a link between the locations s2 and s1, there exists a link between the locations s4 and s0, there exists a link between the locations s4 and s5, there exists a link between the locations s5 and s2, there exists a link between the locations s5 and s4, there exists a path between the locations p0_5 and s0, there exists a path between the locations p4_3 and s3, there exists a path between the locations p5_2 and s2, there exists a path between the locations s0 and p0_5, there exists a path between the locations s3 and p4_3, there exists a path between the locations s4 and p4_0, there is a link between location s2 and location s5, there is a link between location s3 and location s2, there is a link between location s3 and location s5, there is a link between location s5 and location s0, there is a link between location s5 and location s3, there is a path between location p0_5 and location s5, there is a path between location p4_0 and location s0, there is a path between location p4_1 and location s1, there is a path between location p4_3 and location s4, there is a path between location p5_2 and location s5, there is a path between location s1 and location p4_1, there is a path between location s4 and location p4_1, there is a path between location s4 and location p4_3, there is a path between location s5 and location p5_2, truck1 is currently at location s1, truck1 is empty, truck2 contains nothing and truck2 is currently at location s5. Respond with True or False.\n"

    f"Question extracted from plan2: In this state, are all of the following valid properties of the state that do not involve negations? driver1 is at location s1, driver2 is present at location s4, driver3 is present at location s3, locations p4_0 and s4 have a path between them, locations p4_1 and s4 have a path between them, locations s0 and p4_0 have a path between them, locations s0 and s1 have a link between them, locations s0 and s4 have a link between them, locations s0 and s5 have a link between them, locations s1 and s2 have a link between them, locations s2 and p5_2 have a path between them, locations s2 and s0 have a link between them, locations s2 and s3 have a link between them, locations s3 and s4 have a link between them, locations s4 and s1 have a link between them, locations s4 and s3 have a link between them, locations s5 and p0_5 have a path between them, package1 is present at location s3, package2 is currently at location s4, package3 is currently at location s4, package4 is currently at location s4, there exists a link between the locations s0 and s2, there exists a link between the locations s1 and s0, there exists a link between the locations s1 and s4, there exists a link between the locations s2 and s1, there exists a link between the locations s4 and s0, there exists a link between the locations s4 and s5, there exists a link between the locations s5 and s2, there exists a link between the locations s5 and s4, there exists a path between the locations p0_5 and s0, there exists a path between the locations p4_3 and s3, there exists a path between the locations p5_2 and s2, there exists a path between the locations s0 and p0_5, there exists a path between the locations s3 and p4_3, there exists a path between the locations s4 and p4_0, there is a link between location s2 and location s5, there is a link between location s3 and location s2, there is a link between location s3 and location s5, there is a link between location s5 and location s0, there is a link between location s5 and location s3, there is a path between location p0_5 and location s5, there is a path between location p4_0 and location s0, there is a path between location p4_1 and location s1, there is a path between location p4_3 and location s4, there is a path between location p5_2 and location s5, there is a path between location s1 and location p4_1, there is a path between location s4 and location p4_1, there is a path between location s4 and location p4_3, there is a path between location s5 and location p5_2, truck1 is currently at location s1, truck1 is empty, truck2 contains nothing and truck2 is currently at location s5. Respond with True or False.\n"

    f"Plan3: Given the initial condition, the following actions are performed: driver1 walks from location s3 to location p4_3, driver1 walks from location p4_3 to location s4, driver1 walks from location s4 to p4_1, driver1 walks from location p4_1 to location s1, truck1 is boarded by driver1 at location s1, truck1 is driven from location s1 to s0 by driver1, package4 is loaded in truck1 at location s0, driver1 drives truck1 to location s2 from location s0, at location s2, package2 is loaded in truck1 and at location s2, package1 is loaded in truck1 to reach the current state. In this state, is the number of valid properties of the state that involve negations equal to 283? True or False.\n"

    f"Question extracted from plan3: In this state, is the number of valid properties of the state that involve negations equal to 283? True or False.\n"
)


ACTION_TAKER_DRIVERLOG_PROMPT = ( 
    f"Based on the domain description and examples above, take the action and return the new state of all objects. Your answer must satisfy all the following requirements. First, think and respond like examples above, you are required to return states of all objects(truck, driver and package) and connection information(link and path) between locations, including states that are not effected by the action. Second, each object's state must contain all properties mentioned in the domain description above. Third, after your analysis, please return states of all objects into a new paragraph as the end of your answer. Your final paragraph should use the format like: \"Driver0: at location0. Package1: at location0.\" Besides, don't use any markdown formatting."

)



ACTION_TAKER_DRIVERLOG_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: Driver1: at s3. Driver2: at s4. Driver3: at s3. Package1: in truck1. Package2: in truck 1. Package3: at s1. Package4: at s0. Truck1: at s1, has package1 in it, has package2 in it. Truck2: at s5, has no driver on it, has no package in it. p0_5: has a path with s0, has a path with s5. p4_0: has a path with s0, has a path with s4. p4_1: has a path with s1, has a path with s4. p4_3: has a path with s3, has a path with s4. p5_2: has a path with s2, has a path with s5. s0: has a path with p0_5, has a path with p4_0, has a link with s1, has a link with s2, has a link with s4, has a link with s5. s1: has a path with p4_1, has a link with s0, has a link with s2, has a link with s4. s2: has a path with p5_2, has a link with s0, has a link with s1, has a link with s3, has a link with s5. s3: has a path with p4_3, has a link with s2, has a link with s4, has a link with s5. s4: has a path with p4_0, has a path with p4_1, has a path with p4_3, has a link with s0, has a link with s1, has a link with s3, has a link with s5. s5: has a path with p0_5, has a path with p5_2, has a link with s0, has a link with s2, has a link with s3, has a link with s4.\n"
    f"Action 1: At s1, truck1 is loaded with package3.\n"
    f"Answer 1:\n"
    f"Based on the current state and the domain description, we first find states of objects related to this action, then we can take the action and return new states of all objects.\n"
    f"Package3: at s1. Truck1: at s1, has package1 in it, has package2 in it.\n"
    f"Based on the domain description, a package can be loaded into a truck at the location. This action will result in: the package is not at the location, the package is in the truck.\n"
    f"the package is not at the location, the package is in the truck. ::: Package3: in truck1. Truck1: at s1, has package1 in it, has package2 in it, has package3 on it.\n" 
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into a new paragraph as the end of answer.\n"
    f"Driver1: at s3. Driver2: at s4. Driver3: at s3. Package1: in truck1. Package2: in truck 1. Package3: in truck1. Package4: at s0. Truck1: at s1, has package1 in it, has package2 in it, has package3 in it. Truck2: at s5, has no driver on it, has no package in it. p0_5: has a path with s0, has a path with s5. p4_0: has a path with s0, has a path with s4. p4_1: has a path with s1, has a path with s4. p4_3: has a path with s3, has a path with s4. p5_2: has a path with s2, has a path with s5. s0: has a path with p0_5, has a path with p4_0, has a link with s1, has a link with s2, has a link with s4, has a link with s5. s1: has a path with p4_1, has a link with s0, has a link with s2, has a link with s4. s2: has a path with p5_2, has a link with s0, has a link with s1, has a link with s3, has a link with s5. s3: has a path with p4_3, has a link with s2, has a link with s4, has a link with s5. s4: has a path with p4_0, has a path with p4_1, has a path with p4_3, has a link with s0, has a link with s1, has a link with s3, has a link with s5. s5: has a path with p0_5, has a path with p5_2, has a link with s0, has a link with s2, has a link with s3, has a link with s4.\n"
    f"------------\n"
    f"Current state example 2: Driver1: at s3. Driver2: at s3. Driver3: at s0. Package1: at s0, Package2: at s2, Package3: at s0. Truck1: at s0, has no driver on it, has no package in it. Truck2: at s2, has no driver on it, has no package in it. p0_1: has a path with s0. p1_2: has a path with s1, has a path with s2. p1_3: has a path with s1, has a path with s3. p2_0: has a path with s0, has a path with s2. p3_0: has a path with s0, has a path with s3. s0: has a path with p0_1, has a path with p2_0, has a path with p3_0, has a link with s2, has a link with s3. s1: has a path with p0_1, has a path with p1_2, has a path with p1_3, has a link with s2, has a link with s3. s2: has a path with p1_2, has a path with p2_0, has a link with s0, has a link with s1, has a link with s3. s3: has a path with p1_3, has a path with p3_0, has a link with s0, has a link with s1, has a link with s2.\n"
    f"Action 2: at location s0, driver3 boards truck1.\n"
    f"Answer 2:\n"
    f"Based on the current state and the domain description, we first find states of objects related to this action, then we can take the action and return new states of all objects.\n"
    f"Driver3: at s0. Truck1: at s0, has no driver on it, has no package in it.\n"
    f"Based on domain description, a driver can board a truck at the location. This action will result in: the driver is not at the location, the driver is drving the truck, the truck has the driver on it.\n"
    f"the driver is not at the location, the driver is drving the truck ::: Driver3: driving truck1.\n"
    f"the truck has the driver on it. ::: Truck1: at s0, driven by driver3, has no package in it.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into a new paragraph as the end of answer.\n"
    f"Driver1: at s3. Driver2: at s3. Driver3: driving truck1. Package1: at s0. Package2: at s2. Package3: at s0. Truck1: at s0, driven by driver3, has no package in it. Truck2: at s2, has no driver on it, has no package in it. p0_1: has a path with s0. p1_2: has a path with s1, has a path with s2. p1_3: has a path with s1, has a path with s3. p2_0: has a path with s0, has a path with s2. p3_0: has a path with s0, has a path with s3. s0: has a path with p0_1, has a path with p2_0, has a path with p3_0, has a link with s2, has a link with s3. s1: has a path with p0_1, has a path with p1_2, has a path with p1_3, has a link with s2, has a link with s3. s2: has a path with p1_2, has a path with p2_0, has a link with s0, has a link with s1, has a link with s3. s3: has a path with p1_3, has a path with p3_0, has a link with s0, has a link with s1, has a link with s2.\n"
    f"------------\n"
)


EXECUTABILITY_CHECKER_DRIVERLOG_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: Driver1: at s3. Driver2: at s3. Driver3: at s0. Package1: at s0, Package2: at s2, Package3: at s0. Truck1: at s0, has no driver on it, has no package in it. Truck2: at s2, has no driver on it, has no package in it. p0_1: has a path with s0. p1_2: has a path with s1, has a path with s2. p1_3: has a path with s1, has a path with s3. p2_0: has a path with s0, has a path with s2. p3_0: has a path with s0, has a path with s3. s0: has a path with p0_1, has a path with p2_0, has a path with p3_0, has a link with s2, has a link with s3. s1: has a path with p0_1, has a path with p1_2, has a path with p1_3, has a link with s2, has a link with s3. s2: has a path with p1_2, has a path with p2_0, has a link with s0, has a link with s1, has a link with s3. s3: has a path with p1_3, has a path with p3_0, has a link with s0, has a link with s1, has a link with s2.\n"
    f"Action 1: Truck2 is driven from location s3 to p2_1 by driver2.\n"
    f"Answer 1:\n"
    f"In order to check whether this action is executable or not, we first need to find states of objects related to this action, then check whether all preconditions of this action are satisfied.\n"
    f"Truck2: at s2, has no driver on it, has no package in it. Driver2: at s3.\n"
    f"Based on the domain description, a driver can drive a truck from location A to location B. This action is executable only if all following preconditions are satisfied: the truck is at the location, the truck has driver on it(the driver is driving the truck), there is a link betweenlocation A and B.\n"
    f"the truck is at the location, the truck has driver on it(the driver is driving the truck) ::: Truck2: at s2, has no driver on it, has no package in it. ===> NOT SATISFY\n"
    f"Since not all preconditions are satisfied, the action is not executable.\n"
    f"Final answer: False.\n"
    f"------------\n"
    f"Current state example 2: Driver1: at s3. Driver2: at s3. Driver3: at s0. Package1: at s0. Package2: at s2. Package3: at s0. Truck1: at s0, has no driver on it, has no package in it. Truck2: at s2, has no driver on it, has no package in it. p0_1: has a path with s0. p2_0: has a path with s0, has a path with s2. p3_0: has a path with s0, has a path with s3. s0: has a path with p0_1, has a path with p2_0, has a path with p3_0, has a link with s2. s1: has a path with p0_1. p1_2: has a path with s1, has a path with s2. p1_3: has a path with s1, has a path with s3. s2: has a path with p2_0, has a path with p1_2, has a link with s0, has a link with s3. s3: has a path with p3_0, has a path with p1_3, has a link with s0, has a link with s1, has a link with s2.\n"
    f"Action 2: Truck1 is boarded by driver3 at location s0.\n"
    f"Answer 2:\n"
    f"In order to check whether this action is executable or not, we first need to find states of objects related to this action, then check whether all preconditions of this action are satisfied.\n"
    f"Driver3: at s0. Truck1: at s0, has no driver on it, has no package in it.\n"
    f"Based on the domain description, A driver can board a truck at the location. This action is executable only if all following preconditions are satisfied: the truck and the driver at both at the location, the truck has no driver on it.\n"
    f"the truck and the driver at both at the location ::: Driver3: at s0. Truck1: at s0 ===> SATISFY\n"
    f"the truck has no driver on it. Truck1: at s0, has no driver on it, has no package in it. ===>SATISFY\n"
    f"Since all preconditions are satisfied, the action is executable.\n"
    f"Final answer: True.\n"
    f"------------\n"
)


STATE_CHECKER_DRIVERLOG_EXAMPLE = (
    f"[Example1]\n"
    f"Current State example 1: Driver1: at location s2. Driver2: at location s2. Package1: at location s1. Package2: at location s2. Package3: at location s0. Package4: at location s2. Truck1: at location s0, has no package in it, has no driver on it. Truck2: at location s0, has no package in it, has no driver on it. p0_1: has a path with s0, has a path with s1. p0_2: has a path with s0, has a path with s2. p0_3: has a path with s3, has a path with s0. p1_3: has a path with s3, has a path with s1. p2_1: has a path with s2, has a path with s1. s0: has a path with p0_1, has a path with p0_2, has a path with p0_3, has a link with s2, has a link with s3, has a link with s1. s1: has a path with p0_1, has a path with p1_3, has a path with p2_1, has a link with s0, has a link with s2, has a link with s3. s2: has a path with p0_2, has a path with p2_1, has a link with s0, has a link with s1, has a link with s3. s3: has a path with p0_3, has a path with p1_3, has a link with s0, has a link with s1, has a link with s2.\n"
    f"Question 1: In this state, if package3 is loaded into truck1 at location s0 to reach the current state, are following properties true or false? truck 1 is at location s0, driver1 is at location s2, s2 has a path with p0_2, s2 has a path with p2_1, s2 has a path with p1_3.\n"
    f"Answer 1:"
    f"Because the question contains one action, we should first take the action and get new states of all objects. After taking the action, we should return states of all objects, including states that are not effected by the action.\n"
    f"The action is 'package3 is loaded into truck1 at location s0'. Based on the domain description, this action is executable. After taking the action, the curremt states of all objects should be:  Driver1: at location s2. Driver2: at location s2. Package1: at location s1. Package2: at location s2. Package3: in truck1. Package4: at location s2. Truck1: at location s0, has package3 in it, has no driver on it. Truck2: at location s0, has no package in it, has no driver on it. p0_1: has a path with s0, has a path with s1. p0_2: has a path with s0, has a path with s2. p0_3: has a path with s3, has a path with s0. p1_3: has a path with s3, has a path with s1. p2_1: has a path with s2, has a path with s1. s0: has a path with p0_1, has a path with p0_2, has a path with p0_3, has a link with s2, has a link with s3, has a link with s1. s1: has a path with p0_1, has a path with p1_3, has a path with p2_1, has a link with s0, has a link with s2, has a link with s3. s2: has a path with p0_2, has a path with p2_1, has a link with s0, has a link with s1, has a link with s3. s3: has a path with p0_3, has a path with p1_3, has a link with s0, has a link with s1, has a link with s2.\n"
    f"Then, we compare every proposition in the question one by one.\n"
    f"truck 1 is at location s0 ::: Truck1: at location s0, has package3 in it, has no driver on it.  ===> MATCH\n"
    f"driver1 is at location s2 :::  Driver1: at location s2.   ===> MATCH\n"
    f"s2 has a path with p0_2, s2 has a path with p2_1, s2 has a path with p1_3 ::: s2: has a path with p0_2, has a path with p2_1, has a link with s0, has a link with s1, has a link with s3.   ===> NOT MATCH\n"
    f"Since there is a proposition in the question doesn't match with the current state, the question is false.\n"
    f"Final Answer: False.\n"
    f"------------"
)




#----------------------
#Grippers Domain
#----------------------
GRIPPERS_DOMAIN_DESCRIPTION=(
    f"[Domain Description]\n"
    f"The grippers domain involves ball, robot, and room. A robot has a left gripper(written as lgripper) and a right gripper(written as rgripper), both grippers work indepentdently. Lgripper/rgripper can only holy holding a ball at a time. A robot can move between rooms freely. Ball is located at one room and can be picked up by a robot's left or right gripper. A ball is either in a room or being held by the robot's lgripper/rgripper.\n"
    
    f"Different properties are used to describe current states of different objects. For ball we use: at room_x, held by robot_x's lgripper_x/rgripper_x. For robot we use: at room_x, lgripper/rgripper is holding ball_x, lgripper/rgripper is free(available).\n"
    
    f"Following actions are executable only if all preconditions are met, if any condition are not satisfied, the action is not executable.\n"
    
    f"A robot can 'move' from room A to room B. This action is executable only if all following preconditions are satisfied: the robot is currently at room A.\n"
    
    f"A robot can 'pick' one ball at a room by its lgripper/rgripper. This action is executable only if all following preconditions are satisfied: the robot and the ball are both at the same room, the robot's lgripper/rgripper is free.\n"
    
    f"A robot's lgripper/rgripper can 'drop' a ball at a room. This action is executable only if all following preconditions are satisfied: the robot is at the room, the robot's lgripper/rgripper is holding the ball.\n"
    
    f"Executing an action will change states of related objects.\n"
    
    f"A robot 'move' from room A to room B will result in: the robot is at room B.\n"
    
    f"A robot 'pick' one ball at a room by its lgripper/rgripper will result in: the robot's lgripper/rgripper is holding the ball, the robot's lgripper/rgripper is not free, the ball is held by the robot's lgripper/rgripper, the ball is not at the room.\n"
    
    f"A robot's lgripper/rgripper 'drop' a ball at a room will result in: the robot's lgripper/rgripper is free, the robot's lgripper/rgripper is not holding the ball, the ball is at the room.\n"
)


INITIAL_STATE_EXTRACTOR_GRIPPERS_PROMPT =(
    f"This is a question related to the grippers domain. You are required to extract the initial state of every objects in this plan, including balls, and robots. Your answer must satisfy all the following requirements. First, think and respond with the format from the example above, including the word choice and paragraph structure. Second, each object's state should contain all properties mentioned in the domain description above. Besides, don't use any markdown formatting."  
)



INITIAL_STATE_EXTRACTOR_GRIPPERS_EXAMPLE = (
    f"[Examples]"
    f"Initial state example1: Ball1 is at room1, ball2 is located at room2, ball3 is located at room1, ball4 is located at room2, ball5 is present at room3, ball6 is at room1, ball7 is located at room4, robot1 is at room4, robot1's lgripper1 is available and robot1's rgripper1 is free.\n"
    f"Extracted from initial state example1: Ball1: at room1. Ball2: at room2. Ball3: at room1. Ball4: at room2. Ball5: at room3. Ball6: at room1. Ball7: at room4. Robot1: at room4, lgripper1 is free, rgripper1 is free.\n"
    f"------------"
    f"Initial state example2: Ball1 is located at room3, ball2 is at room3, ball3 is at room2, ball4 is present at room3, ball5 is present at room1, ball6 is at room1, ball7 is present at room3, robot1 is present in room2, robot1's lgripper1 is free, robot1's rgripper1 is free, robot2 is located at room2, robot2's lgripper2 is free and robot2's rgripper2 is free.\n"
    f"Extracted from initial state example2: Ball1: at room3. Ball2: at room3. Ball3: at room2. Ball4: at room3. Ball5: at room1. Ball6: at room1. Ball7: at room3. Robot1: at room2, lgripper1 is free, rgripper1 is free. Robot2: at room2, lgripper2 is free, rgripper2 is free.\n"
    f"------------"
    f"Initial state example3: Ball1 is at room1, ball2 is present at room2, ball3 is at room1, ball4 is present at room2, ball5 is present at room2, ball6 is at room1, ball7 is present at room3, robot1 is present in room4, robot1's lgripper1 is free and robot1's rgripper1 is free.\n"
    f"Extracted from initial state example3: Ball1: at room1. Ball2: at room2. Ball3: at room1. Ball4: at room2. Ball5: at room2. Ball6: at room1. Ball7: at room3. Robot1: at room4, lgripper1 is free, rgripper1 is free.\n"
)


QUESTION_EXTRACTOR_GRIPPERS_EXAMPLE = (
    f"[Examples]\n"
    
    f"Plan example1: Given the initial condition, the following actions are performed: from room4, robot1's lgripper1 picks up ball7, robot1 moves to room5 from room4, ball7 is dropped in room5 with lgripper1 by robot1, robot1 moves from room5 to room1, lgripper1 of robot1 picks up ball1 in room1, ball3 is picked from room1 with rgripper1 by robot1, from room1, robot1 moves to room5, in room5, robot1's lgripper1 drops ball1, ball3 is dropped in room5 with rgripper1 by robot1, robot1 moves from room5 to room2, ball2 is picked from room2 with lgripper1 by robot1, from room2, robot1's rgripper1 picks up ball4, robot1 moves from room2 to room1, rgripper1 of robot1 drops ball4 in room1, from room1, robot1's rgripper1 picks up ball6, robot1 moves to room3 from room1, ball6 is dropped in room3 with rgripper1 by robot1, from room3, robot1's rgripper1 picks up ball5 and robot1 moves from room3 to room6 to reach the current state.\n"
    
    f"Question extracted from plan example1: In this state, are all of the following valid properties of the state that involve negations? ball1 is being carried by robot1's lgripper1, ball1 is being carried by robot1's rgripper1, ball1 is located at room6, ball1 is not at room1, ball1 is not at room2, ball1 is not located at room4, ball1 is present at room3, ball2 is at room3, ball2 is at room4, ball2 is not at room5, ball2 is not located at room1, ball2 is not located at room2, ball2 is not located at room6, ball3 is located at room3, ball3 is not at room2, ball3 is not present at room1, ball3 is not present at room6, ball3 is present at room4, ball4 is located at room5, ball4 is not at room6, ball4 is not located at room4, ball4 is not present at room3, ball4 is present at room2, ball5 is at room1, ball5 is at room4, ball5 is at room5, ball5 is being carried by robot1's lgripper1, ball5 is located at room2, ball5 is not at room6, ball5 is not located at room3, ball6 is located at room5, ball6 is not at room6, ball6 is not located at room4, ball6 is not present at room2, ball6 is present at room1, ball7 is located at room3, ball7 is not at room6, ball7 is not being carried by robot1's lgripper1, ball7 is not located at room1, ball7 is not located at room4, ball7 is present at room2, lgripper1 of robot1 is carrying ball4, lgripper1 of robot1 is free, rgripper1 of robot1 is carrying ball2, rgripper1 of robot1 is carrying ball3, rgripper1 of robot1 is carrying ball7, robot1 is at room3, robot1 is carrying ball4 with rgripper1, robot1 is located at room4, robot1 is not at room1, robot1 is not at room2, robot1 is not at room5, robot1 is not carrying ball3 with lgripper1, robot1 is not carrying ball6 with lgripper1, robot1 is not carrying ball6 with rgripper1 and robot1's rgripper1 is available.\n"
    f"------------"
    f"Plan example2: Given the initial condition, the following actions are performed: robot1 moves to room1 from room4, from room1, robot1's lgripper1 picks up ball1, robot1 moves to room2 from room1, rgripper1 of robot1 picks up ball2 in room2, from room2, robot1 moves to room3, ball1 is dropped in room3 with lgripper1 by robot1, robot1 moves to room4 from room3, ball2 is dropped in room4 with rgripper1 by robot1, robot1 moves from room4 to room2, ball4 is picked from room2 with lgripper1 by robot1, rgripper1 of robot1 picks up ball5 in room2, robot1 moves from room2 to room5, lgripper1 of robot1 drops ball4 in room5, from room5, robot1 moves to room1, ball3 is picked from room1 with lgripper1 by robot1, in room1, robot1's rgripper1 drops ball5, from room1, robot1's rgripper1 picks up ball6, from room1, robot1 moves to room5 and in room5, robot1's lgripper1 drops ball3 to reach the current state.\n"
    
    f"Question extracted from plan example2: In this state, are all of the following valid properties of the state that do not involve negations? ball1 is located at room3, ball2 is present at room4, ball3 is located at room5, ball4 is located at room5, ball5 is located at room1, lgripper1 of robot1 is free, robot1 is carrying ball6 with rgripper1 and robot1 is located at room5.\n"
    f"------------"
    f"Plan example3: Given the initial condition, the following actions are performed: from room4, robot1 moves to room1, from room1, robot1's lgripper1 picks up ball1, robot1 moves from room1 to room2, rgripper1 of robot1 picks up ball2 in room2, robot1 moves to room3 from room2, lgripper1 of robot1 drops ball1 in room3, from room3, robot1 moves to room4, rgripper1 of robot1 drops ball2 in room4, robot1 moves to room2 from room4, from room2, robot1's lgripper1 picks up ball4, rgripper1 of robot1 picks up ball5 in room2, from room2, robot1 moves to room5, in room5, robot1's lgripper1 drops ball4, robot1 moves to room1 from room5, from room1, robot1's lgripper1 picks up ball3, ball5 is dropped in room1 with rgripper1 by robot1, rgripper1 of robot1 picks up ball6 in room1, robot1 moves to room5 from room1 and ball3 is dropped in room5 with lgripper1 by robot1 to reach the current state.\n"
    f"Question extracted from plan example3: In this state, if rgripper1 of robot1 drops ball6 in room5, is it True or False that ball6 is at room5?\n"
    f"------------"
)


ACTION_TAKER_GRIPPERS_PROMPT = (
    f"Based on the domain description and examples above, take the action and return the new state of all objects. Your answer must satisfy all the following requirements. First, think and respond like examples above, you are required to return states of all objects(balls and robots), including states that are not effected by the action. Second, each object's state must contain all properties mentioned in the domain description above. Third, after your analysis, please return states of all objects into a new paragraph as the end of your answer. Your final paragraph should use the format like: \"Ball7: at room3. Robot1: at room4, lgripper1 is free, rgripper1 is free. \" Besides, don't use any markdown formatting."
)



ACTION_TAKER_GRIPPERS_EXAMPLE = (
    f"[Examples]\n"
    
    f"Current state example 1: Ball1: at room1. Ball2: at room2. Ball3: at room1. Ball4: at room2. Ball5: at room3. Ball6: at room1. Ball7: at room4. Robot1: at room1, lgripper1 is free, rgripper1 is free.\n"
    f"Action 1: From room1, robot1 moves to room5.\n"
    f"Answer 1:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Robot1: at room1, lgripper1 is free, rgripper1 is free.\n"
    f"Based on the domain description, a robot can 'move' from room A to room B. This action will result in: the robot is at room B. If the robot's lgripper/rgripper is holding any ball, the ball's location will be also at room B.\n"
    f"the robot is at room B ::: Robot1: at room5, lgripper1 is free, rgripper1 is free.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into a new paragraph.\n"
    f"Robot1: at room5, lgripper1 is free, rgripper1 is free. Ball1: at room1. Ball2: at room2. Ball3: at room1. Ball4: at room2. Ball5: at room3. Ball6: at room1. Ball7: at room4.\n"
    
    f"——————\n"
    
    f"Current state example 2: Ball1: at room3. Ball2: at room3. Ball3: at room2. Ball4: at room3. Ball5: at room1. Ball6: at room1. Ball7: at room3. Robot1: at room3, lgripper1 is free, rgripper1 is free. Robot2: at room2, lgripper2 is free, rgripper2 is free.\n"
    f"Action 2: Lgripper1 of robot1 picks up ball7 in room3.\n"
    f"Answer 2:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Robot1: at room3, lgripper1 is free, rgripper1 is free. Ball7: at room3.\n"
    f"Based on the domain description, a robot 'pick' one ball at a room by its lgripper/rgripper. This action will result in: the robot's lgripper/rgripper is holding the ball, the ball is held by the robot's lgripper/rgripper, the ball is not at the room, the robot's lgripper/rgripper is not free.\n"
    f"the robot's lgripper/rgripper is holding the ball, the robot's lgripper/rgripper is not free. ::: Robot1: at room3, lgripper1 is not free, rgripper1 is free, lgripper is holding ball7.\n"
    f"the ball is held by the robot's lgripper/rgripper, the ball is not at the room. ::: Ball7: held by robot1's lgripper.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into a new paragraph.\n"
    f"Ball1: at room3. Ball2: at room3. Ball3: at room2. Ball4: at room3. Ball5: at room1. Ball6: at room1. Ball7: held by robot1's lgripper. Robot1: at room3, lgripper1 is not free, rgripper1 is free, lgripper is holding ball7. Robot2: at room2, lgripper2 is free, rgripper2 is free.\n"
    
    f"——————\n"
    
    f"Current state example 3: Ball1: held by robot1's lgripper1. Ball2: at room2. Ball3: at room1. Ball4: at room2. Ball5: at room3. Ball6: at room1. Ball7: at room4. Robot1: at room4, lgripper1 is not free, rgripper1 is free, lgripper1 is holding ball1.\n"
    
    f"Action 3: Ball1 is dropped in room4 with lgripper1 by robot1.\n"
    
    f"Answer 3:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Ball1: held by robot1's lgripper1. Robot1: at room4, lgripper1 is not free, rgripper1 is free, lgripper1 is holding ball1.\n"
    f"Based on the domain description, a robot's lgripper/rgripper can 'drop' a ball at a room. This action will result in: the robot's lgripper/rgripper is free, the robot's lgripper/rgripper is not holding the ball, the ball is at the room.\n"
    f"the robot's lgripper/rgripper is free, the robot's lgripper/rgripper is not holding the ball ::: Robot1: at room4, lgripper1 is free, rgripper1 is free.\n"
    f"the ball is at the room ::: Ball1: at room1.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into one paragraph.\n"
    f"Ball1: at room1. Ball2: at room2. Ball3: at room1. Ball4: at room2. Ball5: at room3. Ball6: at room1. Robot1: at room4, lgripper1 is free, rgripper1 is free.\n"
    
    f"——————\n"
)



EXECUTABILITY_CHECKER_GRIPPERS_EXAMPLE = (
    f"Current state example 1: Ball1: at room1. Ball2: at room2. Ball3: at room1. Ball4: at room2. Ball5: at room2. Ball6: at room1. Robot1: at room4, lgripper1 is free, rgripper1 is free.\n"
    f"Action 1: Robot1 moves from room4 to room1.\n"
    f"Answer 1:\n"
    f"In order to check whether this action is executable or not, we first need to find states of objects related to this action, then check whether all preconditions of this action are satisfied.\n"
    f"Robot1: at room4, lgripper1 is free, rgripper1 is free.\n"
    f"Based on the domain description, a robot can 'move' from room A to room B. This action is executable only if all following preconditions are satisfied: the robot is currently at room A.\n"
    f"the robot is currently at room A. ::: Robot1: at room4 ===> SATISFY\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final answer: True.\n"
    
    f"——————\n"
    
    f"Current state example 2: Ball1: at room1. Ball2: at room2. Ball3: at room1. Ball4: at room2. Ball5: at room3. Ball6: at room1. Ball7: at room4. Robot1: at room2, lgripper1 is free, rgripper1 is free.\n"
    f"Action 2: Robot1's lgripper1 picks up ball7 in room4.\n"
    f"Answer 2:\n"
    f"In order to check whether this action is executable or not, we first need to find states of objects related to this action, then check whether all preconditions of this action are satisfied.\n"
    f"Robot1: at room2, lgripper1 is free, rgripper1 is free. Ball7: at room4.\n"
    f"Based on the domain description, a robot can 'pick' one ball at a room by its lgripper/rgripper. This action is executable only if all following preconditions are satisfied: the robot and the ball are both at the same room, the robot's lgripper/rgripper is free.\n"
    f"the robot and the ball are both at the room ::: Robot1: at room2, Ball7: at room4 ===> NOT SATISFY\n"
    f"Since not all preconditions are satisfied, this action is not executable.\n"
    f"Final answer: False\n"
    
    f"——————\n"
    
    f"Current state example 3: Ball1: at room1. Ball2: at room2. Ball3: at room1. Ball4: held by robot1's rgripper1. Ball5: at room2. Ball6: at room1. Ball7: at room3. Robot1: at room4, lgripper1 is free, rgripper1 is not free, rgripper1 is holding ball4.\n"
    f"Action 3: Ball4 is dropped in room1 with rgripper1 by robot1.\n"
    f"Answer 3:\n"
    f"In order to check whether this action is executable or not, we first need to find states of objects related to this action, then check whether all preconditions of this action are satisfied.\n"
    f"Ball4: held by robot1's rgripper1. Robot1: at room4, lgripper1 is free, rgripper1 is not free, rgripper1 is holding ball4.\n"
    f"Based on the domain description, A robot's lgripper/rgripper can 'drop' a ball at a room. This action is executable only if all following preconditions are satisfied: the robot is at the room, the robot's lgripper/rgripper is holding the ball.\n"
    f"the robot is at the room ::: Robot1: at room4 ===> SATISFY\n"
    f"the robot's lgripper/rgripper is holding the ball. ::: Robot1: at room4, lgripper1 is free, rgripper1 is not free, rgripper1 is holding ball4. ===> SATISFY\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final answer: True.\n"
    f"——————\n"
)



STATE_CHECKER_GRIPPERS_EXAMPLE = (
    f"[Examples]\n"
    
    f"Current State1: Ball1: at room1. Ball2: at room2. Ball3: at room1. Ball4: at room2. Ball5: at room3. Ball6: at room1. Ball7: at room4. Robot1: at room4, lgripper1 is free, rgripper1 is free.\n"
    
    f"Question1: In this state, is it True or False that ball6 is at room5?\n"
    
    f"Answer1:\n" 
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. If there is any action needed to take in the question, we should first take the action and return all objects states, including those states that are not affected by the action. \n"
    f"Ball6 is at room5 ::: Ball6: at room1. ===> NOT MATCH\n"
    f"Since the question doesn't match with the current state, so the question is false.\n"
    f"Final Answer: False.\n"
    
    f"------------\n"
    
    f"Current State2: Ball1: at room1. Ball2: at room2. Ball3: at room1. Ball4: at room2. Ball5: at room2. Ball6: at room1. Robot1: at room1, lgripper1 is free, rgripper1 is free.\n"
    
    f"Question2: Is it True or False that robot1's lgripper1 is holding ball3?\n"
    
    f"Answer2:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. If there is any action needed to take in the question, we should first take the action and return all objects states, including those states that are not affected by the action. \n"
    f"robot1's lgripper1 is holding ball3 ::: Robot1: at room1, lgripper1 is free, rgripper1 is free. ===> NOT MATCH\n"
    f"Since the question doesn't match with the current state, so the question is false.\n"
    f"Final Answer: False.\n"
    
    f"------------\n"
    
    f"Current State3: Ball1: at room1. Ball2: at room2. Ball3: at room1. Ball4: at room2. Ball5: at room2. Ball6: at room1. Ball7: at room3. Robot1: at room1, lgripper1 is free, rgripper1 is free.\n"
    
    f"Question3: In this state, are all of the following valid properties of the state that involve negations? ball1 is not at room3, ball1 is not at room5, ball1 is not being carried by robot1's lgripper1, ball1 is not being carried by robot1's rgripper1, ball1 is not located at room4, ball1 is not present at room2, ball2 is not at room1, ball2 is not at room5, ball2 is not being carried by robot1's rgripper1, ball2 is not present at room3, ball5 is not located at room3, ball5 is not present at room4, ball6 is not at room2, ball6 is not being carried by robot1's rgripper1, ball6 is not located at room3, ball6 is not located at room4, ball6 is not present at room5, ball7 is not located at room4, ball7 is not present at room1, ball7 is not present at room2, ball7 is not present at room5, lgripper1 of robot1 is not carrying ball2, lgripper1 of robot1 is not carrying ball6, lgripper1 of robot1 is not carrying ball7, rgripper1 of robot1 is not carrying ball4, rgripper1 of robot1 is not carrying ball5. Respond with True or False.\n"
    
    f"Answer3:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. If there is any action needed to take in the question, we should first take the action and return all objects states, including those states that are not affected by the action. \n"
    f"ball1 is not at room3, ball1 is not at room5, ball1 is not being carried by robot1's lgripper1, ball1 is not being carried by robot1's rgripper1, ball1 is not located at room4, ball1 is not present at room2 ::: Ball1: at room1, ===> MATCH\n"
    f"ball2 is not at room1, ball2 is not at room5, ball2 is not being carried by robot1's rgripper1, ball2 is not present at room3, ::: Ball2: at room2, ===> MATCH\n"
    f"ball5 is not located at room3, ball5 is not present at room4, ::: Ball5: at room2, ===> MATCH\n"
    f"ball6 is not at room2, ball6 is not being carried by robot1's rgripper1, ball6 is not located at room3, ball6 is not located at room4, ball6 is not present at room5, ::: Ball6: at room1, ===> MATCH\n"
    f"ball7 is not located at room4, ball7 is not present at room1, ball7 is not present at room2, ball7 is not present at room5, ::: Ball7: at room3, ===> MATCH\n"
)


TWOSHOTCOT_AE_GRIPPERS_EXAMPLE = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"Current state: Ball1 is present at room3, ball2 is located at room3, ball3 is located at room2, ball4 is located at room3, ball5 is present at room1, ball6 is present at room1, ball7 is located at room3, robot1 is at room3 , robot1's lgripper1 is free, robot1's rgripper1 is free, robot2 is present in room2, robot2's lgripper2 is free and robot2's rgripper2 is free.\n"
    f"Question: Given the initial condition, the following actions are planned to be performed: from room3 robot1's rgripper1 picks up ball2. Is it possible to execute it, True or False?\n"
    f"Answer: \n"
    f"Step 1: we can confirm whether this action is executable or not by checking the initial state.\n"
    f"A robot's rgripper picking up a ball at location A must satisfy the following preconditions: the robot and the ball are both at location A, and the robot's rgripper is free. Robot1 and ball2 are in room3, and robot1's rgripper is available.So this action can be executed.\n"
    f"Step 2: we return the final answer based on the checking result.\n" 
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final Answer: True"
    f"------------\n"
    f"(Example 2)\n"
    f"Current state: Ball1 is present at room1, ball2 is located at room2, ball3 is located at room1, ball4 is at room2, ball5 is at room2, ball6 is present at room1, robot1 is present in room4, robot1's lgripper1 is available and robot1's rgripper1 is free.\n"
    f"Question: Given the initial condition, the following actions are planned to be performed: from room4, robot1's rgripper1 picks up ball2. Is it possible to execute it, True or False?\n"
    f"Answer: \n"
    f"Step 1: we can confirm whether this action is executable or not by checking the initial state.\n"
    f"A robot's rgripper picking up a ball at location A must satisfy the following preconditions: the robot and the ball are both at location A, and the robot's rgripper is free. Robot1 is in room4, ball2 is in room2. Since the robot is not in the same location as the ball , this action cannot be executed.\n"
    f"Step 2: we return the final answer based on the checking result.\n"
    f"Since not all preconditions are satisfied, this action is not executable.\n"
    f"Final Answer: False"
    f"------------\n"
)


TWOSHOTCOT_STATE_GRIPPERS_EXAMPLE = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"Current state: Ball1 is located at room1, ball2 is at room2, ball3 is present at room1, ball4 is present at room4, ball5 is present at room3, ball6 is present at room1, ball7 is located at room4, robot1 is present in room4, robot1's lgripper1 is free and robot1's rgripper1 is free.\n"
    f"Question: Given the initial condition, the following actions are performed: ball4 is picked from room4 with lgripper1 by robot1 to reach the current state. In this state, if from room4, robot1 moves to room1, is it True or False that ball4 is present at room4?\n"
    f"Answer: \n"
    f"Step 1: We first execute the action and get the new state. After taking the action 'robot1 uses lgripper1 to pick up ball4 in room4', ball4 is in robot1's lgripper1 and robot1's lgripper1 is occupied. If robot1 moves from room4 to room1, robot1 is in room1.\n"
    f"Step 2: Then, we compare the state and the question and get the answer. Ball4 is in robot1's lgripper1, so ball4 is not in room4.\n"
    f"So the question is false.\n"
    f"Final Answer: False.\n\n"
    f"------------\n"
    f"(Example 2)\n"
    f"Current state: Ball1 is at room1, ball2 is at room2, ball3 is located at room2, ball4 is located at room1, ball5 is located at room2, ball6 is located at room1, lgripper1 of robot1 is free, robot1 is located at room1 and robot1's rgripper1 is available.\n"
    f"Question: Given the initial condition, the following actions are performed: robot1 moves from room1 to room2 to reach the current state. In this state, if from room2, robot1's lgripper1 picks up ball3, is it True or False that ball3 is not located at room2?\n"
    f"Answer: \n"
    f"Step 1: We first execute the action and get the new state. After taking the action 'robot1 moves from room1 to room2' to reach the current state, robot1 is in room2. If from room2, robot1's lgripper1 picks up ball3, robot1's lgripper1 becomes occupied, and ball3 is in robot1's lgripper1.\n"
    f"Step 2: Then, we compare the state and the question and get the answer. Ball3 is in robot1's lgripper1, therefore ball3 is not in room2.\n"
    f"So the question is true.\n"
    f"Final Answer: True."
    f"------------\n"
)

TWOSHOTCOT_AE_DRIVERLOG_EXAMPLE = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"Current state: Driver1 is currently at location s2, driver2 is at location s2, locations p0_1 and s0 have a path between them, locations p0_2 and s0 have a path between them, locations p0_3 and s3 have a path between them, locations p1_3 and s3 have a path between them, locations p2_1 and s2 have a path between them, locations s0 and p0_3 have a path between them, locations s0 and s2 have a link between them, locations s0 and s3 have a link between them, locations s1 and p0_1 have a path between them, locations s1 and p1_3 have a path between them, locations s1 and p2_1 have a path between them, locations s2 and p2_1 have a path between them, locations s2 and s0 have a link between them, locations s3 and p1_3 have a path between them, locations s3 and s0 have a link between them, package1 is present at location s1, package2 is currently at location s2, package3 is present at location s0, package4 is currently at location s2, there exists a link between the locations s0 and s1, there exists a link between the locations s1 and s0, there exists a link between the locations s1 and s3, there exists a link between the locations s2 and s1, there exists a link between the locations s2 and s3, there exists a link between the locations s3 and s2, there exists a path between the locations p0_1 and s1, there exists a path between the locations p0_3 and s0, there exists a path between the locations p1_3 and s1, there exists a path between the locations s0 and p0_2, there exists a path between the locations s3 and p0_3, there is a link between location s1 and location s2, there is a link between location s3 and location s1, there is a path between location p0_2 and location s2, there is a path between location p2_1 and location s1, there is a path between location s0 and location p0_1, there is a path between location s2 and location p0_2, truck1 is at location s0, truck1 is empty, truck2 contains nothing and truck2 is at location s0. \n"
    f"Question: Given the initial condition, the following actions are planned to be performed: load truck1 with package3 at location s0. Is it possible to execute it, True or False?\n"
    f"Answer: \n"
    f"Step 1: we can confirm whether this action is executable or not by checking the initial state.\n"
    f"A package can be loaded into a truck at the location. This action is executable only if all following preconditions are satisfied: the truck and the package are both at the location. We can see now package3 is present at location s0, truck1 is at location s0. So the action sequence is executable.\n"
    f"Step 2: we return the final answer based on the checking result.\n" 
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final Answer: True"
    f"------------\n"
    f"(Example 2)\n"
    f"Current state: Driver1 is currently at location s2, driver2 is at location s2, locations p0_1 and s0 have a path between them, locations p0_2 and s0 have a path between them, locations p0_3 and s3 have a path between them, locations p1_3 and s3 have a path between them, locations p2_1 and s2 have a path between them, locations s0 and p0_3 have a path between them, locations s0 and s2 have a link between them, locations s0 and s3 have a link between them, locations s1 and p0_1 have a path between them, locations s1 and p1_3 have a path between them, locations s1 and p2_1 have a path between them, locations s2 and p2_1 have a path between them, locations s2 and s0 have a link between them, locations s3 and p1_3 have a path between them, locations s3 and s0 have a link between them, package1 is present at location s1, package2 is currently at location s2, package3 is present at location s0, package4 is currently at location s2, there exists a link between the locations s0 and s1, there exists a link between the locations s1 and s0, there exists a link between the locations s1 and s3, there exists a link between the locations s2 and s1, there exists a link between the locations s2 and s3, there exists a link between the locations s3 and s2, there exists a path between the locations p0_1 and s1, there exists a path between the locations p0_3 and s0, there exists a path between the locations p1_3 and s1, there exists a path between the locations s0 and p0_2, there exists a path between the locations s3 and p0_3, there is a link between location s1 and location s2, there is a link between location s3 and location s1, there is a path between location p0_2 and location s2, there is a path between location p2_1 and location s1, there is a path between location s0 and location p0_1, there is a path between location s2 and location p0_2, truck1 is at location s0, truck1 is empty, truck2 contains nothing and truck2 is at location s0.\n"
    f"Question: Given the initial condition, the following actions are planned to be performed: driver1 boards truck1 at location p0_2. Is it possible to execute it, True or False?\n"
    f"Answer: \n"
    f"Step 1: we can confirm whether this action is executable or not by checking the initial state.\n"
    f"A driver can board a truck at the location. This action is executable only if all following preconditions are satisfied: the truck and the driver are both at the location, the truck has no driver on it. We can see driver1 is at location s2, truck1 is at location s0. Since the driver and the truck are not at the same location, this action is not executable.\n "
    f"Step 2: we return the final answer based on the checking result.\n" 
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final Answer: False.\n"
    f"------------\n"
)


TWOSHOTCOT_STATE_DRIVERLOG_EXAMPLE = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"Current state: Driver1 is at location s1. Driver2 is at location s0. Truck1 is at location s2 and is empty. Truck2 is at location s1 and is empty. Package1 is at location s1, Package2 is at location s2. There exists a link between locations s1 and s2, and a link between s2 and s1. There is a link between s0 and s1. There is a path between s1 and p1_2, and between p1_2 and s2. There is a path between s2 and p2_3, and between p2_3 and s0.\n"
    f"Question: Given the initial condition, the following actions are performed: driver1 walks from location s1 to location s2. In this state, is it True or False that driver1 is at location s2?\n"
    f"Answer: \n"
    f"Step 1: We first execute the action and get the new state.\n"
    f"driver1 walks from location s1 to location s2. After this action, driver1 is at location s2.\n"
    f"Step 2: Then, we compare the state and the question and get the answer.\n"
    f"In this state, is it True or False that driver1 is at location s2? We can see now the driver is at s2, so this question is true.\n"
    f"Step 3: Return the answer based on the analysis.\n"
    f"Final Answer: True.\n"
    f"---------------\n"
    f"(Example 2)\n"
    f"Current state: Driver1 is at location s0. Driver2 is on truck2. Truck1 is at location s0. Truck2 is at location s1 and is empty. Package1 is at s2, Package2 is at s3. There exists a link between s1 and s2, and a link between s2 and s1. There is a link between s0 and s1. There is a link between s2 and s3. There is a path between s1 and p2_2, and between p2_2 and s2.\n"
    f"Question: Given the initial condition, the following actions are performed: driver2 drives truck2 from s1 to s2. In this state, is it True or False that truck2 is at location s3?\n"
    f"Step 1: We first execute the action and get the new state.\n"
    f"driver2 drives truck2 from s1 to s2. After this action, truck2 is at s2.\n"
    f"Step 2: Then, we compare the state and the question and get the answer.\n"
    f"In this state, is it True or False that truck2 is at location s3? We can see now truck2 is at s3. So the question is false.\n"
    f"Step 3: Return the answer based on the analysis.\n"
    f"Final Answer: True.\n"
    f"---------------\n"
)




#----------------------
#Mystery domain
#----------------------
MYSTERY_DOMAIN_DESCRIPTION = (
    f"[Domain Description]\n"
    f"Mystery domain includes cargo, vehicle, location, fuel level and space(or space level). Vehicle can drive between locations if two locations are connected. Cargo can be loaded into vehicle, and can also be unloaded from vehicle. 'Space(or space level)' is used to describe vehicle's ability to load cargo. Vehicle's space may vary case by case, but it should be s_x>s_x-1>...>s1>s0, where s_x and s_x-1 are called neighboring levels. 'Fuel(or fuel level)' is used to describe location's fuel reserve. Location's fuel level may vary case by case, but it should be f_x>f_x-1>f_x -2>…>f0, where f_x and f_x-1 are called neighboring levels."
    
    f"Different properties are used to describe current states of different objects. For vehicle we use: at location_x, has space s_x, has cargo_x in it, has no cargo in it. For location we use: connected with location_x, has fuel level f_x. For cargo we use: at location_x/in vehicle v_x.\n"
    
    f"Following actions are executable only if all preconditions are met, if any condition are not satisfied, the action is not executable.\n"
    	
    f"A vehicle can 'move' from location A which has fuel-level f_x and f_y to location B. This action is executable only if all following preconditions are satisfied: the vehicle is current at location A, location A and B are connected, location A's has fuel level f_x, fuel level f_x and f_y are neighboring and f_x>f_y.\n"
    
    f"A cargo can be 'loaded' in a vehicle with space s_x and space s_y at location A. This action is executable only if all following preconditions are satisfied: the vehicle and the cargo are both at location A, the vehicle has space s_x, s_x and s_y are neighboring and s_x>s_y.\n"
    
    f"A cargo can be 'unload' from a vehicle utilizing space s_x and s_y at location A. This action is executable only if all following preconditions are satisfied: the cargo is in the vehicle, the vehicle is at location A, the vehicle has space s_x, space s_x and s_y are neighboring and s_x<s_y.\n"
    
    f"Executing an action will change states of related objects.\n"
    
    f"A vehicle can 'move' from location A which has fuel-level f_x and f_y to location B. This action will result in: the vehicle is at location B(not at location A), location A's fuel level is f_y(not f_x).\n"
    
    f"A cargo can be 'loaded' in a vehicle with space s_x and space s_y at location A. This action will result in: the cargo is not at location A, the cargo is in the vehicle, the vehicle's space is s_y(not s_x).\n"
    
    f"A cargo can be 'unload' from a vehicle utilizing space s_x and s_y at location A. This action will result in: the cargo is not in the vehicle, the cargo is at location A, the vehicle has space s_y(not s_x).\n"
)



INITIAL_STATE_EXTRACTOR_MYSTERY_PROMPT =(
    f"This is a question related to the mystery domain. You are required to extract the initial state of every objects in this plan, including cargo, vehicle, space, location and fuel level. Your answer must satisfy all the following requirements. First, think and respond with the format from the example above, including the word choice and paragraph structure. Second, each object's state should contain all properties mentioned in the domain description above. Besides, don't use any markdown formatting."
)


INITIAL_STATE_EXTRACTOR_MYSTERY_EXAMPLE = (
    f"[Examples]\n"
    f"Initial state example 1: Cargo c0 is at location l0, cargo c1 is present at location l0, cargo c2 is present at location l1, cargo c3 is present at location l1, cargo c4 is situated at location l1, cargo c5 is at location l1, cargo c6 is present at location l0, cargo c7 is at location l0, cargo c8 is present at location l1, cargo c9 is present at location l1, fuel level f3 neighbors fuel level f4, fuel level f4 neighbors fuel level f5, fuel level f5 neighbors fuel level f6, fuel level f6 neighbors fuel level f7, fuel level f7 neighbors fuel level f8, fuel-levels f0 and f1 are neighbors, fuel-levels f1 and f2 are neighbors, fuel-levels f2 and f3 are neighbors, location l0 has a fuel-level of f3, location l0 is connected to location l1, location l1 has fuel f8, location l1 is connected to location l0, spaces s0 and s1 are neighbors, vehicle v0 has space s1, vehicle v0 is present at location l1, vehicle v1 has space s1 and vehicle v1 is situated at location l0.\n"
    
    f"Extracted from initial state example 1:\n"
    
    f"We fist find following objects in the intial state description:\n"
    f"cargo c0, c1, c2, c3, c4, c5, c6, c7, c8, c9; vehicle v0, v1. We can find fuel level from f8 to f0. We can find location l0 and l1.\n"
    f"Then, we find all descriptions related to an object, and organize then into the required format. Repeat this process until all objects' states are extracted, and each object's state contains all related properties:\n"

    f"Cargo c0 is at location l0, cargo c1 is present at location l0, cargo c2 is present at location l1, cargo c3 is present at location l1, cargo c4 is situated at location l1, cargo c5 is at location l1, cargo c6 is present at location l0, cargo c7 is at location l0, cargo c8 is present at location l1, cargo c9 is present at location l1 ::: Cargo c0: at location l0. Cargo c1: at location l0. Cargo c2: at location l1. Cargo c3: at location l1. Cargo c4: at location l1. Cargo c5: at location l1. Cargo c6: at location l0. Cargo c7: at location l0. Cargo c8: at location l1. Cargo c9: at location l1. \n"

    f"fuel level f3 neighbors fuel level f4, fuel level f4 neighbors fuel level f5, fuel level f5 neighbors fuel level f6, fuel level f6 neighbors fuel level f7, fuel level f7 neighbors fuel level f8, fuel-levels f0 and f1 are neighbors, fuel-levels f1 and f2 are neighbors, fuel-levels f2 and f3 are neighbors, location l0 has a fuel-level of f3, location l0 is connected to location l1, location l1 has fuel f8 ::: Fuel level: f8>f7>f6>f5>f4>f3>f2>f1>f0. \n"
    
    f"location l0 has a fuel-level of f3, location l0 is connected to location l1, location l1 has fuel f8, location l1 is connected to location l0. ::: Location l0: connected with location l1, has fuel level f3. Location l1: connected with location l0, has fuel level f8. \n"
    
    f"spaces s0 and s1 are neighbors. ::: Space: s1>s0. \n"
 
    f"vehicle v0 has space s1, vehicle v0 is present at location l1, vehicle v1 has space s1 and vehicle v1 is situated at location l0. ::: Vehicle v0: at l1, has space s1. Vehicle v1: at l0, has space s1."
    
    f"Then, we organize all objects' states into a new paragraph as the end of answer.\n"
    
    f"Cargo c0: at location l0. Cargo c1: at location l0. Cargo c2: at location l1. Cargo c3: at location l1. Cargo c4: at location l1. Cargo c5: at location l1. Cargo c6: at location l0. Cargo c7: at location l0. Cargo c8: at location l1. Cargo c9: at location l1. Fuel level: f8>f7>f6>f5>f4>f3>f2>f1>f0. Location l0: connected with location l1, has fuel level f3. Location l1: connected with location l0, has fuel level f8. Space: s1>s0. Vehicle v0: at l1, has space s1. Vehicle v1: at l0, has space s1."

    f"-------------"

)


QUESTION_EXTRACTOR_MYSTERY_EXAMPLE = (
    f"[Examples]\n"
    f"Plan 1: Given the initial condition, the following actions are performed: cargo c2 is loaded in vehicle v0 with space s1 and space s0 at location l1 to reach the current state. In this state, if vehicle v0 moves from location l1 which has fuel-levels f8 and f7 to location l0, is it True or False that cargo c8 is in vehicle v0?\n"
    f"Question extracted from plan 1: In this state, if vehicle v0 moves from location l1 which has fuel-levels f8 and f7 to location l0, is it True or False that cargo c8 is in vehicle v0?\n"
    f"------------\n"
    f"Plan 2: Given the initial condition, the following actions are performed: vehicle v0 moves from location l1 which has fuel-levels f3 and f2 to location l0, cargo c0 is loaded in vehicle v0 with space s2 and space s1 at location l0, at location l0, cargo c2 is loaded in vehicle v0 with spaces s1 and s0, vehicle v0 moves to location l1 from location l0 that has fuel level f4 and f3, at location l1, cargo c0 is unloaded from vehicle v0 with spaces s0 and s1, cargo c10 is loaded in vehicle v0 with space s1 and space s0 at location l1, cargo c2 is unloaded from vehicle v0 with space s0 and space s1 at location l1, vehicle v0 moves to location l0 from location l1 that has fuel level f2 and f1, cargo c10 is unloaded from vehicle v0 with space s1 and space s2 at location l0 and cargo c3 is loaded in vehicle v0 with space s2 and space s1 at location l0 to reach the current state. In this state, are all of the following valid properties of the state that involve negations? cargo c0 is not at location l0cargo c0 is not present at location l0, cargo c1 is not in vehicle v1, cargo c1 is not situated at location l0, cargo c10 is not located in vehicle v0, cargo c10 is not located in vehicle v1, cargo c10 is not situated at location l1, cargo c2 is not in vehicle v0, cargo c2 is not situated at location l0, cargo c3 is not at location l0cargo c3 is not present at location l0, cargo c3 is not at location l1cargo c3 is not present at location l1, cargo c4 is not at location l1cargo c4 is not present at location l1, cargo c4 is not in vehicle v0, cargo c4 is not located in vehicle v1, cargo c5 is not in vehicle v0, cargo c5 is not located in vehicle v1, cargo c5 is not situated at location l0, cargo c6 is not in vehicle v0, cargo c6 is not situated at location l1, cargo c7 is not at location l1cargo c7 is not present at location l1, cargo c7 is not in vehicle v1, cargo c7 is not located in vehicle v0, cargo c8 is not at location l0cargo c8 is not present at location l0, cargo c8 is not in vehicle v0, cargo c8 is not in vehicle v1, cargo c9 is not in vehicle v1, cargo c9 is not located in vehicle v0, cargo c9 is not situated at location l0, fuel f0 does not exist in location l0, fuel f1 does not exist in location l0, fuel level f0 does not neighbour fuel level f2, fuel level f0 does not neighbour fuel level f3, fuel level f0 does not neighbour fuel level f4, fuel level f1 does not neighbour fuel level f5, fuel level f2 does not neighbour fuel level f0, fuel level f2 does not neighbour fuel level f1, fuel level f2 does not neighbour fuel level f4, fuel level f2 does not neighbour fuel level f5, fuel level f3 does not neighbour fuel level f0, fuel level f3 does not neighbour fuel level f2, fuel level f3 does not neighbour fuel level f5, fuel level f4 does not neighbour fuel level f0, fuel level f4 does not neighbour fuel level f2, fuel level f4 does not neighbour fuel level f3, fuel level f5 does not neighbour fuel level f0, fuel level f5 does not neighbour fuel level f1, fuel level f5 does not neighbour fuel level f4, fuel-levels f0 and f5 are not neighbors, fuel-levels f1 and f0 are not neighbors, fuel-levels f1 and f3 are not neighbors, fuel-levels f1 and f4 are not neighbors, fuel-levels f3 and f1 are not neighbors, fuel-levels f4 and f1 are not neighbors, fuel-levels f5 and f2 are not neighbors, fuel-levels f5 and f3 are not neighbors, location l0 does not have fuel f2, location l0 does not have fuel f4, location l0 does not have fuel f5, location l1 does not have a fuel-level of f0, location l1 does not have a fuel-level of f2, location l1 does not have a fuel-level of f3, location l1 does not have a fuel-level of f4, location l1 does not have a fuel-level of f5, spaces s0 and s2 are not neighbors, spaces s1 and s0 are not neighbors, spaces s2 and s0 are not neighbors, spaces s2 and s1 are not neighbors, vehicle v0 does not contain cargo c0, vehicle v0 does not contain cargo c1, vehicle v0 does not contain space s0, vehicle v0 does not have space s2, vehicle v0 is not at location l1, vehicle v1 does not contain cargo c0, vehicle v1 does not contain cargo c2, vehicle v1 does not contain cargo c3, vehicle v1 does not contain cargo c6, vehicle v1 does not contain space s0, vehicle v1 does not have space s1 and vehicle v1 is not situated at location l0. Respond with True or False.\n"
    f"Question extracted from plan 2: In this state, are all of the following valid properties of the state that involve negations? cargo c0 is not at location l0cargo c0 is not present at location l0, cargo c1 is not in vehicle v1, cargo c1 is not situated at location l0, cargo c10 is not located in vehicle v0, cargo c10 is not located in vehicle v1, cargo c10 is not situated at location l1, cargo c2 is not in vehicle v0, cargo c2 is not situated at location l0, cargo c3 is not at location l0cargo c3 is not present at location l0, cargo c3 is not at location l1cargo c3 is not present at location l1, cargo c4 is not at location l1cargo c4 is not present at location l1, cargo c4 is not in vehicle v0, cargo c4 is not located in vehicle v1, cargo c5 is not in vehicle v0, cargo c5 is not located in vehicle v1, cargo c5 is not situated at location l0, cargo c6 is not in vehicle v0, cargo c6 is not situated at location l1, cargo c7 is not at location l1cargo c7 is not present at location l1, cargo c7 is not in vehicle v1, cargo c7 is not located in vehicle v0, cargo c8 is not at location l0cargo c8 is not present at location l0, cargo c8 is not in vehicle v0, cargo c8 is not in vehicle v1, cargo c9 is not in vehicle v1, cargo c9 is not located in vehicle v0, cargo c9 is not situated at location l0, fuel f0 does not exist in location l0, fuel f1 does not exist in location l0, fuel level f0 does not neighbour fuel level f2, fuel level f0 does not neighbour fuel level f3, fuel level f0 does not neighbour fuel level f4, fuel level f1 does not neighbour fuel level f5, fuel level f2 does not neighbour fuel level f0, fuel level f2 does not neighbour fuel level f1, fuel level f2 does not neighbour fuel level f4, fuel level f2 does not neighbour fuel level f5, fuel level f3 does not neighbour fuel level f0, fuel level f3 does not neighbour fuel level f2, fuel level f3 does not neighbour fuel level f5, fuel level f4 does not neighbour fuel level f0, fuel level f4 does not neighbour fuel level f2, fuel level f4 does not neighbour fuel level f3, fuel level f5 does not neighbour fuel level f0, fuel level f5 does not neighbour fuel level f1, fuel level f5 does not neighbour fuel level f4, fuel-levels f0 and f5 are not neighbors, fuel-levels f1 and f0 are not neighbors, fuel-levels f1 and f3 are not neighbors, fuel-levels f1 and f4 are not neighbors, fuel-levels f3 and f1 are not neighbors, fuel-levels f4 and f1 are not neighbors, fuel-levels f5 and f2 are not neighbors, fuel-levels f5 and f3 are not neighbors, location l0 does not have fuel f2, location l0 does not have fuel f4, location l0 does not have fuel f5, location l1 does not have a fuel-level of f0, location l1 does not have a fuel-level of f2, location l1 does not have a fuel-level of f3, location l1 does not have a fuel-level of f4, location l1 does not have a fuel-level of f5, spaces s0 and s2 are not neighbors, spaces s1 and s0 are not neighbors, spaces s2 and s0 are not neighbors, spaces s2 and s1 are not neighbors, vehicle v0 does not contain cargo c0, vehicle v0 does not contain cargo c1, vehicle v0 does not contain space s0, vehicle v0 does not have space s2, vehicle v0 is not at location l1, vehicle v1 does not contain cargo c0, vehicle v1 does not contain cargo c2, vehicle v1 does not contain cargo c3, vehicle v1 does not contain cargo c6, vehicle v1 does not contain space s0, vehicle v1 does not have space s1 and vehicle v1 is not situated at location l0. Respond with True or False.\n"
    f"------------\n"
    f"Plan 3: Given the initial condition, the following actions are planned to be performed: at location l1, cargo c2 is loaded in vehicle v0 with spaces s1 and s0, vehicle v0 moves from location l1 which has fuel-levels f8 and f7 to location l0, cargo c2 is unloaded from vehicle v0 with space s0 and space s1 at location l0, cargo c0 is loaded in vehicle v0 with space s1 and space s0 at location l0, vehicle v0 moves to location l1 from location l0 that has fuel level f3 and f2, cargo c0 is unloaded from vehicle v0 with space s0 and space s1 at location l1, at location l1, cargo c3 is loaded in vehicle v0 with spaces s1 and s0, vehicle v0 moves from location l1 which has fuel-levels f7 and f6 to location l0, at location l0, cargo c3 is unloaded from vehicle v0 with spaces s0 and s1, cargo c1 is loaded in vehicle v0 with space s1 and space s0 at location l0, vehicle v0 moves from location l0 which has fuel-levels f2 and f1 to location l1, at location l1, cargo c1 is unloaded from vehicle v0 with spaces s0 and s1, cargo c5 is loaded in vehicle v0 with space s1 and space s0 at location l1, vehicle v0 moves to location l0 from location l1 that has fuel level f6 and f5, cargo c5 is unloaded from vehicle v0 with space s0 and space s1 at location l0, cargo c7 is loaded in vehicle v0 with space s1 and space s0 at location l0, vehicle v0 moves to location l0 from location l1 that has fuel level f7 and f4, cargo c7 is unloaded from vehicle v0 with space s0 and space s1 at location l1 and at location l1, cargo c9 is loaded in vehicle v0 with spaces s1 and s0 to reach the current state. Are the following valid properties of the state (both with and without negations) true for f1 before the first inexecutable action in the sequence? Fuel level f1 does not neighbour fuel level f3, fuel level f1 does not neighbour fuel level f5, fuel level f1 neighbors fuel level f0, fuel level f1 neighbors fuel level f2, fuel level f1 neighbors fuel level f4, fuel level f1 neighbors fuel level f7, fuel level f2 neighbors fuel level f1, fuel level f5 does not neighbour fuel level f1, fuel level f6 neighbors fuel level f1, fuel level f7 does not neighbour fuel level f1, fuel-levels f0 and f1 are neighbors, fuel-levels f1 and f6 are not neighbors, fuel-levels f1 and f8 are not neighbors, fuel-levels f3 and f1 are neighbors, fuel-levels f4 and f1 are neighbors and fuel-levels f8 and f1 are neighbors.\n"
    f"Question extracted from plan 3: Are the following valid properties of the state (both with and without negations) true for f1 before the first inexecutable action in the sequence? Fuel level f1 does not neighbour fuel level f3, fuel level f1 does not neighbour fuel level f5, fuel level f1 neighbors fuel level f0, fuel level f1 neighbors fuel level f2, fuel level f1 neighbors fuel level f4, fuel level f1 neighbors fuel level f7, fuel level f2 neighbors fuel level f1, fuel level f5 does not neighbour fuel level f1, fuel level f6 neighbors fuel level f1, fuel level f7 does not neighbour fuel level f1, fuel-levels f0 and f1 are neighbors, fuel-levels f1 and f6 are not neighbors, fuel-levels f1 and f8 are not neighbors, fuel-levels f3 and f1 are neighbors, fuel-levels f4 and f1 are neighbors and fuel-levels f8 and f1 are neighbors.\n"
    f"------------\n"
)


EXECUTABILITY_CHECKER_MYSTERY_EXAMPLE = (
    
    f"[Examples]\n"
    f"Current state example 1: Cargo c0: at location l1. Cargo c1: at location l1. Cargo c2: at location l0. Cargo c3: at location l0. Cargo c4: at location l1. Cargo c5: at location l1. Cargo c6: at location l1. Cargo c7: at location l1. Cargo c8: at location l1. Cargo c9: at location l1. Cargo c10: at location l0. Vehicle v0: at location l1, has space s1. Location l0: has fuel level f7, connected with l1. Location l1: has fuel level f6, connected with l0. Space Level: s1>s0. Fuel level: f8>f7>f6>f5>f4>f3>f2>f1>f0.\n"
    f"Action 1: Cargo c1 is loaded from vehicle v0 at location l0 with space s1 and space s0.\n"
    f"Answer 1:\n"
    f"In order to check whether this action is executable or not, we first need to find states of objects related to this action, then check whether all preconditions of this action are satisfied.\n"
    f"Cargo c1: at location l1. Vehicle v0: at location l1, has space s1. Space Level: s1>s0.\n"
    f"Based on the domain description, a vehicle can 'load' a cargo into the vehicle at location A. This action is executable only if all following preconditions are satisfied: the vehicle and the cargo are both at location A, the vehicle has space s_x, s_x and s_y are neighboring. \n"

    f"the vehicle and the cargo are both at location A ::: Cargo c1: at location l1, Vehicle v0: at location l1,  ===> SATISFY\n"
    f"the vehicle has space s_x ::: Vehicle v0: has space s1.  ===> SATISFY\n"
    f"s_x and s_y are neighboring. ::: Space Level: s1>s0. ===> SATISFY\n"
    f"Since all preconditions are satisfied, the action is executable.\n"
    f"Final answer: True.\n"
    f"——————\n"
    f"Current state example 2: Cargo c0: at location l1. Cargo c1: at location l1. Cargo c10: at location l0. Cargo c2: at location l0. Cargo c3: at location l0. Cargo c4: at location l1. Cargo c5: at location l1. Cargo c6: at location l1. Cargo c7: at location l1. Cargo c8: at location l1. Cargo c9: at location l1. Vehicle v0: at location l1, has space s1. Location l0: has fuel level f7, connected with l1. Location l1: has fuel level f6, connected with l0. Space Level: s1>s0. Fuel level: f8>f7>f6>f5>f4>f3>f2>f1>f0.\n"
    f"Action 2: Vehicle v0 moves to location l1 from location l0 whicwhich has fuel level f7 and f6.\n"
    f"Answer 2:\n"
    f"In order to check whether this action is executable or not, we first need to find states of objects related to this action, then check whether all preconditions of this action are satisfied.\n"
    f"Vehicle v0: at location l1, has space s1. Location l1: has fuel level f6, connected with l0.\n"
    f"Based on the domain description, a vehicle can 'move' from location A which has fuel-level f_x and f_y to location B. This action is executable only if all following preconditions are satisfied: the vehicle is current at location A, location A and B are connected, location A's has fuel level f_x, fuel level f_x and f_y are neighboring.\n"
    f"the vehicle is current at location A ::: Vehicle v0: at location l1, has space s1.  ===> NOT SATISFY\n"
    f"Since not all preconditions are satisfied, the action is not executable.\n"
    f"Final answer: False.\n"
    f"——————\n"

)


STATE_CHECKER_MYSTERY_EXAMPLE = (
    f"[Examples]\n"
    
    f"Current state 1: Cargo c0: at location l1. Cargo c1: at location l1. Cargo c2: at location l1. Cargo c3: at location l0. Cargo c4: at location l1. Cargo c5: at location l0. Cargo c6: at location l1. Cargo c7: at location l1. Cargo c8: at location l0. Vehicle v0: at location l0, has space s1, has no cargo in it. Vehicle v1: at location l1, has space s1, has no cargo in it. Location l0: has fuel level f5, connected with l1. Location l1: has fuel level f7, connected with l0. Space Level: s1>s0. Fuel level: f7>f6>f5>f4>f3>f2>f1>f0.\n"
    f"Question 1: In this state, are following following valid properties of the state (both with and without negations) true? Cargo c0 is not at location l0, Cargo c1 is not at location l0, Cargo c2 is not at location l0, Location l0's fuel level is not f0, Location l0's fuel level is not f1, Location l0's fuel level is not f2, Location l0's fuel level is not f3,  Vehicle v0 is not at location l1, vehicle v0 has space s1, Vehicle v1 is not at location l1 and vehicle v1 has space s1.\n"
    f"Answer 1:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. If there is any action needed to take in the question, we should first take the action and return all objects states, including those states that are not affected by the action.\n"
    f"Cargo c0 is not at location l0, ::: Cargo c0: at location l1. ===>MATCH\n"
    f"Cargo c1 is not at location l0, ::: Cargo c1: at location l1. ===>MATCH\n"
    f"Cargo c2 is not at location l0, ::: Cargo c2: at location l1. ===>MATCH\n"
    f"Location l0's fuel level is not f0, Location l0's fuel level is not f1, Location l0's fuel level is not f2, Location l0's fuel level is not f3,  ::: Location l0: has fuel level f5, connected with l1. ===>MATCH\n"
    f"Vehicle v0 is not at location l1, vehicle v0 has space s1, ::: Vehicle v0: at location l0, has space s1, has no cargo in it. ===>MATCH\n"
    f"Vehicle v1 is not a tlocation l1, vehicle v1 has space s1. ::: Vehicle v1: at location l1, has space s1, has no cargo in it. ===> NOT MATCH\n"
    f"Since there is a proposition in the question doesn't match with the current state, the question is false.\n"
    f"Final Answer: False.\n"

    f"------------\n"
    
    f"Current state 2: Cargo c0: at location l0. Cargo c1: at location l0. Cargo c2: at location l1. Cargo c3: at location l1. Cargo c4: at location l1. Cargo c5: at location l1. Cargo c6: at location l0. Cargo c7: at location l0. Cargo c8: at location l1. Cargo c9: at location l1. Vehicle v0: at location l1, has space s1, has no cargo in it. Vehicle v1: at location l0, has space s1, has no cargo in it. Location l0: has fuel level f3, connected with l1. Location l1: has fuel level f8, connected with l0. Space Level: s1 > s0. Fuel level: f8 > f7 > f6 > f5 > f4 > f3 > f2 > f1 > f0.\n"
    f"Question 2: In this state, if vehicle v1 move from l0 to l1, are following following valid properties of the state (both with and without negations) true? Cargo c0 is not at l1, Cargo c1 is not at l1, Cargo c2 is not at l0, Cargo c3 is not at l0, Cargo c4 is not at l0, Location l0's fuel level is not f0,  Location l0's fuel level is not f1, Location l0's fuel level is not f2, Location l0's fuel level is not f4, Location l0's fuel level is not f5, Location l0's fuel level is not f6, Location l0's fuel level is not f7, Location l0's fuel level is not f8, vehicle v0 is at location l1, vehicle l1 is at l0.\n"
    f"Answer 2:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. If there is any action needed to take in the question, we should first take the action and return all objects states, including those states that are not affected by the action.\n"
    f"Because the question contains one action, we should first take the action and get new states of all objects. After taking the action, we should return states of all objects, including states that are not effected by the action.\n"
    f"The action is \"vehicle v1 move from l0 which has fuel-levels f3 and f2 to l1\". Based on the domain description, this action is executable.\n"
    f"After taking the action, the curremt states of all objects should be: Cargo c0: at location l0. Cargo c1: at location l0. Cargo c2: at location l1. Cargo c3: at location l1. Cargo c4: at location l1. Cargo c5: at location l1. Cargo c6: at location l0. Cargo c7: at location l0. Cargo c8: at location l1. Cargo c9: at location l1. Vehicle v0: at location l1, has space s1, has no cargo in it. Vehicle v1: at location l1, has space s1, has no cargo in it. Location l0: has fuel level f2, connected with l1. Location l1: has fuel level f8, connected with l0. Space Level: s1 > s0. Fuel level: f8 > f7 > f6 > f5 > f4 > f3 > f2 > f1 > f0.\n"
    f"Then, we compare each proposition in the question one by one.\n"
    f"Cargo c0 is not at l1, ::: Cargo c0: at location l0. ===> MATCH\n"
    f"Cargo c1 is not at l1, :::  Cargo c1: at location l0. ===> MATCH\n"
    f"Cargo c2 is not at l0, ::: Cargo c2: at location l1. ===> MATCH\n"
    f"Cargo c3 is not at l0, ::: Cargo c3: at location l1. ===> MATCH\n"
    f"Cargo c4 is not at l0, ::: Cargo c4: at location l1. ===> MATCH\n"
    f"Location l0's fuel level is not f0,  Location l0's fuel level is not f1, Location l0's fuel level is not f3, Location l0's fuel level is not f4, Location l0's fuel level is not f5, Location l0's fuel level is not f6, Location l0's fuel level is not f7, Location l0's fuel level is not f8,  :::  Location l0: has fuel level f2, connected with l1. ===> MATCH\n"
    f"vehicle v0 is at location l1, ::: Vehicle v0: at location l1, has space s1, has no cargo in it.  ===> MATCH\n"
    f"vehicle l1 is at l0. ::: Vehicle v1: at location l1, has space s1, has no cargo in it.  ===> MATCH\n"
    f"Since all propositions in the question match with the curent state, so the question is true.\n"
    f"Final Answer: True.\n"
)


ACTION_TAKER_MYSTERY_PROMPT =(
     f"Based on the domain description and examples above, take the action and return the new state of all objects. Your answer must satisfy all the following requirements. First, think and respond like examples above, you are required to return states of all objects(cargo, vehicle, location, space and fuel level), including states that are not effected by the action. Second, each object's state must contain all properties mentioned in the domain description above. Third, after your analysis, please return states of all objects into a new paragraph as the end of your answer. Your final paragraph should use the format like: \"Cargo c8: at location l0. Vehicle v0: at location l0, has space s1, has no cargo in it. Fuel level: f8>f7>f6>f5>f4>F3>F2>f1>f0.\" Besides, don't use any markdown formatting."
)



ACTION_TAKER_MYSTERY_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1:\n"
    f"Cargo c0: at location l1. Cargo c1: at location l1. Cargo c2: at location l1. Cargo c3: at location l0. Cargo c4: at location l1. Cargo c5: at location l0. Cargo c6: at location l1. Cargo c7: at location l1. Cargo c8: at location l0. Vehicle v0: at location l0, has space s1, has no cargo in it. Vehicle v1: at location l1, has space s1, has no cargo in it. Location l0: has fuel level f5, connected with l1. Location l1: has fuel level f7, connected with l0. Space Level: s1>s0. Fuel level: f7>f6>f5>f4>f3>f2>f1>f0.\n"
    f"Action 1: Vehicle v0 moves to location l1 from location l0 which has fuel level f5 and f4.\n"
    f"Answer 1:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Vehicle v0: at location l0, has space s1. Location l0: has fuel level f5, connected with l1.\n"
    f"Based on the domain description, a vehicle can 'move' from location A which has fuel-level f_x and f_y to location B. This action will result in: the vehicle is at location B(not at location A), location A's fuel level is f_y(not f_x).\n"
    f"the vehicle is at location B(not at location A) ::: Vehicle v0: at location l1, has space s1, has no cargo in it.\n"
    f"location A's fuel level is f_y(not f_x). ::: Location l0: has fuel level f4, connected with l1.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into one paragraph.\n"
    f"Cargo c0: at location l1. Cargo c1: at location l1. Cargo c2: at location l1. Cargo c3: at location l0. Cargo c4: at location l1. Cargo c5: at location l0. Cargo c6: at location l1. Cargo c7: at location l1. Cargo c8: at location l0. Vehicle v0: at location l1, has space s1, has no cargo in it. Vehicle v1: at location l1, has space s1, has no cargo in it. Location l0: has fuel level f4, connected with l1. Location l1: has fuel level f7, connected with l0. Space Level: s1>s0. Fuel level: f7>f6>f5>f4>f3>f2>f1>f0.\n"
    f"——————\n"
    f"Current state example 2:\n"
    f"Cargo c0: at location l0. Cargo c1: at location l0. Cargo c2: at location l1. Cargo c3: at location l1. Cargo c4: at location l1. Cargo c5: at location l1. Cargo c6: at location l0. Cargo c7: at location l0. Cargo c8: at location l1. Cargo c9: at location l1. Vehicle v0: at location l1, has space s1, has no cargo in it. Vehicle v1: at location l0, has space s1, has no cargo in it. Location l0: has fuel level f3, connected with l1. Location l1: has fuel level f8, connected with l0. Space Level: s1>s0. Fuel level: f8>f7>f6>f5>f4>f3>f2>f1>f0.\n"
    f"Action 2: Cargo c2 is loaded in vehicle v0 with space s1 and s0 at location l1.\n"
    f"Answer 2:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Cargo c2: at location l1. Vehicle v0: at location l1, has space s1, has no cargo in it.\n"
    f"Based on the domain description,A cargo can be 'loaded' in a vehicle with space s_x and space s_y at location A. This action will result in: the cargo is not at location A, the cargo is in the vehicle, the vehicle's space is s_y(not s_x).\n"
    f"the cargo is not at location A, the cargo is in the vehicle ::: Cargo c2: in vehicle v0.\n"
    f"the vehicle's space is s_y(not s_x) ::: Vehicle v0: at location l1, has space s0, has cargo c2 in it."
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into one paragraph.\n"
    f"Cargo c0: at location l0. Cargo c1: at location l0. Cargo c2: in vehicle v0. Cargo c3: at location l1. Cargo c4: at location l1. Cargo c5: at location l1. Cargo c6: at location l0. Cargo c7: at location l0. Cargo c8: at location l1. Cargo c9: at location l1. Vehicle v0: at location l1, has space s0, has cargo c2 in it. Vehicle v1: at location l0, has space s1. Location l0: has fuel level f3, connected with l1. Location l1: has fuel level f8, connected with l0. Space Level: s1>s0. Fuel level: f8>f7>f6>f5>f4>f3>f2>f1>f0.\n"
    f"——————\n"
    f"Current state example 3:\n"
    f"Cargo c0: at location l1. Cargo c1: in vehicle v0. Cargo c2: at location l0. Cargo c3: at location l0. Cargo c4: at location l1. Cargo c5: at location l1. Cargo c6: at location l1. Cargo c7: at location l1. Cargo c8: at location l1. Cargo c9: at location l1. Cargo c10: at location l0. Vehicle v0: at location l0, has space s0, has cargo c1 in it. Location l0: has fuel level f7, connected with l1. Location l1: has fuel level f6, connected with l0. Space Level: s1>s0. Fuel level: f8>f7>f6>f5>f4>f3>f2>f1>f0.\n"
    f"Action 3: Cargo c1 is unloaded from vehicle v0 with space s0 and space s1 at location l0.\n"
    f"Answer 3:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Cargo c1: at location l1, on vehicle v0. Vehicle v0: at location l0, has space s0, has cargo c1 on it.\n"
    f"Based on the domain description, a cargo can be 'unload' from a vehicle utilizing space s_x and s_y at location A. This action will result in: the cargo is not in the vehicle, the cargo is at location A, the vehicle has space s_y(not s_x).\n"
    f"the cargo is at location A ::: Cargo c1: at location l1. \n"
    f"the vehicle has space s_y(not s_x), the cargo is not in the vehicle ::: Vehicle v0: at location l0, has space s1, has no cargo in it.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into one paragraph.\n"
    f"Cargo c0: at location l1. Cargo c1: at location l1. Cargo c2: at location l0. Cargo c3: at location l0. Cargo c4: at location l1. Cargo c5: at location l1. Cargo c6: at location l1. Cargo c7: at location l1. Cargo c8: at location l1. Cargo c9: at location l1. Cargo c10: at location l0. Vehicle v0: at location l0, has space s1, has no cargo in it. Location l0: has fuel level f7, connected with l1. Location l1: has fuel level f6, connected with l0. Space Level: s1>s0. Fuel level: f8>f7>f6>f5>f4>f3>f2>f1>f0.\n"
    f"——————\n"
)

TWOSHOTCOT_AE_MYSTERY_EXAMPLE = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"current state: Cargo c0 is present at location l1, cargo c1 is present at location l1, cargo c10 is situated at location l0, cargo c2 is situated at location l0, cargo c3 is at location l0, cargo c4 is at location l1, cargo c5 is present at location l1, cargo c6 is present at location l1, cargo c7 is at location l1, cargo c8 is present at location l1, cargo c9 is present at location l1, fuel f6 exists in location l1, fuel level f0 neighbors fuel level f1, fuel level f3 neighbors fuel level f4, fuel level f5 neighbors fuel level f6, fuel level f6 neighbors fuel level f7, fuel level f7 neighbors fuel level f8, fuel-levels f1 and f2 are neighbors, fuel-levels f2 and f3 are neighbors, fuel-levels f4 and f5 are neighbors, location l1 has fuel f8, location l0 is connected to location l1, location l1 is connected to location l0, space s0 neighbors space s1, vehicle v0 contains space s1 and vehicle v0 is situated at location l1.\n"
    f"Question: Given the initial condition, the following actions are planned to be performed: vehicle v0 moves from location l1 which has fuel-levels f7 and f8 to location l0. Is it possible to execute it, True or False?\n"
    f"Answer: \n"
    f"Step 1: we can confirm whether this action is executable or not by checking the initial state.\n"
    f"A vehicle moving from location A to location B must satisfy the following preconditions: the vehicle is at location A, and location l1 doesn't have f0. Vehicle v0 is at location l1, and location l1 has fuel f8. So this action is executable.\n"
    f"Step 2: we return the final answer based on the checking result.\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final Answer: True\n\n"
    f"---------------\n"
    f"(Example 2)\n"
    f"current state: Cargo c0 is situated at location l0, cargo c1 is present at location l0, cargo c2 is situated at location l1, cargo c3 is present at location l1, cargo c4 is present at location l1, cargo c5 is present at location l1, cargo c6 is present at location l0, cargo c7 is at location l0, cargo c8 is at location l1, cargo c9 is present at location l1, fuel f3 exists in location l0, fuel f8 exists in location l1, fuel level f0 neighbors fuel level f1, fuel level f1 neighbors fuel level f2, fuel level f6 neighbors fuel level f7, fuel level f7 neighbors fuel level f8, fuel-levels f2 and f3 are neighbors, fuel-levels f3 and f4 are neighbors, fuel-levels f4 and f5 are neighbors, fuel-levels f5 and f6 are neighbors, location l0 and location l1 are connected, location l1 and location l0 are connected, space s0 neighbors space s1, vehicle v0 contains space s2, vehicle v0 is situated at location l1, vehicle v1 contains space s2 and vehicle v1 is present at location l1.\n"
    f"Question: Given the initial condition, the following actions are planned to be performed: At location l1 cargo c2 is loaded in vehicle v0 with spaces s2 and s1. Is it possible to execute it, True or False?\n"
    f"Answer: \n"
    f"Step 1: we can confirm whether this action is executable or not by checking the initial state.\n"
    f"At location A loading cargo into a vehicle must satisfy the following preconditions: both the cargo and the vehicle are at location A, and the vehicle does not contain space s0. Cargo c2 is at location l1, vehicle v0 is situated at location l1, and vehicle v1 contains space s2. So this action is executable.\n"
    f"Step 2: we return the final answer based on the checking result.\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final Answer: True"
    f"---------------\n"
)

TWOSHOTCOT_STATE_MYSTERY_EXAMPLE = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"Current state: Cargo c0 is at location l0, cargo c1 is present at location l0, cargo c2 is present at location l1, cargo c3 is at location l1, cargo c4 is situated at location l1, cargo c5 is at location l1, cargo c6 is at location l0, cargo c7 is at location l0, cargo c8 is present at location l1, cargo c9 is at location l1, fuel f3 exists in location l0, fuel level f1 neighbors fuel level f2, fuel level f3 neighbors fuel level f4, fuel level f4 neighbors fuel level f5, fuel level f6 neighbors fuel level f7, fuel-levels f0 and f1 are neighbors, fuel-levels f2 and f3 are neighbors, fuel-levels f5 and f6 are neighbors, fuel-levels f7 and f8 are neighbors, location l1 has fuel f7, space s0 neighbors space s1, there is a connection between locations l0 and l1, there is a connection between locations l1 and l0, vehicle v0 has space s1, vehicle v0 is present at location l1, vehicle v1 contains space s1 and vehicle v1 is present at location l0.\n"
    f"Question: Given the initial condition, the following actions are performed: cargo c3 is loaded in vehicle v0 with space s1 and space s0 at location l1 to reach the current state. In this state, if vehicle v0 moves from location l1 which has fuel-levels f7 and f6 to location l0, is it True or False that cargo c8 is in vehicle v0?\n"
    f"Answer: \n"
    f"Step 1: We first execute the action and get the new state.\n"
    f"After taking the action 'cargo c3 is loaded in vehicle v0 with space s1 and space s0 at location l1' to reach the current state, vehicle v0 has space s0, and cargo c3 is loaded in vehicle v0. If vehicle v0 moves from location l1 which has fuel-levels f7 and f6 to location l0, vehicle v0 is at location l0, and location l1 has fuel f6.\n"
    f"Step 2: Then, we compare the state and the question and get the answer.\n"
    f"Cargo c8 is at location l1, so it is not in vehicle v0.\n"
    f"So the question is false.\n"
    f"Final Answer: False.\n\n"
    f"---------------\n"
    f"(Example 2)\n"
    f"Current state: Cargo c0 is present at location l1, cargo c1 is at location l1, cargo c2 is situated at location l1, cargo c3 is present at location l0, cargo c4 is situated at location l1, cargo c5 is at location l0, cargo c6 is at location l1, cargo c7 is situated at location l1, cargo c8 is at location l0, fuel level f1 neighbors fuel level f2, fuel level f2 neighbors fuel level f3, fuel level f3 neighbors fuel level f4, fuel level f4 neighbors fuel level f5, fuel level f5 neighbors fuel level f6, fuel-levels f0 and f1 are neighbors, fuel-levels f6 and f7 are neighbors, location l0 has fuel f3, location l1 and location l0 are connected, location l1 has fuel f7, space s0 neighbors space s1, there is a connection between locations l0 and l1, vehicle v0 has space s1, vehicle v0 is at location l0, vehicle v1 contains space s1 and vehicle v1 is situated at location l1.\n"
    f"Question: Given the initial condition, the following actions are performed: vehicle v0 moves to location l1 from location l0 that has fuel level f3 and f2 to reach the current state. In this state, if cargo c0 is loaded in vehicle v0 with space s1 and space s0 at location l1, is it True or False that fuel f2 exists in location l0?\n"
    f"Answer: \n"
    f"Step 1: We first execute the action and get the new state.\n"
    f"After taking the action 'vehicle v0 moves to location l1 from location l0 which has fuel-levels f3 and f2' to reach the current state, vehicle v0 is at location l1, and location l0 has fuel f2. If cargo c0 is loaded in vehicle v0 with space s1 and space s0 at location l1, cargo c0 is loaded in vehicle v0, and vehicle v0 has space s0.\n"
    f"Step 2: Then, we compare the state and the question and get the answer.\n"
    f"Location l0 has fuel f2.\n"
    f"So the question is true.\n"
    f"Final Answer: True."
    f"---------------\n"
)


#------------------
#Satellite domain
#------------------
SATELLITE_DOMAIN_DESCRIPTION = (
    f"[Domain Description]\n"
    
    f"Satellite domain includes instrument and satellite. Instrument has fixed location, carried by a satellite. Instrument is used to take image of target such as star, groundstation, phemonemon or planet. Different instruments support different format such as image0, infrared1, spectrograph3, etc. An instrument must be turned(switched) on and calibrated before it is used to take images. Different instruments use different calibration target to calibrate, only calibration target can be used to calibrate an instrument. Satellite can carries one or more instruments. A satellite can only point to a target at a time. Target includes star, phenomenon, groundstation and planet, etc.\n"
    
    f"Different properties are used to describe current states of different objects. For instrument we use: on satellite_x, compatible(supported) with image_x/infrared_x/spectrograph_x, turned(switched) on/turned(switched) off, is calibrated/not calibrated, star_x/planet_x/phenomenon_x/groundstation_x is its calibration target. For satellite we use: carries instrument_x, has power, pointing to planet_x/phenomenon_x/groundstation_x/star_x.\n"
    
    f"Following actions are executable only if all preconditions are met, if any condition are not satisfied, the action is not executable.\n"
    
    f"An instrument on a satellite can be \"switched(turned) on\". This action is executable only if all following preconditions are satisfied: the instrument is on the satellite, the satellite has power supply.\n"
    
    f"An instrument on a satellite can be \"switched(turned) off\". This action is executable only if all following preconditions are satisfied: the instrument is on the satellite, the instrument is switched(turned) on.\n"
    
    f"An instrument on the satellite can be \"calibrated\" for a target. This action is executable only if all following preconditions are satisfied: the instrument is on the satellite, the instrument can be calibrated using the target(calibration target), the satellite is pointing to the calibration target, the instrument is switched(turned) on.\n"
    
    f"An instrument on a satellite can 'take' an image of the target in the specific format. This action is executable only if all following preconditions are satisfied: the satellite is currently pointing the target, the instrument is on the satellite, the instrument is turned on, the instrument is calibrated, the instrument supports the specific fortmat.\n"
    
    f"A satellite can 'turn' from target A to target B. This action is executable only if all following preconditions are satisfied: the satellite is currently pointing target A.\n"
    
    f"Executing an action will change states of related objects.\n"
    
    f"An instrument on a satellite is \"switched(turned) on\" will result in: the instrument is turned on, the instrument is not calibrated, the satellite doesn't have power supply.\n"
    
    f"An instrument on a satellite is \"switched(turned) off\" will result in: the instrument is turned off, the satellite has power supply.\n"
    
    f"An instrument on the satellite is \"calibrated\" for a target will result in: the instrument is calibrated.\n"
    
    f"An instrument on a satellite 'take' an image of the target in the specific format will result in: the instrument has target's image in the specific format.\n"
    
    f"A satellite 'turn' from target A to target B will result in: the satellite is currently pointing target B, the sattlite is not pointing to target A.\n"
)


INITIAL_STATE_EXTRACTOR_SATELLITE_PROMPT =(
    f"This is initial states of all objects of satellite domain, you are required to extract states of all objects based on examples above. Your answer must satisfy all the following requirements. First, think and respond with the format from the example above, including the word choice and paragraph structure. Second, each object's state should contain all properties mentioned in the domain description above. Third, organize states of all objects in one paragraph without other contents. Besides, don't use any markdown formatting."    
)


INITIAL_STATE_EXTRACTOR_SATELLITE_EXAMPLE = (
    f"[Examples]\n"
    f"Initial state example 1: Calibration of instrument2 for groundstation5 is complete, calibration of instrument2 for groundstation7 is complete, calibration of instrument2 for star9 is complete, calibrat ion of instrument3 for star6 is complete, for groundstation0, instrument1 is calibrated, for star9, instrument0 is calibrated, groundstation3 is where satellite0 is pointed, image0 is compatible with instrument1, image0 is supported by instrument3, image2 is compatible with instrument2, image2 is compatible with instrument3, image3 is compatible with instrument1, image3 is compatible with instrument2, image3 is supported by instrument3, infrared1 is compatible with instrument0, infrared1 is supported by instrument1, instrument0 is calibrated for star1, instrument0 supports image3, instrument2 is on board satellite0, instrument3 is calibrated for groundstation5, instrument3 is calibrated for star8, satellite0 carries instrument1 on board, satellite0 has instrument0 on board, satellite0 has power available, satellite1 carries instrument3 on board, satellite1 has power available and satellite1 is pointing to phenomenon10.\n"
    
    f"Extracted from initial state example 1:\n"
    f"We can find following objects in the intial state description: instrument0, instrument1, instrument2, instrument3, satellite0, satellite1.\n"
    f"Then, we find all descriptions related to an object, and organize then into the required format. Repeat this process until all objects' states are extracted, and each object's state contains all related properties.\n"
    
    f"satellite0 has instrument0 on board, for star9, instrument0 is calibrated, instrument0 is calibrated for star1, infrared1 is compatible with instrument0, instrument0 supports image3. ::: Instrument0: on satellite0, is calibrated, star9 is its calibration target, star1 is its calibration target, compatible with infrared1, compatible with image3.\n"
    
    f"for groundstation0, instrument1 is calibrated, image0 is compatible with instrument1, image3 is compatible with instrument1, infrared1 is supported by instrument1, satellite0 carries instrument1 on board, ::: Instrument1: on satellite0, is calibrated, groundstation0 is its calibration target, compatible with image0, compatible with image3, compatible with infrared1.\n"
    
    f"Calibration of instrument2 for groundstation5 is complete, calibration of instrument2 for groundstation7 is complete, calibration of instrument2 for star9 is complete, image2 is compatible with instrument2, image3 is compatible with instrument2, instrument2 is on board satellite0. ::: Instrument2: on satellite0, is calibrated, groundstation5 is its calibration target, groundstation7 is its calibration target, star9 is its calibration target, compatible with image2, compatible with image3.\n"
    
    f"satellite1 carries instrument3 on board, calibration of instrument3 for star6 is complete, instrument3 is calibrated for star8, instrument3 is calibrated for groundstation5, image0 is supported by instrument3, image2 is compatible with instrument3, image3 is supported by instrument3. ::: Instrument3: on satellite1, is calibrated, star6 is its calibration target, star8 is its calibration target, groundstation5 is its calibration target, compatible with image0, compatible with image2, compatible with image3.\n"
    
    f"satellite0 carries instrument1 on board, instrument2 is on board satellite0, satellite0 has instrument0 on board, satellite0 has power available, groundstation3 is where satellite0 is pointed. ::: Satellite0: carries instrument0, carries instrument1, carries instrument2, pointing groundstation3, has power supply.\n"
    
    f"satellite1 carries instrument3 on board, satellite1 has power available, and satellite1 is pointing to phenomenon10. ::: Satellite1: carries instrument3, pointing to phenomenon10, has power supply.\n"
    
    f"After extracting all states, we organize states of all objects into one paragraph.\n"
    f"Instrument0: on satellite0, is calibrated, star9 is its calibration target, star1 is its calibration target, compatible with infrared1, compatible with image3. Instrument1: on satellite0, is calibrated, groundstation0 is its calibration target, compatible with image0, compatible with image3, compatible with infrared1. Instrument2: on satellite0, is calibrated, groundstation5 is its calibration target, groundstation7 is its calibration target, star9 is its calibration target, compatible with image2, compatible with image3. Instrument3: on satellite1, is calibrated, star6 is its calibration target, star8 is its calibration target, groundstation5 is its calibration target, compatible with image0, compatible with image2, compatible with image3. Satellite0: carries instrument0, carries instrument1, carries instrument2, pointing groundstation3, has power supply. Satellite1: carries instrument3, pointing to phenomenon10, has power supply.\n"
    f"----------------\n"
    
    f"Initial state example 2:\n" 
    f"For star1, instrument1 is calibrated, image0 is compatible with instrument1, image2 is compatible with instrument0, image2 is supported by instrument1, image4 is supported by instrument1, instrument0 is calibrated for star1, instrument1 supports image5, power is available for satellite1, satellite0 has instrument0 on board, satellite0 has power available, satellite0 is aimed towards phenomenon5, satellite1 has instrument1 on board, satellite1 is pointing to star3, spectrograph1 is compatible with instrument1 and spectrograph3 is supported by instrument1.\n"
    
    f"Extracted from initial state example 2:\n"
    f"We can find following objects in the intial state description: instrument0, instrument1, satellite0, satellite1.\n"
    f"Then, we find all descriptions related to an object, and organize then into the required format. Repeat this process until all objects' states are extracted, and each object's state contains all related properties.\n"
    
    f"image2 is compatible with instrument0, instrument0 is calibrated for star1, satellite0 has instrument0 on board. ::: Instrument0: on satellite0, is calibrated, star1 is its calibration target, compatible with image2.\n"
    
    f"satellite1 has instrument1 on board, For star1, instrument1 is calibrated, image0 is compatible with instrument1, image2 is supported by instrument1, image4 is supported by instrument1, instrument1 supports image5, spectrograph1 is compatible with instrument1 and spectrograph3 is supported by instrument1. ::: Instrument1: on satellite1, is calibrated, star1 is its calibration target, compatible with image0, compatible with image2, compatible with image4, compatible with image5, compatible with spectrograph1, compatible with spectrograph3.\n"
    
    f"satellite0 has instrument0 on board, satellite0 has power available, satellite0 is aimed towards phenomenon5, ::: Satellite0: carries instrument0, has power supply, pointing to phenomenon5.\n"
    
    f"power is available for satellite1, satellite1 has instrument1 on board, satellite1 is pointing to star3. ::: Satellite1: carries instrument1, has power supply, pointing to star3.\n"
    
    f"After extracting all states, we organize states of all objects into a new paragraph.\n"
    f"Instrument0: on satellite0, is calibrated, star1 is its calibration target, compatible with image2. Instrument1: on satellite1, is calibrated, star1 is its calibration target, compatible with image0, compatible with image2, compatible with image4, compatible with image5, compatible with spectrograph1, compatible with spectrograph3. Satellite0: carries instrument0, has power supply, pointing phenomenon5. Satellite1: carries instrument1, has power supply, pointing star3.\n"
    f"----------------\n"
)


QUESTION_EXTRACTOR_SATELLITE_EXAMPLE =(
    f"[Example]\n"
    f"Plan 1: Given the initial condition, the following actions are performed: instrument1 that is on satellite1 is turned on to reach the current state. In this state, is it True or False that satellite0 does not have power?\n"
    f"Question extracted from plan 1: In this state, is it True or False that satellite0 does not have power?\n"
    f"------------\n"
    f"Plan 2: Given the initial condition, the following actions are performed: instrument1 on satellite0 is switched on, from groundstation2, satellite0 turns to groundstation0, calibration of instrument1 which is on satellite0 to groundstation0 is complete, from groundstation0, satellite0 turns to planet11, instrument1 which is on satellite0 takes an image of planet11 in image5, instrument1 which is on satellite0 takes an image of planet11 in image6, satellite0 turns from planet11 to planet13, instrument1 which is on satellite0 takes an image of planet13 in image5, instrument1 which is on satellite0 takes an image of planet13 in spectrograph2, satellite0 turns from planet13 to star10, image of star10 is taken with instrument1 on satellite0 in image6, instrument1 which is on satellite0 takes an image of star10 in spectrograph2, on satellite0, instrument1 is switched off, on satellite0, instrument2 is switched on, from star10, satellite0 turns to star4, instrument2 that is on satellite0 is calibrated to star4, from star4, satellite0 turns to star16, satellite0's instrument2 takes an image of star16 in image0 and on satellite0, instrument2 is switched off to reach the current state. In this state, if on satellite0, instrument3 is switched on, is it True or False that power is not available for satellite0?\n"
    f"Question extracted from plan 2: In this state, if on satellite0, instrument3 is switched on, is it True or False that power is not available for satellite0?\n"
    f"------------\n"
    f"Plan 3:Given the initial condition, the following actions are performed: instrument3 on satellite1 is switched on, instrument0 on satellite0 is switched on, satellite1 turns to groundstation5 from phenomenon10, instrument3 is calibrated on satellite1 to groundstation5, satellite1 turns to phenomenon16 from groundstation5, image of phenomenon16 is taken with instrument3 on satellite1 in image3, satellite1 turns to phenomenon17 from phenomenon16, satellite1's instrument3 takes an image of phenomenon17 in image3, satellite1 turns to planet11 from phenomenon17 and image of planet11 is taken with instrument3 on satellite1 in image3 to reach the current state. In this state, are all of the following valid properties of the state that involve negations? calibration of instrument0 for groundstation4 is complete, calibration of instrument0 for groundstation5 is incomplete, calibration of instrument0 for phenomenon17 is complete, calibration of instrument0 for planet13 is complete, calibration of instrument0 is complete, calibration of instrument1 for groundstation5 is incomplete, calibration of instrument1 for phenomenon10 is complete, calibration of instrument1 for planet12 is incomplete, calibration of instrument1 for planet14 is incomplete, calibration of instrument1 for star15 is complete, calibration of instrument1 for star8 is incomplete, calibration of instrument1 is complete, calibration of instrument2 for groundstation3 is incomplete, calibration of instrument2 for phenomenon10 is incomplete, calibration of instrument2 for planet13 is complete, calibration of instrument2 for star15 is complete, calibration of instrument2 is incomplete, calibration of instrument3 for groundstation2 is complete, calibration of instrument3 for planet13 is complete, for groundstation0, instrument0 is calibrated, for groundstation2, instrument0 is not calibrated, for groundstation2, instrument1 is calibrated, for groundstation3, instrument0 is calibrated, for groundstation3, instrument1 is calibrated, for groundstation4, instrument2 is calibrated, for groundstation7, instrument3 is not calibrated, for phenomenon10, instrument0 is not calibrated, for phenomenon10, instrument3 is not calibrated, for phenomenon16, instrument1 is calibrated, for phenomenon16, instrument3 is not calibrated, for phenomenon17, instrument1 is not calibrated, for phenomenon17, instrument2 is calibrated, for planet11, instrument2 is calibrated, for planet12, instrument0 is calibrated, for planet12, instrument3 is not calibrated, for planet13, instrument1 is not calibrated, for star1, instrument2 is not calibrated, for star6, instrument1 is not calibrated, for star8, instrument0 is not calibrated, groundstation0 is not where satellite0 is pointed, groundstation2 is not where satellite1 is pointed, groundstation5 is not where satellite0 is pointed, groundstation5 is not where satellite1 is pointed, groundstation7 is not where satellite0 is pointed, groundstation7 is where satellite1 is pointed, image of groundstation0 exists in image0, image of groundstation0 exists in infrared1, image of groundstation2 does not exist in infrared1, image of groundstation3 does not exist in image2, image of groundstation3 exists in infrared1, image of groundstation4 does not exist in image3, image of groundstation5 does not exist in image3, image of groundstation5 exists in image2, image of groundstation5 exists in infrared1, image of groundstation7 exists in image0, image of groundstation7 exists in infrared1, image of phenomenon16 does not exist in infrared1, image of phenomenon17 does not exist in infrared1, image of phenomenon17 exists in image0, image of planet11 exists in image2, image of planet11 exists in infrared1, image of planet12 does not exist in image3, image of planet13 does not exist in image2, image of planet13 does not exist in infrared1, image of planet13 exists in image0, image of planet13 exists in image3, image of planet14 exists in infrared1, image of star1 does not exist in infrared1, image of star1 exists in image0, image of star15 exists in image3, image of star6 does not exist in image2, image of star6 does not exist in image3, image of star6 exists in infrared1, image of star8 exists in image2, image of star9 does not exist in image3, image of star9 does not exist in infrared1, image of star9 exists in image2, image2 is compatible with instrument0, image2 is not compatible with instrument1, infrared1 is compatible with instrument3, infrared1 is not compatible with instrument2, instrument0 is calibrated for groundstation7, instrument0 is calibrated for planet11, instrument0 is calibrated for star15, instrument0 is not calibrated for phenomenon16, instrument0 is not calibrated for planet14, instrument0 is not calibrated for star6, instrument0 supports image0, instrument1 is calibrated for groundstation4, instrument1 is calibrated for groundstation7, instrument1 is not calibrated for planet11, instrument1 is not calibrated for star1, instrument1 is not calibrated for star9, instrument1 is turned on, instrument2 is calibrated for star6, instrument2 is not calibrated for groundstation0, instrument2 is not calibrated for groundstation2, instrument2 is not calibrated for phenomenon16, instrument2 is not calibrated for planet12, instrument2 is not calibrated for planet14, instrument2 is not calibrated for star8, instrument2 is not powered on, instrument2 is on board satellite1, instrument2 supports image0, instrument3 is calibrated for groundstation4, instrument3 is calibrated for planet14, instrument3 is calibrated for star1, instrument3 is not calibrated for groundstation0, instrument3 is not calibrated for groundstation3, instrument3 is not calibrated for phenomenon17, instrument3 is not calibrated for planet11, instrument3 is not calibrated for star15, instrument3 is not calibrated for star9, phenomenon10 is where satellite0 is pointed, phenomenon16 is not where satellite0 is pointed, phenomenon17 is not where satellite0 is pointed, planet13 is where satellite1 is pointed, power is available for satellite1, satellite0 does not carry instrument3 on board, satellite0 has power, satellite0 is aimed towards planet13, satellite0 is aimed towards star6, satellite0 is not aimed towards groundstation2, satellite0 is not aimed towards groundstation4, satellite0 is not aimed towards star8, satellite0 is not pointing to planet11, satellite0 is pointing to planet12, satellite0 is pointing to planet14, satellite1 does not carry instrument0 on board, satellite1 has instrument1 on board, satellite1 is aimed towards groundstation3, satellite1 is aimed towards phenomenon10, satellite1 is aimed towards phenomenon17, satellite1 is aimed towards planet12, satellite1 is aimed towards star1, satellite1 is not aimed towards phenomenon16, satellite1 is not aimed towards star15, satellite1 is not aimed towards star6, satellite1 is not aimed towards star8, satellite1 is not pointing to groundstation0, satellite1 is not pointing to planet14, satellite1 is pointing to groundstation4, satellite1 is pointing to star9, star1 is where satellite0 is pointed, star15 is where satellite0 is pointed, star9 is where satellite0 is pointed, there is an image of groundstation0 in image2, there is an image of groundstation0 in image3, there is an image of groundstation2 in image0, there is an image of groundstation3 in image0, there is an image of groundstation4 in image0, there is an image of phenomenon10 in image2, there is an image of phenomenon10 in image3, there is an image of phenomenon16 in image2, there is an image of planet12 in image0, there is an image of planet12 in infrared1, there is an image of planet14 in image2, there is an image of star1 in image2, there is an image of star15 in image0, there is an image of star15 in image2, there is an image of star15 in infrared1, there is an image of star8 in image0, there is an image of star8 in image3, there is an image of star9 in image0, there is no image of direction groundstation2 in image2, there is no image of direction groundstation2 in image3, there is no image of direction groundstation3 in image3, there is no image of direction groundstation4 in image2, there is no image of direction groundstation4 in infrared1, there is no image of direction groundstation5 in image0, there is no image of direction groundstation7 in image2, there is no image of direction groundstation7 in image3, there is no image of direction phenomenon10 in image0, there is no image of direction phenomenon10 in infrared1, there is no image of direction phenomenon16 in image0, there is no image of direction phenomenon17 in image2, there is no image of direction planet11 in image0, there is no image of direction planet12 in image2, there is no image of direction planet14 in image0, there is no image of direction planet14 in image3, there is no image of direction star1 in image3, there is no image of direction star6 in image0 and there is no image of direction star8 in infrared1. Respond with True or False.\n"
    f"Question extracted from plan 3: In this state, are all of the following valid properties of the state that involve negations? calibration of instrument0 for groundstation4 is complete, calibration of instrument0 for groundstation5 is incomplete, calibration of instrument0 for phenomenon17 is complete, calibration of instrument0 for planet13 is complete, calibration of instrument0 is complete, calibration of instrument1 for groundstation5 is incomplete, calibration of instrument1 for phenomenon10 is complete, calibration of instrument1 for planet12 is incomplete, calibration of instrument1 for planet14 is incomplete, calibration of instrument1 for star15 is complete, calibration of instrument1 for star8 is incomplete, calibration of instrument1 is complete, calibration of instrument2 for groundstation3 is incomplete, calibration of instrument2 for phenomenon10 is incomplete, calibration of instrument2 for planet13 is complete, calibration of instrument2 for star15 is complete, calibration of instrument2 is incomplete, calibration of instrument3 for groundstation2 is complete, calibration of instrument3 for planet13 is complete, for groundstation0, instrument0 is calibrated, for groundstation2, instrument0 is not calibrated, for groundstation2, instrument1 is calibrated, for groundstation3, instrument0 is calibrated, for groundstation3, instrument1 is calibrated, for groundstation4, instrument2 is calibrated, for groundstation7, instrument3 is not calibrated, for phenomenon10, instrument0 is not calibrated, for phenomenon10, instrument3 is not calibrated, for phenomenon16, instrument1 is calibrated, for phenomenon16, instrument3 is not calibrated, for phenomenon17, instrument1 is not calibrated, for phenomenon17, instrument2 is calibrated, for planet11, instrument2 is calibrated, for planet12, instrument0 is calibrated, for planet12, instrument3 is not calibrated, for planet13, instrument1 is not calibrated, for star1, instrument2 is not calibrated, for star6, instrument1 is not calibrated, for star8, instrument0 is not calibrated, groundstation0 is not where satellite0 is pointed, groundstation2 is not where satellite1 is pointed, groundstation5 is not where satellite0 is pointed, groundstation5 is not where satellite1 is pointed, groundstation7 is not where satellite0 is pointed, groundstation7 is where satellite1 is pointed, image of groundstation0 exists in image0, image of groundstation0 exists in infrared1, image of groundstation2 does not exist in infrared1, image of groundstation3 does not exist in image2, image of groundstation3 exists in infrared1, image of groundstation4 does not exist in image3, image of groundstation5 does not exist in image3, image of groundstation5 exists in image2, image of groundstation5 exists in infrared1, image of groundstation7 exists in image0, image of groundstation7 exists in infrared1, image of phenomenon16 does not exist in infrared1, image of phenomenon17 does not exist in infrared1, image of phenomenon17 exists in image0, image of planet11 exists in image2, image of planet11 exists in infrared1, image of planet12 does not exist in image3, image of planet13 does not exist in image2, image of planet13 does not exist in infrared1, image of planet13 exists in image0, image of planet13 exists in image3, image of planet14 exists in infrared1, image of star1 does not exist in infrared1, image of star1 exists in image0, image of star15 exists in image3, image of star6 does not exist in image2, image of star6 does not exist in image3, image of star6 exists in infrared1, image of star8 exists in image2, image of star9 does not exist in image3, image of star9 does not exist in infrared1, image of star9 exists in image2, image2 is compatible with instrument0, image2 is not compatible with instrument1, infrared1 is compatible with instrument3, infrared1 is not compatible with instrument2, instrument0 is calibrated for groundstation7, instrument0 is calibrated for planet11, instrument0 is calibrated for star15, instrument0 is not calibrated for phenomenon16, instrument0 is not calibrated for planet14, instrument0 is not calibrated for star6, instrument0 supports image0, instrument1 is calibrated for groundstation4, instrument1 is calibrated for groundstation7, instrument1 is not calibrated for planet11, instrument1 is not calibrated for star1, instrument1 is not calibrated for star9, instrument1 is turned on, instrument2 is calibrated for star6, instrument2 is not calibrated for groundstation0, instrument2 is not calibrated for groundstation2, instrument2 is not calibrated for phenomenon16, instrument2 is not calibrated for planet12, instrument2 is not calibrated for planet14, instrument2 is not calibrated for star8, instrument2 is not powered on, instrument2 is on board satellite1, instrument2 supports image0, instrument3 is calibrated for groundstation4, instrument3 is calibrated for planet14, instrument3 is calibrated for star1, instrument3 is not calibrated for groundstation0, instrument3 is not calibrated for groundstation3, instrument3 is not calibrated for phenomenon17, instrument3 is not calibrated for planet11, instrument3 is not calibrated for star15, instrument3 is not calibrated for star9, phenomenon10 is where satellite0 is pointed, phenomenon16 is not where satellite0 is pointed, phenomenon17 is not where satellite0 is pointed, planet13 is where satellite1 is pointed, power is available for satellite1, satellite0 does not carry instrument3 on board, satellite0 has power, satellite0 is aimed towards planet13, satellite0 is aimed towards star6, satellite0 is not aimed towards groundstation2, satellite0 is not aimed towards groundstation4, satellite0 is not aimed towards star8, satellite0 is not pointing to planet11, satellite0 is pointing to planet12, satellite0 is pointing to planet14, satellite1 does not carry instrument0 on board, satellite1 has instrument1 on board, satellite1 is aimed towards groundstation3, satellite1 is aimed towards phenomenon10, satellite1 is aimed towards phenomenon17, satellite1 is aimed towards planet12, satellite1 is aimed towards star1, satellite1 is not aimed towards phenomenon16, satellite1 is not aimed towards star15, satellite1 is not aimed towards star6, satellite1 is not aimed towards star8, satellite1 is not pointing to groundstation0, satellite1 is not pointing to planet14, satellite1 is pointing to groundstation4, satellite1 is pointing to star9, star1 is where satellite0 is pointed, star15 is where satellite0 is pointed, star9 is where satellite0 is pointed, there is an image of groundstation0 in image2, there is an image of groundstation0 in image3, there is an image of groundstation2 in image0, there is an image of groundstation3 in image0, there is an image of groundstation4 in image0, there is an image of phenomenon10 in image2, there is an image of phenomenon10 in image3, there is an image of phenomenon16 in image2, there is an image of planet12 in image0, there is an image of planet12 in infrared1, there is an image of planet14 in image2, there is an image of star1 in image2, there is an image of star15 in image0, there is an image of star15 in image2, there is an image of star15 in infrared1, there is an image of star8 in image0, there is an image of star8 in image3, there is an image of star9 in image0, there is no image of direction groundstation2 in image2, there is no image of direction groundstation2 in image3, there is no image of direction groundstation3 in image3, there is no image of direction groundstation4 in image2, there is no image of direction groundstation4 in infrared1, there is no image of direction groundstation5 in image0, there is no image of direction groundstation7 in image2, there is no image of direction groundstation7 in image3, there is no image of direction phenomenon10 in image0, there is no image of direction phenomenon10 in infrared1, there is no image of direction phenomenon16 in image0, there is no image of direction phenomenon17 in image2, there is no image of direction planet11 in image0, there is no image of direction planet12 in image2, there is no image of direction planet14 in image0, there is no image of direction planet14 in image3, there is no image of direction star1 in image3, there is no image of direction star6 in image0 and there is no image of direction star8 in infrared1. Respond with True or False.\n"
    f"------------\n"
)


ACTION_TAKER_SATELLITE_PROMPT =(
    f"Based on the domain description and examples above, take the action and return the new state of all objects. Your answer must satisfy all the following requirements. First, think and respond like examples above, you are required to return states of all objects(instruments and satellites), including states that are not effected by the action. Second, each object's state must contain all properties mentioned in the domain description above. Third, after your analysis, please return states of all objects in a new paragraph as the end of your answer, and use the format such as: \"Instrument3: on satellite1, is calibrated, star6 is its calibration target, compatible with image0, compatible with image2, compatible with image3. Satellite0: carries instrument1, carries instrument0, carries instrument2, has power available.\" Besides, don't use any markdown formatting."
)


ACTION_TAKER_SATELLITE_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: Instrument0: on satellite0, is calibrated, groundstation2 is its  calibration target, star0 is its calibration target, compatible with spectrograph0, compatible with thermograph4. Instrument1: on satellite0, is calibrated, groundstation4 is its calibration target, star8 is its calibration target, compatible with spectrograph0, compatible with spectrograph1. Instrument2: on satellite1, is calibrated, groundstation4 is its calibration target, star7 is its calibration target, compatible with infrared3, compatible with spectrograph0, compatible with spectrograph2. Instrument3: on satellite1, is calibrated, star6 is its calibration target, compatible with spectrograph1, compatible with spectrograph2. Satellite0: carries instrument0, carries instrument1, has power supply, pointing to star1. Satellite1: carries instrument2, carries instrument3, has power supply, pointing to groundstation4.\n"
    f"Action 1: Instrument3 that is on satellite1 is turned on.\n"
    f"Answer 1:\n" 
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Instrument3: on satellite1, is calibrated, star6 is its calibration target, compatible with spectrograph1, compatible with spectrograph2. Satellite1: carries instrument2, carries instrument3, has power supply, pointing to groundstation4.\n"
    f"Based on the domain description, an instrument on a satellite can be \"switched(turned) on\". This action will result in: the instrument is turned on, the instrument is not calibrated, the satellite doesn't have power supply.\n"
    f"the instrument is turned on, the instrument is not calibrated ::: Instrument3: on satellite1, switched on, not calibrated, star6 is its calibration target, compatible with spectrograph1, compatible with spectrograph2.\n"
    f"the satellite doesn't have power supply. ::: Satellite1: carries instrument2, carries instrument3, doesn't have power supply, pointing to groundstation4.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into one paragraph.\n"
    f"Instrument0: on satellite0, is calibrated, groundstation2 is its  calibration target, star0 is its calibration target, compatible with spectrograph0, compatible with thermograph4. Instrument1: on satellite0, is calibrated, groundstation4 is its calibration target, star8 is its calibration target, compatible with spectrograph0, compatible with spectrograph1. Instrument2: on satellite1, is calibrated, groundstation4 is its calibration target, star7 is its calibration target, compatible with infrared3, compatible with spectrograph0, compatible with spectrograph2. Instrument3: on satellite1, switched on, not calibrated, star6 is its calibration target, compatible with spectrograph1, compatible with spectrograph2. Satellite0: carries instrument0, carries instrument1, has power supply, pointing to star1. Satellite1: carries instrument2, carries instrument3, doesn't have power supply, pointing to groundstation4.\n"
    f"------------\n"
    f"Current state example 2: Instrument0: on satellite0, is calibrated, star1 is its calibration target, star9 is its calibration target, compatible with image3, compatible with infrared1. Instrument1: on satellite0, is calibrated, groundstation0 is its calibration target, compatible with image0, compatible with image3, compatible with infrared1. Instrument2: on satellite0, is calibrated, star9 is its calibration target, groundstation5 is its calibration target, groundstation7 is its calibration target, compatible with image2, compatible with image3. Instrument3: on satellite1, is calibrated, star6 is its calibration target, star8 is its calibration target, groundstation5 is its calibration target, compatible with image0, compatible with image2, compatible with image3. Satellite0: carries instrument0, carries instrument1, carries instrument2, pointing groundstation3, has power supply. Satellite1: carries instrument3, pointing to phenomenon10, has power supply.\n"        
    f"Action 2: Satellite1 turns from phenomenon10 to groundstation5.\n"
    f"Answer 2:\n" 
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"    
    f"Satellite1: carries instrument3, pointing to phenomenon10, has power supply.\n"    
    f"Based on the domain description, A satellite can 'turn' from target A to target B. This action will result in: the satellite is currently pointing target B, the sattlite is not pointing to target A.\n"
    f"the satellite is currently pointing target B, the sattlite is not pointing to target A. ::: Satellite1: carries instrument3, pointing to groundstation5, has power supply.\n"    
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into one paragraph.\n"
    f"Instrument0: on satellite0, is calibrated, star1 is its calibration target, star9 is its calibration target, compatible with image3, compatible with infrared1. Instrument1: on satellite0, is calibrated, groundstation0 is its calibration target, compatible with image0, compatible with image3, compatible with infrared1. Instrument2: on satellite0, is calibrated, star9 is its calibration target, groundstation5 is its calibration target, groundstation7 is its calibration target, compatible with image2, compatible with image3. Instrument3: on satellite1, is calibrated, star6 is its calibration target, star8 is its calibration target, groundstation5 is its calibration target, compatible with image0, compatible with image2, compatible with image3. Satellite0: carries instrument0, carries instrument1, carries instrument2, pointing groundstation3, has power supply. Satellite1: carries instrument3, pointing to groundstation5, has power supply.\n"
    f"------------\n"
    f"Current state example 3: Instrument0: on satellite0, is calibrated, star0 is its calibration target, groundstation2 is its calibration target, groundstation4 is its calibration target, compatible with spectrograph0, compatible with thermograph4. Instrument1: on satellite0, is calibrated, star8 is its calibration target, groundstation2 is its calibration target, groundstation4 is its calibration target, compatible with spectrograph1, compatible with spectrograph0. Instrument2: on satellite1, is calibrated, groundstation9 is its calibration target, star7 is its calibration target, compatible with infrared3, compatible with spectrograph0, compatible with spectrograph2. Instrument3: on satellite1, switched on, is calibrated, star6 is its calibration target, compatible with spectrograph1, compatible with spectrograph2. Satellite0: carries instrument0, carries instrument1, has power supply, pointing to star1. Satellite1: carries instrument2, carries instrument3, doesn't have power supply, pointing to groundstation4.\n"
    f"Action 3: An image of groundstation4 is taken with instrument3 on satellite1 in spectrograph1.\n"
    f"Answer 3:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n" 
    f"Instrument3: on satellite1, switched on, is calibrated, star6 is its calibration target, compatible with spectrograph1, compatible with spectrograph2.\n"
    f"Based on the domain description, an instrument on a satellite 'take' an image of the target in the specific format. This action will result in: the instrument has target's image in the specific format.\n"
    f"the instrument has target's image in the specific format. ::: Instrument3: on satellite1, switched on, is calibrated, star6 is its calibration target, compatible with spectrograph1, compatible with spectrograph2, has groundstation4's image in spectrograph1.\n"
    f"------------\n"
)



EXECUTABILITY_CHECKER_SATELLITE_EXAMPLE = (
    f"[Examples]\n"
    f"Current state example 1: Instrument0: on satellite0, is calibrated, star0 is its calibration target, groundstation2 is its calibration target, groundstation4 is its calibration target, compatible with spectrograph0, compatible with thermograph4. Instrument1: on satellite0, is calibrated, star8 is its calibration target, groundstation2 is its calibration target, groundstation4 is its calibration target, compatible with spectrograph1, compatible with spectrograph0. Instrument2: on satellite1, is calibrated, groundstation9 is its calibration target, star7 is its calibration target, compatible with infrared3, compatible with spectrograph0, compatible with spectrograph2. Instrument3: on satellite1, is calibrated, star6 is its calibration target, compatible with spectrograph1, compatible with spectrograph2. Satellite0: carries instrument0, carries instrument1, has power supply, pointing to star1. Satellite1: carries instrument2, carries instrument3, has power supply, pointing to groundstation4.\n"
    f"Action 1: Instrument3 on satellite1 is switched on.\n"
    f"Answer 1:\n"
    f"In order to check whether this action is executable or not, we first need to find states of objects related to this action, then check whether all preconditions of this action are satisfied.\n"
    f"Instrument3: on satellite1, is calibrated, star6 is its calibration target, compatible with spectrograph1, compatible with spectrograph2. Satellite1: carries instrument2, carries instrument3, has power supply, pointing to groundstation4.\n"
    f"Based on the domain description, an instrument on a satellite can be \"switched(turned) on\". This action is executable only if all following preconditions are satisfied: the instrument is on the satellite, the satellite has power supply.\n"
    f"the instrument is on the satellite ::: Instrument3: on satellite1===> SATISFY\n"
    f"the satellite has power supply. ::: Satellite1: carries instrument2, carries instrument3, has power supply, pointing to groundstation4. ===> SATISFY\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final answer: True.\n"
    f"------------\n"
    f"Current state example 2: Instrument0: on satellite0, star1 is its calibration target, star9 is its calibration target, compatible with image3, compatible with infrared1. Instrument1: on satellite0, groundstation0 is its calibration target, compatible with image0, compatible with infrared1, compatible with image3. Instrument2: on satellite0, star9 is its calibration target, compatible with image2, compatible with image3. Instrument3: on satellite1, switched on, not calibrated, star6 is its calibration target, star8 is its calibration target, groundstation5 is its calibration target, compatible with image0, compatible with image2, compatible with image3. Satellite0: carries instrument0, carries instrument1, carries instrument2, has power supply, pointing groundstation3. Satellite1: carries instrument3, doesn't have power supply, pointing groundstation5.\n"
    f"Action 2: Instrument3 that is on satellite1 is calibrated to groundstation5.\n"
    f"Answer 2:\n"
    f"In order to check whether this action is executable or not, we first need to find states of objects related to this action, then check whether all preconditions of this action are satisfied.\n"
    f"Instrument3: on satellite1, switched on, not calibrated, star6 is its calibration target, star8 is its calibration target, groundstation5 is its calibration target, compatible with image0, compatible with image2, compatible with image3. Satellite1: carries instrument3, doesn't have power supply, pointing groundstation5.\n"
    f"Based on the domain description, an instrument on the satellite can be \"calibrated\" for a target. This action is executable only if all following preconditions are satisfied: the instrument is on the satellite, the instrument can be calibrated using the target(calibration target), the satellite is pointing to the calibration target, the instrument is switched(turned) on.\n"
    f"the instrument is on the satellite ::: Instrument3: on satellite1 ===>SATISFY\n"
    f"the instrument can be calibrated using the target(calibration target) ::: Instrument3: on satellite1, switched on, not calibrated, star6 is its calibration target, star8 is its calibration target, groundstation5 is its calibration target, ===> SATISFY\n"
    f"the satellite is pointing to the calibration target ::: Satellite1: carries instrument3, doesn't have power supply, pointing groundstation5. ===> SATISFY\n"
    f"the instrument is switched(turned) on ::: Instrument3: on satellite1, switched on,  ===> SATISFY\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final answer: True.\n"
    f"------------\n"
    f"Current state example 3: Instrument0: on satellite0, is calibrated, groundstation7 is its calibration target, compatible with image6. Instrument1: on satellite0, is calibrated,  groundstation0 is its calibration target, groundstation6 is its calibration target, compatible with image5, compatible with image6, compatible with spectrograph2. Instrument2: on satellite0, is calibrated, star4 is its calibration target, compatible with image0, compatible with image1. Instrument3: on satellite0, is calibrated, groundstation9 is its calibration target, compatible with image1, compatible with spectrograph4, compatible with thermograph3. Instrument4: on satellite1, is calibrated, groundstation8 is its calibration target, compatible with image1, compatible with infrared7. Satellite0: carries instrument0, carries instrument1, carries instrument2, carries instrument3, has power supply, pointing groundstation2. Satellite1: carries instrument4, has power supply, pointing planet13.\n"
    f"Action 3: Satellite0 turns from planet13 to groundstation0.\n"
    f"Answer 3:\n"
    f"In order to check whether this action is executable or not, we first need to find states of objects related to this action, then check whether all preconditions of this action are satisfied.\n"
    f"Satellite0: carries instrument0, carries instrument1, carries instrument2, carries instrument3, has power supply, pointing groundstation2.\n"
    f"Based on the domain description, a satellite can 'turn' from target A to target B. This action is executable only if all following preconditions are satisfied: the satellite is currently pointing target A.\n"
    f"the satellite is currently pointing target A ::: Satellite1: carries instrument4, has power supply, pointing planet13.  ===> NOT SATISFY\n"
    f"Since not all preconditions are satisfied, the action is not executable.\n"
    f"Final answer: False.\n"
    f"------------\n"
)


STATE_CHECKER_SATELLITE_EXAMPLE =(
    f"[Examples]\n"
    
    f"Current state1: Instrument0: on satellite0, star1 is its calibration target, compatible with image2. Instrument1: on satellite1, turned on, is calibrated, star1 is its calibration target, compatible with image0, compatible with image2, compatible with image4, compatible with image5, compatible with spectrograph1, compatible with spectrograph3, has phenomenon10's image in image5, has phenomenon10's image in spectrograph3, has phenomenon11's image in spectrograph1. Satellite0: carries instrument0, has power supply, pointing phenomenon5. Satellite1: carries instrument1, doesn't have power supply, pointing phenomenon5.\n"
    
    f"Question 1: In current state, if image of phenomenon5 is taken with instrument1 on satellite1 in image4 to reach the current state. In this state, are all of the following valid properties of the state (both with and without negations)? Calibration of instrument0 for star1 is complete, satellite0 is poting to phenomenon5, instruments1 on satellite1 has an image of phenomenon10 in image5, instrument1 has an image of phenomenon10 in spectrograph3, instrument1 has an image of phenomenon11 in image4.\n"
    
    f"Answer 1:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. If there is any action needed to take in the question, we should first take the action and return all objects states, including those states that are not affected by the action. \n"
    f"Because the question contains one action, we should first take the action and get new states of all objects. After taking the action, we should return states of all objects, including states that are not effected by the action.\n" 
    f"The action is \" image of phenomenon5 is taken with instrument1 on satellite1 in image4\". Based on the domain description, this action is executable(instrument 1 is turned on, is calibrated, is on satellite1, satellite1 is pointing phenomenon5, instrument1 supports image4)\n"
    f"After taking the action, the curremt states of all objects should be: Instrument0: on satellite0, star1 is its calibration target, compatible with image2. Instrument1: on satellite1, turned on, is calibrated, star1 is its calibration target, compatible with image0, compatible with image2, compatible with image4, compatible with image5, compatible with spectrograph1, compatible with spectrograph3, has phenomenon10's image in image5, has phenomenon10's image in spectrograph3, has phenomenon11's image in spectrograph1, has phenomenon5's image in image4. Satellite0: carries instrument0, has power supply, pointing phenomenon5. Satellite1: carries instrument1, doesn't have power supply, pointing phenomenon5.\n"
    
    f"Then, we compare each proposition in the question one by one.\n"
    f"Calibration of instrument0 for star1 is complete, ::: Instrument0: on satellite0, is calibrated, star1 is its calibration target ===> MATCH\n"
    f"satellite0 is poting to phenomenon5, ::: Satellite0: carries instrument0, has power supply, pointing phenomenon5. ===> MATCH\n"
    f"instruments1 on satellite1 has an image of phenomenon10 in image5, ::: Instrument1: has phenomenon10's image in image5. ===> MATCH\n"
    f"instrument1 has an image of phenomenon10 in spectrograph3,  ::: Instrument1: has phenomenon10's image in spectrograph3. ===> MATCH\n"
    f"instrument1 has an image of phenomenon11 in image4. ::: Instrument1: on satellite1, turned on, is calibrated, can be calibrated using star1, compatible with image0, compatible with image2, compatible with image4, compatible with image5, compatible with spectrograph1, compatible with spectrograph3, has phenomenon10's image in image5, has phenomenon10's image in spectrograph3, has phenomenon11's image in spectrograph1, has phenomenon5's image in image4. ===> NOT MATCH\n"
    
    f"Since there is a proposition in the question doesn't match with the current state, the question is false.\n"
    f"Final Answer: False.\n"
    f"------------\n"
    
    f"Current state2: Instrument0: on satellite0, turned on, is calibrated, groundstation2 is its calibration target, star0 is its calibration target, compatible with spectrograph0, compatible with thermograph4. Instrument1: on satellite0, is calibrated, groundstation4 is its calibration target, star8 is its calibration target, compatible with spectrograph0, compatible with spectrograph1. Instrument2: on satellite1, turned on, is calibrated, groundstation4 is its calibration target, star7 is its calibration target, groundstation9 is its calibration target, compatible with infrared3, compatible with spectrograph0, compatible with spectrograph2. Instrument3: on satellite1, turned on, is calibrated, star6 is its calibration target, compatible with spectrograph1, compatible with spectrograph2, has planet14's image in image3. Satellite0: carries instrument0, carries instrument1, doesn't have power supply, pointing to star1. Satellite1: carries instrument2, carries instrument3, doesn't have power supply, pointing to planet14.\n"
    
    f"Question 2: In this state, is it True or False that there is an image of planet14 in image3?\n"
    
    f"Answer 2:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. If there is any action needed to take in the question, we should first take the action and return all objects states, including those states that are not affected by the action.\n"
    f"there is an image of planet14 in image3 ::: Instrument3: on satellite1, turned on, is calibrated, star6 is its calibration target, compatible with spectrograph1, compatible with spectrograph2, has planet14's image in image3.  ===> MATCH\n"
    f"Since all propositions in the question match with the curent state, so the question is true.\n"
    f"Final Answer: True.\n"
    f"------------\n"
)


TWOSHOTCOT_AE_SATELLITE_EXAMPLE = (
     f"[Examples]\n"
    f"(Example 1)\n"
    f"current state: Instrument5 is on board satellite2, satellite2 has power available, satellite2 is pointing at star12, instrument5 is calibrated for star12. Instrument4 is on board satellite2 and is calibrated for groundstation9. Satellite1 has instrument2 on board and has no power available. Satellite0 is pointing at groundstation3 and carries instrument0. Instrument2 supports image1, image1 is compatible with instrument5. Infrared2 is compatible with instrument4 and instrument5. Image3 is compatible with instrument2 and supported by instrument5. Instrument5 supports image1 and image3.\n"
    f"Question: Given the initial condition, for steps 1 through 1 the following actions are planned to be performed: on satellite2, instrument5 is switched on. Is the action: instrument5 on satellite2 is switched on executable at step 1, True or False?\n"
    f"Answer: \n"
    f"Step 1: we can confirm whether this action is executable or not by checking the initial state.\n"
    f"An instrument on the satellite can be switched on only if following preconditions are satisfied: the instrument is on the satellite, the satellite has power supply. We can see satellite2 has power supply and instrument5 is on satellite2. So this action is executable.\n"
    f"Step 2: we return the final answer based on the checking result.\n" f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final Answer: True"
    f"------------\n"
    f"(Example 2)\n"
    f"Current state: Satellite0 is pointing at star6. Satellite0 carries instrument1 and instrument2. Instrument1 is switched on but not calibrated for star6. Instrument1 supports image2. Image2 is compatible with instrument1. Satellite0 has power available. Satellite1 has instrument4 and is pointing at groundstation1, but has no power.\n"
    f"Question: Given the initial condition, the following action is planned at step 1: satellite0 uses instrument1 to take image2 of star6. Is this action executable at step 1, True or False?\n"
    f"Answer: \n"
    f"Step 1: we can confirm whether this action is executable or not by checking the initial state.\n"
    f"An instrument on the satellite can take image of the object in mode X only if the satellite is pointing the object, the instrument is switched on, the instrument is calibrated, the instrument supports the mode. We can see satellite0 is pointing at star6, instrument1 is switched on, but instrument1 is not calibrated for star6. So this action is not executable.\n"
    f"Step 2: we return the final answer based on the checking result.\n"
    f"Since not all preconditions are satisfied, this action is not executable.\n"
    f"Final Answer: False"
    f"------------\n"
)


TWOSHOTCOT_STATE_SATELLITE_EXAMPLE = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"Current state: Satellite0 is currently pointing at star3. Satellite0 carries instrument0 and has power supply. Satellite1 is currently pointing at star4. Satellite1 carries instrument1. Instrument0 is not calibrated for star9 and supports image1. Instrument1 is calibrated for star3 and supports image2. Satellite1 has instrument2 on board and is pointing at star6.\n"
    f"Question: Given the initial condition, the following action is performed: satellite0 is turned to point at star7. In this state, is it True or False that satellite1 is now pointing at star7?\n"
    f"Answer: \n"
    f"Step 1: We first execute the action and get the new state.\n"
    f"After taking the action 'satellite0 is turned to point at star7', the satellite0 is pointing star7.\n"
    f"Step 2: Then, we compare the state and the question and get the answer.\n"
    f"The satellite1 is still pointing at star4. So the question is false\n"
    f"Final Answer: False.\n"
    f"---------------\n"
    f"(Example 2)\n"
    f"Current state: Satellite1 is pointing at star4 and carries instrument2. Instrument2 is switched on and is calibrated for star4. Image4 is compatible with instrument2, but instrument2 does not support it. Satellite1 has power available. Satellite0 is pointing at groundstation1 and carries instrument0 and instrument1.\n"
    f"Question: Given the initial condition, the following action is performed: satellite1 uses instrument2 to take image4 of star4. Is it True or False that instrument2 has the image of star4 in image4?\n"
    f"Answer:\n"
    f"Step 1: We first execute the action and get the new state.\n"
    f"After taking the action 'satellite1 uses instrument2 to take image4 of star4', instrument2 has star4's image in image4.\n"
    f"Step 2: Then, we compare the state and the question and get the answer.\n"
    f"We can see instrument2 has the image of star4 in image4, so the question is true.\n"
    f"Final Answer: False.\n"
    f"---------------\n"
)


#--------------
#Visitall domain
#---------------
VISITALL_DOMAIN_DESCRIPTION = (
    f"The VisitAll domain involves a robot moving between locations in a connected n×m grid. Each location can have at most four neighbouring locations, and some locations may not be connected to their neighbours. Locations are named in the format location xi_yj, where x and y represent their coordinates. When a robot move from location A to location B, location B will be marked as visited.\n"
    f"Different properties are used to describe current states of different objects. For a robot we use: at location_x, has visited location_x. For a location we use: connected with location_y.\n"
    f"Following actions are executable only if all preconditions are met, if any condition are not satisfied, the action is not executable.\n"
    f"A robot can 'move' from location A to location B. This action is executable only if all following preconditions are satisfied: the robot is currently at location A, location B is connected with location A.\n"
    f"Executing an action will change states of related objects.\n"
    f"A robot can 'move' from location A to location B. This action will result in: the robot is not at location A, the robot is currently at location B, location B has been visited.\n"
)


INITIAL_STATE_EXTRACTOR_VISITALL_PROMPT = (
    f"This is a question related to the visitall domain. You are required to extract the initial state of every objects in this plan, including locations and the robot. Your answer must satisfy all the following requirements. First, think and respond with the format from the example above, including the word choice and paragraph structure. Second, each object's state should contain all properties mentioned in the domain description above. Besides, don't use any markdown formatting."
)



INITIAL_STATE_EXTRACTOR_VISITALL_EXAMPLE = (
    f"[Examples]\n"
    f"Initial state example 1: Loc_x0_y0 and loc_x1_y0 are connected, loc_x0_y1 and loc_x0_y0 are connected, loc_x0_y1 and loc_x1_y1 are connected, loc_x0_y3 is connected to loc_x0_y4, loc_x0_y3 is connected to loc_x1_y3, loc_x0_y3 is marked as visited, loc_x0_y4 and loc_x0_y3 are connected, loc_x0_y4 and loc_x1_y4 are connected, loc_x1_y0 is connected to loc_x1_y1, loc_x1_y1 and loc_x1_y0 are connected, loc_x1_y1 and loc_x2_y1 are connected, loc_x1_y3 and loc_x0_y3 are connected, loc_x1_y3 and loc_x1_y4 are connected, loc_x1_y3 and loc_x2_y3 are connected, loc_x1_y4 and loc_x2_y4 are connected, loc_x1_y4 is connected to loc_x1_y3, loc_x2_y0 is connected to loc_x1_y0, loc_x2_y1 and loc_x2_y2 are connected, loc_x2_y1 and loc_x3_y1 are connected, loc_x2_y1 is connected to loc_x1_y1, loc_x2_y1 is connected to loc_x2_y0, loc_x2_y2 and loc_x3_y2 are connected, loc_x2_y3 and loc_x1_y3 are connected, loc_x2_y3 and loc_x2_y2 are connected, loc_x2_y3 is connected to loc_x2_y4, loc_x2_y3 is connected to loc_x3_y3, loc_x2_y4 and loc_x3_y4 are connected, loc_x2_y4 is connected to loc_x1_y4, loc_x2_y4 is connected to loc_x2_y3, loc_x3_y0 is connected to loc_x4_y0, loc_x3_y2 and loc_x3_y1 are connected, loc_x3_y2 and loc_x3_y3 are connected, loc_x3_y2 and loc_x4_y2 are connected, loc_x3_y3 and loc_x3_y2 are connected, loc_x3_y3 is connected to loc_x3_y4, loc_x3_y4 and loc_x2_y4 are connected, loc_x4_y0 is connected to loc_x3_y0, loc_x4_y0 is connected to loc_x4_y1, loc_x4_y1 and loc_x3_y1 are connected, loc_x4_y1 and loc_x4_y2 are connected, robot is located at loc_x0_y3, there is a connection between loc_x0_y0 and loc_x0_y1, there is a connection between loc_x1_y0 and loc_x0_y0, there is a connection between loc_x1_y0 and loc_x2_y0, there is a connection between loc_x1_y1 and loc_x0_y1, there is a connection between loc_x1_y4 and loc_x0_y4, there is a connection between loc_x2_y0 and loc_x2_y1, there is a connection between loc_x2_y0 and loc_x3_y0, there is a connection between loc_x2_y2 and loc_x2_y1, there is a connection between loc_x2_y2 and loc_x2_y3, there is a connection between loc_x3_y0 and loc_x2_y0, there is a connection between loc_x3_y0 and loc_x3_y1, there is a connection between loc_x3_y1 and loc_x2_y1, there is a connection between loc_x3_y1 and loc_x3_y0, there is a connection between loc_x3_y1 and loc_x3_y2, there is a connection between loc_x3_y1 and loc_x4_y1, there is a connection between loc_x3_y2 and loc_x2_y2, there is a connection between loc_x3_y3 and loc_x2_y3, there is a connection between loc_x3_y4 and loc_x3_y3, there is a connection between loc_x4_y1 and loc_x4_y0, there is a connection between loc_x4_y2 and loc_x3_y2 and there is a connection between loc_x4_y2 and loc_x4_y1.\n"
    f"Extracted from initial state example 1:\n"
    f"First, we find all locations in the initial state:\n"
    f"loc_x0_y0, loc_x0_y1,loc_x0_y3, loc_x0_y4, loc_x1_y0, loc_x1_y1, loc_x1_y3, loc_x1_y4,  loc_x2_y0, loc_x2_y1, loc_x2_y2, loc_x2_y3, loc_x2_y4, loc_x3_y0, loc_x3_y1, loc_x3_y2, loc_x3_y3, loc_x3_y4,  loc_x4_y0, loc_x4_y1, loc_x4_y2.\n"
    f"Then, we confirm locations not mentioned in the initial state: loc_x0_y2、loc_x1_y2、loc_x4_y3、loc_x4_y4.\n"
    f"Then, we organize robot's state and all locations' connectivity.\n"
    f"robot is located at loc_x0_y3, loc_x0_y3 is marked as visited ::: Robot: at loc_x0_y3, has visited loc_x0_y3.\n"
    f"Loc_x0_y0 and loc_x1_y0 are connected, loc_x0_y1 and loc_x0_y0 are connected, ::: loc_x0_y0: connected with loc_x0_y1, connected with loc_x1_y0.\n"
    f"loc_x0_y1 and loc_x0_y0 are connected, loc_x0_y1 and loc_x1_y1 are connected, ::: loc_x0_y1: connected with loc_x0_y0, connected with loc_x1_y1.\n"
    f"loc_x0_y3 is connected to loc_x0_y4, loc_x0_y3 is connected to loc_x1_y3, :::  loc_x0_y3: connected with loc_x0_y4, connected with loc_x1_y3.\n"
    f"loc_x0_y3 is connected to loc_x0_y4, loc_x0_y4 and loc_x1_y4 are connected :::  loc_x0_y4: connected with loc_x0_y3, connected with loc_x1_y4.\n"
    f"Loc_x0_y0 and loc_x1_y0 are connected, loc_x1_y0 is connected to loc_x1_y1, loc_x2_y0 is connected to loc_x1_y0, ::: loc_x1_y0: connected with loc_x0_y0, connected with loc_x1_y1, connected with loc_x0_y0, connected with loc_x2_y0.\n"
    f"loc_x0_y1 and loc_x1_y1 are connected, loc_x1_y1 and loc_x2_y1 are connected, loc_x1_y0 is connected to loc_x1_y1 ::: loc_x1_y1: connected with loc_x0_y1, connected with loc_x1_y0, connected with loc_x2_y1.\n"
    f"loc_x1_y3 and loc_x0_y3 are connected, loc_x1_y3 and loc_x1_y4 are connected, loc_x1_y3 and loc_x2_y3 are connected, ::: loc_x1_y3: connected with loc_x0_y3, connected with loc_x1_y4, connected with loc_x2_y3.\n"
    f"loc_x1_y4 and loc_x2_y4 are connected, loc_x1_y4 is connected to loc_x1_y3, loc_x1_y4 and loc_x0_y4 are connected, ::: loc_x1_y4: connected with loc_x0_y4, connected with loc_x1_y3, connected with loc_x2_y4.\n"
    f"loc_x2_y0 is connected to loc_x1_y0, loc_x2_y0 and loc_x2_y1 are connected, loc_x2_y0 and loc_x3_y0 are connected, ::: loc_x2_y0: connected with loc_x1_y0, connected with loc_x2_y1, connected with loc_x3_y0.\n"
    f"loc_x2_y1 and loc_x2_y2 are connected, loc_x2_y1 and loc_x3_y1 are connected, loc_x2_y1 is connected to loc_x1_y1, loc_x2_y1 is connected to loc_x2_y0, ::: loc_x2_y1: connected with loc_x1_y1, connected with loc_x2_y0, connected with loc_x2_y2, connected with loc_x3_y1.\n"
    f"loc_x2_y2 and loc_x3_y2 are connected, loc_x2_y2 and loc_x2_y1 are connected, loc_x2_y2 and loc_x2_y3 are connected, ::: loc_x2_y2: connected with loc_x2_y1, connected with loc_x2_y3, connected with loc_x3_y2.\n"
    f"loc_x2_y3 and loc_x1_y3 are connected, loc_x2_y3 and loc_x2_y2 are connected, loc_x2_y3 is connected to loc_x2_y4, loc_x2_y3 is connected to loc_x3_y3, ::: loc_x2_y3: connected with loc_x1_y3, connected with loc_x2_y2, connected with loc_x2_y4, connected with loc_x3_y3.\n"
    f"loc_x2_y4 and loc_x3_y4 are connected, loc_x2_y4 is connected to loc_x1_y4, loc_x2_y4 is connected to loc_x2_y3, ::: loc_x2_y4: connected with loc_x1_y4, connected with loc_x2_y3, connected with loc_x3_y4.\n"
    f"loc_x3_y0 is connected to loc_x4_y0, loc_x3_y0 and loc_x2_y0 are connected, loc_x3_y0 and loc_x3_y1 are connected, ::: loc_x3_y0: connected with loc_x2_y0, connected with loc_x3_y1, connected with loc_x4_y0.\n"
    f"loc_x3_y1 and loc_x3_y2 are connected, loc_x3_y1 and loc_x2_y1 are connected, loc_x3_y1 and loc_x3_y0 are connected, loc_x3_y1 and loc_x4_y1 are connected, ::: loc_x3_y1: connected with loc_x2_y1, connected with loc_x3_y0, connected with loc_x3_y2, connected with loc_x4_y1.\n"
    f"loc_x3_y2 and loc_x3_y1 are connected, loc_x3_y2 and loc_x3_y3 are connected, loc_x3_y2 and loc_x4_y2 are connected, loc_x3_y2 and loc_x2_y2 are connected, ::: loc_x3_y2: connected with loc_x2_y2, connected with loc_x3_y1, connected with loc_x3_y3, connected with loc_x4_y2.\n"
    f"loc_x3_y3 and loc_x3_y2 are connected, loc_x3_y3 is connected to loc_x3_y4, loc_x3_y3 and loc_x2_y3 are connected, ::: loc_x3_y3: connected with loc_x2_y3, connected with loc_x3_y2, connected with loc_x3_y4.\n"
    f"loc_x3_y4 and loc_x2_y4 are connected, loc_x3_y4 and loc_x3_y3 are connected, ::: loc_x3_y4: connected with loc_x2_y4, connected with loc_x3_y3.\n"
    f"loc_x4_y0 is connected to loc_x3_y0, loc_x4_y0 is connected to loc_x4_y1, ::: loc_x4_y0: connected with loc_x3_y0, connected with loc_x4_y1.\n"
    f"loc_x4_y1 and loc_x3_y1 are connected, loc_x4_y1 and loc_x4_y2 are connected, loc_x4_y1 and loc_x4_y0 are connected, ::: loc_x4_y1: connected with loc_x3_y1, connected with loc_x4_y0, connected with loc_x4_y2.\n"
    f"loc_x4_y2 and loc_x3_y2 are connected, loc_x4_y2 and loc_x4_y1 are connected, ::: loc_x4_y2: connected with loc_x3_y2, connected with loc_x4_y1.\n"
    f"Then, we organize all locations' state and the robot's state into a new paragraph as the end of our answer.\n"
    f"Robot: at loc_x0_y3, has visited loc_x0_y3. loc_x0_y0: connected with loc_x0_y1, connected with loc_x1_y0. loc_x0_y1: connected with loc_x0_y0, connected with loc_x1_y1. loc_x0_y3: connected with loc_x0_y4, connected with loc_x1_y3. loc_x0_y4: connected with loc_x0_y3, connected with loc_x1_y4. loc_x1_y0: connected with loc_x0_y0, connected with loc_x1_y1, connected with loc_x0_y0, connected with loc_x2_y0. loc_x1_y1: connected with loc_x0_y1, connected with loc_x1_y0, connected with loc_x2_y1. loc_x1_y3: connected with loc_x0_y3, connected with loc_x1_y4, connected with loc_x2_y3. loc_x1_y4: connected with loc_x0_y4, connected with loc_x1_y3, connected with loc_x2_y4. loc_x2_y0: connected with loc_x1_y0, connected with loc_x2_y1, connected with loc_x3_y0. loc_x2_y1: connected with loc_x1_y1, connected with loc_x2_y0, connected with loc_x2_y2, connected with loc_x3_y1. loc_x2_y2: connected with loc_x2_y1, connected with loc_x2_y3, connected with loc_x3_y2. loc_x2_y3: connected with loc_x1_y3, connected with loc_x2_y2, connected with loc_x2_y4, connected with loc_x3_y3. loc_x2_y4: connected with loc_x1_y4, connected with loc_x2_y3, connected with loc_x3_y4. loc_x3_y0: connected with loc_x2_y0, connected with loc_x3_y1, connected with loc_x4_y0. loc_x3_y1: connected with loc_x2_y1, connected with loc_x3_y0, connected with loc_x3_y2, connected with loc_x4_y1. loc_x3_y2: connected with loc_x2_y2, connected with loc_x3_y1, connected with loc_x3_y3, connected with loc_x4_y2. loc_x3_y3: connected with loc_x2_y3, connected with loc_x3_y2, connected with loc_x3_y4. loc_x3_y4: connected with loc_x2_y4, connected with loc_x3_y3. loc_x4_y0: connected with loc_x3_y0, connected with loc_x4_y1. loc_x4_y1: connected with loc_x3_y1, connected with loc_x4_y0, connected with loc_x4_y2. loc_x4_y2: connected with loc_x3_y2, connected with loc_x4_y1.\n"
    f"——————\n"
)

QUESTION_EXTRACTOR_VISITALL_EXAMPLE = (
    f"[Examples]\n"
    
    f"Plan 1: Given the initial condition, the following actions are performed: moves to loc_x0_y1 from loc_x0_y2 to reach the current state. In this state, are all of the following valid properties of the state that do not involve negations True or False: robot is at loc_x0_y3, robot is at loc_x0_y5, robot is at loc_x1_y3, robot is at loc_x1_y4, robot is at loc_x1_y5, robot is at loc_x2_y4, robot is at loc_x3_y1, robot is located at loc_x0_y1, robot is located at loc_x0_y4, robot is located at loc_x1_y0, robot is located at loc_x1_y2, robot is located at loc_x2_y0, robot is located at loc_x2_y3, robot is located at loc_x3_y0, robot is located at loc_x3_y2, robot is located at loc_x3_y3, robot is placed at loc_x0_y0, robot is placed at loc_x0_y2, robot is placed at loc_x1_y1, robot is placed at loc_x2_y1, robot is placed at loc_x2_y2, robot is placed at loc_x2_y5 and robot is placed at loc_x3_y4?\n"
    
    f"Question extracted from plan 1: In this state, are all of the following valid properties of the state that do not involve negations True or False: robot is at loc_x0_y3, robot is at loc_x0_y5, robot is at loc_x1_y3, robot is at loc_x1_y4, robot is at loc_x1_y5, robot is at loc_x2_y4, robot is at loc_x3_y1, robot is located at loc_x0_y1, robot is located at loc_x0_y4, robot is located at loc_x1_y0, robot is located at loc_x1_y2, robot is located at loc_x2_y0, robot is located at loc_x2_y3, robot is located at loc_x3_y0, robot is located at loc_x3_y2, robot is located at loc_x3_y3, robot is placed at loc_x0_y0, robot is placed at loc_x0_y2, robot is placed at loc_x1_y1, robot is placed at loc_x2_y1, robot is placed at loc_x2_y2, robot is placed at loc_x2_y5 and robot is placed at loc_x3_y4?\n"
    
    f"——————\n"
    
    f"Plan 2: Given the initial condition, the following actions are performed: robot moves from loc_x0_y2 to loc_x0_y1 to reach the current state. In this state, are all of the following valid properties of the state that do not involve negations? loc_x0_y0 is connected to loc_x0_y1, loc_x0_y1 and loc_x0_y2 are connected, loc_x0_y1 is visited, loc_x0_y2 is connected to loc_x0_y1, loc_x0_y2 is connected to loc_x1_y2, loc_x0_y2 is visited, loc_x0_y3 is connected to loc_x1_y3, loc_x0_y4 and loc_x1_y4 are connected, loc_x0_y4 is connected to loc_x0_y3, loc_x0_y4 is connected to loc_x0_y5, loc_x0_y5 is connected to loc_x1_y5, loc_x1_y0 and loc_x0_y0 are connected, loc_x1_y0 and loc_x1_y1 are connected, loc_x1_y1 and loc_x1_y2 are connected, loc_x1_y1 and loc_x2_y1 are connected, loc_x1_y2 and loc_x1_y3 are connected, loc_x1_y2 is connected to loc_x1_y1, loc_x1_y3 and loc_x1_y2 are connected, loc_x1_y3 is connected to loc_x1_y4, loc_x1_y3 is connected to loc_x2_y3, loc_x1_y4 is connected to loc_x1_y3, loc_x1_y4 is connected to loc_x1_y5, loc_x1_y5 is connected to loc_x2_y5, loc_x2_y0 and loc_x2_y1 are connected, loc_x2_y0 and loc_x3_y0 are connected, loc_x2_y0 is connected to loc_x1_y0, loc_x2_y1 and loc_x2_y0 are connected, loc_x2_y1 and loc_x3_y1 are connected, loc_x2_y1 is connected to loc_x1_y1, loc_x2_y2 and loc_x2_y1 are connected, loc_x2_y2 and loc_x3_y2 are connected, loc_x2_y3 and loc_x1_y3 are connected, loc_x2_y3 and loc_x2_y2 are connected, loc_x2_y3 is connected to loc_x3_y3, loc_x2_y4 and loc_x2_y3 are connected, loc_x2_y5 and loc_x1_y5 are connected, loc_x3_y0 and loc_x2_y0 are connected, loc_x3_y2 is connected to loc_x2_y2, loc_x3_y2 is connected to loc_x3_y1, loc_x3_y3 and loc_x2_y3 are connected, loc_x3_y3 and loc_x3_y4 are connected, loc_x3_y3 is connected to loc_x3_y2, loc_x3_y4 and loc_x2_y4 are connected, robot is at loc_x0_y1, there is a connection between loc_x0_y0 and loc_x1_y0, there is a connection between loc_x0_y1 and loc_x0_y0, there is a connection between loc_x0_y1 and loc_x1_y1, there is a connection between loc_x0_y2 and loc_x0_y3, there is a connection between loc_x0_y3 and loc_x0_y2, there is a connection between loc_x0_y3 and loc_x0_y4, there is a connection between loc_x0_y5 and loc_x0_y4, there is a connection between loc_x1_y0 and loc_x2_y0, there is a connection between loc_x1_y1 and loc_x0_y1, there is a connection between loc_x1_y1 and loc_x1_y0, there is a connection between loc_x1_y2 and loc_x0_y2, there is a connection between loc_x1_y2 and loc_x2_y2, there is a connection between loc_x1_y3 and loc_x0_y3, there is a connection between loc_x1_y4 and loc_x0_y4, there is a connection between loc_x1_y4 and loc_x2_y4, there is a connection between loc_x1_y5 and loc_x0_y5, there is a connection between loc_x1_y5 and loc_x1_y4, there is a connection between loc_x2_y1 and loc_x2_y2, there is a connection between loc_x2_y2 and loc_x1_y2, there is a connection between loc_x2_y2 and loc_x2_y3, there is a connection between loc_x2_y3 and loc_x2_y4, there is a connection between loc_x2_y4 and loc_x1_y4, there is a connection between loc_x2_y4 and loc_x2_y5, there is a connection between loc_x2_y4 and loc_x3_y4, there is a connection between loc_x2_y5 and loc_x2_y4, there is a connection between loc_x3_y0 and loc_x3_y1, there is a connection between loc_x3_y1 and loc_x2_y1, there is a connection between loc_x3_y1 and loc_x3_y0, there is a connection between loc_x3_y1 and loc_x3_y2, there is a connection between loc_x3_y2 and loc_x3_y3 and there is a connection between loc_x3_y4 and loc_x3_y3.\n"
    
    f"Question extracted from plan 2: In this state, are all of the following valid properties of the state that do not involve negations? loc_x0_y0 is connected to loc_x0_y1, loc_x0_y1 and loc_x0_y2 are connected, loc_x0_y1 is visited, loc_x0_y2 is connected to loc_x0_y1, loc_x0_y2 is connected to loc_x1_y2, loc_x0_y2 is visited, loc_x0_y3 is connected to loc_x1_y3, loc_x0_y4 and loc_x1_y4 are connected, loc_x0_y4 is connected to loc_x0_y3, loc_x0_y4 is connected to loc_x0_y5, loc_x0_y5 is connected to loc_x1_y5, loc_x1_y0 and loc_x0_y0 are connected, loc_x1_y0 and loc_x1_y1 are connected, loc_x1_y1 and loc_x1_y2 are connected, loc_x1_y1 and loc_x2_y1 are connected, loc_x1_y2 and loc_x1_y3 are connected, loc_x1_y2 is connected to loc_x1_y1, loc_x1_y3 and loc_x1_y2 are connected, loc_x1_y3 is connected to loc_x1_y4, loc_x1_y3 is connected to loc_x2_y3, loc_x1_y4 is connected to loc_x1_y3, loc_x1_y4 is connected to loc_x1_y5, loc_x1_y5 is connected to loc_x2_y5, loc_x2_y0 and loc_x2_y1 are connected, loc_x2_y0 and loc_x3_y0 are connected, loc_x2_y0 is connected to loc_x1_y0, loc_x2_y1 and loc_x2_y0 are connected, loc_x2_y1 and loc_x3_y1 are connected, loc_x2_y1 is connected to loc_x1_y1, loc_x2_y2 and loc_x2_y1 are connected, loc_x2_y2 and loc_x3_y2 are connected, loc_x2_y3 and loc_x1_y3 are connected, loc_x2_y3 and loc_x2_y2 are connected, loc_x2_y3 is connected to loc_x3_y3, loc_x2_y4 and loc_x2_y3 are connected, loc_x2_y5 and loc_x1_y5 are connected, loc_x3_y0 and loc_x2_y0 are connected, loc_x3_y2 is connected to loc_x2_y2, loc_x3_y2 is connected to loc_x3_y1, loc_x3_y3 and loc_x2_y3 are connected, loc_x3_y3 and loc_x3_y4 are connected, loc_x3_y3 is connected to loc_x3_y2, loc_x3_y4 and loc_x2_y4 are connected, robot is at loc_x0_y1, there is a connection between loc_x0_y0 and loc_x1_y0, there is a connection between loc_x0_y1 and loc_x0_y0, there is a connection between loc_x0_y1 and loc_x1_y1, there is a connection between loc_x0_y2 and loc_x0_y3, there is a connection between loc_x0_y3 and loc_x0_y2, there is a connection between loc_x0_y3 and loc_x0_y4, there is a connection between loc_x0_y5 and loc_x0_y4, there is a connection between loc_x1_y0 and loc_x2_y0, there is a connection between loc_x1_y1 and loc_x0_y1, there is a connection between loc_x1_y1 and loc_x1_y0, there is a connection between loc_x1_y2 and loc_x0_y2, there is a connection between loc_x1_y2 and loc_x2_y2, there is a connection between loc_x1_y3 and loc_x0_y3, there is a connection between loc_x1_y4 and loc_x0_y4, there is a connection between loc_x1_y4 and loc_x2_y4, there is a connection between loc_x1_y5 and loc_x0_y5, there is a connection between loc_x1_y5 and loc_x1_y4, there is a connection between loc_x2_y1 and loc_x2_y2, there is a connection between loc_x2_y2 and loc_x1_y2, there is a connection between loc_x2_y2 and loc_x2_y3, there is a connection between loc_x2_y3 and loc_x2_y4, there is a connection between loc_x2_y4 and loc_x1_y4, there is a connection between loc_x2_y4 and loc_x2_y5, there is a connection between loc_x2_y4 and loc_x3_y4, there is a connection between loc_x2_y5 and loc_x2_y4, there is a connection between loc_x3_y0 and loc_x3_y1, there is a connection between loc_x3_y1 and loc_x2_y1, there is a connection between loc_x3_y1 and loc_x3_y0, there is a connection between loc_x3_y1 and loc_x3_y2, there is a connection between loc_x3_y2 and loc_x3_y3 and there is a connection between loc_x3_y4 and loc_x3_y3.\n"
    
    f"—————\n"
)

ACTION_TAKER_VISITALL_PROMPT = (
    f"Based on the domain description and examples above, take the action and return the new state of all objects. Your answer must satisfy all the following requirements. First, think and respond like examples above, you must return the robot's state and of all locations connectivity information. Second, each object's state must contain all properties mentioned in the domain description above. Third, after your analysis, please return robot's state and all locations' connectivity information in a new paragraph as the end of your answer, and use the format such as: \"Robot: at loc_x0_y3, has visited loc_x0_y3, has visited loc_x0_y4, has visited loc_x1_y3, has visited loc_x2_y3. loc_x0_y0: connected with loc_x0_y1, connected with loc_x1_y0.\" Besides, don't use any markdown formatting."
)



ACTION_TAKER_VISITALL_EXAMPLE = (
    f"[Examples]\n"
    
    f"Current state example 1: Robot: at loc_x0_y2, has visited loc_x0_y2, has visited loc_x0_y1, has visited loc_x0_y0. loc_x0_y0: connected with loc_x0_y1. loc_x0_y1: connected with loc_x0_y0, connected with loc_x0_y2, connected with loc_x1_y1. loc_x0_y2: connected with loc_x0_y1, connected with loc_x0_y3, connected with loc_x1_y2. loc_x0_y3: connected with loc_x0_y2, connected with loc_x0_y4. loc_x0_y4: connected with loc_x0_y3, connected with loc_x0_y5, connected with loc_x1_y4. loc_x0_y5: connected with loc_x0_y4. loc_x1_y0: connected with loc_x2_y0. loc_x1_y1: connected with loc_x0_y1, connected with loc_x1_y0, connected with loc_x1_y2, connected with loc_x2_y1. loc_x1_y2: connected with loc_x0_y2, connected with loc_x1_y3, connected with loc_x2_y2. loc_x1_y3: connected with loc_x0_y3, connected with loc_x1_y2, connected with loc_x1_y4, connected with loc_x2_y3. loc_x1_y4: connected with loc_x0_y4, connected with loc_x1_y5. loc_x1_y5: connected with loc_x0_y5, connected with loc_x2_y5, connected with loc_x1_y4. loc_x2_y0: connected with loc_x3_y0. loc_x2_y1: connected with loc_x1_y1. loc_x2_y2: connected with loc_x1_y2, connected with loc_x2_y3, connected with loc_x3_y2. loc_x2_y3: connected with loc_x1_y3, connected with loc_x2_y2, connected with loc_x2_y4, connected with loc_x3_y3. loc_x2_y4: connected with loc_x2_y3, connected with loc_x2_y5. loc_x2_y5: connected with loc_x1_y5, connected with loc_x2_y4. loc_x3_y0: connected with loc_x2_y0, connected with loc_x3_y1. loc_x3_y1: connected with loc_x2_y1, connected with loc_x3_y0, connected with loc_x3_y2. loc_x3_y2: connected with loc_x2_y2, connected with loc_x3_y1, connected with loc_x3_y3. loc_x3_y3: connected with loc_x3_y2. loc_x3_y4: connected with loc_x2_y4.\n"
    
    f"Action 1: The robot moves from loc_x0_y2 to loc_x0_y3.\n"
    
    f"Answer 1:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Robot: at loc_x0_y2, has visited loc_x0_y2, has visited loc_x0_y1, has visited loc_x0_y0. loc_x0_y2: connected with loc_x0_y1, connected with loc_x0_y3, connected with loc_x1_y2.\n"
    f"Based on the domain description, A robot can 'move' from location A to location B. This action will result in: the robot is not at location A, the robot is currently at location B, location A has been visited.\n"
    f"the robot is not at location A, the robot is currently at location B, location A has been visited. ::: Robot: at loc_x0_y3, has visited loc_x0_y3, has visited loc_x0_y2, has visited loc_x0_y1, has visited loc_x0_y0, has visited loc_x0_y1.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into a new paragraph as the end of answer.\n"
    f"Robot: at loc_x0_y3, has visited loc_x0_y3, has visited loc_x0_y2, has visited loc_x0_y1, has visited loc_x0_y0, has visited loc_x0_y1. loc_x0_y0: connected with loc_x0_y1. loc_x0_y1: connected with loc_x0_y0, connected with loc_x0_y2, connected with loc_x1_y1. loc_x0_y2: connected with loc_x0_y1, connected with loc_x0_y3, connected with loc_x1_y2. loc_x0_y3: connected with loc_x0_y2, connected with loc_x0_y4. loc_x0_y4: connected with loc_x0_y3, connected with loc_x0_y5, connected with loc_x1_y4. loc_x0_y5: connected with loc_x0_y4. loc_x1_y0: connected with loc_x2_y0. loc_x1_y1: connected with loc_x0_y1, connected with loc_x1_y0, connected with loc_x1_y2, connected with loc_x2_y1. loc_x1_y2: connected with loc_x0_y2, connected with loc_x1_y3, connected with loc_x2_y2. loc_x1_y3: connected with loc_x0_y3, connected with loc_x1_y2, connected with loc_x1_y4, connected with loc_x2_y3. loc_x1_y4: connected with loc_x0_y4, connected with loc_x1_y5. loc_x1_y5: connected with loc_x0_y5, connected with loc_x2_y5, connected with loc_x1_y4. loc_x2_y0: connected with loc_x3_y0. loc_x2_y1: connected with loc_x1_y1. loc_x2_y2: connected with loc_x1_y2, connected with loc_x2_y3, connected with loc_x3_y2. loc_x2_y3: connected with loc_x1_y3, connected with loc_x2_y2, connected with loc_x2_y4, connected with loc_x3_y3. loc_x2_y4: connected with loc_x2_y3, connected with loc_x2_y5. loc_x2_y5: connected with loc_x1_y5, connected with loc_x2_y4. loc_x3_y0: connected with loc_x2_y0, connected with loc_x3_y1. loc_x3_y1: connected with loc_x2_y1, connected with loc_x3_y0, connected with loc_x3_y2. loc_x3_y2: connected with loc_x2_y2, connected with loc_x3_y1, connected with loc_x3_y3. loc_x3_y3: connected with loc_x3_y2. loc_x3_y4: connected with loc_x2_y4."
        
    f"——————\n"
)



EXECUTABILITY_CHECKER_VISITALL_EXAMPLE = (
    f"[Examples]\n"
    
    f"Current state example 1:\n"
    f"Robot: at loc_x0_y2, has visited loc_x0_y2. loc_x0_y0: connected with loc_x0_y1. loc_x0_y1: connected with loc_x0_y0, connected with loc_x0_y2, connected with loc_x1_y1. loc_x0_y2: connected with loc_x0_y1, connected with loc_x0_y3, connected with loc_x1_y2. loc_x0_y3: connected with loc_x0_y2, connected with loc_x0_y4. loc_x0_y4: connected with loc_x0_y3, connected with loc_x0_y5, connected with loc_x1_y4. loc_x0_y5: connected with loc_x0_y4. loc_x1_y0: connected with loc_x2_y0. loc_x1_y1: connected with loc_x0_y1, connected with loc_x1_y0, connected with loc_x1_y2, connected with loc_x2_y1. loc_x1_y2: connected with loc_x0_y2, connected with loc_x1_y3, connected with loc_x2_y2. loc_x1_y3: connected with loc_x0_y3, connected with loc_x1_y2, connected with loc_x1_y4, connected with loc_x2_y3. loc_x1_y4: connected with loc_x0_y4, connected with loc_x1_y5. loc_x1_y5: connected with loc_x0_y5, connected with loc_x2_y5, connected with loc_x1_y4. loc_x2_y0: connected with loc_x3_y0. loc_x2_y1: connected with loc_x1_y1. loc_x2_y2: connected with loc_x1_y2, connected with loc_x2_y3, connected with loc_x3_y2. loc_x2_y3: connected with loc_x1_y3, connected with loc_x2_y2, connected with loc_x2_y4, connected with loc_x3_y3. loc_x2_y4: connected with loc_x2_y3, connected with loc_x2_y5. loc_x2_y5: connected with loc_x1_y5, connected with loc_x2_y4. loc_x3_y0: connected with loc_x2_y0, connected with loc_x3_y1. loc_x3_y1: connected with loc_x2_y1, connected with loc_x3_y0, connected with loc_x3_y2. loc_x3_y2: connected with loc_x2_y2, connected with loc_x3_y1, connected with loc_x3_y3. loc_x3_y3: connected with loc_x3_y2. loc_x3_y4: connected with loc_x2_y4.\n"
    
    f"Action 1: The robot moves from loc_x0_y2 to loc_x0_y1.\n"
    
    f"Answer 1:\n"
    f"In order to check whether this action is executable or not, we first need to find states of objects related to this action, then check whether all preconditions of this action are satisfied.\n"
    f"Robot: at loc_x0_y2, has visited loc_x0_y2. loc_x0_y2: connected with loc_x0_y1, connected with loc_x0_y3, connected with loc_x1_y2.\n"
    f"Based on the domain description, A robot can 'move' from location A to location B. This action is executable only if all following preconditions are satisfied: the robot is currently at location A, location B is connected with location A.\n"
    f"the robot is currently at location A ::: Robot: at loc_x0_y2, has visited loc_x0_y2. ===> SATISFY\n"
    f"location B is connected with location A ::: loc_x0_y2: connected with loc_x0_y1, connected with loc_x0_y3, connected with loc_x1_y2. ===> SATISFY\n"
    f"Since all preconditions are satisfied, the action is executable.\n"
    f"Final answer: True.\n"
    
    f"——————\n"
    
    f"Current state example 2:\n"
    f"Robot: at loc_x0_y3, has visited loc_x0_y3. loc_x0_y0: connected with loc_x1_y0, connected with loc_x0_y1. loc_x0_y1: connected with loc_x0_y0, connected with loc_x1_y1. loc_x0_y3: connected with loc_x0_y4, connected with loc_x1_y3. loc_x0_y4: connected with loc_x0_y3, connected with loc_x1_y4. loc_x1_y0: connected with loc_x0_y0, connected with loc_x1_y1, connected with loc_x2_y0. loc_x1_y1: connected with loc_x0_y1, connected with loc_x1_y0, connected with loc_x2_y1. loc_x1_y3: connected with loc_x0_y3, connected with loc_x1_y4, connected with loc_x2_y3. loc_x1_y4: connected with loc_x0_y4, connected with loc_x1_y3, connected with loc_x2_y4. loc_x2_y0: connected with loc_x1_y0, connected with loc_x2_y1, connected with loc_x3_y0. loc_x2_y1: connected with loc_x1_y1, connected with loc_x2_y0, connected with loc_x2_y2, connected with loc_x3_y1. loc_x2_y2: connected with loc_x2_y1, connected with loc_x2_y3, connected with loc_x3_y2. loc_x2_y3: connected with loc_x1_y3, connected with loc_x2_y2, connected with loc_x2_y4, connected with loc_x3_y3. loc_x2_y4: connected with loc_x1_y4, connected with loc_x2_y3, connected with loc_x3_y4. loc_x3_y0: connected with loc_x2_y0, connected with loc_x3_y1, connected with loc_x4_y0. loc_x3_y1: connected with loc_x2_y1, connected with loc_x3_y0, connected with loc_x3_y2, connected with loc_x4_y1. loc_x3_y2: connected with loc_x2_y2, connected with loc_x3_y1, connected with loc_x3_y3, connected with loc_x4_y2. loc_x3_y3: connected with loc_x2_y3, connected with loc_x3_y2, connected with loc_x3_y4. loc_x3_y4: connected with loc_x2_y4, connected with loc_x3_y3. loc_x4_y0: connected with loc_x3_y0, connected with loc_x4_y1. loc_x4_y1: connected with loc_x3_y1, connected with loc_x4_y0, connected with loc_x4_y2. loc_x4_y2: connected with loc_x3_y2, connected with loc_x4_y1.\n"
    
    f"Action 2: Robot moves from loc_x0_y4 to loc_x0_y3.\n"
    
    f"Answer 2:\n"
    f"In order to check whether this action is executable or not, we first need to find states of objects related to this action, then check whether all preconditions of this action are satisfied.\n"
    f"Robot: at loc_x0_y3, has visited loc_x0_y3. loc_x0_y4: connected with loc_x0_y3, connected with loc_x1_y4.\n"
    f"Based on the domain description, A robot can 'move' from location A to location B. This action is executable only if all following preconditions are satisfied: the robot is currently at location A, location B is connected with location A.\n"
    f"the robot is currently at location A ::: Robot: at loc_x0_y3, has visited loc_x0_y3. ===> NOT SATISFIED\n"
    f"Since not all preconditions are satisfied, the action is not executable.\n"
    f"Final answer: False.\n"
    
    f"——————\n"
)


STATE_CHECKER_VISITALL_EXAMPLE = (
    f"[Examples]\n"
    
    f"Current State example 1: Robot: at loc_x4_y2, has visited loc_x0_y0, has visited loc_x0_y1, has visited loc_x0_y3, has visited loc_x0_y4, has visited loc_x4_y2. loc_x0_y0: connected with loc_x0_y1, connected with loc_x1_y0. loc_x0_y1: connected with loc_x0_y0, connected with loc_x1_y1. loc_x0_y3: connected with loc_x1_y3, connected with loc_x0_y4. loc_x0_y4: connected with loc_x0_y3, connected with loc_x1_y4. loc_x1_y0: connected with loc_x0_y0, connected with loc_x2_y0. loc_x1_y1: connected with loc_x0_y1, connected with loc_x2_y1, connected with loc_x1_y2, connected with loc_x1_y0. loc_x1_y2: connected with loc_x1_y1, connected with loc_x1_y3, connected with loc_x2_y2. loc_x1_y3: connected with loc_x0_y3, connected with loc_x1_y2, connected with loc_x1_y4, connected with loc_x2_y3. loc_x1_y4: connected with loc_x0_y4, connected with loc_x1_y3, connected with loc_x2_y4. loc_x2_y0: connected with loc_x1_y0, connected with loc_x2_y1, connected with loc_x3_y0. loc_x2_y1: connected with loc_x1_y1, connected with loc_x2_y0, connected with loc_x2_y2, connected with loc_x3_y1. loc_x2_y2: connected with loc_x1_y2, connected with loc_x2_y1, connected with loc_x2_y3, connected with loc_x3_y2. loc_x2_y3: connected with loc_x1_y3, connected with loc_x2_y2, connected with loc_x3_y3, connected with loc_x2_y4. loc_x2_y4: connected with loc_x1_y4, connected with loc_x2_y3, connected with loc_x3_y4. loc_x3_y0: connected with loc_x2_y0, connected with loc_x3_y1, connected with loc_x4_y0. loc_x3_y1: connected with loc_x2_y1, connected with loc_x3_y0, connected with loc_x3_y2, connected with loc_x4_y1. loc_x3_y2: connected with loc_x2_y2, connected with loc_x3_y1, connected with loc_x4_y2, connected with loc_x3_y3. loc_x3_y3: connected with loc_x2_y3, connected with loc_x3_y2, connected with loc_x3_y4. loc_x3_y4: connected with loc_x2_y4, connected with loc_x3_y3, connected with loc_x4_y4. loc_x4_y0: connected with loc_x3_y0, connected with loc_x4_y1. loc_x4_y1: connected with loc_x3_y1, connected with loc_x4_y0, connected with loc_x4_y2. loc_x4_y2: connected with loc_x3_y2, connected with loc_x4_y1. loc_x4_y4: connected with loc_x3_y4.\n"
    
    f"Question 1: In this state, if moves from loc_x4_y2 to loc_x3_y2, is it True or False that loc_x3_y3 is marked as visited?\n"
    
    f"Answer 1:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. If there is any action needed to take in the question, we should first take the action and return all objects states, including those states that are not affected by the action.\n"
    f"Because the question contains one action, we should first take the action and get new states of all objects. After taking the action, we should return states of all objects, including states that are not effected by the action.\n"
    f"The action is \"moves from loc_x4_y2 to loc_x3_y2\". Based on the domain description, this action is executable. After taking the action, the curremt states of all objects should be:\n"
    f"Robot: at loc_x3_y2, has visited loc_x0_y0, has visited loc_x0_y1, has visited loc_x0_y3, has visited loc_x0_y4, has visited loc_x4_y2, has visited loc_x3_y2. loc_x0_y0: connected with loc_x0_y1, connected with loc_x1_y0. loc_x0_y1: connected with loc_x0_y0, connected with loc_x1_y1. loc_x0_y3: connected with loc_x1_y3, connected with loc_x0_y4. loc_x0_y4: connected with loc_x0_y3, connected with loc_x1_y4. loc_x1_y0: connected with loc_x0_y0, connected with loc_x2_y0. loc_x1_y1: connected with loc_x0_y1, connected with loc_x2_y1, connected with loc_x1_y2, connected with loc_x1_y0. loc_x1_y2: connected with loc_x1_y1, connected with loc_x1_y3, connected with loc_x2_y2. loc_x1_y3: connected with loc_x0_y3, connected with loc_x1_y2, connected with loc_x1_y4, connected with loc_x2_y3. loc_x1_y4: connected with loc_x0_y4, connected with loc_x1_y3, connected with loc_x2_y4. loc_x2_y0: connected with loc_x1_y0, connected with loc_x2_y1, connected with loc_x3_y0. loc_x2_y1: connected with loc_x1_y1, connected with loc_x2_y0, connected with loc_x2_y2, connected with loc_x3_y1. loc_x2_y2: connected with loc_x1_y2, connected with loc_x2_y1, connected with loc_x2_y3, connected with loc_x3_y2. loc_x2_y3: connected with loc_x1_y3, connected with loc_x2_y2, connected with loc_x3_y3, connected with loc_x2_y4. loc_x2_y4: connected with loc_x1_y4, connected with loc_x2_y3, connected with loc_x3_y4. loc_x3_y0: connected with loc_x2_y0, connected with loc_x3_y1, connected with loc_x4_y0. loc_x3_y1: connected with loc_x2_y1, connected with loc_x3_y0, connected with loc_x3_y2, connected with loc_x4_y1. loc_x3_y2: connected with loc_x2_y2, connected with loc_x3_y1, connected with loc_x4_y2, connected with loc_x3_y3. loc_x3_y3: connected with loc_x2_y3, connected with loc_x3_y2, connected with loc_x3_y4. loc_x3_y4: connected with loc_x2_y4, connected with loc_x3_y3, connected with loc_x4_y4. loc_x4_y0: connected with loc_x3_y0, connected with loc_x4_y1. loc_x4_y1: connected with loc_x3_y1, connected with loc_x4_y0, connected with loc_x4_y2. loc_x4_y2: connected with loc_x3_y2, connected with loc_x4_y1. loc_x4_y4: connected with loc_x3_y4.\n"
    f"Then, we compare each proposition in the question one by one.\n"
    f"loc_x3_y3 is marked as visited? ::: Robot: at loc_x3_y2, has visited loc_x0_y0, has visited loc_x0_y1, has visited loc_x0_y3, has visited loc_x0_y4, has visited loc_x4_y2, has visited loc_x3_y2.  ===>NOT SATISFIED.\n"
    f"Since there is a proposition in the question doesn't match with the current state, the question is false.\n"
    f"Final Answer: False.\n"
    
    f"——————\n"
    
    f"Current state exmaple 2: Robot: at loc_x4_y2, has visited loc_x4_y2. loc_x0_y0: connected with loc_x0_y1, connected with loc_x1_y0. loc_x0_y1: connected with loc_x0_y0, connected with loc_x1_y1. loc_x0_y3: connected with loc_x1_y3, connected with loc_x0_y4. loc_x0_y4: connected with loc_x0_y3, connected with loc_x1_y4. loc_x1_y0: connected with loc_x0_y0, connected with loc_x2_y0. loc_x1_y1: connected with loc_x0_y1, connected with loc_x2_y1, connected with loc_x1_y2, connected with loc_x1_y0. loc_x1_y2: connected with loc_x1_y1, connected with loc_x1_y3, connected with loc_x2_y2. loc_x1_y3: connected with loc_x0_y3, connected with loc_x1_y2, connected with loc_x1_y4, connected with loc_x2_y3. loc_x1_y4: connected with loc_x0_y4, connected with loc_x1_y3, connected with loc_x2_y4. loc_x2_y0: connected with loc_x1_y0, connected with loc_x2_y1, connected with loc_x3_y0. loc_x2_y1: connected with loc_x1_y1, connected with loc_x2_y0, connected with loc_x2_y2, connected with loc_x3_y1. loc_x2_y2: connected with loc_x1_y2, connected with loc_x2_y1, connected with loc_x2_y3, connected with loc_x3_y2. loc_x2_y3: connected with loc_x1_y3, connected with loc_x2_y2, connected with loc_x3_y3, connected with loc_x2_y4. loc_x2_y4: connected with loc_x1_y4, connected with loc_x2_y3, connected with loc_x3_y4. loc_x3_y0: connected with loc_x2_y0, connected with loc_x3_y1, connected with loc_x4_y0. loc_x3_y1: connected with loc_x2_y1, connected with loc_x3_y0, connected with loc_x3_y2, connected with loc_x4_y1. loc_x3_y2: connected with loc_x2_y2, connected with loc_x3_y1, connected with loc_x4_y2, connected with loc_x3_y3. loc_x3_y3: connected with loc_x2_y3, connected with loc_x3_y2, connected with loc_x3_y4. loc_x3_y4: connected with loc_x2_y4, connected with loc_x3_y3, connected with loc_x4_y4. loc_x4_y0: connected with loc_x3_y0, connected with loc_x4_y1. loc_x4_y1: connected with loc_x3_y1, connected with loc_x4_y0, connected with loc_x4_y2. loc_x4_y2: connected with loc_x3_y2, connected with loc_x4_y1. loc_x4_y4: connected with loc_x3_y4.\n"
    
    f"Question 2: In this state, is it True or False that loc_x2_y0 and loc_x2_y2 are not connected and loc_x4_y2 is marked visited?\n"
    
    f"Answer 2:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. If there is any action needed to take in the question, we should first take the action and return all objects states, including those states that are not affected by the action.\n"
    f"loc_x2_y0 and loc_x2_y2 are not connected ::: loc_x2_y0: connected with loc_x1_y0, connected with loc_x2_y1, connected with loc_x3_y0. ===> SATISFIED\n"
    f"loc_x4_y2 is marked visited? ::: Robot: at loc_x4_y2, has visited loc_x4_y2. ===>SATISFIED\n"
    f"Since all propositions in the question match with the curent state, so the question is true.\n"
    f"Final Answer: True.\n"
    
    f"——————\n"
)


TWOSHOTCOT_AE_VISITALL_EXAMPLE = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"Current state: loc_x1_y2 is connected to loc_x2_y2, loc_x2_y2 is connected to loc_x1_y2, loc_x1_y2 is connected to loc_x1_y3, loc_x1_y3 is connected to loc_x1_y2, loc_x2_y2 is connected to loc_x2_y3, loc_x2_y3 is connected to loc_x2_y2, robot is located at loc_x1_y2, loc_x1_y2 has been visited.\n"
    f"Question: Given the initial condition, the following actions are planned to be performed: robot moves from loc_x1_y2 to loc_x2_y2. Is it possible to execute it, True or False?\n"
    f"Answer: \n"
    f"Step 1: we can confirm whether this action is executable or not by checking the initial state.\n"
    f"A robot can move from location A to location B only if A and B is connected. We can see robot is currently at loc_x1_y2 and loc_x1_y2 is connected to loc_x2_y2. So this action is executable.\n"
    f"Step 2: we return the final answer based on the checking result.\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final Answer: True\n"
    f"---------------\n"
    f"(Example 2)\n"
    f"Current state: loc_x0_y0 is connected to loc_x0_y1, loc_x0_y1 is connected to loc_x0_y0, loc_x0_y1 is connected to loc_x1_y1, loc_x1_y1 is connected to loc_x1_y2, loc_x1_y2 is connected to loc_x1_y1, loc_x1_y2 is connected to loc_x2_y2, robot is located at loc_x0_y0, loc_x0_y0 has been visited. No direct or indirect connection from loc_x0_y0 to loc_x3_y3 exists\n"
    f"Question: Given the initial condition, the following actions are planned to be performed: robot moves from loc_x0_y0 to loc_x3_y3. Is it possible to execute it, True or False?\n"
    f"Answer: \n"
    f"Step 1: we can confirm whether this action is executable or not by checking the initial state.\n"
    f"A robot can move from location A to location B only if A and B is connected. We can see robot is currently at loc_x0_y0 and no direct or indirect connection from loc_x0_y0 to loc_x3_y3 exists. So this action is not executable.\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final Answer: False."
    f"---------------\n"
)


TWOSHOTCOT_STATE_VISITALL_EXAMPLE = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"Current state: Loc_x0_y0 and loc_x0_y1 are connected, loc_x0_y1 and loc_x0_y2 are connected, loc_x0_y2 and loc_x0_y3 are connected, loc_x0_y3 and loc_x1_y3 are connected, loc_x1_y3 and loc_x2_y3 are connected, loc_x1_y2 and loc_x1_y3 are connected, loc_x1_y2 and loc_x2_y2 are connected, loc_x2_y1 and loc_x2_y2 are connected, loc_x2_y0 and loc_x2_y1 are connected, loc_x3_y0 and loc_x3_y1 are connected, loc_x3_y1 and loc_x3_y2 are connected, loc_x3_y2 and loc_x3_y3 are connected, robot is located at loc_x1_y1, loc_x1_y1 is connected to loc_x1_y2.\n"
    f"Question: Given the initial condition, the following actions are performed: moves from loc_x1_y1 to loc_x1_y2 to reach the current state. In this state, if moves from loc_x1_y2 to loc_x1_y3, is it True or False that robot is at loc_x1_y3 and robot is not at loc_x1_y2?\n"
    f"Answer:\n"
    f"Step 1: We first execute the action and get the new state.\n"
    f"After taking the action 'moves from loc_x1_y2 to loc_x1_y3', robot is at loc_x1_y3. Then, the robot moves from loc_x1_y2 to loc_x1_y3, the robot is at loc_x1_y3. \n"
    f"Step 2: Then, we compare the state and the question and get the answer.\n"
    f"is it True or False that robot is at loc_x1_y3 and robot is not at loc_x1_y2? We can see now the robot it at loc_x1_y3."
    f"So the question is true.\n"
    f"Final Answer: False.\n"
    f"---------------\n"
    f"(Example 2)\n"
    f"Current state: Loc_x0_y0 and loc_x0_y1 are connected, loc_x0_y1 and loc_x0_y2 are connected, loc_x0_y2 and loc_x0_y3 are connected, loc_x1_y1 and loc_x1_y2 are connected, loc_x1_y2 and loc_x1_y3 are connected, loc_x1_y3 and loc_x2_y3 are connected, loc_x2_y2 and loc_x2_y1 are connected, loc_x2_y1 and loc_x3_y1 are connected, loc_x3_y0 and loc_x3_y1 are connected, loc_x3_y1 and loc_x3_y2 are connected, loc_x3_y2 and loc_x3_y3 are connected, loc_x2_y2 and loc_x3_y2 are connected, robot is located at loc_x0_y0, loc_x0_y0 is connected to loc_x0_y1.\n"
    f"Question: Given the initial condition, the following actions are performed: moves from loc_x0_y0 to loc_x0_y1 to reach the current state. In this state, if moves from loc_x0_y1 to loc_x2_y2, is it True or False that robot is at loc_x2_y2 and loc_x3_y1 is connected with loc_x4_y1?\n"
    f"Answer: \n"
    f"Step 1: We first execute the action and get the new state.\n"
    f"After taking the action 'moves from loc_x0_y0 to loc_x0_y1', the robot is currently at loc_x0_y1. Then the robot moves loc_x0_y1 to loc_x2_y2, the robot is now at loc_x2_y2."
    f"Step 2: Then, we compare the state and the question and get the answer.\n"
    f"is it True or False that robot is at loc_x2_y2 and loc_x3_y1 is connected with loc_x4_y1? We can see the robot is at loc_x2_y2. However, we can't find any description stating loc_x3_y1 is connected with loc_x4_y1."
    f"So the question is false.\n"
    f"Final Answer: False."
    f"---------------\n"
)




#--------------
#Spanner domain
#---------------
SPANNER_DOMAIN_DESCRIPTION = (
    f"[Domain Description]\n"
    f"The Spanner domain involves man, spanner, location and nut. This domain involves a man use spanners to tighten nuts. Nut's location is fixed, but man and spanner's location can be changed. Man can carry multiple spanners at a time. Location can be location_x, gate or shed.\n"
    
    f"Different properties are used to describe different objects. For man we use: at location_x, carrying spanner_x/carrying nothing. For spanner we use: at location_x, carried by man, usable/not usable. For location we use: linked with location_x. For nut we use: at location_x, loose(not secured)/tighten(secured).\n"
    
    f"Following actions are executable only if all preconditions are met, if any condition are not satisfied, the action is not executable.\n"
    
    f"Man can 'walk' from location A to location B. This action is executable only if all following preconditions are satisfied: man is currently at location A, loacation A and B are linked.\n"
    
    f"Man can 'pick up' a spanner from location A. This action is executable only if all following preconditions are satisfied: man is currently at location A, the spanner is currently at location A.\n"
    
    f"Man can 'tighten' a nut with a spanner at location A. This action is executable only if all following preconditions are satisfied: man is currently at location A, the nut man is at location A, man is carrying the spanner, the spanner is useable, the nut is loose.\n"
    
    f"Executing an action will change states of related objects.\n"
    
    f"Man can 'walk' from location A to location B. This action will result in: the man is at location B.\n"
    
    f"Man can 'pick up' a spanner from location A. This action will result in: the spanner is not at location A, the spanner is carried by the man, the man is carrying the spanner.\n"
    
    f"Man can 'tighten' a nut with a spanner at location A. This action will result in: the nut is not loose, the nut is tighten, the spanner is not useable.\n"
)


INITIAL_STATE_EXTRACTOR_SPANNER_PROMPT = (
    f"This is a question related to the spanner domain. You are required to extract the initial state of every objects in this plan, including man, nuts and spanner. Your answer must satisfy all the following requirements. First, think and respond with the format from the example above, including the word choice and paragraph structure. Second, each object's state should contain all properties mentioned in the domain description above. Besides, don't use any markdown formatting."
)


INITIAL_STATE_EXTRACTOR_SPANNER_EXAMPLE = (
    f"[Examples]\n"
    
    f"Initial state example 1: A link between location1 and location2 exists, a link between location5 and location6 exists, a link between location9 and gate exists, a link between shed and location1 exists, bob is currently at shed, location2 is linked to location3, location3 is linked to location4, location4 is linked to location5, location6 is linked to location7, location7 and location8 are linked, location8 and location9 are linked, nut1 is located at gate, nut1 is not secured, nut2 is currently at gate, nut2 is loose, nut3 is located at gate, nut3 is loose, nut4 is located at gate, nut4 is loose, nut5 is at gate, nut5 is loose, spanner1 is currently at location3, spanner1 is usable, spanner2 can be used, spanner2 is located at location5, spanner3 is currently at location2, spanner3 is usable, spanner4 is functional, spanner4 is located at location6, spanner5 is functional and spanner5 is located at location3.\n"
    
    f"Extracted from initial state example 1:\n" 
    f"We can find following objects in the intial state description: bob, location1,  location2,  location3,  location4,  location5,  location6,  location7,  location8,  location9, gate, shed, nut1, nut2, nut3, nut4, nut5, spanner1, spanner2, spanner3, spanner4, spanner5.\n"
    
    f"bob is currently at shed, ::: Bob: at shed, carrying nothing.\n"
    
    f"A link between location1 and location2 exists, a link between location5 and location6 exists, a link between location9 and gate exists, a link between shed and location1 exists, bob is currently at shed, location2 is linked to location3, location3 is linked to location4, location4 is linked to location5, location6 is linked to location7, location7 and location8 are linked, location8 and location9 are linked. ::: Shed: linked with location1. Location1: linked with location 2, linked with shed. Location2: linked with location 1, linked with location 3. Location3: linked with location 2, linked with location 4. Location4: linked with location 3, linked with location 5. Location5: linked with location 4, linked with location 6. Location6: linked with location 5, linked with location 7. Location7: linked with location 6, linked with location 8. Location8: linked with location 7, linked with location 9. Location9: linked with location 8, linked with gate. Gate: linked with location9.\n"
    
    f"nut1 is located at gate, nut1 is not secured, ::: nut1: at gate, loose.\n"
    f"nut2 is currently at gate, nut2 is loose, ::: nut2: at gate, loose.\n"
    f"nut3 is located at gate, nut3 is loose, ::: nut3: at gate, loose.\n"
    f"nut4 is located at gate, nut4 is loose, ::: nut4: at gate, loose.\n"
    f"nut5 is at gate, nut5 is loose, ::: nut5: at gate, loose.\n"
    
    f"spanner1 is currently at location3, spanner1 is usable, ::: spanner1: at location3, usable.\n"
    f"spanner2 can be used, spanner2 is located at location5, ::: spanner2: at location5, usable.\n"
    f"spanner3 is currently at location2, spanner3 is usable, ::: spanner3: at location2, usable.\n"
    f"spanner4 is functional, spanner4 is located at location6, ::: spanner4: at location6, usable.\n"
    f"spanner5 is functional and spanner5 is located at location3. ::: spanner5: at location3, usable.\n"
    
    f"After extracting all states, we organize all states into a new paragraph.\n"
    f"Bob: at shed, carrying nothing. Shed: linked with location1. Location1: linked with location 2, linked with shed. Location2: linked with location 1, linked with location 3. Location3: linked with location 2, linked with location 4. Location4: linked with location 3, linked with location 5. Location5: linked with location 4, linked with location 6. Location6: linked with location 5, linked with location 7. Location7: linked with location 6, linked with location 8. Location8: linked with location 7, linked with location 9. Location9: linked with location 8, linked with gate. Gate: linked with location9. nut1: at gate, loose. nut2: at gate, loose. nut3: at gate, loose. nut4: at gate, loose. nut5: at gate, loose. spanner1: at location3, usable. spanner2: at location5, usable. spanner3: at location2, usable. spanner4: at location6, usable. spanner5: at location3, usable.\n"
    
    f"———————\n"
    
    f"Initial state example 2: A link between shed and location1 exists, bob is currently at shed, location1 and location2 are linked, location2 is linked to location3, location3 and location4 are linked, location4 is linked to location5, location5 and location6 are linked, location6 is linked to location7, location7 is linked to location8, location8 and location9 are linked, location9 and gate are linked, nut1 is located at gate, nut1 is loose, nut2 is at gate, nut2 is loose, nut3 is currently at gate, nut3 is not secured, nut4 is located at gate, nut4 is not secured, nut5 is at gate, nut5 is loose, spanner1 can be used, spanner1 is at location8, spanner2 can be used, spanner2 is currently at location6, spanner3 is located at location2, spanner3 is usable, spanner4 is at location2, spanner4 is usable, spanner5 is currently at location6 and spanner5 is functional.\n"
    
    f"Extracted from initial state example 2:\n"
    f"We can find following objects in the initial state description: bob, shed, location1, location2, location3, location4, location5, location6, location7, location8, location9, gate, nut1, nut2, nut3, nut4, nut5, spanner1, spanner2, spanner3, spanner4, spanner5.\n"
    
    f"bob is currently at shed, ::: Bob: at shed, carrying nothing.\n"
    
    f"A link between shed and location1 exists, location1 and location2 are linked, location2 is linked to location3, location3 and location4 are linked, location4 is linked to location5, location5 and location6 are linked, location6 is linked to location7, location7 is linked to location8, location8 and location9 are linked, location9 and gate are linked. ::: Shed: linked with location1. Location1: linked with shed, linked with location2. Location2: linked with location1, linked with location3. Location3: linked with location2, linked with location4. Location4: linked with location3, linked with location5. Location5: linked with location4, linked with location6. Location6: linked with location5, linked with location7. Location7: linked with location6, linked with location8. Location8: linked with location7, linked with location9. Location9: linked with location8, linked with gate. Gate: linked with location9.\n"
    
    f"nut1 is located at gate, nut1 is loose, ::: nut1: at gate, loose.\n"
    f"nut2 is at gate, nut2 is loose, ::: nut2: at gate, loose.\n"
    f"nut3 is currently at gate, nut3 is not secured, ::: nut3: at gate, not secured.\n"
    f"nut4 is located at gate, nut4 is not secured, ::: nut4: at gate, not secured.\n"
    f"nut5 is at gate, nut5 is loose, ::: nut5: at gate, loose.\n"
    
    f"spanner1 can be used, spanner1 is at location8, ::: spanner1: at location8, usable.\n"
    f"spanner2 can be used, spanner2 is currently at location6, ::: spanner2: at location6, usable.\n"
    f"spanner3 is located at location2, spanner3 is usable, ::: spanner3: at location2, usable.\n"
    f"spanner4 is at location2, spanner4 is usable, ::: spanner4: at location2, usable.\n"
    f"spanner5 is currently at location6 and spanner5 is functional. ::: spanner5: at location6, usable.\n"
    
    f"After extracting all states, we organize all states into a new paragraph.\n"
    f"Bob: at shed, carrying nothing. Shed: linked with location1. Location1: linked with shed, linked with location2. Location2: linked with location1, linked with location3. Location3: linked with location2, linked with location4. Location4: linked with location3, linked with location5. Location5: linked with location4, linked with location6. Location6: linked with location5, linked with location7. Location7: linked with location6, linked with location8. Location8: linked with location7, linked with location9. Location9: linked with location8, linked with gate. Gate: linked with location9. nut1: at gate, loose. nut2: at gate, loose. nut3: at gate, not secured. nut4: at gate, not secured. nut5: at gate, loose. spanner1: at location8, usable. spanner2: at location6, usable. spanner3: at location2, usable. spanner4: at location2, usable. spanner5: at location6, usable.\n"
    
    f"———————\n"
)



QUESTION_EXTRACTOR_SPANNER_EXAMPLE = (
    f"[Examples]\n"
    
    f"Plan example 1: Given the initial condition, the following actions are performed: bob walks from shed to location1, bob picks up spanner5 from location1, bob picks up spanner4 from location1, bob walks to location2 from location1, bob walks from location2 to location3, from location3 to location4, bob walks, spanner1 is picked up by bob from location4, bob walks to location5 from location4, bob walks from location5 to location6 and from location6, bob picks up spanner3 to reach the current state.\n"
    
    f"Question extracted from plan 1: In this state, if bob walks from location6 to location7, is it True or False that nut3 is at gate and spanner2 is not currently at location1?\n"
    
    f"———————\n"
    
    f"Plan example 2: Given the initial condition, the following actions are performed: bob walks to location1 from shed, spanner5 is picked up by bob from location1, bob picks up spanner4 from location1, bob walks from location1 to location2, from location2 to location3, bob walks, bob walks from location3 to location4, spanner1 is picked up by bob from location4, bob walks from location4 to location5, bob walks from location5 to location6 and bob picks up spanner3 from location6 to reach the current state. In this state, are all of the following valid properties of the state that involve negations? a link between gate and location1 exists, a link between gate and location6 does not exist, a link between gate and location7 does not exist, a link between gate and location8 exists, a link between gate and location9 does not exist, a link between location1 and gate does not exist, a link between location1 and shed does not exist, a link between location2 and gate does not exist, a link between location2 and location1 does not exist, a link between location2 and location7 does not exist, a link between location2 and location8 does not exist, a link between location3 and location2 does not exist, a link between location3 and location5 exists, a link between location3 and location6 exists, a link between location3 and location7 exists, a link between location4 and gate does not exist, a link between location4 and location6 exists, a link between location4 and shed exists, a link between location5 and location2 exists, a link between location5 and location3 does not exist, a link between location5 and location8 exists, a link between location5 and location9 does not exist, a link between location5 and shed does not exist, a link between location6 and location4 does not exist, a link between location6 and location8 exists, a link between location7 and location2 does not exist, a link between location7 and shed exists, a link between location8 and location1 exists, a link between location8 and location2 does not exist, a link between location8 and location5 exists, a link between location8 and location6 does not exist, a link between location8 and shed does not exist, a link between location9 and location1 does not exist, a link between location9 and location4 exists, a link between shed and location2 does not exist, a link between shed and location3 exists, bob is at location1, bob is at location2, bob is carrying spanner2, bob is currently at location3, bob is currently at location8, bob is located at gate, bob is located at location9, bob is located at shed, bob is not at location4, bob is not at location5, bob is not currently at location7, gate and location2 are not linked, gate and location5 are not linked, gate and shed are linked, gate is not linked to location3, gate is not linked to location4, location1 and location4 are linked, location1 and location6 are linked, location1 and location7 are not linked, location1 is linked to location3, location1 is linked to location5, location1 is not linked to location8, location1 is not linked to location9, location2 and location4 are not linked, location2 and location5 are not linked, location2 and location6 are not linked, location2 and shed are linked, location2 is linked to location9, location3 and location1 are not linked, location3 and location8 are linked, location3 and shed are not linked, location3 is linked to gate, location3 is linked to location9, location4 and location8 are not linked, location4 is linked to location1, location4 is linked to location2, location4 is linked to location3, location4 is linked to location7, location4 is linked to location9, location5 and location1 are not linked, location5 is linked to location4, location5 is not linked to gate, location5 is not linked to location7, location6 and location1 are linked, location6 and location5 are not linked, location6 and shed are linked, location6 is linked to gate, location6 is not linked to location2, location6 is not linked to location3, location6 is not linked to location9, location7 and location4 are not linked, location7 and location5 are not linked, location7 is linked to gate, location7 is linked to location1, location7 is not linked to location3, location7 is not linked to location6, location7 is not linked to location9, location8 and location4 are linked, location8 is linked to location3, location8 is linked to location7, location8 is not linked to gate, location9 and location5 are linked, location9 and location7 are linked, location9 and shed are not linked, location9 is linked to location2, location9 is linked to location6, location9 is not linked to location3, location9 is not linked to location8, nut1 is at location5, nut1 is at location9, nut1 is located at location1, nut1 is located at location3, nut1 is located at location7, nut1 is not at location8, nut1 is not currently at location4, nut1 is not currently at location6, nut1 is not located at location2, nut1 is not located at shed, nut1 is tightened, nut2 is at location3, nut2 is at location6, nut2 is currently at location5, nut2 is currently at location9, nut2 is located at location8, nut2 is not at location1, nut2 is not at shed, nut2 is not currently at location4, nut2 is not located at location2, nut2 is not located at location7, nut2 is tightened, nut3 is at location1, nut3 is currently at location2, nut3 is currently at location5, nut3 is currently at location6, nut3 is currently at location8, nut3 is located at location4, nut3 is located at shed, nut3 is not currently at location3, nut3 is not currently at location7, nut3 is not located at location9, nut4 is at location6, nut4 is currently at location7, nut4 is currently at location9, nut4 is located at location2, nut4 is not at location8, nut4 is not currently at location1, nut4 is not currently at location4, nut4 is not currently at shed, nut4 is not located at location3, nut4 is not located at location5, nut4 is tightened, nut5 is at location2, nut5 is at location3, nut5 is at location5, nut5 is at location8, nut5 is currently at location1, nut5 is located at shed, nut5 is not currently at location7, nut5 is not currently at location9, nut5 is not located at location4, nut5 is not located at location6, shed and location4 are linked, shed and location6 are not linked, shed and location8 are linked, shed is linked to location9, shed is not linked to gate, shed is not linked to location5, shed is not linked to location7, spanner1 is at gate, spanner1 is at location3, spanner1 is at location4, spanner1 is at location5, spanner1 is at location8, spanner1 is currently at location2, spanner1 is located at location9, spanner1 is not at location1, spanner1 is not at location6, spanner1 is not at location7, spanner1 is not at shed, spanner2 is currently at location2, spanner2 is located at location5, spanner2 is located at location6, spanner2 is not currently at location4, spanner2 is not currently at location9, spanner2 is not currently at shed, spanner2 is not located at gate, spanner2 is not located at location1, spanner2 is not located at location3, spanner2 is not located at location8, spanner3 is currently at location1, spanner3 is currently at shed, spanner3 is located at location3, spanner3 is not at location2, spanner3 is not at location5, spanner3 is not at location6, spanner3 is not currently at location4, spanner3 is not currently at location8, spanner3 is not located at gate, spanner3 is not located at location7, spanner3 is not located at location9, spanner4 is currently at location2, spanner4 is currently at location7, spanner4 is located at gate, spanner4 is located at location1, spanner4 is located at location8, spanner4 is not at location3, spanner4 is not at location6, spanner4 is not at location9, spanner4 is not at shed, spanner4 is not located at location4, spanner4 is not located at location5, spanner5 is at location1, spanner5 is at location3, spanner5 is currently at location4, spanner5 is currently at location5, spanner5 is located at gate, spanner5 is located at shed, spanner5 is not at location2, spanner5 is not at location7, spanner5 is not at location9, spanner5 is not currently at location8, spanner5 is not located at location6, tightening of nut3 is complete and tightening of nut5 is complete. Respond with True or False.\n"
    
    f"Question extracted from plan 2: In this state, are all of the following valid properties of the state that involve negations? a link between gate and location1 exists, a link between gate and location6 does not exist, a link between gate and location7 does not exist, a link between gate and location8 exists, a link between gate and location9 does not exist, a link between location1 and gate does not exist, a link between location1 and shed does not exist, a link between location2 and gate does not exist, a link between location2 and location1 does not exist, a link between location2 and location7 does not exist, a link between location2 and location8 does not exist, a link between location3 and location2 does not exist, a link between location3 and location5 exists, a link between location3 and location6 exists, a link between location3 and location7 exists, a link between location4 and gate does not exist, a link between location4 and location6 exists, a link between location4 and shed exists, a link between location5 and location2 exists, a link between location5 and location3 does not exist, a link between location5 and location8 exists, a link between location5 and location9 does not exist, a link between location5 and shed does not exist, a link between location6 and location4 does not exist, a link between location6 and location8 exists, a link between location7 and location2 does not exist, a link between location7 and shed exists, a link between location8 and location1 exists, a link between location8 and location2 does not exist, a link between location8 and location5 exists, a link between location8 and location6 does not exist, a link between location8 and shed does not exist, a link between location9 and location1 does not exist, a link between location9 and location4 exists, a link between shed and location2 does not exist, a link between shed and location3 exists, bob is at location1, bob is at location2, bob is carrying spanner2, bob is currently at location3, bob is currently at location8, bob is located at gate, bob is located at location9, bob is located at shed, bob is not at location4, bob is not at location5, bob is not currently at location7, gate and location2 are not linked, gate and location5 are not linked, gate and shed are linked, gate is not linked to location3, gate is not linked to location4, location1 and location4 are linked, location1 and location6 are linked, location1 and location7 are not linked, location1 is linked to location3, location1 is linked to location5, location1 is not linked to location8, location1 is not linked to location9, location2 and location4 are not linked, location2 and location5 are not linked, location2 and location6 are not linked, location2 and shed are linked, location2 is linked to location9, location3 and location1 are not linked, location3 and location8 are linked, location3 and shed are not linked, location3 is linked to gate, location3 is linked to location9, location4 and location8 are not linked, location4 is linked to location1, location4 is linked to location2, location4 is linked to location3, location4 is linked to location7, location4 is linked to location9, location5 and location1 are not linked, location5 is linked to location4, location5 is not linked to gate, location5 is not linked to location7, location6 and location1 are linked, location6 and location5 are not linked, location6 and shed are linked, location6 is linked to gate, location6 is not linked to location2, location6 is not linked to location3, location6 is not linked to location9, location7 and location4 are not linked, location7 and location5 are not linked, location7 is linked to gate, location7 is linked to location1, location7 is not linked to location3, location7 is not linked to location6, location7 is not linked to location9, location8 and location4 are linked, location8 is linked to location3, location8 is linked to location7, location8 is not linked to gate, location9 and location5 are linked, location9 and location7 are linked, location9 and shed are not linked, location9 is linked to location2, location9 is linked to location6, location9 is not linked to location3, location9 is not linked to location8, nut1 is at location5, nut1 is at location9, nut1 is located at location1, nut1 is located at location3, nut1 is located at location7, nut1 is not at location8, nut1 is not currently at location4, nut1 is not currently at location6, nut1 is not located at location2, nut1 is not located at shed, nut1 is tightened, nut2 is at location3, nut2 is at location6, nut2 is currently at location5, nut2 is currently at location9, nut2 is located at location8, nut2 is not at location1, nut2 is not at shed, nut2 is not currently at location4, nut2 is not located at location2, nut2 is not located at location7, nut2 is tightened, nut3 is at location1, nut3 is currently at location2, nut3 is currently at location5, nut3 is currently at location6, nut3 is currently at location8, nut3 is located at location4, nut3 is located at shed, nut3 is not currently at location3, nut3 is not currently at location7, nut3 is not located at location9, nut4 is at location6, nut4 is currently at location7, nut4 is currently at location9, nut4 is located at location2, nut4 is not at location8, nut4 is not currently at location1, nut4 is not currently at location4, nut4 is not currently at shed, nut4 is not located at location3, nut4 is not located at location5, nut4 is tightened, nut5 is at location2, nut5 is at location3, nut5 is at location5, nut5 is at location8, nut5 is currently at location1, nut5 is located at shed, nut5 is not currently at location7, nut5 is not currently at location9, nut5 is not located at location4, nut5 is not located at location6, shed and location4 are linked, shed and location6 are not linked, shed and location8 are linked, shed is linked to location9, shed is not linked to gate, shed is not linked to location5, shed is not linked to location7, spanner1 is at gate, spanner1 is at location3, spanner1 is at location4, spanner1 is at location5, spanner1 is at location8, spanner1 is currently at location2, spanner1 is located at location9, spanner1 is not at location1, spanner1 is not at location6, spanner1 is not at location7, spanner1 is not at shed, spanner2 is currently at location2, spanner2 is located at location5, spanner2 is located at location6, spanner2 is not currently at location4, spanner2 is not currently at location9, spanner2 is not currently at shed, spanner2 is not located at gate, spanner2 is not located at location1, spanner2 is not located at location3, spanner2 is not located at location8, spanner3 is currently at location1, spanner3 is currently at shed, spanner3 is located at location3, spanner3 is not at location2, spanner3 is not at location5, spanner3 is not at location6, spanner3 is not currently at location4, spanner3 is not currently at location8, spanner3 is not located at gate, spanner3 is not located at location7, spanner3 is not located at location9, spanner4 is currently at location2, spanner4 is currently at location7, spanner4 is located at gate, spanner4 is located at location1, spanner4 is located at location8, spanner4 is not at location3, spanner4 is not at location6, spanner4 is not at location9, spanner4 is not at shed, spanner4 is not located at location4, spanner4 is not located at location5, spanner5 is at location1, spanner5 is at location3, spanner5 is currently at location4, spanner5 is currently at location5, spanner5 is located at gate, spanner5 is located at shed, spanner5 is not at location2, spanner5 is not at location7, spanner5 is not at location9, spanner5 is not currently at location8, spanner5 is not located at location6, tightening of nut3 is complete and tightening of nut5 is complete. Respond with True or False.\n"
    
    f"———————\n" 
)


ACTION_TAKER_SPANNER_PROMPT = (
    f"Based on the domain description and examples above, take the action and return the new state of all objects. Your answer must satisfy all the following requirements. First, think and respond like examples above, you are required to return states of all objects(spanner, man and nuts) and states of locations, including states that are not effected by the action. Second, each object's state must contain all properties mentioned in the domain description above. Third, after your analysis, please return states of all objects into a new paragraph as the end of your answer. Your final paragraph should use the format like: \"Bob: at shed, carrying nothing. Shed: linked with location1. \" Besides, don't use any markdown formatting."
)


ACTION_TAKER_SPANNER_EXAMPLE = (
    f"[Examples]\n"    
    f"Current state example 1: Bob: at shed, carrying nothing. Shed: linked with location1. Location1: linked with shed, linked with location2. Location2: linked with location1, linked with location3. Location3: linked with location2, linked with location4. Location4: linked with location3, linked with location5. Location5: linked with location4, linked with location6. Location6: linked with location5, linked with location7. Location7: linked with location6, linked with location8. Location8: linked with location7, linked with location9. Location9: linked with location8, linked with gate. Gate: linked with location9. nut1: at gate, loose. nut2: at gate, loose. nut3: at gate, loose. nut4: at gate, loose. nut5: at gate, loose. spanner1: at location3, usable. spanner2: at location5, usable. spanner3: at location2, usable. spanner4: at location6, usable. spanner5: at location3, usable.\n"
    f"Action 1: Bob walks from shed to location1.\n"
    f"Answer 1:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Bob: at shed, carrying nothing.\n" 
    f"Based on the domain description, Man can 'walk' from location A to location B. This action will result in: the man is at location B.\n"
    f"the man is at location B. ::: Bob: at location1, carrying nothing.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into one paragraph.\n"
    f"Bob: at location1, carrying nothing. Shed: linked with location1. Location1: linked with shed, linked with location2. Location2: linked with location1, linked with location3. Location3: linked with location2, linked with location4. Location4: linked with location3, linked with location5. Location5: linked with location4, linked with location6. Location6: linked with location5, linked with location7. Location7: linked with location6, linked with location8. Location8: linked with location7, linked with location9. Location9: linked with location8, linked with gate. Gate: linked with location9. nut1: at gate, loose. nut2: at gate, loose. nut3: at gate, loose. nut4: at gate, loose. nut5: at gate, loose. spanner1: at location3, usable. spanner2: at location5, usable. spanner3: at location2, usable. spanner4: at location6, usable. spanner5: at location3, usable.\n"
    
    f"———————\n"
    
    f"Current state example 2: Bob: at location4, carrying spanner4. Shed: linked with location1. Location1: linked with shed, linked with location2. Location2: linked with location1, linked with location3. Location3: linked with location2, linked with location4. Location4: linked with location3, linked with location5. Location5: linked with location4, linked with location6. Location6: linked with location5, linked with location7. Location7: linked with location6, linked with location8. Location8: linked with location7, linked with location9. Location9: linked with location8, linked with gate. Gate: linked with location9. nut1: at gate, loose. nut2: at gate, loose. nut3: at gate, loose. nut4: at gate, loose. nut5: at gate, loose. spanner1: at location4, usable. spanner2: at location7, usable. spanner3: at location6, usable. spanner4: carried by Bob, usable. spanner5: at location1, usable.\n"
    f"Action 2: Bob picks up spanner1 from location4.\n"
    f"Answer 2:\n"
    f"Based on the current state and the domain description, we first find states of related objects, then we can take the action and return new states of all objects.\n"
    f"Bob: at location4, carrying nothing. spanner1: at location4, usable.\n"
    f"Based on the domain description, man can 'pick up' a spanner from location A. This action will result in: the spanner is not at location A, the spanner is carried by the man, the man is carrying the spanner.\n"
    f"the spanner is not at location A, the spanner is carried by the man ::: spanner1: carried by bob, usable.\n" 
    f"the man is carrying the spanner. ::: Bob: at location4, carrying spanner4, carrying spanner1.\n"
    f"Then, we return states of all objects, including those states that are not affected by the action and organize them into one paragraph.\n"
    f"Bob: at location4, carrying spanner4, carrying spanner1. Shed: linked with location1. Location1: linked with shed, linked with location2. Location2: linked with location1, linked with location3. Location3: linked with location2, linked with location4. Location4: linked with location3, linked with location5. Location5: linked with location4, linked with location6. Location6: linked with location5, linked with location7. Location7: linked with location6, linked with location8. Location8: linked with location7, linked with location9. Location9: linked with location8, linked with gate. Gate: linked with location9. nut1: at gate, loose. nut2: at gate, loose. nut3: at gate, loose. nut4: at gate, loose. nut5: at gate, loose. spanner1: carried by bob, usable.  spanner2: at location7, usable. spanner3: at location6, usable. spanner4: at location1, usable. spanner5: at location1, usable.\n"
    
    f"———————\n"
)

EXECUTABILITY_CHECKER_SPANNER_EXAMPLE = (
    f"[Examples]"
    f"Current state example 1: Bob: at shed, carrying nothing. Shed: linked with location1. Location1: linked with shed, linked with location2. Location2: linked with location1, linked with location3. Location3: linked with location2, linked with location4. Location4: linked with location3, linked with location5. Location5: linked with location4, linked with location6. Location6: linked with location5, linked with location7. Location7: linked with location6, linked with location8. Location8: linked with location7, linked with location9. Location9: linked with location8, linked with gate. Gate: linked with location9. nut1: at gate, loose. nut2: at gate, loose. nut3: at gate, loose. nut4: at gate, not secured. nut5: at gate, loose. spanner1: at location8, usable. spanner2: at location6, usable. spanner3: at location2, usable. spanner4: at location2, usable. spanner5: at location6, usable.\n"
    
    f"Action 1: Bob walks from shed to location1.\n"
    
    f"Answer 1:\n"
    f"In order to check whether this action is executable or not, we first need to find states of objects related to this action, then check whether all preconditions of this action are satisfied.\n"
    f"Bob: at shed, carrying nothing. Shed: linked with location1.\n"
    f"Based on the domain description, Man can 'walk' from location A to location B. This action is executable only if all following preconditions are satisfied: man is currently at location A, loacation A and B are linked.\n"
    f"man is currently at location A, ::: Bob: at shed, carrying nothing. ===> SATISFY\n"
    f"loacation A and B are linked. ::: Shed: linked with location1. ===> SATISFY\n"
    f"Since all preconditions are satisfied, the action is executable.\n"
    f"Final answer: True.\n"
    
    f"———————\n"
    
    f"Current state example 2: Bob: at shed, carrying nothing. Shed: linked with location1. Location1: linked with location2, linked with shed. Location2: linked with location1, linked with location3. Location3: linked with location2, linked with location4. Location4: linked with location3, linked with location5. Location5: linked with location4, linked with location6. Location6: linked with location5, linked with location7. Location7: linked with location6, linked with location8. Location8: linked with location7, linked with location9. Location9: linked with location8, linked with gate. Gate: linked with location9. nut1: at gate, loose. nut2: at gate, loose. nut3: at gate, loose. nut4: at gate, loose. nut5: at gate, loose. spanner1: at location4, usable. spanner2: at location7, usable. spanner3: at location6, usable. spanner4: at location1, usable. spanner5: at location1, usable.\n"
    
    f"Action 2: Bob picks up spanner5 from location1.\n"
    
    f"Answer 2:\n"
    f"In order to check whether this action is executable or not, we first need to find states of objects related to this action, then check whether all preconditions of this action are satisfied.\n"
    f"Bob: at shed, carrying nothing. spanner5: at location1, usable.\n"
    f"Based on the domain description, Man can 'pick up' a spanner from location A. This action is executable only if all following preconditions are satisfied: man is currently at location A, the spanner is currently at location A.\n"
    f"man is currently at location A, ::: Bob: at shed, carrying nothing. ===> NOT SATISFY\n"
    f"Since not all preconditions are satisfied, the action is not executale.\n"
    f"Final answer: False.\n"
    
    f"———————\n"
)


STATE_CHECKER_SPANNER_EXAMPLE = (
    f"[Examples]\n"
    
    f"Current state example 1: Bob: at location1, carrying nothing. Shed: linked with location1. Location1: linked with shed, linked with location2. Location2: linked with location1, linked with location3. Location3: linked with location2, linked with location4. Location4: linked with location3, linked with location5. Location5: linked with location4, linked with location6. Location6: linked with location5, linked with location7. Location7: linked with location6, linked with location8. Location8: linked with location7, linked with location9. Location9: linked with location8, linked with gate. Gate: linked with location9. nut1: at gate, loose. nut2: at gate, loose. nut3: at gate, not secured. nut4: at gate, loose. nut5: at gate, loose. spanner1: at location6, usable. spanner2: at location8, usable. spanner3: at location8, usable. spanner4: at location5, usable. spanner5: at location7, usable.\n"
    
    f"Question 1: In this state, are all of the following valid properties of the state that do not involve negations True or False: bob is at location3, bob is at shed, bob is currently at location2, nut1 is currently at location8, nut1 is currently at location9, nut1 is located at shed, nut2 is at location1, nut2 is at location3.\n"
    
    f"Answer 1:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. If there is any action needed to take in the question, we should first take the action and return all objects states, including those states that are not affected by the action.\n"
    f"bob is at location3, bob is at shed, bob is currently at location2, ::: Bob: at location1, carrying nothing. ===> NOT MATCH.\n" 
    f"Since there are some propositions in the question doesn't match with the current state, the question is false.\n"
    f"Final Answer: False.\n"
    
    f"———————\n"
    
    f"Current state example 2: Bob: at gate, carrying spanner3, carrying spanner5, carrying spanner1. Shed: linked with location1. Location1: linked with shed, linked with location2. Location2: linked with location1, linked with location3. Location3: linked with location2, linked with location4. Location4: linked with location3, linked with location5. Location5: linked with location4, linked with location6. Location6: linked with location5, linked with location7. Location7: linked with location6, linked with location8. Location8: linked with location7, linked with location9. Location9: linked with location8, linked with gate. Gate: linked with location9. nut1: at gate, loose. nut2: at gate, loose. nut3: at gate, not secured. nut4: at gate, not secured. nut5: at gate, loose. spanner1: carried by Bob, usable. spanner2: at location5, usable. spanner3: carried by Bob, usable. spanner4: at location6, usable. spanner5: carried by Bob, usable.\n"
    
    f"Question 2: In this state, if bob uses spanner1 to tighten nut2. Are all of the following valid properties of the state that do not involve negations True or False: bob is carrying spanner1, bob is carrying spanner2, spanner3 is carried by bob and spanner5 is carried by bob?\n"
    
    f"Answer 2:\n"
    f"In order to check whether the question matches with the current state, we need to find related objects in the current state, and then compare one by one. If any object can't match, then the question is false. If there is any action needed to take in the question, we should first take the action and return all objects states, including those states that are not affected by the action.\n"
    f"Because the question contains one action, we should first take the action and get new states of all objects. After taking the action, we should return states of all objects, including states that are not effected by the action.\n"
    f"The action is 'bob uses spanner1 to tighten nut2'. Based on the domain description, this action is executable(the spanner is carried by man, the spanner is usable, the nut and the man is at the same location, the nut is loose).\n"
    f"After taking the action, the curremt states of all objects should be: Bob: at gate, carrying spanner3, carrying spanner5, carrying spanner1. Shed: linked with location1. Location1: linked with shed, linked with location2. Location2: linked with location1, linked with location3. Location3: linked with location2, linked with location4. Location4: linked with location3, linked with location5. Location5: linked with location4, linked with location6. Location6: linked with location5, linked with location7. Location7: linked with location6, linked with location8. Location8: linked with location7, linked with location9. Location9: linked with location8, linked with gate. Gate: linked with location9. nut1: at gate, loose. nut2: at gate, tighten. nut3: at gate, not secured. nut4: at gate, not secured. nut5: at gate, loose. spanner1: carried by Bob, not usable. spanner2: at location5, usable. spanner3: carried by Bob, usable. spanner4: at location6, usable. spanner5: carried by Bob, usable.\n"
    f"Then, we compare each proposition in the question one by one.\n"
    f"bob is carrying spanner1, spanner3 is carried by bob and spanner5 is carried by bob? ::: Bob: at gate, carrying spanner3, carrying spanner5, carrying spanner1. ===> MATCH\n"
    f"Since all propositions in the question match with the curent state, so the question is true.\n"
    f"Final Answer: True.\n"
    
    f"———————\n"
)

TWOSHOTCOT_AE_SPANNER_EXAMPLE = (
    f"[Examples]\n"
    f"(Example 1)\n"
    f"Current state: A link exists between location1 and location2, location2 and location3 are linked, location3 and location4 are linked, location4 is linked to location5, alice is at location3, alice is carrying spanner2, nut1 is at location4 and is loose, nut2 is at location3 and is loose, nut3 is at location2 and is not secured, spanner1 is at location2 and functional, spanner2 is and functional, spanner3 is located at location5 and is broken, spanner4 is located at shed and is usable, spanner5 is located at gate and is usable.\n"
    f"Question: Given the initial condition, the following actions are planned to be performed: at location3, alice uses spanner2 to tighten nut2. Is it possible to execute it, True or False?\n"
    f"Answer: \n"
    f"Step 1: we can confirm whether this action is executable or not by checking the initial state.\n" 
    f"Man can 'tighten' a nut with a spanner at location A. This action is executable only if all following preconditions are satisfied: man is currently at location A, the nut man is at location A, man is carrying the spanner, the spanner is useable, the nut is loose. We can see alice is at location3, nut2 is at location3, alice is carrying spanner2, spanner2 is useable, nut2 is loose. So this action is executable.\n"
    f"Step 2: we return the final answer based on the checking result.\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final Answer: True.\n"
    f"---------------\n"
    f"(Example 1)\n"
    f"Current state: A link exists between location1 and location2, location2 and location4 are linked, location4 and location6 are connected, location6 and location7 are linked, alice is at location6, nut3 is located at location6 and is loose, nut4 is at location7 and is not secured, spanner1 is located at location2 and is functional, spanner2 is at location7 and is broken, spanner3 is located at location5 and is usable, spanner4 is at location3 and functional, spanner5 is located at location1 and is usable.\n"
    f"Question: Given the initial condition, the following actions are planned to be performed: at location6, alice walks to location7. Is it possible to execute it, True or False?\n"
    f"Answer: \n"
    f"Step 1: we can confirm whether this action is executable or not by checking the initial state.\n" 
    f"Man can 'walk' from location A to location B. This action is executable only if all following preconditions are satisfied: man is currently at location A, loacation A and B are linked. We can see alice is at location6, location 6 and location7 is linked. So the action is executable.\n"
    f"Step 2: we return the final answer based on the checking result.\n"
    f"Since all preconditions are satisfied, this action is executable.\n"
    f"Final Answer: True.\n"
    f"---------------\n"
)


TWOSHOTCOT_STATE_SPANNER_EXAMPLE = (
    f"(Example 1)\n"
    f"Current state: A link exists between location1 and location2, a link connects location2 and location3, location3 and location4 are linked, bob is currently at location2, location4 is connected to location5, location5 is connected to location6, location6 is connected to location7, location7 is linked to location8, location8 is connected to gate, location9 and location8 are not linked, nut1 is located at gate and is not secured, nut2 is loose at gate, nut3 is loose at gate, nut4 is not secured at gate, nut5 is not secured at gate, spanner1 is usable and located at location3, spanner2 is located at location5 and is usable, spanner3 is located at location6 and functional, spanner4 is located at location7 and is functional, spanner5 is currently at location8 and is usable.\n"
    f"Question: Given the initial condition, the following actions are performed: bob walks from location2 to location3 to reach the current state. In this state, is it True or False that location3 is linked to location2?\n"
    f"Step 1: We first execute the action and get the new state.\n"
    f"bob walks from location2 to location3 to reach the current state. After taking the action, bob is at location3.\n"
    f"Step 2: Then, we compare the state and the question and get the answer.\n"
    f"location3 is linked to location2. So the question is true.\n"
    f"Step 3: Return the answer based on the analysis.\n"
    f"Final Answer: True.\n"
    f"---------------\n"
    f"(Example 2)\n"
    f"Current state: Bob is currently at gate. Bob is carrying spanner2. There is a link between location1 and location2, a link between location2 and location5, a link between location4 and location5, location5 is linked to location6, location6 is linked to location7, location7 and location8 are connected, location8 and gate are linked. Location3 has no direct link to location4. Nut4 is located at gate and is not secured. Spanner2 is functional. Spanner1 is at location5 and usable. Spanner3 is at location6 and usable. Spanner4 is at location7 and functional. Spanner5 is located at gate and is functional. Nut1, nut2, nut3, nut5 are also at gate and all are not secured.\n"
    f"Question: Given the initial condition, the following actions are performed: at gate, bob uses spanner2 to tighten nut4 to reach the current state. In this state, is it True or False that location3 is linked to location4?\n"
    f"Step 1: We first execute the action and get the new state.\n"
    f"at gate, bob uses spanner2 to tighten nut4. After taking the action, spanner2 is not useable, nut4 is tighten.\n"
    f"Step 2: Then, we compare the state and the question and get the answer.\n"
    f"is it True or False that location3 is linked to location4? We can see location3 is linked to location4. So the question is true.\n"
    f"Step 3: Return the answer based on the analysis.\n"
    f"Final Answer: True.\n"
    f"---------------\n"
)