import utils
import ARB_utils
import argparse
import tqdm
import json
import os

#---------------------------------------------------
#IMPORTANT
#Put your api key and your LLM provider's base url here, no need to put `v1/chat/completion`
BASE_URL = ""
API_KEY = ""
#---------------------------------------------------



def main():
    parser = argparse.ArgumentParser(description='Run ActionReasoningBench benchmark')

    #Benchmark related args
    parser.add_argument('--domain', type=str, help='Domain of the plan')
    parser.add_argument('--task', type=str, help='Task should be one of action_executability, composite, effects, fluent_tracking, numerical_reasoning, state_tracking')
    parser.add_argument("--file_path", type=str, help="Path of the file containing the data")
    parser.add_argument("--save_name", type=str, help="Name of the file to save the results")
    parser.add_argument("--is0Shot", action='store_true', help="0shot baseline evaluation")
    parser.add_argument("--is0ShotCoT",action='store_true', help="0shot-CoT baseline evaluation")
    parser.add_argument("--is2ShotCoT",action='store_true', help="2shot-CoT baseline evaluation")


    #LLM related args
    parser.add_argument('--model', type=str, default="gpt-4o", help='LLM model')
    parser.add_argument('--url', type=str, default=BASE_URL, help='API proxy website')
    parser.add_argument('--api', type=str, default=API_KEY, help='API key')

    args = parser.parse_args()
    correct_prediction = 0
    print(args)
    print("======")

    #Load data
    data = ARB_utils.DataLoader(args.file_path)
    total_samples = len(data)
    correct_prediction = 0
    mode = "2Shot-CoT" if args.is2ShotCoT else ("0Shot-CoT" if args.is0ShotCoT else "0Shot")

    #Evaluation
    valid_samples = 0  # Count only samples that were successfully processed

    if mode=="0Shot":
        for item in tqdm.tqdm(data, desc=f'Processing {args.save_name}-{args.domain}-{args.task}-0Shot-response', unit='data'):
            llm_label = ARB_utils.BaselineEvaluation(item, args.domain, args.save_name, "0Shot", args.model, base_url=args.url, api_key=args.api, task=args.task)

            # Skip failed requests when calculating accuracy
            if llm_label is None:
                print(f"Skipping sample {item.get('question_id', 'unknown')} due to API failure")
                continue

            valid_samples += 1
            label_value = 1 if item["answer"].lower() == "true" else 0
            if llm_label == label_value:
                correct_prediction += 1

    elif mode=="0Shot-CoT":
        for item in tqdm.tqdm(data, desc=f'Processing {args.save_name}-{args.domain}-{args.task}-0CoT-response', unit='data'):
            llm_label = ARB_utils.BaselineEvaluation(item, args.domain, args.save_name, "0Shot-CoT", args.model, base_url=args.url, api_key=args.api, task=args.task)

            # Skip failed requests when calculating accuracy
            if llm_label is None:
                print(f"Skipping sample {item.get('question_id', 'unknown')} due to API failure")
                continue

            valid_samples += 1
            label_value = 1 if item["answer"].lower() == "true" else 0
            if llm_label == label_value:
                correct_prediction += 1
    else:
        for item in tqdm.tqdm(data, desc=f'Processing {args.save_name}-{args.domain}-{args.task}-2CoT-response', unit='data'):
            llm_label = ARB_utils.BaselineEvaluation(item, args.domain, args.save_name, "2Shot-CoT", args.model, base_url=args.url, api_key=args.api, task=args.task)

            # Skip failed requests when calculating accuracy
            if llm_label is None:
                print(f"Skipping sample {item.get('question_id', 'unknown')} due to API failure")
                continue

            valid_samples += 1
            label_value = 1 if item["answer"].lower() == "true" else 0
            if llm_label == label_value:
                correct_prediction += 1

    #Log accuracy
    accuracy = correct_prediction / valid_samples if valid_samples > 0 else 0
    print(f"Accuracy: {accuracy} ({correct_prediction}/{valid_samples} correct)")
    print(f"Skipped samples: {total_samples - valid_samples} out of {total_samples} total")

    accuracy_data = {
        "domain": args.domain,
        "task": args.task,
        "correct_predictions": correct_prediction,
        "valid_samples": valid_samples,
        "total_samples": total_samples,
        "skipped_samples": total_samples - valid_samples,
        "accuracy": accuracy
    }

    accuracy_file = f"{args.save_name}-{args.domain}-{args.task}-{mode}-accuracy.jsonl"
   
    with open(accuracy_file, 'a', encoding='utf-8') as f:
        f.write(json.dumps(accuracy_data, ensure_ascii=False) + '\n')


if __name__ == "__main__":
    main()