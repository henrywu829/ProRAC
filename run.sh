#Evaluating TRAC
##BASELINE: is2ShotCoT=2ShotCoT, is0ShotCoT=0ShotCoT, is0Shot=0Shot
python TRAC_run_baseline.py --task 'Projection' --file_path './TRAC-Benchmark/projection/projection-blocksworld-5-3k.jsonl' --is2ShotCoT --save_name '0314-4o' --model 'gpt-4o' 
python TRAC_run_baseline.py --task 'Executability' --file_path './TRAC-Benchmark/legality/legality-blocksworld-5-3k.jsonl' --is2ShotCoT --save_name '0314-4o' --model 'gpt-4o' 
python TRAC_run_baseline.py --task 'PlanVerification' --file_path './TRAC-Benchmark/planning/planning-blocksworld-5-3k.jsonl' --is2ShotCoT --save_name '0314-4o' --model 'gpt-4o' 
##ProRAC
python TRAC_run_baseline.py --task 'Projection' --file_path './TRAC-Benchmark/projection/projection-blocksworld-5-3k.jsonl' --is2ShotCoT --save_name '0314-4o' --model 'gpt-4o' 
python TRAC_run_baseline.py --task 'Executability' --file_path './TRAC-Benchmark/legality/legality-blocksworld-5-3k.jsonl' --is2ShotCoT --save_name '0314-4o' --model 'gpt-4o' 
python TRAC_run_baseline.py --task 'PlanVerification' --file_path './TRAC-Benchmark/planning/planning-blocksworld-5-3k.jsonl' --is2ShotCoT --save_name '0314-4o' --model 'gpt-4o' 

#Evaluating ActionReasoningBench
##BASELINE: is2ShotCoT=2ShotCoT, is0ShotCoT=0ShotCoT, is0Shot=0Shot
python ARB_run_baseline.py --domain 'depots' --task 'action_executability' --file_path './ARB-Benchmark/depots/depots-action_executability-true_false_answer.jsonl' --is0Shot --save_name '0317'
python ARB_run_baseline.py --domain 'depots' --task 'effects' --file_path './ARB-Benchmark/depots/depots-effects-true_false_answer.jsonl' --is0Shot --save_name '0317'
python ARB_run_baseline.py --domain 'depots' --task 'fluent_tracking' --file_path './ARB-Benchmark/depots/depots-fluent_tracking-true_false_answer.jsonl' --is0Shot --save_name '0317'
python ARB_run_baseline.py --domain 'depots' --task 'state_tracking' --file_path './ARB-Benchmark/depots/depots-state_tracking-true_false_answer.jsonl' --is0Shot --save_name '0317'
##ProRAC
python ARB_run.py --domain 'depots' --task 'action_executability' --answer_type 'true_false_answer' --file_path './ARB-Benchmark/depots/depots-action_executability-true_false_answer.jsonl' --save_name '0226'
python ARB_run.py --domain 'depots' --task 'effects' --answer_type 'true_false_answer' --file_path './ARB-Benchmark/depots/depots-effects-true_false_answer.jsonl' --save_name '0226'
python ARB_run.py --domain 'depots' --task 'fluent_tracking' --answer_type 'true_false_answer' --file_path './ARB-Benchmark/depots/depots-fluent_tracking-true_false_answer.jsonl' --save_name '0228'
python ARB_run.py --domain 'depots' --task 'state_tracking' --answer_type 'true_false_answer' --file_path './ARB-Benchmark/depots/depots-state_tracking-true_false_answer.jsonl' --save_name '0226'

#Evaluating ACPBench
##BASELINE: is2ShotCoT=2ShotCoT, is0ShotCoT=0ShotCoT, is0Shot=0Shot
python ACP_run_baseline.py --domain 'logistics' --task 'Applicability' --answer_form 'bool' --is2ShotCoT --file_path './ACPBench-Benchmark/logistics/logistics_app_bool.jsonl' --save_name '0511-4o' --model 'gpt-4o' 
python ACP_run_baseline.py --domain 'logistics' --task 'Applicability' --answer_form 'mcq' --is2ShotCoT --file_path './ACPBench-Benchmark/logistics/logistics_app_mcq.jsonl' --save_name '0511-4o' --model 'gpt-4o' 
python ACP_run_baseline.py --domain 'logistics' --task 'Progression' --answer_form 'bool' --is2ShotCoT --file_path './ACPBench-Benchmark/logistics/logistics_prog_bool.jsonl' --save_name '0511-4o' --model 'gpt-4o' 
python ACP_run_baseline.py --domain 'logistics' --task 'Progression' --answer_form 'mcq' --is2ShotCoT --file_path './ACPBench-Benchmark/logistics/logistics_prog_mcq.jsonl' --save_name '0511-4o' --model 'gpt-4o' 
python ACP_run_baseline.py --domain 'logistics' --task 'Validation' --answer_form 'bool' --is2ShotCoT --file_path './ACPBench-Benchmark/logistics/logistics_val_bool.jsonl' --save_name '0511-4o' --model 'gpt-4o' 
python ACP_run_baseline.py --domain 'logistics' --task 'Validation' --answer_form 'mcq' --is2ShotCoT --file_path './ACPBench-Benchmark/logistics/logistics_val_mcq.jsonl' --save_name '0511-4o' --model 'gpt-4o' 
##ProRAC
python ACP_run.py --domain 'ferry' --task 'Applicability' --answer_form 'bool' --file_path './ACPBench-Benchmark/ferry/ferry_app_bool.jsonl' --save_name '0427-4o' --model 'gpt-4o' 
python ACP_run.py --domain 'ferry' --task 'Applicability' --answer_form 'mcq' --file_path './ACPBench-Benchmark/ferry/ferry_app_mcq.jsonl' --save_name '0427-4o' --model 'gpt-4o' 
python ACP_run.py --domain 'ferry' --task 'Progression' --answer_form 'bool' --file_path './ACPBench-Benchmark/ferry/ferry_prog_bool.jsonl' --save_name '0501-4o' --model 'gpt-4o' 
python ACP_run.py --domain 'ferry' --task 'Progression' --answer_form 'mcq' --file_path './ACPBench-Benchmark/ferry/ferry_prog_mcq.jsonl' --save_name '0501-4o' --model 'gpt-4o' 
python ACP_run.py --domain 'ferry' --task 'Validation' --answer_form 'bool' --file_path './ACPBench-Benchmark/ferry/ferry_val_bool.jsonl' --save_name '0501-4o' --model 'gpt-4o' 
python ACP_run.py --domain 'ferry' --task 'Validation' --answer_form 'mcq' --file_path './ACPBench-Benchmark/ferry/ferry_val_mcq.jsonl' --save_name '0508-4o' --model 'gpt-4o' 
