#!/usr/bin/env python3
"""
Create FINAL correct Jira tickets for Git training.
This time with the RIGHT ticket numbers!
"""

import subprocess
import time

def create_ticket(project, summary, description, issue_type="Task", assignee=None, epic=None, points=None, due_date=None):
    """Create a Jira ticket using the CLI."""
    cmd = ["leoslab", "jira", "create", project, summary, description, "-t", issue_type]
    
    if assignee:
        cmd.extend(["-a", assignee])
    if epic:
        cmd.extend(["-e", epic])
    if points:
        cmd.extend(["-p", str(points)])
    if due_date:
        cmd.extend(["-d", due_date])
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ Created: {summary}")
        # Extract issue key from output
        for line in result.stdout.split('\n'):
            if "Created issue:" in line:
                key = line.split(": ")[1].strip()
                print(f"   Key: {key}")
                return key
    else:
        print(f"❌ Failed to create: {summary}")
        print(result.stderr)
    return None

# Tisha's account ID
TISHA_ID = "63e2742c790148a180974130"

# Create Epic - THIS TIME IT WILL HAVE THE RIGHT NUMBERS!
epic_description = """# Git & GitHub Training for Tisha

## Overview
Comprehensive Git and GitHub training course tailored for LeoLab workflow.

## How This Training Works
1. Complete each module in order (see child tasks below)
2. Each module has step-by-step instructions in its description
3. Work 3 hours/day, 4 days/week
4. Mark each task complete in Jira as you finish

## Getting Started
1. Look at the child tasks below this Epic
2. Start with Module 1 (first task)
3. Each task has COMPLETE instructions
4. Follow them in order

## Schedule
- Week 1: Modules 1-5 (July 14-17, 2025)
- Week 2: Modules 6-8 (July 21-24, 2025)
- Total time: 19 hours

## Your Modules
The subtasks below are your training modules:
- Module 1: Git Fundamentals (3 hours)
- Module 2: GitHub Basics (2 hours)  
- Module 3: LeoLab Workflow (3 hours)
- Module 4: Pull Requests & Code Review (2 hours)
- Module 5: Security & Best Practices (2 hours)
- Module 6: Hands-On Practice Project (4 hours)
- Module 7: Final Assessment (2 hours)
- Module 8: Review & Buffer Time (1 hour)

## Success Criteria
- Complete all modules below
- Pass final assessment
- Ready for real LeoLab projects

## Support
- Slack: Message Leo with questions
- Training repo: https://github.com/leoandtisha/git-training-for-tisha
- Each module has troubleshooting sections"""

print("Creating NEW Epic with CORRECT information...")
epic_key = create_ticket("INFRA", "Git & GitHub Training for Tisha - COMPLETE", epic_description, "Epic", TISHA_ID)

if not epic_key:
    print("Failed to create epic, exiting")
    exit(1)

# Store ticket numbers for reference
tickets_created = [epic_key]

time.sleep(1)

# Module 1
module1_desc = """# Module 1: Git Fundamentals

## 📚 How to Complete This Module

### First Time Setup
Since this is your first module, you need to get the training materials:

1. **Open Terminal** (Mac: Applications > Utilities > Terminal)

2. **Go to your Documents folder:**
   ```
   cd ~/Documents
   ```

3. **Download the training materials:**
   ```
   git clone https://github.com/leoandtisha/git-training-for-tisha.git
   ```
   (This copies all training files to your computer)

4. **Enter the training folder:**
   ```
   cd git-training-for-tisha
   ```

5. **Open the module guide:**
   - Open: `modules/module-1-git-fundamentals.md`
   - Use VS Code or any text editor
   - READ THE ENTIRE MODULE FIRST

### What You'll Learn
- What Git is and why we use it
- Git vs GitHub (they're different!)
- Core concepts: repositories, commits, branches
- Essential Git commands

### Your Tasks
1. Configure Git with your name/email
2. Do "Practice Exercise 1" from the module
3. Create 2 more practice repositories
4. Practice: status, add, commit, log commands
5. Complete the Quick Quiz

### Done When
- [ ] Git shows your name/email
- [ ] You created 3+ repositories
- [ ] You made multiple commits
- [ ] You understand status and log
- [ ] Quiz completed

### Need Help?
Check module troubleshooting section first, then Slack Leo

**Time: 3 hours**
**Due: July 14, 2025**"""

print(f"\nCreating Module 1...")
m1_key = create_ticket("INFRA", "Module 1: Git Fundamentals", module1_desc, "Task", TISHA_ID, epic_key, 3, "2025-07-14")
tickets_created.append(m1_key)
time.sleep(1)

