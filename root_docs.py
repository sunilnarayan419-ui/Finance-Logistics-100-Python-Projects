"""
root_docs.py — content generators for the repository's root-level files.
Kept separate from file_generator.py so the writer logic and the prose
don't get tangled together.
"""

from textwrap import dedent
from projects_data import Project, PHASE_FOLDERS


def _project_table(projects: list[Project]) -> str:
    lines = ["| Project | Domain | Difficulty | Main Technology |",
             "| ------- | ------ | ---------- | --------------- |"]
    for p in projects:
        tech = p.technologies[0] if p.technologies else "Python (stdlib)"
        lines.append(f"| {p.number:03d}. {p.title} | {p.domain} | {p.difficulty} | {tech} |")
    return "\n".join(lines)


def _phase_map(projects: list[Project]) -> str:
    lines = []
    for phase_num, folder in PHASE_FOLDERS.items():
        members = [p for p in projects if p.phase == phase_num]
        lo, hi = members[0].number, members[-1].number
        lines.append(f"- **Phase {phase_num}** (`{folder}/`) — projects {lo:03d}–{hi:03d}")
    return "\n".join(lines)


def root_readme(projects: list[Project]) -> str:
    return dedent(f"""\
        # Finance-Logistics-100-Python-Projects

        100 progressively difficult Python projects in **finance, business
        analytics, logistics, supply-chain, operations research, and network
        engineering** — built in the spirit of `Mini-Bio-Python-Projects`,
        retargeted at computational business engineering.

        The goal is not to "learn Python." The goal is to learn how to use
        Python to **understand, diagnose, model, optimize, and engineer real
        business systems** — moving from a single script to a modular
        application, to a data pipeline, to an optimization system, to an
        intelligent decision-support system.

        ## Learning Philosophy

        Each project answers a real business question. Complexity is always
        isolated inside modules — no 1,000-line `main.py`, no artificially
        inflated beginner projects. Architecture scales with difficulty:
        Phase 1 projects are `README.md` + `main.py`; Phase 8 projects have
        full `config/ data/ src/ tests/ notebooks/ models/ outputs/` trees.

        ## Project Map

        {_phase_map(projects)}

        ## Phase Structure

        | Phase | Focus | Projects |
        |---|---|---|
        | 1 | Python Business Foundations | 001–015 |
        | 2 | Business Logic & Decision Systems | 016–030 |
        | 3 | Data Structures & Business Systems | 031–045 |
        | 4 | File Handling & Real Business Data | 046–060 |
        | 5 | NumPy, Simulation & Quantitative Computing | 061–075 |
        | 6 | Pandas & Business Intelligence | 076–085 |
        | 7 | Visualization, Graphs & Network Analysis | 086–092 |
        | 8 | Machine Learning, Optimization & Integrated Systems | 093–100 |

        ## Technology Progression

        Python → data structures → file handling → NumPy → Pandas →
        Matplotlib/Plotly → SciPy → NetworkX → scikit-learn → OR-Tools →
        integrated systems. See `roadmap.md` for the full skill map.

        ## Domain Roadmaps

        - **Finance:** cash flow, revenue, expenses, margins, pricing, loans,
          investments, risk, portfolio analysis, working capital,
          profitability, financial forecasting.
        - **Logistics:** inventory, warehouses, procurement, suppliers,
          transportation, routing, distributors, retailers, delivery,
          lead time, capacity, stockouts, demand.
        - **Operations Research:** linear/integer programming, transportation
          optimization, assignment, facility location, routing, resource
          allocation, scheduling, network flow.
        - **Network Analysis:** graph modeling, shortest paths, bottlenecks,
          centrality, dependency, resilience, flow networks.
        - **Machine Learning:** demand forecasting, delay prediction,
          supplier risk, inventory prediction, payment risk, cost
          prediction, anomaly detection, clustering.

        ## Installation

        ```bash
        git clone <this-repo-url>
        cd Finance-Logistics-100-Python-Projects
        python -m venv .venv && source .venv/bin/activate   # or .venv\\Scripts\\activate on Windows
        pip install -r requirements.txt   # root dev tooling (pytest, etc.)
        ```

        Each project also has its own `requirements.txt` with only the
        dependencies it actually needs — install those inside the project
        folder before running it.

        ## Usage

        ```bash
        cd phase1_python_business_foundations/project_001_personal_cash_flow_analyzer
        pip install -r requirements.txt
        python main.py
        ```

        ## Generating / Regenerating the Repository

        The full folder structure is produced by `file_generator.py`, driven
        by the metadata in `projects_data.py`. It is idempotent and will
        never overwrite an existing file unless you pass `--force`:

        ```bash
        python file_generator.py --root .
        python file_generator.py --root . --only 45     # regenerate one project
        python file_generator.py --root . --dry-run       # preview, write nothing
        ```

        ## Contribution Guidelines

        See `CONTRIBUTING.md`.

        ## Project Difficulty Levels

        - **Beginner** — 001–030
        - **Intermediate** — 031–060
        - **Advanced** — 061–085
        - **Professional** — 086–100

        ## Full Project Index

        {_project_table(projects)}
        """)


