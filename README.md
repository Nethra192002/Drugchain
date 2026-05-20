# DrugChain

A reasoning system that surfaces non-obvious, multi-step drug interaction
risks through the CYP3A4 metabolic pathway.

## What it does

Given a list of medications, DrugChain flags pairs where one drug inhibits
the CYP3A4 enzyme while another relies on that same enzyme to be cleared from
the body. These interactions are dangerous because the inhibitor slows
clearance of the substrate, allowing it to build toward toxic levels — a risk
that pairwise lookups across separate prescribers often miss.

Each flagged chain is ranked by severity, derived from the inhibitor's potency
and the substrate's sensitivity.

## What it does not do

This is a research and learning project. It surfaces risks for a human to
review. It does not provide medical advice, does not replace a clinician or
pharmacist, and should not be used to make treatment decisions. Drug
classifications are drawn from public FDA interaction data and are limited to
a small curated set during early development.

## Project status

Stage 1 of a planned multi-stage build: the core graph and detection logic,
with a tested two-step chain detector.

## Setup
```
conda create -n drugchain python=3.11
conda activate drugchain
pip install -r requirements.txt
```

## Running
python main.py

## Tests
pytest

## Structure

- `data/` — drug facts (the knowledge the graph is built from)
- `src/graph.py` — builds the CYP3A4 interaction graph
- `src/detector.py` — detects and ranks interaction chains
- `tests/` — behavioral tests for the detector
- `main.py` — entry point that runs the detector on a sample list