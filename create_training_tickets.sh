#!/bin/bash

# Create Jira tickets for Tisha's Git training using leoslab CLI

echo "Creating Git Training tickets in Jira..."
echo "======================================="

# First, let's create the training tickets manually using curl/API
# since we need to create an Epic with subtasks

# For now, let's document what needs to be created in Jira:

cat << 'EOF'

JIRA TICKETS TO CREATE:

1. EPIC: Git & GitHub Training for Tisha
   - Assignee: Tisha
   - Labels: training, git, onboarding
   
2. SUBTASKS under the Epic:
   
   - Module 1: Git Fundamentals
   - Module 2: GitHub Basics  
   - Module 3: LeoLab Workflow
   - Module 4: Pull Requests & Code Review
   - Module 5: Security & Best Practices
   - Module 6: Hands-On Practice Project
   - Module 7: Final Assessment & Quick Reference

Each subtask should:
- Be assigned to Tisha
- Have detailed acceptance criteria
- Include link to the training materials
- Have appropriate labels (training, git, module-X)

The training materials are located at:
/Users/leomaguire/Documents/GitHub/git-training-for-tisha/

EOF

echo ""
echo "Please create these tickets manually in Jira for now."
echo "Use project key: INFRA or TRAINING as appropriate."