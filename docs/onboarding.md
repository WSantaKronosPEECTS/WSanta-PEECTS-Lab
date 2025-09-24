mkdir -p docs
# Create files
echo "<paste onboarding content here>" > docs/onboarding.md
echo "<paste glossary content here>" > docs/glossary.md

# Commit and push
git add docs/onboarding.md docs/glossary.md
git commit -m "Add onboarding guide and glossary for PEECTS Lab"
git push origin main

