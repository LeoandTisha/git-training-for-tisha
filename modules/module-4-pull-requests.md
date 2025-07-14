# Module 4: Pull Requests & Code Review

## 🎯 Learning Objectives

By the end of this module, you will:
- Understand what Pull Requests (PRs) are and why we use them
- Create PRs using GitHub CLI and web interface
- Link PRs to Jira tickets
- Participate in code reviews
- Understand PR requirements and checks

## 📚 What is a Pull Request?

A Pull Request (PR) is:
- A request to merge your feature branch into another branch (usually main)
- A place for code review and discussion
- A safety gate before code goes to production
- A record of what changed and why

### Why Pull Requests?

1. **Code Review**: Others check your work for bugs, style, and improvements
2. **Discussion**: Ask questions, get feedback, share knowledge
3. **Quality Gate**: Automated tests run before merging
4. **Documentation**: PRs document what changed and why

## 💻 Creating a Pull Request

### Method 1: GitHub CLI (Recommended)

```bash
# After pushing your feature branch
git push -u origin feature/your-feature

# Create PR with GitHub CLI
gh pr create --title "Add user authentication feature" \
  --body "## Summary
  
  Implements secure user authentication using Vault.
  
  ## Changes
  - Add VaultAuth class
  - Integrate with existing login flow
  - Add unit tests
  
  ## Jira Ticket
  INFRA-25
  
  ## Testing
  - All tests pass
  - Manual testing completed"
```

### Method 2: GitHub Web Interface

1. Go to the repository on GitHub
2. Click "Pull requests" tab
3. Click "New pull request"
4. Select your feature branch
5. Fill in title and description
6. Click "Create pull request"

## 📋 LeoLab PR Requirements

Every PR must include:

### ✅ PR Title Format
```
[JIRA-TICKET] Brief description

Examples:
[INFRA-25] Add Vault authentication to login flow
[WM-42] Fix responsive design on mobile devices
```

### ✅ PR Description Template

```markdown
## Summary
Brief overview of what this PR does

## Changes
- Specific change 1
- Specific change 2
- Specific change 3

## Jira Ticket
[INFRA-25](https://leoslab.atlassian.net/browse/INFRA-25)

## Testing
- [ ] All unit tests pass
- [ ] Manual testing completed
- [ ] No security vulnerabilities

## Screenshots (if applicable)
Add screenshots for UI changes

## Notes
Any additional context for reviewers
```

### ✅ Required Checks

Before merging, these must pass:
1. **All tests green**: Automated tests must pass
2. **Security scan clean**: No vulnerabilities detected
3. **Code quality**: Linting and formatting checks
4. **No secrets**: Secret scanning must pass
5. **Approved review**: At least one approval

## 🔗 Linking to Jira

### Automatic Linking

Include the Jira ticket number in:
- PR title: `[INFRA-25] Add feature`
- PR description: `Jira: INFRA-25`
- Commit messages: `INFRA-25: Fix bug`

This automatically:
- Links the PR in Jira
- Updates ticket status
- Shows progress to stakeholders

## 👥 Code Review Process

### As the PR Author

1. **Create descriptive PR**: Help reviewers understand your changes
2. **Respond to feedback**: Address comments promptly
3. **Update your PR**: Push new commits to the same branch
4. **Re-request review**: After making changes

### As a Reviewer

1. **Understand the goal**: Read the PR description and Jira ticket
2. **Check the code**: Look for bugs, style, security issues
3. **Test if needed**: Pull the branch and test locally
4. **Provide feedback**: Be constructive and specific
5. **Approve or request changes**: Use GitHub's review feature

### Review Comments Examples

Good feedback:
- ✅ "Consider using VaultClient here for consistency with our other services"
- ✅ "This could throw an exception if the API is down. Should we add error handling?"
- ✅ "Great implementation! One suggestion: we could cache this result for better performance"

Less helpful:
- ❌ "This is wrong"
- ❌ "I don't like this"
- ❌ "Change this"

## 🎯 Practice Exercise 4: Your First PR

### Step 1: Create a Feature Branch

```bash
git checkout main
git pull origin main
git checkout -b feature/tisha-first-pr
```

### Step 2: Make Changes

```bash
echo "# Tisha's First PR

This is practice for creating pull requests at LeoLab.

## What I Learned
- Creating feature branches
- Writing good commit messages
- Following LeoLab standards" > first-pr.md

git add first-pr.md
git commit -m "Add documentation for PR practice

- Create first-pr.md with learning summary
- Practice proper commit message format
- Prepare for PR creation

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

### Step 3: Push and Create PR

```bash
# Push the branch
git push -u origin feature/tisha-first-pr

# Create PR
gh pr create --title "[TRAINING-1] Tisha's first pull request" \
  --body "## Summary
  
  Practice creating a pull request following LeoLab standards.
  
  ## Changes
  - Add first-pr.md documentation file
  - Practice proper PR format
  
  ## Jira Ticket
  TRAINING-1
  
  ## Testing
  - [x] File renders correctly
  - [x] No sensitive information"
```

## 🔄 The PR Lifecycle

```
1. Create Feature Branch
   ↓
2. Make Changes & Commit
   ↓
3. Push to GitHub
   ↓
4. Create Pull Request
   ↓
5. Automated Checks Run
   ↓
6. Code Review
   ↓
7. Address Feedback
   ↓
8. Get Approval
   ↓
9. Merge to Main
   ↓
10. Delete Feature Branch
```

## 🚨 Common PR Mistakes

1. **PR Too Large**
   - Keep PRs focused and small
   - Easier to review and less risky

2. **No Jira Link**
   - Always link to the Jira ticket
   - Provides context and tracking

3. **Ignoring CI Failures**
   - Fix all test failures before requesting review
   - Don't ignore security warnings

4. **Not Responding to Feedback**
   - Engage with reviewers
   - Update PR based on suggestions

## 📊 Understanding PR Checks

### GitHub Status Checks

You'll see status indicators:
- ✅ **Green checkmark**: All checks passed
- ❌ **Red X**: Something failed
- 🟡 **Yellow dot**: Checks are running

### Common Check Types

1. **Unit Tests**: Your code's tests
2. **Integration Tests**: How your code works with others
3. **Security Scan**: Looking for vulnerabilities
4. **Code Quality**: Style and formatting
5. **Build**: Can the project build successfully

## 📝 Module Summary

You've learned:
- ✅ What Pull Requests are and why we use them
- ✅ How to create PRs with proper format
- ✅ Linking PRs to Jira tickets
- ✅ Participating in code reviews
- ✅ Understanding PR requirements and checks

## 🚀 What's Next?

Module 5 covers security and best practices:
- Keeping secrets out of code
- Using .gitignore
- Security scanning
- Vault integration

## 📖 PR Quick Reference

```bash
# Create PR with GitHub CLI
gh pr create --title "[TICKET-NUM] Description" --body "..."

# Check PR status
gh pr status

# View PR in browser
gh pr view --web

# List all PRs
gh pr list
```

### PR Checklist
- [ ] Branch created from latest main
- [ ] Commits have proper messages
- [ ] PR title includes Jira ticket
- [ ] Description explains changes
- [ ] All tests pass
- [ ] No secrets in code
- [ ] Ready for review

---

**Remember**: PRs are conversations! Don't be afraid to ask questions or discuss different approaches.