def roadmap_md(projects: list[Project]) -> str:
    def rng(lo, hi):
        return f"{lo:03d}–{hi:03d}"

    return dedent(f"""\
        # Roadmap

        ```text
        Python
         ↓
        Business Logic
         ↓
        Data Structures
         ↓
        Data Handling
         ↓
        NumPy
         ↓
        Pandas
         ↓
        Visualization
         ↓
        Network Analysis
         ↓
        Optimization
         ↓
        Machine Learning
         ↓
        Integrated Finance + Logistics Systems
        ```

        | Skill | Projects |
        |---|---|
        | Python fundamentals | {rng(1, 15)} |
        | Business logic / decision rules | {rng(16, 30)} |
        | Data structures & business systems | {rng(31, 45)} |
        | File handling & real business data | {rng(46, 60)} |
        | NumPy & numerical simulation | {rng(61, 75)} |
        | Pandas & business intelligence | {rng(76, 85)} |
        | Visualization & network analysis | {rng(86, 92)} |
        | Machine learning, optimization & integrated systems | {rng(93, 100)} |

        ## Difficulty progression

        - Beginner: {rng(1, 30)}
        - Intermediate: {rng(31, 60)}
        - Advanced: {rng(61, 85)}
        - Professional: {rng(86, 100)}

        Difficulty is not artificially forced — a project that naturally
        crosses categories (e.g. an Intermediate project that needs a
        richer test suite) is allowed to.
        """)


def contributing_md() -> str:
    return dedent("""\
        # Contributing

        1. Fork the repository and create a feature branch.
        2. Pick a project directory (or propose a new one via issue first).
        3. Keep changes scoped to a single project unless you're editing
           root-level docs or `file_generator.py` / `projects_data.py`.
        4. Follow the existing structure — don't add files a project's
           difficulty tier doesn't call for (see `README.md` → Project
           Difficulty Levels, and section 5 of the original architecture
           spec: "complexity must be isolated inside modules").
        5. Use `snake_case` for Python files, lowercase project folder
           names, and keep `main.py` a thin entry point — business logic
           belongs in `src/`.
        6. Add or update tests in `tests/` alongside any logic change.
        7. Run `pytest` inside the project folder before opening a PR.
        8. No secrets, credentials, or API keys in commits. No large
           datasets — put real dataset sources in the project's README
           instead of committing the file.
        9. Open a PR with a clear description of which project(s) changed
           and why.
        """)


def gitignore() -> str:
    return dedent("""\
        __pycache__/
        *.pyc
        *.pyo
        .venv/
        venv/
        env/
        .env
        .pytest_cache/
        .mypy_cache/
        .ipynb_checkpoints/
        *.egg-info/
        dist/
        build/
        .DS_Store
        *.log

        # generated artifacts — keep the repo light
        outputs/reports/*
        outputs/charts/*
        outputs/results/*
        !outputs/**/.gitkeep
        data/raw/*
        data/processed/*
        !data/**/.gitkeep
        models/*
        !models/.gitkeep
        """)


def pyproject_toml() -> str:
    return dedent("""\
        [build-system]
        requires = ["setuptools>=68.0"]
        build-backend = "setuptools.build_meta"

        [project]
        name = "finance-logistics-100-python-projects"
        version = "0.1.0"
        description = "100 progressive Python projects in finance, logistics, operations research, and network engineering."
        readme = "README.md"
        requires-python = ">=3.10"
        license = { text = "MIT" }

        [tool.pytest.ini_options]
        testpaths = ["."]
        python_files = ["test_*.py"]
        """)


def setup_py() -> str:
    return dedent('''\
        """
        setup.py — kept for tooling that doesn't yet read pyproject.toml.
        The canonical build config is pyproject.toml.
        """
        from setuptools import setup

        setup()
        ''')


def root_requirements() -> str:
    # Root-level dev tooling only — per-project requirements.txt files
    # hold the actual runtime dependencies for each project.
    return dedent("""\
        pytest>=7.4
        """)


def license_mit() -> str:
    return dedent("""\
        MIT License

        Copyright (c) 2026 <repository owner>

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.
        """)
