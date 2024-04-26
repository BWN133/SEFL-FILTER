# SELF-FILTER Architecture for Enhanced Solution Generation and Filtering

SELF-FILTER is a two-stage architecture designed to generate and filter solutions for mathematical word problems (MWPs) by leveraging multiple instances of language models. This project uses LangChain to orchestrate the process, improving the likelihood of obtaining correct solutions by generating diverse candidate solutions and filtering them effectively.

## Overview

The architecture consists of two main stages:
1. **Candidate Generation Stage**: Utilizes multiple agents to generate a variety of solutions, aiming to cover a wide range of possible answers.
2. **Filtering Stage**: Employs a novel "Arena match-like" algorithm to filter out incorrect solutions and select the most plausible one.

### Candidate Generation Stage

In this stage, `n` agents are tasked with solving a proposed MWP. Each agent is prompted with three distinct Few-shot examples and the question itself. This diversity in prompting is intended to maximize the uniqueness of each generated solution. After the agents complete their tasks, `n` solutions are generated, each comprising a reasoning field and an answer field. These solutions are then enhanced by another set of `n` agents, each instructed to critique and propose alternatives to the initial solutions, resulting in `2n` solutions ready for filtering.

### Filtering Stage

The filtering stage introduces the Pick Correct Agent (PCA), a specialized agent that compares two candidate solutions at a time, selecting the more likely correct answer. This binary comparison helps maintain high accuracy in solution selection. Solutions with repetitive answers are excluded, and unique candidate solutions undergo PCA in an "Arena Match" setup, where the winning solution from each match proceeds to the next round. This process continues until only one solution remains, which is deemed the final correct answer.

## Project Structure

- `src/`: Source files for the SELF-FILTER architecture.
- `data/`: Directory for storing Few-shot prompts and other data inputs.
- `scripts/`: Utility scripts for setting up and running the agents.
- `results/`: Output directory for generated solutions and final results.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/self-filter.git
2. Navigate to the project directory:
   ```bash
   cd self-filter
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
## Usage

To run the package, input the target question in main.py and
```bash
python main.py
```

# References
Cobbe, K., Kosaraju, V., Klimov, O., Schulman, J., Hilton,
J., & Hausknecht, M. (2021). Training verifiers to solve
math word problems. arXiv preprint arXiv:2110.14168
