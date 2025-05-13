#!/bin/bash
# Auto commit every change

# Change to the repository directory (if needed)
cd /path/to/your/repo

# Stage all changes
git add -A

# Commit with a custom message
git commit -m "Automated commit for all changes"

# Push to remote (replace 'main' with your branch name)
git push origin main
