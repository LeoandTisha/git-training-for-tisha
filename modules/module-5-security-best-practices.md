# Module 5: Security & Best Practices

## 🎯 Learning Objectives

By the end of this module, you will:
- Understand why we never commit secrets to Git
- Know how to use .gitignore effectively
- Understand Vault integration for secure credential management
- Recognize security warnings in CI/CD
- Follow LeoLab security best practices

## 🔐 The Golden Rule: Never Commit Secrets!

### What Are Secrets?

Secrets are any sensitive information that could compromise security:
- 🔑 Passwords
- 🎫 API tokens
- 🗝️ Private keys
- 📧 Email credentials
- 🔒 Database connection strings
- 🆔 AWS/Cloud credentials

### Why This Matters

Once something is in Git history, it's there FOREVER (even if deleted later):
- Anyone with repo access can see it
- It's backed up on GitHub
- Hackers scan GitHub for exposed secrets
- Can cost thousands in compromised resources

### Real Example of What NOT to Do

```python
# ❌ NEVER DO THIS
JIRA_TOKEN = "abc123mysecrettoken"
DB_PASSWORD = "SuperSecret123!"
AWS_KEY = "AKIAIOSFODNN7EXAMPLE"

# ✅ DO THIS INSTEAD
vault = VaultClient()
JIRA_TOKEN = vault.get_secret("services/jira/token")
```

## 📁 Using .gitignore

The `.gitignore` file tells Git which files to ignore.

### Common Files to Ignore

```bash
# Environment files
.env
.env.local
.env.*.local

# Credentials
*.pem
*.key
credentials.json
secrets.yaml

# Personal config
.vault-token
config.local.yaml

# IDE files
.vscode/
.idea/
*.swp

# OS files
.DS_Store
Thumbs.db

# Python
__pycache__/
*.pyc
.pytest_cache/
venv/
.env

# Logs
*.log
logs/
```

### Creating a .gitignore

```bash
# Create .gitignore in your project root
echo "# Secrets
.env
*.key
*.pem
credentials.json

# Python
__pycache__/
*.pyc
venv/

# IDE
.vscode/
.idea/

# OS
.DS_Store" > .gitignore

# Add and commit it
git add .gitignore
git commit -m "Add .gitignore for security"
```

### Checking If a File Is Ignored

```bash
# Check if a file would be ignored
git check-ignore -v filename.env

# See all ignored files
git status --ignored
```

## 🏛️ Vault Integration at LeoLab

### What is Vault?

HashiCorp Vault is our secure secret storage:
- Centralized secret management
- Access control and audit logs
- Automatic token rotation
- Encrypted storage

### How We Use Vault

```python
# Using the leoslab CLI tool (from command line):
# leoslab vault jira-token --token-type cloud
# leoslab vault get leoslab services/api/key

# In your Python code, you would retrieve these values
# from environment variables or config files
import os
jira_token = os.environ.get('JIRA_TOKEN')
api_key = os.environ.get('API_KEY')

# Never hardcode these values!
```

### Vault Best Practices

1. **Never share your Vault token**
2. **Use minimum required permissions**
3. **Access only what you need**
4. **Report any suspicious activity**

## 🚨 Security in CI/CD

### Automated Security Checks

Our CI/CD pipeline includes:

1. **Secret Scanning**: Detects accidentally committed secrets
2. **Dependency Scanning**: Checks for vulnerable packages
3. **Code Analysis**: Looks for security anti-patterns
4. **SAST**: Static Application Security Testing

### Understanding Security Warnings

When you see security warnings in your PR:

```
❌ Secret Scanner Failed
   Detected potential secret in config.py line 42
   
What to do:
1. Remove the secret from your code
2. Use Vault instead
3. If it's a false positive, add to allowlist
```

### Common Security Warnings

1. **Hardcoded Password**
   ```python
   # ❌ This triggers a warning
   password = "admin123"
   
   # ✅ Do this instead
   password = vault.get_secret("app/password")
   ```

