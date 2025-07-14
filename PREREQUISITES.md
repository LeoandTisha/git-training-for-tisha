# Prerequisites for Git Training

Before starting the training, make sure you have the following tools installed and configured.

## Required Tools

### 1. Git
Check if Git is installed:
```bash
git --version
```

If not installed:
- **macOS**: Git comes pre-installed, or use `brew install git`
- **Linux**: `sudo apt-get install git` or `sudo yum install git`

### 2. GitHub CLI (gh)
Check if GitHub CLI is installed:
```bash
gh --version
```

If not installed:
- **macOS**: `brew install gh`
- **Linux**: Follow [GitHub CLI installation guide](https://github.com/cli/cli#installation)

After installation, authenticate:
```bash
gh auth login
```

### 3. Vault CLI
This should already be installed from your Vault setup:
```bash
vault --version
```

If not, run the setup script Leo provided:
```bash
~/setup-vault-for-tisha.sh
```

### 4. Text Editor
You'll need a text editor. VS Code is recommended:
- Download from [code.visualstudio.com](https://code.visualstudio.com)

### 5. Terminal Access
- **macOS**: Use Terminal.app or iTerm2
- **Linux**: Use your default terminal

## Account Setup

### GitHub Account
- Leo will provide access to the LeoLab GitHub organization
- Make sure you can access https://github.com/leoslab

### Jira Access
- Ensure you can log into https://leoslab.atlassian.net
- Your training progress will be tracked here

### Practice Repository
- Leo will create a practice repository for you
- He'll provide the URL when you reach Module 2

## Optional Tools

These are mentioned in the training but not required:

### git-secrets (Module 5)
For additional security scanning:
```bash
brew install git-secrets
```

## Verification Checklist

Run these commands to verify your setup:

```bash
# Check Git
git --version

# Check GitHub CLI
gh --version
gh auth status

# Check Vault
vault --version
vault status

# Check your Git configuration
git config --get user.name
git config --get user.email
```

If any of these fail, resolve the issue before starting the training.

## Getting Help

If you encounter issues during setup:
1. Check the error message carefully
2. Ask Leo for assistance
3. Document any issues for future reference

---

**Ready to start?** Proceed to [Module 1: Git Fundamentals](modules/module-1-git-fundamentals.md)!