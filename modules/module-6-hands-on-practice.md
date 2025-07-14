# Module 6: Hands-On Practice Project

## 🎯 Learning Objectives

By the end of this module, you will:
- Complete a full feature workflow from start to finish
- Handle common real-world scenarios
- Troubleshoot typical Git problems
- Demonstrate proficiency with LeoLab standards
- Build confidence with Git and GitHub

## 📚 Your Practice Project

You'll build a simple Python script that integrates with our toolkit, following all LeoLab standards.

### Project: Jira Ticket Reporter

Create a script that:
1. Connects to Jira using Vault credentials
2. Lists your assigned tickets
3. Generates a simple report
4. Follows all security practices

## 🚀 Complete Workflow Walkthrough

### Step 1: Setup and Planning

```bash
# 1. Make sure you're starting fresh
# Navigate to a directory where you keep your projects
cd ~/Projects  # or wherever you keep your code
# Clone your practice repository (Leo will provide the URL)
git clone <practice-repository-url>
cd <practice-repository-name>

# 2. Start from main
git checkout main
git pull origin main

# 3. Create your feature branch
git checkout -b feature/jira-ticket-reporter
```

### Step 2: Create the Project Structure

```bash
# Create project directories
mkdir -p jira_reporter/src
mkdir -p jira_reporter/tests

# Create initial files
touch jira_reporter/src/__init__.py
touch jira_reporter/src/reporter.py
touch jira_reporter/README.md
touch jira_reporter/.gitignore
```

### Step 3: Add .gitignore First!

```bash
cat > jira_reporter/.gitignore << 'EOF'
# Security - Never commit these
.env
.vault-token
secrets.json
*.key
*.pem

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Project specific
reports/
*.log
config.local.yaml
EOF

# Commit the .gitignore
git add jira_reporter/.gitignore
git commit -m "Add .gitignore for Jira reporter project

- Include security patterns for secrets
- Add Python-specific ignores
- Include IDE and OS files
- Prevent report output from being committed

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

### Step 4: Create the Reporter Script

```bash
cat > jira_reporter/src/reporter.py << 'EOF'
"""
Jira Ticket Reporter - Practice Project for Git Training
This script demonstrates secure credential handling and LeoLab standards.
"""

import sys
from datetime import datetime
from typing import List, Dict

# Note: In a real project, we would use the leoslab CLI tool
# to interact with Jira and Vault. This is a simplified example.

def generate_report(tickets: List[Dict]) -> str:
    """
    Generate a formatted report of Jira tickets.
    
    Args:
        tickets: List of ticket dictionaries
        
    Returns:
        Formatted report string
    """
    report = f"# Jira Ticket Report\n"
    report += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    if not tickets:
        report += "No tickets found.\n"
        return report
    
    report += f"Total tickets: {len(tickets)}\n\n"
    report += "## Tickets\n\n"
    
    for ticket in tickets:
        report += f"- **{ticket['key']}**: {ticket['summary']}\n"
        report += f"  - Status: {ticket['status']}\n"
        report += f"  - Assignee: {ticket['assignee']}\n\n"
    
    return report


def main():
    """Main function to run the reporter."""
    print("Jira Ticket Reporter")
    print("=" * 50)
    
    # In real implementation, we would:
    # 1. Initialize JiraClient with Vault
    # 2. Fetch actual tickets
    # 3. Generate real report
    
    # For now, use sample data
    sample_tickets = [
        {
            "key": "TRAINING-1",
            "summary": "Complete Git training",
            "status": "In Progress",
            "assignee": "Tisha"
        },
        {
            "key": "TRAINING-2", 
            "summary": "Practice pull requests",
            "status": "To Do",
            "assignee": "Tisha"
        }
    ]
    
    report = generate_report(sample_tickets)
    print(report)
    
    # Save report (but don't commit it!)
    with open("jira_reporter/my_report.md", "w") as f:
        f.write(report)
    print("Report saved to my_report.md")


if __name__ == "__main__":
    main()
EOF

# Commit the reporter
git add jira_reporter/src/
git commit -m "Add Jira ticket reporter script

- Create reporter.py with report generation logic
- Include type hints and documentation
- Prepare structure for Vault integration
- Add sample data for testing

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

### Step 5: Add Documentation

