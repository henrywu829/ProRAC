# ProRAC: ProRAC: A Neural-symbolic Method for Reasoning about Actions with LLM-based Progression

## Before you use
1. Enter your API key and you LLM provider's base url in `x_run.py` or `x_run_baseline.py`.
2. All benchmarks are in `X-benchmarks` folder, separated by domains.

## Evaluation
1. Use command line instructions to run the evaluations. See `run.sh` for examples.
2. The results will be saved in the current folder, with `save_name` as prefix of the file name. Each task include two files: `response.jsonl` and `accuracy.jsonl`, the first one includes LLM's response for each data entry, the second one includes the accuracy for the evalution.

## Repository Structure
├── ACPBench-Benchmark/        # ACPBench Benchmark 
├── ARB-Benchmark/             # ActionReasoningBench Benchmark
├── TRAC-Benchmark/            # TRAC Benchmark
├── ACP_Prompt.py              # All prompts used ACPBench
├── ACP_run.py                 # ProRAC evaluation for ACPBench
├── ACP_run_baseline.py        # Baseline evaluation for ACPBench
├── ACP_utils.py               # Utility functions for ACPBench
├── ARB_Prompt.py              # Prompt templates for ARB domain
├── ARB_run.py                 # ProRAC evaluation for ARB
├── ARB_run_baseline.py        # Baseline evaluation for ARB
├── ARB_utils.py               # Utility functions for ARB
├── TRAC_Prompt.py             # Prompt templates for TRAC domain
├── TRAC_run.py                # ProRAC evaluation for TRAC
├── TRAC_run_baseline.py       # Baseline evaluation for TRAC
├── TRAC_utils.py              # Utility functions for TRAC
├── utils.py                   # Shared utility functions
├── run.sh                     # Command line instructions examples 
└── README.md                  # Project documentation

## X_utils.py
Some parameters used in functions
- `save_name`: The prefix of the file name for the results and accuracy
- `model`: LLM used
- `api` and `api_key`: API key 
- `url` and `base_url`: LLM provider's base url
- `domain`: Domain name. This parameter is only used in ACPBench and ActionReasoningBench, not in TRAC
- `task`: Task name
- `states`: A lists with all intermediate states progressed from S0
  