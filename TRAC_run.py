import utils
import TRAC_Prompt
import TRAC_utils
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
    parser.add_argument('--task', type=str, help='Task should be one of action_executability, composite, effects, fluent_tracking, numerical_reasoning, state_tracking')
    parser.add_argument("--file_path", type=str, help="Path to the file containing the data")
    parser.add_argument("--save_name", type=str, help="Name of the file to save the results")

    #LLM related args
    parser.add_argument('--model', type=str, default="gpt-4o", help='LLM model')
    parser.add_argument('--url', type=str, default=BASE_URL)
    parser.add_argument('--api', type=str, default=API_KEY, help='API key')

    args = parser.parse_args()
    print(args)

    #Load data
    data = TRAC_utils.DataLoader(args.file_path)
    total_samples = len(data)
    correct_prediction = 0
    processed_samples = 0

    #Evaluation
    for item in tqdm.tqdm(data, desc=f'Processing {args.save_name}-{args.domain}-{args.task}-response', unit='data'):
        try:
            answer = TRAC_utils.Progression(item, args.task, args.save_name, model=args.model, url=args.url, api=args.api)

            # Skip samples where the model response failed
            if answer is None:
                print(f"Skipping sample {item.get('problem_id', 'unknown')} due to failed API request")
                continue

            # Count this as a processed sample
            processed_samples += 1

            # Convert
            label_value = 1 if item["label"].lower() == "true" else 0
            if answer == label_value:
                correct_prediction += 1
        except Exception as e:
            print(f"Error processing sample {item.get('problem_id', 'unknown')}: {str(e)}")
            continue


     # Read the response file to count processed samples
    response_file = f"{args.save_name}-{args.task}-response.jsonl"
    if os.path.exists(response_file):
        with open(response_file, 'r', encoding='utf-8') as f:
            processed_samples = sum(1 for _ in f)

    skipped_samples = total_samples - processed_samples

    # Calculate accuracy based on processed samples
    accuracy = correct_prediction / processed_samples if processed_samples > 0 else 0
    print(f"Accuracy: {accuracy} (based on {processed_samples} processed samples, {skipped_samples} skipped)")

    accuracy_data = {
        "task": args.task,
        "correct_predictions": correct_prediction,
        "processed_samples": processed_samples,
        "total_samples": total_samples,
        "skipped_samples": skipped_samples,
        "accuracy": accuracy
    }

    accuracy_file = f"{args.save_name}-{args.task}-accuracy.jsonl"
    with open(accuracy_file, 'a', encoding='utf-8') as f:
        f.write(json.dumps(accuracy_data, ensure_ascii=False) + '\n')

if __name__ == "__main__":
    main()
