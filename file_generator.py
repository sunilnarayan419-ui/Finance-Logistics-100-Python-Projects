#!/usr/bin/env python3
"""
file_generator.py

Generates the complete repository architecture for:

    Finance-Logistics-100-Python-Projects

Design goals (see README.md / roadmap.md for the full spec):
  - Idempotent: safe to run multiple times.
  - Non-destructive: never overwrites an existing file unless --force is passed.
  - Data-driven: all 100 projects are described in projects_data.py.
    Change a project's tech stack/domain there; this script derives layout.
  - Scales structure to difficulty: Phase 1 projects get a two-file skeleton,
    Phase 8 projects get the full config/src/tests/notebooks/models/outputs tree.

Usage:
    python file_generator.py                 # generate everything under ./out
    python file_generator.py --root .        # generate in place
    python file_generator.py --only 45        # generate a single project
    python file_generator.py --force          # overwrite existing files
    python file_generator.py --dry-run        # print the plan, write nothing
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from textwrap import dedent

from projects_data import Project, PHASE_FOLDERS, load_projects


# --------------------------------------------------------------------------
# Layout planning: for a given project, decide which folders/files it needs.
# This is the one place that encodes the "architecture scales with
# complexity" rule (spec section 5 / 17 / 23).
# --------------------------------------------------------------------------

def modules_for(p: Project) -> list[str]:
    """Return the src/ module filenames appropriate for this project's
    phase and domain. Only modules that are actually useful are created —
    no 15-file skeletons for a 20-line beginner script."""

    if p.phase == 1:
        return []  # main.py only
    if p.phase == 2:
        return ["calculations.py"]
    if p.phase == 3:
        return ["models.py", "operations.py"]
    if p.phase == 4:
        return ["data_loader.py", "preprocessing.py", "analysis.py"]
    if p.phase == 5:
        mods = ["simulation.py", "calculations.py"]
        if "matplotlib" in p.technologies:
            mods.append("visualization.py")
        return mods
    if p.phase == 6:
        return ["data_loader.py", "analytics.py", "visualization.py", "reporting.py"]
    if p.phase == 7:
        if p.domain == "Network Science":
            return ["graph_builder.py", "network_analysis.py", "visualization.py"]
        return ["data_loader.py", "visualization.py", "dashboard.py"]
    if p.phase == 8:
        if p.domain == "Operations Research":
            return ["data_loader.py", "graph_builder.py", "optimization.py",
                    "routing.py", "visualization.py"]
        if p.number == 100:
            # Integrated system — package-style src/ (sub-packages, not flat modules)
            return ["data", "finance", "demand", "inventory", "warehouse",
                    "transportation", "network", "optimization",
                    "machine_learning", "simulation", "economics", "reporting"]
        # standard ML projects (93-98)
        return ["data_loader.py", "preprocessing.py", "features.py",
                "model.py", "evaluation.py", "prediction.py"]
    return []


def tests_for(p: Project) -> list[str]:
    if p.difficulty == "Beginner":
        return ["test_main.py"]
    if p.difficulty == "Intermediate":
        return ["test_calculations.py", "test_processing.py", "test_validation.py"]
    if p.difficulty == "Advanced":
        if p.phase == 7:
            return ["test_network.py", "test_visualization.py"]
        if p.phase == 6:
            return ["test_data_pipeline.py", "test_analytics.py", "test_integration.py"]
        return ["test_simulation.py", "test_calculations.py", "test_integration.py"]
    # Professional
    tests = ["test_data_pipeline.py"]
    if p.domain == "Machine Learning":
        tests.append("test_model.py")
    if p.domain == "Operations Research":
        tests.append("test_optimizer.py")
    if p.domain == "Network Science" or p.number in (99, 100):
        tests.append("test_network.py")
    tests.append("test_integration.py")
    return tests


def needs_outputs(p: Project) -> bool:
    # Any project that analyzes, reports, forecasts, or dashboards something
    return p.phase >= 4


def requirements_for(p: Project) -> list[str]:
    reqs = list(p.technologies)
    if p.difficulty in ("Advanced", "Professional"):
        reqs.append("pytest")
    elif p.phase >= 3:
        reqs.append("pytest")
    # de-dupe, keep order
    seen = set()
    out = []
    for r in reqs:
        if r not in seen:
            seen.add(r)
            out.append(r)
    return out


# --------------------------------------------------------------------------
# File content templates. These are intentionally skeletons/scaffolding —
# not full implementations (see repo spec section 25: architecture first,
# implementation on request).
# --------------------------------------------------------------------------

def readme_template(p: Project) -> str:
    advanced_extra = ""
    if p.difficulty in ("Advanced", "Professional"):
        advanced_extra = dedent("""
            ## Mathematical / Optimization Model

            _TODO: document the formulas, objective function, and/or model used._

            ## Assumptions

            _TODO_

            ## Constraints

            _TODO_

            ## Evaluation Metrics

            _TODO_

            ## Failure Scenarios

            _TODO_

            ## Economic Interpretation

            _TODO_
            """)

    return dedent(f"""\
        # {p.number:03d}. {p.title}

        **Phase {p.phase} — {PHASE_FOLDERS[p.phase].replace('_', ' ').title()}**
        **Domain:** {p.domain}  **Difficulty:** {p.difficulty}

        ## Business Problem

        _TODO: describe the real business problem this project addresses._

        ## Objective

        _TODO_

        ## Real-World Use Case

        _TODO_

        ## Concepts Practiced

        _TODO: list the Python / data / business concepts this project teaches._

        ## Technologies

        {', '.join(p.technologies) if p.technologies else 'Python standard library only'}

        ## Project Architecture

        See the folder tree in this directory. Business logic lives in `src/`;
        `main.py` is the entry point only.

        ## Input

        _TODO_

        ## Output

        _TODO_

        ## How to Run

        ```bash
        pip install -r requirements.txt
        python main.py
        ```

        ## Expected Result

        _TODO_

        ## Possible Improvements

        _TODO_

        ## Scaling the Project

        _TODO_

        ## Business Questions

        _TODO: 2-3 questions this project should let the learner answer._
        {advanced_extra}""")


def main_py_template(p: Project) -> str:
    if not modules_for(p):
        return dedent(f'''\
            """
            main.py — {p.title}

            Entry point for project {p.number:03d}. Keep business logic here minimal;
            once this file grows, split logic into src/ modules (see other phases
            for the pattern).
            """


            def main() -> None:
                # TODO: implement {p.title.lower()}
                raise NotImplementedError("{p.title} not yet implemented")


            if __name__ == "__main__":
                main()
            ''')
    return dedent(f'''\
        """
        main.py — {p.title}

        Thin entry point. All real logic lives in src/ — this file should only
        wire modules together, not contain business logic itself.
        """

        # from src import ...  # TODO: import the modules this project needs


        def main() -> None:
            # TODO: orchestrate {p.title.lower()} using the src/ modules
            raise NotImplementedError("{p.title} not yet implemented")


        if __name__ == "__main__":
            main()
        ''')


def module_stub(module_name: str, project_title: str) -> str:
    purpose = module_name.replace(".py", "").replace("_", " ")
    return dedent(f'''\
        """
        {module_name} — {purpose} logic for "{project_title}".
        """


        # TODO: implement {purpose}
        ''')


def test_stub(test_name: str, project_title: str) -> str:
    target = test_name.replace("test_", "").replace(".py", "")
    return dedent(f'''\
        """
        {test_name} — tests for the {target.replace("_", " ")} of "{project_title}".
        """

        import pytest


        def test_placeholder():
            """TODO: replace with real assertions once {target.replace("_", " ")} is implemented."""
            assert True
        ''')


def requirements_txt(reqs: list[str]) -> str:
    return "\n".join(reqs) + ("\n" if reqs else "")


def config_yaml_template(p: Project) -> str:
    return dedent(f"""\
        # config/settings.yaml — {p.title}
        project:
          number: {p.number}
          name: "{p.title}"

        # TODO: add tunable parameters (paths, thresholds, model params, etc.)
        paths:
          raw_data: "data/raw"
          processed_data: "data/processed"
          outputs: "outputs"
        """)


# --------------------------------------------------------------------------
# Filesystem writer
# --------------------------------------------------------------------------

class Writer:
    def __init__(self, force: bool, dry_run: bool):
        self.force = force
        self.dry_run = dry_run
        self.created = 0
        self.skipped = 0

    def write(self, path: Path, content: str) -> None:
        if path.exists() and not self.force:
            self.skipped += 1
            return
        if self.dry_run:
            print(f"WOULD WRITE  {path}")
            return
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        self.created += 1

    def touch_dir(self, path: Path) -> None:
        if self.dry_run:
            print(f"WOULD MKDIR  {path}/")
            return
        path.mkdir(parents=True, exist_ok=True)
        gitkeep = path / ".gitkeep"
        if not any(path.iterdir()):
            gitkeep.write_text("", encoding="utf-8")


def build_project(root: Path, p: Project, w: Writer) -> None:
    phase_dir = root / PHASE_FOLDERS[p.phase]
    proj_dir = phase_dir / p.slug

    w.write(proj_dir / "README.md", readme_template(p))
    w.write(proj_dir / "main.py", main_py_template(p))
    w.write(proj_dir / "requirements.txt", requirements_txt(requirements_for(p)))

    mods = modules_for(p)
    if mods:
        if p.number == 100:
            # sub-package style
            w.write(proj_dir / "src" / "__init__.py", "")
            for sub in mods:
                w.write(proj_dir / "src" / sub / "__init__.py", "")
        else:
            w.write(proj_dir / "src" / "__init__.py", "")
            for m in mods:
                w.write(proj_dir / "src" / m, module_stub(m, p.title))

    for t in tests_for(p):
        w.write(proj_dir / "tests" / t, test_stub(t, p.title))

    if p.needs_data:
        for sub in ("raw", "processed", "sample"):
            w.touch_dir(proj_dir / "data" / sub)

    if needs_outputs(p):
        subs = ("reports", "charts", "results") if p.phase >= 6 else ("reports", "results")
        for sub in subs:
            w.touch_dir(proj_dir / "outputs" / sub)

    if p.needs_notebook:
        w.write(
            proj_dir / "notebooks" / "exploration.ipynb",
            '{\n "cells": [],\n "metadata": {},\n "nbformat": 4,\n "nbformat_minor": 5\n}\n',
        )

    if p.needs_models:
        w.touch_dir(proj_dir / "models")

    if p.needs_config:
        w.write(proj_dir / "config" / "settings.yaml", config_yaml_template(p))


def build_root_files(root: Path, projects: list[Project], w: Writer) -> None:
    from root_docs import (
        root_readme, roadmap_md, contributing_md, gitignore,
        pyproject_toml, setup_py, root_requirements, license_mit,
    )

    w.write(root / "README.md", root_readme(projects))
    w.write(root / "roadmap.md", roadmap_md(projects))
    w.write(root / "CONTRIBUTING.md", contributing_md())
    w.write(root / ".gitignore", gitignore())
    w.write(root / "pyproject.toml", pyproject_toml())
    w.write(root / "setup.py", setup_py())
    w.write(root / "requirements.txt", root_requirements())
    w.write(root / "LICENSE", license_mit())


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default="./out", help="Repository root to generate into")
    ap.add_argument("--only", type=int, default=None, help="Generate only this project number")
    ap.add_argument("--force", action="store_true", help="Overwrite existing files")
    ap.add_argument("--dry-run", action="store_true", help="Print the plan without writing")
    args = ap.parse_args()

    root = Path(args.root)
    projects = load_projects()
    w = Writer(force=args.force, dry_run=args.dry_run)

    if args.only:
        projects = [p for p in projects if p.number == args.only]
        if not projects:
            raise SystemExit(f"No project numbered {args.only}")
    else:
        build_root_files(root, load_projects(), w)
        for phase_dir in PHASE_FOLDERS.values():
            w.touch_dir(root / phase_dir)

    for p in projects:
        build_project(root, p, w)

    print(f"Done. {w.created} files/dirs written, {w.skipped} skipped "
          f"(already existed — use --force to overwrite).")


if __name__ == "__main__":
    main()
