# 🧪 CI/CD Validation Status

This document tracks the operational status of all workflows in WSanta-PEECTS-Lab. It supports reproducibility, contributor onboarding, and Zenodo DOI metadata integrity.

---

## ✅ Active Workflows

| Workflow Name               | Platform        | Status      | Last Updated | Notes                          |
|----------------------------|-----------------|-------------|---------------|--------------------------------|
| Starter Tests              | Ubuntu (Python) | ✅ Validated | Oct 2025      | Uses `upload-artifact@v4`      |
| Full Appliance Validation  | Windows (Conda) | ✅ Validated | Oct 2025      | VM appliance test + log upload |
| Python / Conda on Windows  | Windows (Conda) | ✅ Validated | Oct 2025      | Console validation + logs      |
| Link Check                 | Ubuntu          | ✅ Validated | Oct 2025      | Checks README and DOI links    |

---

## 🛠️ Known Issues

- All deprecated `@v3` actions have been replaced with `@v4`
- Artifact uploads now succeed across platforms
- Console usability confirmed for Windows and Ubuntu runners

---

## 📣 Contributor Notes

- All workflows auto-trigger on `push` and `pull_request` to `main`
- Logs are uploaded to GitHub Actions for audit and review
- Contributors may run validations locally using `validate_appliance.py` or `validate_windows.py`

---

## 🔗 Related Resources

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [Show & Tell Discussion](https://github.com/WSantaKronosPEECTS/WSanta-PEECTS-Lab/discussions)
- [Zenodo DOI Landing Page](https://zenodo.org/record/XXXXXX) ← *(replace with actual DOI)*

---

This file is updated with each CI/CD upgrade. For questions or validation logs, please open an issue or join the pinned discussion.