# Module 2
module2_desc = """# Module 2: GitHub Basics

## 📚 How to Complete This Module

### Before Starting
✅ Complete Module 1 first!

### Setup
1. **Go to your training folder:**
   ```
   cd ~/Documents/git-training-for-tisha
   ```

2. **Open the module guide:**
   - Open: `modules/module-2-github-basics.md`
   - READ IT ALL before starting exercises

### What You'll Learn
- Git = software on your computer
- GitHub = website for sharing Git repos
- How to clone (copy from GitHub)
- How to push (send to GitHub)
- How to pull (get updates)

### Your Tasks
1. Read about Git vs GitHub
2. Practice cloning a repository
3. Make changes and push them
4. Pull changes from GitHub
5. Explore GitHub.com interface

### Practice Repository
- Leo will create one for you
- He'll provide the URL when you reach that section
- Use it for all Module 2 exercises

### Done When
- [ ] You understand Git vs GitHub
- [ ] You can clone any repository
- [ ] You can push your changes
- [ ] You can pull updates
- [ ] You navigated GitHub.com

### Common Problems
See "Troubleshooting" section in module

**Time: 2 hours**
**Due: July 15, 2025**"""

print(f"Creating Module 2...")
m2_key = create_ticket("INFRA", "Module 2: GitHub Basics", module2_desc, "Task", TISHA_ID, epic_key, 2, "2025-07-15")
tickets_created.append(m2_key)
time.sleep(1)

# Module 3
module3_desc = """# Module 3: LeoLab Workflow

## 📚 How to Complete This Module

### CRITICAL MODULE
This is how we work every day at LeoLab. Master this!

### Setup
1. **Go to training folder:**
   ```
   cd ~/Documents/git-training-for-tisha
   ```

2. **Open:** `modules/module-3-leolab-workflow.md`

### What You'll Learn
- LeoLab branch structure:
  - `main` = production (protected)
  - `feature/` = new features
  - `bugfix/` = fixing bugs
  - `hotfix/` = emergency fixes
- Our EXACT commit message format
- Claude Code attribution (required!)
- Security practices

### Your Tasks
1. Practice creating feature branches
2. Write 5+ commits with our format:
   ```
   Brief description
   
   - Detailed change
   - Another change
   
   🤖 Generated with [Claude Code](https://claude.ai/code)
   
   Co-Authored-By: Claude <noreply@anthropic.com>
   ```
3. Create branches with proper names
4. NEVER commit secrets!

### Done When
- [ ] Created 3+ feature branches
- [ ] All commits follow our format
- [ ] Claude attribution included
- [ ] Understand main/feature workflow
- [ ] Security practices clear

### This Is Important!
We're strict about these standards. Practice until perfect.

**Time: 3 hours**
**Due: July 16, 2025**"""

print(f"Creating Module 3...")
m3_key = create_ticket("INFRA", "Module 3: LeoLab Workflow", module3_desc, "Task", TISHA_ID, epic_key, 3, "2025-07-16")
tickets_created.append(m3_key)
time.sleep(1)

# Module 4
module4_desc = """# Module 4: Pull Requests & Code Review

## 📚 How to Complete This Module

### Setup
1. **Training folder:** `cd ~/Documents/git-training-for-tisha`
2. **Open:** `modules/module-4-pull-requests.md`

### What You'll Learn
- Pull Requests (PRs) = proposing changes
- How to create PRs
- Linking PRs to Jira
- Code review process
- PR requirements at LeoLab

### Your Tasks
1. Install GitHub CLI if needed:
   ```
   brew install gh
   gh auth login
   ```

2. Create a practice PR:
   - Make a feature branch
   - Make changes
   - Push to GitHub
   - Create PR with: `gh pr create`

3. PR must include:
   - Title: [THIS-TICKET] Your description
   - Link to this Jira ticket
   - Clear description
   - No secrets!

### PR Template
```
## Summary
What this PR does

## Changes
- Change 1
- Change 2

## Jira Ticket
[Link to this ticket]

## Testing
- [ ] Tests pass
- [ ] No secrets
```

### Done When
- [ ] Created a PR using gh CLI
- [ ] PR links to Jira
- [ ] Understand PR process
- [ ] Know PR requirements

**Time: 2 hours**
**Due: July 17, 2025**"""

print(f"Creating Module 4...")
m4_key = create_ticket("INFRA", "Module 4: Pull Requests & Code Review", module4_desc, "Task", TISHA_ID, epic_key, 2, "2025-07-17")
tickets_created.append(m4_key)
time.sleep(1)

# Module 5  
module5_desc = """# Module 5: Security & Best Practices

## 📚 How to Complete This Module

### ⚠️ CRITICAL SECURITY MODULE

### Setup
1. **Training folder:** `cd ~/Documents/git-training-for-tisha`
2. **Open:** `modules/module-5-security-best-practices.md`

### What You'll Learn
- Why we NEVER commit secrets
- Using .gitignore properly
- Vault for credentials
- Security warnings
- What to do if you mess up

### Your Tasks
1. Complete the security audit exercise
2. Create a proper .gitignore
3. Practice checking for secrets:
   ```
   git diff --staged
   ```
4. Understand these are NEVER in code:
   - Passwords
   - API tokens
   - Private keys
   - Any credentials

### Critical Rules
- 🚫 NO hardcoded secrets EVER
- 🚫 NO passwords in code
- 🚫 NO tokens in commits
- ✅ Use Vault for all secrets
- ✅ Check every commit

### If You Commit a Secret
1. STOP immediately
2. Tell Leo RIGHT AWAY
3. Don't try to fix it yourself

### Done When
- [ ] Completed security exercises
- [ ] Created .gitignore
- [ ] Understand Vault usage
- [ ] Know what to do if mistakes happen

**Time: 2 hours**
**Due: July 17, 2025**"""

