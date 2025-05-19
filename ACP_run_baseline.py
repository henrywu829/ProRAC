import ACP_utils
import argparse
import time
import json
import tqdm
import os



#---------------------------------------------------
#IMPORTANT
#PUT YOUR API KEY AND YOUR LLM PROVIDER'S BASE URL HERE
#NO `v1/chat/completion` REQUIRED
BASE_URL = ""
API_KEY = ""
#---------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description='Run ActionReasoningBench benchmark')

    #Benchmark related args
    parser.add_argument('--domain', type=str, help='Domain of the plan')
    parser.add_argument('--task', type=str, help='Task should be one of Applicability, Progression, Validation')
    parser.add_argument("--file_path", type=str, help="Path to the file containing the data")
    parser.add_argument("--save_name", type=str, help="Name of the file to save the results")
    parser.add_argument("--answer_form", type=str, help="The form of the answer, should be one of bool, mcq")
    parser.add_argument("--is0Shot", action='store_true', help="0shot baseline evaluation")
    parser.add_argument("--is0ShotCoT",action='store_true', help="0shot-CoT baseline evaluation")
    parser.add_argument("--is2ShotCoT",action='store_true', help="2shot-CoT baseline evaluation")

    #LLM related args
    parser.add_argument('--model', type=str, default="gpt-4o", help='LLM model')
    parser.add_argument('--url', type=str, default=BASE_URL, help='API proxy website')
    parser.add_argument('--api', type=str, default=API_KEY, help='API key')

    args = parser.parse_args()
    print(args)
    print("======")

    #Load data
    data = ACP_utils.DataLoader(args.file_path)
    total_samples = len(data)
    correct_prediction = 0
    processed_samples = 0
    answer_mapping = {0:"A", 1:"B", 2:"C", 3:"D", 999:"N/A"}
    mode = "2Shot-CoT" if args.is2ShotCoT else ("0Shot-CoT" if args.is0ShotCoT else "0Shot")


    #Evaluation
    if args.answer_form == "bool":
        for item in tqdm.tqdm(data, desc=f'Processing {args.save_name}-{args.domain}-{args.task}-{args.answer_form}-{mode}-response', unit='data'):
            answer = ACP_utils.BaselineEvaluation(item, args.domain, args.task, mode, args.answer_form, args.save_name, model=args.model, url=args.url, api=args.api)
            label_value = 1 if item["answer"].lower() == "yes" else 0
            if answer == label_value:
                correct_prediction += 1

    elif args.answer_form == "mcq":
        for item in tqdm.tqdm(data, desc=f'Processing {args.save_name}-{args.domain}-{args.task}-{args.answer_form}-{mode}-response', unit='data'):
            answer_choice = ACP_utils.BaselineEvaluation(item, args.domain, args.task, mode, args.answer_form, args.save_name, model=args.model, url=args.url, api=args.api)
            if answer_choice == item["answer"]:
                correct_prediction += 1


    # Read the response file to count processed samples
    response_file = f"{args.save_name}-{args.domain}-{args.task}-{args.answer_form}-{mode}-response.jsonl"
    if os.path.exists(response_file):
        with open(response_file, 'r', encoding='utf-8') as f:
            processed_samples = sum(1 for _ in f)

    skipped_samples = total_samples - processed_samples

    # Calculate accuracy based on processed samples
    accuracy = correct_prediction / processed_samples if processed_samples > 0 else 0
    print(f"Accuracy: {accuracy} (based on {processed_samples} processed samples, {skipped_samples} skipped)")

    accuracy_data = {
        "domain": args.domain,
        "task": args.task,
        "correct_predictions": correct_prediction,
        "processed_samples": processed_samples,
        "total_samples": total_samples,
        "skipped_samples": skipped_samples,
        "accuracy": accuracy
    }

    accuracy_file = f"{args.save_name}-{args.domain}-{args.task}-{args.answer_form}-{mode}-accuracy.jsonl"
    with open(accuracy_file, 'a', encoding='utf-8') as f:
        f.write(json.dumps(accuracy_data, ensure_ascii=False) + '\n')

if __name__ == "__main__":
    main()