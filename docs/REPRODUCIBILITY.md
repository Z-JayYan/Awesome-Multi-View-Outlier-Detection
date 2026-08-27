# Reproducibility Registry

The first public release records conservative, observable artifacts:

- `official_code`: repository explicitly connected to the paper by an author, paper, or project page;
- `official_config`: runnable experiment configs or documented hyperparameters;
- `dataset_instructions`: acquisition and preprocessing steps;
- `pretrained_weights`: downloadable model parameters;
- `environment`: dependency file or environment instructions;
- `license`: an explicit software license in the repository.

Values are `yes`, `no`, `partial`, or `unknown`. `no` means the checked official artifact did not contain the item at audit time; `unknown` means the audit could not establish it. Third-party reimplementations are never labeled official.

## Public-information boundary

This registry does not contain local reproduction gaps, unpublished AUROC values, server results, private audits, advisor discussions, or unpublished method details. Public entries must be re-verified from a paper, proceedings page, DBLP record, author page, or official repository.

## What the registry does not score

The project does not publish a single reproducibility grade. Artifact availability is factual; reproducibility quality also depends on environment age, nondeterminism, undocumented preprocessing, and access to the exact benchmark variant.
