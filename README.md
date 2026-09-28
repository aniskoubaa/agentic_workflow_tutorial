# mai580-agent

Starter repository for the MAI 580 course project. You grow this one project through 16 stages.
The full instructions are in the tutorial: open `tutorial/index.html` in your browser.

## Layout

```
mai580-agent/
├── app/
│   ├── llm.py         # the model, created once
│   ├── state.py       # ONE state class that grows stage by stage
│   ├── nodes.py       # node functions
│   ├── graph.py       # build_graph(): all the wiring lives here (you write it)
│   ├── tools.py       # tools (Stage 4+)
│   ├── rag.py         # retrieval (Stage 8+)
│   ├── planning.py    # planner and executor (Stage 9+)
│   ├── monitor.py     # tracing and run logs (Stage 12+)
│   ├── guards.py      # security guards (Stage 14+)
│   └── reflection.py  # output evaluator and retry (Stage 15+)
├── data/              # catalogue.json, policies/, your use-case data
├── eval/              # test set, attack set, results (Stage 13+)
├── improve/           # improvement proposals and log.jsonl (Stage 16)
├── notes/             # progress notes and experiment tables, one note per milestone
├── tests/             # pytest, one file per stage (test_stage01.py, ...)
├── tutorial/          # index.html: the stage-by-stage tutorial
├── run.py             # command-line chat loop
├── .env.example       # copy to .env and add your key
└── requirements.txt
```

## Start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then add your OPENAI_API_KEY
pytest                      # fails until you write build_graph() in app/graph.py
python run.py
```

After each stage: `git tag stage-NN && git push --tags`.
