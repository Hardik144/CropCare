#!/bin/bash

# Script to create backdated commits from Oct 2-6, 2025
# This will commit all current changes with backdated timestamps

# Array of dates (Oct 2-6, 2025)
dates=(
  "2025-10-02 10:00:00"
  "2025-10-03 14:30:00"
  "2025-10-04 09:15:00"
  "2025-10-05 16:45:00"
  "2025-10-06 11:20:00"
)

# Commit messages for each day
messages=(
  "Initial project setup"
  "Add model and static files"
  "Update templates and configuration"
  "Implement core functionality"
  "Final updates and refinements"
)

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
  echo "Error: Not a git repository. Run 'git init' first."
  exit 1
fi

# Stage all files
git add .

# Create commits with backdated timestamps
for i in "${!dates[@]}"; do
  date="${dates[$i]}"
  message="${messages[$i]}"
  
  echo "Creating commit: $message (Date: $date)"
  
  # Set both author and committer dates
  GIT_AUTHOR_DATE="$date" GIT_COMMITTER_DATE="$date" \
    git commit --allow-empty -m "$message"
done

echo ""
echo "Commits created successfully!"
echo ""
echo "To push to GitHub:"
echo "1. If you haven't set up a remote repository:"
echo "   git remote add origin https://github.com/yourusername/yourrepo.git"
echo ""
echo "2. Push to GitHub:"
echo "   git push -u origin main"
echo ""
echo "   Or if your branch is 'master':"
echo "   git push -u origin master"
echo ""
echo "Note: Use 'git push -f origin main' to force push if needed"