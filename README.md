# ProRAC: ProRAC: A Neural-symbolic Method for Reasoning about Actions with LLM-based Progression

## Before you use
1. Enter your API key and you LLM provider's base url in `x_run.py` or `x_run_baseline.py`.

## Evaluation
1. Use command line instructions to run the evaluations. See `run.sh` for examples.
2. The results will be saved in the current folder, with `save_name` as prefix of the file name. Each task include two files: `response.jsonl` and `accuracy.jsonl`, the first one includes LLM's response for each data entry, the second one includes the accuracy for the evalution.

## Repository Structure
- `X-Benchmark` folders contains all benchmarks, separated by domains.
- `X_Prompt.py` contains all prompts used in the project.
- `X_run.py` is used to evaluate ProRAC on a specific benchmark.
- `X_run_baseline.py` is used to evaluate baselines on a specific benchmark.
- `X_utils.py` contains all utility functions used in the project.
- `utils.py` contains shared utility functions.
- `run.sh` contains command line instructions examples.

## X_utils.py
Some parameters used in functions
- `save_name`: The prefix of the file name for the results and accuracy
- `model`: LLM used
- `api` and `api_key`: API key 
- `url` and `base_url`: LLM provider's base url
- `domain`: Domain name. This parameter is only used in ACPBench and ActionReasoningBench, not in TRAC
- `task`: Task name
- `states`: A lists with all intermediate states progressed from S0
  