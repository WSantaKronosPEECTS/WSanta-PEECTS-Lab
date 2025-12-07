# Zenodo Archive Verification Report

## Archive Information

**Archive Name:** `WSanta-PEECTS-Lab_v1.0.0_FULL_EXPORT.zip`

**Date Created:** 2025-12-07

**File Size:** 2.6 MB (2,710,269 bytes uncompressed across 94 files)

**SHA-256 Checksum:** `ead1385cd8272f91cefe538dceb831491fa64015e74d968100094423a1475309`

## Archive Integrity

✅ **ZIP Integrity Test:** PASSED - No errors detected in compressed data

## Required Components Verification

### ✅ Core Files
- [x] README.md
- [x] CITATION.cff
- [x] Licence (LICENSE file)
- [x] CONTRIBUTING.md
- [x] SECURITY.md
- [x] GET_STARTED.md

### ✅ Documentation Directory
- [x] docs/
  - docs/onboarding.md
  - docs/glossary.md
  - docs/dashboard.md

### ✅ GitHub Workflows
- [x] .github/workflows/
  - .github/workflows/full-appliance-validation.yml
  - .github/workflows/python-package-conda.yml
  - .github/workflows/starter-tests.yml
  - .github/workflows/link-check.yml
  - .github/workflows/main.yml

### ✅ Supporting Assets
- [x] Core/ directory with PEECTS Dr Santa.txt
- [x] CONSOLE (Kronas)/ directory with console files
- [x] CONSOLE-Kronas/ directory
- [x] WSanta-PEECTS-StressTest-Starter/ (complete stress test suite)
  - alerts/
  - benchmarks/
  - data/
  - notebooks/
  - pipelines/
  - protocols/
  - scripts/
  - tests/
  - CITATIONS/
- [x] ISSUE_TEMPLATE/ directory
- [x] ci-status.md
- [x] .lychee.toml

### ✅ Additional Package Files
- [x] Build & Run Demo
- [x] MirrorTerminal.bat.bat
- [x] MirrorTerminalApp.exe
- [x] Various ZIP packages (for reference)

## Archive Structure

The ZIP archive preserves:
- ✅ Original folder structure
- ✅ Relative paths
- ✅ File permissions and attributes
- ✅ All 94 files and directories from the main branch

## Exclusions

The following were correctly excluded from the archive:
- .git/ directory (version control metadata not needed for Zenodo)
- The ZIP file itself (to avoid recursion)

## Zenodo Readiness

This archive is **READY FOR ZENODO DEPOSIT** with the following characteristics:

1. **Complete Repository Export:** All files from the main branch are included
2. **Proper Metadata:** CITATION.cff file included for DOI linkage
3. **Documentation:** Comprehensive docs/ directory and README.md
4. **License Information:** Licence file clearly included
5. **Reproducibility:** GitHub workflows and all supporting assets preserved
6. **Integrity Verified:** ZIP file integrity test passed successfully

## Download Location Note

**Important:** Due to the sandboxed CI/CD environment, the ZIP file has been created in the repository root:
```
/home/runner/work/WSanta-PEECTS-Lab/WSanta-PEECTS-Lab/WSanta-PEECTS-Lab_v1.0.0_FULL_EXPORT.zip
```

To download this file locally:
1. This file will be available as a build artifact (if configured in CI/CD)
2. Alternatively, you can clone the branch and the file will be present
3. Or download it directly from the repository if pushed

## Verification Commands

To verify the archive yourself:

```bash
# Check file size
ls -lh WSanta-PEECTS-Lab_v1.0.0_FULL_EXPORT.zip

# Verify SHA-256 checksum
sha256sum WSanta-PEECTS-Lab_v1.0.0_FULL_EXPORT.zip

# Test ZIP integrity
unzip -t WSanta-PEECTS-Lab_v1.0.0_FULL_EXPORT.zip

# List contents
unzip -l WSanta-PEECTS-Lab_v1.0.0_FULL_EXPORT.zip
```

## Next Steps for Zenodo Deposit

1. Download the ZIP file to your local system
2. Log in to Zenodo (https://zenodo.org)
3. Click "New upload"
4. Upload `WSanta-PEECTS-Lab_v1.0.0_FULL_EXPORT.zip`
5. Fill in metadata (title, authors, description, keywords)
6. Select appropriate license (based on your Licence file)
7. Review and publish to receive DOI

---

**Archive Generation Completed Successfully** ✅