2. **API Key in Code**
   ```python
   # ❌ Detected as secret
   headers = {"API-Key": "sk_live_abc123"}
   
   # ✅ Secure approach
   headers = {"API-Key": vault.get_secret("api/key")}
   ```

## 🎯 Practice Exercise 5: Security Audit

Let's practice secure coding:

### Step 1: Create a Project with Secrets (Wrong Way)

```bash
# Create a new branch
git checkout -b feature/security-practice

# Create a file with "secrets" (for practice only!)
cat > bad_example.py << 'EOF'
# THIS IS INTENTIONALLY BAD - DO NOT COPY!
DATABASE_URL = "postgresql://user:password@localhost/db"
API_KEY = "sk_test_123456789"
SECRET = "super_secret_value"
EOF

# Try to commit it
git add bad_example.py
git status
```

### Step 2: Fix It the Right Way

```bash
# Remove the bad file
rm bad_example.py

# Create the secure version
cat > good_example.py << 'EOF'
import os

# Get secrets from environment variables
# These would be set using the leoslab CLI tool:
# export DATABASE_URL=$(leoslab vault get leoslab database/url)
# export API_KEY=$(leoslab vault get leoslab services/api/key)
# export SECRET=$(leoslab vault get leoslab app/secret)

DATABASE_URL = os.environ.get('DATABASE_URL')
API_KEY = os.environ.get('API_KEY')
SECRET = os.environ.get('SECRET')

# Verify secrets are loaded
if not all([DATABASE_URL, API_KEY, SECRET]):
    raise ValueError("Missing required secrets. Use leoslab CLI to set them.")
EOF

# Create .gitignore
echo "# Never commit these
.env
*.key
secrets.json
config.local.py" > .gitignore

# Commit the secure version
git add good_example.py .gitignore
git commit -m "Add secure secret management example"
```

## 🛡️ Security Best Practices Checklist

Before every commit:

- [ ] No passwords or tokens in code
- [ ] No private keys or certificates
- [ ] .gitignore includes sensitive files
- [ ] Using Vault for all secrets
- [ ] Reviewed `git diff` for secrets
- [ ] No personal information in code

## 🔍 How to Check for Secrets

### Before Committing

```bash
# Review what you're about to commit
git diff --staged

# Look for patterns like:
# - password =
# - token =
# - api_key =
# - secret =
# - key =
```

### Using git-secrets (Optional Tool)

```bash
# Install git-secrets
brew install git-secrets

# Set up for a repo
git secrets --install
git secrets --register-aws

# Scan for secrets
git secrets --scan
```

## 🚫 What If You Accidentally Commit a Secret?

**DON'T PANIC, but ACT QUICKLY:**

1. **Tell Leo immediately**
2. **Do NOT try to "fix" it yourself**
3. **The secret needs to be rotated**
4. **We may need to clean Git history**

## 📊 Security Tools We Use

### 1. Vault
- Stores all our secrets
- Access through leoslab-toolkit
- Never bypass Vault

### 2. GitHub Security
- Secret scanning
- Dependabot alerts
- Code scanning

### 3. CI/CD Checks
- Bandit (Python security)
- Safety (dependency check)
- Custom secret patterns

## 📝 Module Summary

You've learned:
- ✅ Never commit secrets to Git
- ✅ How to use .gitignore effectively
- ✅ Vault integration for secure secrets
- ✅ Understanding security warnings
- ✅ Best practices for secure coding

## 🚀 What's Next?

Module 6 brings it all together with hands-on practice:
- Complete workflow from start to finish
- Real-world scenarios
- Troubleshooting common issues

## 📖 Security Quick Reference

### Red Flags in Code Reviews
```
password = "..."        ❌
api_key = "..."        ❌
token = "..."          ❌
secret = "..."         ❌
private_key = "..."    ❌
```

### Secure Alternatives
```bash
# Use leoslab CLI to get secrets
leoslab vault get leoslab path/to/secret  ✅
```

```python
# Use environment variables (set via leoslab CLI)
os.environ.get("VAR_NAME")  ✅

# Use config files (that are gitignored)
config.load("local.yaml")  ✅
```

---

**Remember**: Security is everyone's responsibility. When in doubt, ask!