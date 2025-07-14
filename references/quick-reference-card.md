# Git Quick Reference Card - LeoLab

## 🚀 Daily Workflow

```bash
# Start your day
git checkout main
git pull origin main

# Create feature
git checkout -b feature/description

# Save work
git add .
git commit -m "Message with Claude attribution"
git push origin feature/branch

# Create PR
gh pr create --title "[TICKET-123] Description"
```

## 📝 Commit Message Format

```
Brief description (50 chars max)

- What changed
- Why it changed

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

## 🌳 Branch Names

- `feature/description`
- `bugfix/description`
- `hotfix/description`
- `docs/description`

## 🔍 Status Commands

```bash
git status          # What's changed?
git diff           # See changes
git log --oneline  # Recent commits
git branch         # Current branch
```

## 🚨 Security Checklist

Before EVERY commit:
- [ ] No passwords/tokens
- [ ] Check git diff
- [ ] Update .gitignore
- [ ] Use Vault for secrets

## 🆘 Emergency

**Committed a secret?** → Tell Leo IMMEDIATELY!

## 📋 PR Checklist

- [ ] Branch from latest main
- [ ] Commits have Claude attribution
- [ ] Title includes [TICKET-123]
- [ ] All tests pass
- [ ] No secrets in code

---
**Remember**: When in doubt, ask!