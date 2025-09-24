mkdir -p docs
# Create files
echo "<paste onboarding content here>" > docs/onboarding.md
echo "<paste glossary content here>" > docs/glossary.md

# Commit and push
git add docs/onboarding.md docs/glossary.md
git commit -m "Add onboarding guide and glossary for PEECTS Lab"
git push origin main
# 🚀 WSanta-PEECTS Lab Onboarding Guide

Welcome to the WSanta-PEECTS Lab—a deployable framework for forensic simulation, elastic time modeling, and entanglement-aware audit tools. This guide helps contributors, reviewers, and agencies get started with modules, workflows, and validation logic.

---

## 🧭 Quick Start

1. **Clone the repository**  
   ```bash
   git clone https://github.com/WSantaKronosPEECTS/WSanta-PEECTS-Lab.git
   cd WSanta-PEECTS-Lab
npm install

