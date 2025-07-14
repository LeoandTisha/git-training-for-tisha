# Module 3: LeoLab Workflow

## 🎯 Learning Objectives

By the end of this module, you will:
- Understand LeoLab's branch structure (main, stg, dev, feature)
- Create proper feature branches
- Write commit messages following our standards
- Include Claude Code attribution in commits
- Follow our security practices

## 📚 LeoLab Branch Structure

At LeoLab, we use a structured branching strategy to keep our code organized and stable.

### Primary Branches (Protected)

#### `main` Branch
- **Purpose**: Production-ready code
- **Protection**: Cannot push directly, requires Pull Request
- **Rule**: This code is live or ready to go live

#### `stg` Branch (Staging)
- **Purpose**: Testing environment that mirrors production
- **Protection**: Similar to main
- **Rule**: Code here is being validated before production

#### `dev` Branch
- **Purpose**: Development integration
- **Protection**: Less strict than main/stg
- **Rule**: Where features come together for testing

### Feature Branches

We create temporary branches for new work:

- `feature/description` - New features
- `bugfix/description` - Fixing bugs  
- `hotfix/description` - Emergency fixes
- `docs/description` - Documentation updates

### Examples
- ✅ `feature/jira-integration`
- ✅ `bugfix/auth-timeout`
- ✅ `hotfix/critical-security-fix`
- ✅ `docs/update-readme`

## 💻 Creating Feature Branches

### The Golden Rule
**ALWAYS start from main and ALWAYS create a feature branch!**

```bash
# Step 1: Make sure you're on main
git checkout main

# Step 2: Get latest changes
git pull origin main

# Step 3: Create your feature branch
git checkout -b feature/add-user-dashboard

# Verify you're on the new branch
git branch
```

### Branch Naming Conventions

Keep branch names:
- **Descriptive**: What does this branch do?
- **Lowercase**: Use hyphens, not spaces
- **Concise**: But clear enough to understand

Good examples:
- `feature/vault-authentication`
- `bugfix/login-error-special-chars`
- `docs/api-documentation`

## 📝 LeoLab Commit Message Standards

### The Format

```
Brief description (50 chars max)

Detailed explanation if needed:
- What was changed
- Why it was changed
- Any breaking changes

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

### Real Example

```bash
git commit -m "Add Vault authentication to Jira client

- Implement secure token retrieval from HashiCorp Vault
- Add comprehensive error handling for auth failures
- Include retry logic for transient failures
- Update tests for new auth flow

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

### Why This Format?

1. **First line**: Quick summary for git log
2. **Body**: Detailed context for reviewers
3. **Attribution**: Shows AI-assisted development
4. **Clarity**: Helps future developers (including you!)

## 🔒 Security Practices

### Never Commit Secrets!

Before every commit, check:
- ❌ No passwords
- ❌ No API tokens  
- ❌ No private keys
- ❌ No credentials of any kind

### Use Vault for Secrets

All secrets at LeoLab go in Vault:
```python
# ❌ WRONG
api_token = "abc123secret"

# ✅ RIGHT  
vault = VaultClient()
api_token = vault.get_secret("services/api/token")
```

### Check Before Committing

```bash
# Always review what you're about to commit
git diff --staged

# Look for any sensitive information
git status
```

## 🎯 Practice Exercise 3: LeoLab Workflow

Let's practice the complete workflow:

```bash
# 1. Start from main
git checkout main
git pull origin main

# 2. Create a feature branch
git checkout -b feature/tisha-practice-feature

# 3. Make changes
echo "## New Feature\nThis is Tisha's practice feature" > feature.md

# 4. Stage the changes
git add feature.md

# 5. Commit with proper message
git commit -m "Add practice feature documentation

- Create feature.md with basic structure
- Include feature description
- Prepare for future enhancements

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# 6. Push the feature branch
git push -u origin feature/tisha-practice-feature
```

## 📊 Workflow Diagram

```
main (protected)
  |
  |-- git checkout -b feature/new-feature
  |
  feature/new-feature
  |-- make changes
  |-- git add .
  |-- git commit -m "Proper message..."
  |-- git push origin feature/new-feature
  |
  |-- Create Pull Request on GitHub
  |-- Code Review
  |-- Merge to main
```

## 🚨 Common Workflow Mistakes

1. **Working directly on main**
   - Always create a feature branch!
   - Main is protected anyway

2. **Forgetting Claude attribution**
   - Include it in every commit when using Claude
   - It's part of our standards

3. **Poor branch names**
   - ❌ `feature/stuff`
   - ✅ `feature/add-user-authentication`

4. **Not pulling before starting**
   - Always start with the latest main
   - Prevents conflicts later

## 🔍 Checking Your Work

Before pushing, verify:

```bash
# Check you're on the right branch
git branch

# Check your commit message
git log -1

# Check no secrets are included
git diff origin/main

# Check status is clean
git status
```

## 📝 Module Summary

You've learned:
- ✅ LeoLab's branch structure (main, stg, dev, feature)
- ✅ How to create and name feature branches
- ✅ Proper commit message format with Claude attribution
- ✅ Security practices (no secrets!)
- ✅ The complete feature workflow

## 🚀 What's Next?

Module 4 will teach you about Pull Requests:
- Creating PRs
- Linking to Jira tickets
- Participating in code reviews

## 📖 Quick Reference Card

```bash
# Start new feature
git checkout main
git pull origin main
git checkout -b feature/description

# Commit with proper message
git add .
git commit -m "Brief description

- Detailed change 1
- Detailed change 2

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# Push feature branch
git push -u origin feature/description
```

## 🎉 You're Following the LeoLab Way!

Practice this workflow until it becomes natural. Remember:
- Feature branches protect main
- Good commit messages help everyone
- Security is everyone's responsibility

---

**Golden Rule**: When in doubt, create a PR for discussion rather than pushing directly to main!