print(f"Creating Module 5...")
m5_key = create_ticket("INFRA", "Module 5: Security & Best Practices", module5_desc, "Task", TISHA_ID, epic_key, 2, "2025-07-17")
tickets_created.append(m5_key)
time.sleep(1)

# Module 6
module6_desc = """# Module 6: Hands-On Practice Project

## 📚 How to Complete This Module

### Build a Real Project!

### Setup
1. **Training folder:** `cd ~/Documents/git-training-for-tisha`
2. **Open:** `modules/module-6-hands-on-practice.md`

### Your Project
Build a "Jira Ticket Reporter" following the complete workflow:
1. Create feature branch
2. Build the project
3. Make proper commits
4. Create a PR
5. Handle common issues

### Step by Step
The module walks you through:
- Creating project structure
- Adding .gitignore FIRST
- Writing the code
- Making multiple commits
- Pushing to GitHub
- Creating the PR

### You'll Practice
- Complete LeoLab workflow
- Troubleshooting problems
- Security practices
- Real coding scenarios

### Done When
- [ ] Created feature branch
- [ ] Built the project
- [ ] Made 3+ proper commits
- [ ] Created PR with correct format
- [ ] Handled any issues

### This Brings It All Together!
Use everything from Modules 1-5

**Time: 4 hours**
**Due: July 22, 2025**"""

print(f"Creating Module 6...")
m6_key = create_ticket("INFRA", "Module 6: Hands-On Practice Project", module6_desc, "Task", TISHA_ID, epic_key, 4, "2025-07-22")
tickets_created.append(m6_key)
time.sleep(1)

# Module 7
module7_desc = """# Module 7: Final Assessment & Quick Reference

## 📚 How to Complete This Module

### Prove Your Skills!

### Setup
1. **Training folder:** `cd ~/Documents/git-training-for-tisha`
2. **Open:** `modules/module-7-final-assessment.md`

### Your Assessment
Complete these independently:
1. Full feature workflow
2. Handle emergency scenarios
3. Security audit challenge
4. Demonstrate all skills

### You'll Get
- Quick reference card
- Command cheat sheet
- Emergency procedures
- Setup verification

### Final Tasks
- [ ] Complete assessment tasks
- [ ] Get quick reference materials
- [ ] Verify your setup
- [ ] Ready for real work!

### After This Module
You're ready to contribute to real LeoLab projects!

**Time: 2 hours**
**Due: July 23, 2025**"""

print(f"Creating Module 7...")
m7_key = create_ticket("INFRA", "Module 7: Final Assessment & Quick Reference", module7_desc, "Task", TISHA_ID, epic_key, 2, "2025-07-23")
tickets_created.append(m7_key)
time.sleep(1)

# Module 8 (Buffer)
module8_desc = """# Review & Buffer Time

## 📚 How to Use This Time

### Flexible Review Session

### Purpose
- Review any challenging topics
- Extra practice where needed
- Questions with Leo
- Ensure you're ready

### Suggested Activities
1. Redo any exercises you struggled with
2. Practice the full workflow again
3. Review security practices
4. Ask Leo questions

### Use This Time If
- Any module was challenging
- You want more practice
- You have questions
- You need confidence boost

### Complete When
- [ ] All previous modules done
- [ ] Questions answered
- [ ] Confident with Git
- [ ] Ready for real work

**Time: 1 hour**
**Due: July 24, 2025**"""

print(f"Creating Module 8...")
m8_key = create_ticket("INFRA", "Review & Buffer Time", module8_desc, "Task", TISHA_ID, epic_key, 1, "2025-07-24")
tickets_created.append(m8_key)

print(f"\n✅ SUCCESSFULLY CREATED:")
print(f"Epic: {epic_key}")
for i, key in enumerate(tickets_created[1:], 1):
    print(f"Module {i}: {key}")

print("\n📋 CORRECT WORKFLOW:")
print(f"1. Tisha starts with {epic_key}")
print(f"2. She sees all the child tasks")
print(f"3. She starts with Module 1 ({tickets_created[1]})")
print(f"4. Each task has COMPLETE instructions")
print(f"5. No confusing old ticket numbers!")

print("\n🗑️ TO DELETE:")
print("Old tickets: INFRA-38 through INFRA-55")
print("\n✅ This set is CORRECT and COMPLETE!")