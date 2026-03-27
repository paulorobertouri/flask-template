# Customizing the Flask Template

This template is designed for easy renaming and customization. Follow these steps to adapt it to your project:

## 1. Rename the Project

- Update all references to `flask-template` in:
  - `pyproject.toml`, `setup.py`, or `main.py`
  - `README.md` and other docs
  - `.github/workflows/*`

- Optionally, run the provided script:

  ```sh
  ./scripts/rename-template.sh <your-new-project-name>
  ```

## 2. Update Metadata

- Change author, description, and repository fields in `pyproject.toml` or `setup.py`.
- Update badges in `README.md`.

## 3. Review Environment Variables

- Copy `.env.example` to `.env` and adjust values as needed.

## 4. Update CI/CD

- Edit workflow files in `.github/workflows/` to match your project and org.

## 5. Review Security & Contribution Policies

- Update `SECURITY.md` and `CONTRIBUTING.md` as needed.

## 6. Remove Template Scripts

- Delete `scripts/rename-template.sh` after renaming.

---

For more details, see the main documentation and comments in each file.