```bash
cat > jira_reporter/README.md << 'EOF'
# Jira Ticket Reporter

A practice project for learning Git and GitHub workflows at LeoLab.

## Overview

This script generates reports of Jira tickets assigned to a user, demonstrating:
- Secure credential handling with Vault
- Proper project structure
- LeoLab coding standards

## Setup

```bash
# No external dependencies for this practice project
# In a real project, we would use the leoslab CLI tool
```

## Usage

```bash
python src/reporter.py
```

## Security

- Never commit credentials
- All secrets come from Vault
- Reports are gitignored

## Author

Tisha - Git Training Project 2024
EOF

# Commit the README
git add jira_reporter/README.md
git commit -m "Add README documentation

- Include project overview
- Add setup and usage instructions
- Document security practices
- Credit author

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

### Step 6: Push and Create PR

```bash
# Push your feature branch
git push -u origin feature/jira-ticket-reporter

# Create the pull request
gh pr create \
  --title "[TRAINING-6] Add Jira ticket reporter project" \
  --body "## Summary

Created a Jira ticket reporter as practice for the complete Git workflow.

## Changes
- Add project structure with proper .gitignore
- Create reporter.py with ticket reporting logic
- Add comprehensive README documentation
- Follow all LeoLab security practices

## Jira Ticket
TRAINING-6

## Testing
- [x] Script runs without errors
- [x] No secrets in code
- [x] Proper .gitignore in place
- [x] All commits follow standards

## Security Checklist
- [x] No hardcoded credentials
- [x] .gitignore includes all sensitive patterns
- [x] Ready for Vault integration

## Notes
This is a practice project for Git training. The actual Vault integration is commented out but the structure is ready."
```

## 🔧 Common Scenarios and Solutions

### Scenario 1: Merge Conflicts

What if someone else changed main while you were working?

```bash
# You try to push and get an error
git push origin feature/your-branch
# Error: Updates were rejected

# Solution:
git checkout main
git pull origin main
git checkout feature/your-branch
git merge main

# Resolve conflicts if any, then:
git add .
git commit -m "Merge main into feature branch"
git push origin feature/your-branch
```

### Scenario 2: Committed to Wrong Branch

Oops, you committed to main instead of a feature branch:

```bash
# Create a new branch with your changes
git branch feature/fix-mistake

# Reset main to origin/main
git reset --hard origin/main

# Switch to your feature branch
git checkout feature/fix-mistake
```

### Scenario 3: Need to Undo Last Commit

Made a mistake in your last commit:

```bash
# Undo commit but keep changes
git reset --soft HEAD~1

# Now you can fix and recommit
git add .
git commit -m "Better commit message"
```

### Scenario 4: Accidentally Committed a Secret

**STOP! Tell Leo immediately!** But here's what happens:

```bash
# DO NOT try to fix it yourself
# The secret is already in history
# Even if you delete it, it's still there
# The secret must be rotated
```

## 🎯 Practice Challenges

### Challenge 1: Add a Feature

Add error handling to the reporter:

```python
try:
    # Existing code
except Exception as e:
    print(f"Error generating report: {e}")
    sys.exit(1)
```

### Challenge 2: Fix a "Bug"

The date format is hard to read. Change it to:
```python
datetime.now().strftime('%B %d, %Y at %I:%M %p')
```

### Challenge 3: Update Documentation

Add a "Contributing" section to the README explaining how others can contribute.

## 🚨 Troubleshooting Guide

### Problem: "Permission denied (publickey)"
**Solution**: Make sure you're authenticated with GitHub

### Problem: "fatal: not a git repository"
**Solution**: You're not in a Git repo. Check with `pwd` and `ls -la`

### Problem: "Your branch is behind origin/main"
**Solution**: Pull the latest changes: `git pull origin main`

### Problem: PR checks failing
**Solution**: Read the error messages, fix issues, push new commits

## 📊 Final Checklist

Before considering this module complete:

- [ ] Created feature branch from main
- [ ] Made multiple meaningful commits
- [ ] All commits have proper messages with Claude attribution
- [ ] No secrets in code
- [ ] .gitignore properly configured
- [ ] Pushed feature branch to GitHub
- [ ] Created PR with proper format
- [ ] PR links to Jira ticket
- [ ] All checks pass
- [ ] Ready for review

## 📝 Module Summary

You've successfully:
- ✅ Completed a full feature workflow
- ✅ Handled real-world Git scenarios
- ✅ Followed all LeoLab standards
- ✅ Created a working project
- ✅ Demonstrated Git proficiency

## 🚀 What's Next?

Module 7 will be your final assessment where you'll:
- Complete a workflow without guidance
- Demonstrate emergency procedures
- Receive your quick reference materials
- Set up your development environment

## 🎉 Congratulations!

You've built your first project following the complete LeoLab workflow! This is exactly how you'll work on real projects.

### Key Takeaways

1. **Always start from main**
2. **Feature branches for everything**
3. **Security first - no secrets**
4. **Commit messages matter**
5. **PRs are conversations**

---

**You're ready for real projects! Keep practicing and don't hesitate to ask questions.**