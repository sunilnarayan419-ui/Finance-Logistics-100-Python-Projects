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
