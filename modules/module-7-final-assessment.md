# Module 7: Final Assessment & Quick Reference

## 🎯 Learning Objectives

By the end of this module, you will:
- Demonstrate proficiency with the complete workflow
- Handle emergency procedures
- Have quick reference materials for daily use
- Be fully set up for LeoLab development
- Feel confident using Git and GitHub

## 📋 Final Assessment

Complete the following tasks independently to demonstrate your Git proficiency.

### Task 1: Complete Feature Workflow

Create a feature that adds a configuration file to the Jira reporter:

1. Start from main and create branch: `feature/add-config-support`
2. Add a `config.yaml` file with sample configuration
3. Update .gitignore to ignore `config.local.yaml`
4. Make at least 2 meaningful commits
5. Push and create a PR
6. Link to ticket TRAINING-7

**Success Criteria:**
- Branch created correctly
- Commits follow our format
- No secrets in code
- PR properly formatted

### Task 2: Emergency Procedures

Demonstrate knowledge of emergency procedures:

1. **Hotfix Scenario**: Show how you would create a hotfix branch
2. **Accidental Secret**: Explain what to do if you committed a password
3. **Wrong Branch**: Show how to move commits from main to a feature branch
4. **Merge Conflict**: Resolve a simple merge conflict

### Task 3: Security Audit

Review this code and identify security issues:

```python
# config.py
DATABASE_URL = "postgresql://admin:password123@prod.db.com/myapp"
API_KEY = "sk_live_abc123xyz789"
JWT_SECRET = "my-super-secret-key"

def connect_to_jira():
    username = "tisha@leolab.com"
    password = "TishaPassword123!"
    return JiraClient(username, password)
```

**What would you change?**

## 🚀 Quick Reference Guide

### Daily Git Commands

```bash
# Start your day
git checkout main
git pull origin main

# Create feature branch
git checkout -b feature/description

# Check what you're doing
git status
git diff
git branch

# Save your work
git add .
git commit -m "Message..."
git push origin feature/branch

# Create PR
gh pr create --title "[TICKET] Description"
```

### Commit Message Template

Save this as `.gitmessage` in your home directory:

```
Brief description (50 chars max)

Detailed explanation:
- What changed
- Why it changed
- Breaking changes

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

Configure Git to use it:
```bash
git config --global commit.template ~/.gitmessage
```

### Branch Naming Cheat Sheet

| Type | Format | Example |
|------|--------|---------|
| Feature | `feature/description` | `feature/add-user-auth` |
| Bug Fix | `bugfix/description` | `bugfix/login-timeout` |
| Hotfix | `hotfix/description` | `hotfix/security-patch` |
| Docs | `docs/description` | `docs/update-readme` |

### PR Template

```markdown
## Summary
[What does this PR do?]

## Changes
- [Specific change 1]
- [Specific change 2]

## Jira Ticket
[TICKET-123](https://leoslab.atlassian.net/browse/TICKET-123)

## Testing
- [ ] All tests pass
- [ ] Manual testing completed
- [ ] No security issues

## Screenshots
[If applicable]
```

### Security Checklist

Before EVERY commit:
- [ ] Run `git diff --staged`
- [ ] No passwords, tokens, or keys
- [ ] .gitignore is updated
- [ ] Using Vault for secrets
- [ ] No personal information

### Emergency Contacts

- **Accidentally committed secret**: Tell Leo IMMEDIATELY
- **Can't resolve issue**: Ask in Slack
- **PR stuck**: Tag Leo for review
- **Vault issues**: Check vault.hcl configuration

## 🛠️ Your Development Setup

### Essential Tools

Make sure you have:
- [x] Git installed and configured
- [x] GitHub CLI (`gh`) installed
- [x] Vault CLI installed
- [x] vault.hcl configured
- [x] leoslab-toolkit installed
- [x] VS Code or preferred editor

### Git Configuration

```bash
# Your identity
git config --global user.name "Tisha"
git config --global user.email "tisha@leoandtisha.net"

# Helpful aliases
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.last 'log -1 HEAD'

# Better diffs
git config --global diff.colorMoved zebra
```

### VS Code Extensions

Recommended for Git:
- GitLens
- Git Graph
- GitHub Pull Requests

## 📊 Workflow Diagram

Keep this handy:

```
┌─────────────┐
│    main     │ (protected)
└──────┬──────┘
       │
       ├─> git checkout -b feature/new
       │
┌──────┴──────┐
│   feature/  │ (your work)
│   branch    │
└──────┬──────┘
       │
       ├─> make changes
       ├─> git add .
       ├─> git commit -m "..."
       ├─> git push origin feature/branch
       │
┌──────┴──────┐
│     PR      │ (code review)
│   Review    │
└──────┬──────┘
       │
       ├─> address feedback
       ├─> get approval
       │
┌──────┴──────┐
│   Merge     │
│  to main    │
└─────────────┘
```

## 🎓 Certification Checklist

You're certified LeoLab Git ready when you can:

### Git Basics
- [x] Create and navigate repositories
- [x] Make commits with proper messages
- [x] Use branches effectively
- [x] Check status and view logs

### GitHub Skills
- [x] Clone repositories
- [x] Push and pull changes
- [x] Create pull requests
- [x] Participate in code reviews

### LeoLab Specific
- [x] Follow our branch naming
- [x] Write proper commit messages with attribution
- [x] Link PRs to Jira tickets
- [x] Never commit secrets

### Security
- [x] Use .gitignore properly
- [x] Understand Vault integration
- [x] Recognize security warnings
- [x] Follow security checklist

## 🎉 Congratulations!

You've completed the LeoLab Git & GitHub training! You now have:

- ✅ Solid understanding of Git fundamentals
- ✅ Proficiency with GitHub workflows
- ✅ Knowledge of LeoLab standards
- ✅ Security-first mindset
- ✅ Quick reference materials
- ✅ Confidence to contribute to projects

## 📚 Continuing Education

Keep learning:
- Practice on real projects
- Read other people's PRs
- Ask questions in code reviews
- Share knowledge with others

## 🆘 Getting Help

Remember:
- **Check this guide first**
- **Ask in Slack**
- **Tag Leo in PRs**
- **Never guess with security**

## 📝 Quick Command Reference

```bash
# Daily workflow
git checkout main && git pull
git checkout -b feature/my-feature
git add . && git commit -m "Message"
git push -u origin feature/my-feature
gh pr create

# Checking things
git status           # What's changed?
git diff            # What exactly changed?
git log --oneline   # Recent commits
git branch          # Which branch am I on?

# Fixing mistakes
git checkout .      # Undo all changes
git reset HEAD~1    # Undo last commit
git stash          # Temporarily save changes
```

---

**Welcome to the team! You're now ready to contribute to LeoLab projects with confidence. Happy coding! 🚀**