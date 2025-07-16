# Module 2: GitHub Basics

## 🎯 Learning Objectives

By the end of this module, you will:
- Understand the difference between Git and GitHub
- Know how to clone repositories
- Push your local changes to GitHub
- Navigate the GitHub web interface
- Understand the concept of remote repositories

## 📚 Git vs GitHub

### Git
- **What**: Version control software installed on your computer
- **Where**: Lives on your local machine
- **Purpose**: Tracks changes in your code

### GitHub
- **What**: A website/service that hosts Git repositories
- **Where**: Cloud-based (github.com)
- **Purpose**: 
  - Store your Git repos online
  - Collaborate with others
  - Share code publicly or privately
  - Track issues and projects

Think of it this way:
- Git = The technology
- GitHub = A place to store and share Git repositories

## 🔑 Key Concepts

### Remote Repository
A remote repository is a Git repo hosted on the internet (like on GitHub). You can:
- **Push**: Send your local commits to the remote
- **Pull**: Get changes from the remote to your local
- **Clone**: Copy a remote repo to your local machine

### Origin
"Origin" is the default name Git gives to the remote repository you cloned from. Think of it as a nickname for the GitHub URL.

## 💻 Working with GitHub

### Cloning a Repository

Cloning creates a local copy of a remote repository:

```bash
# Clone a repository (example URL - replace with actual)
git clone https://github.com/username/repository-name.git

# This creates a new directory with the repository name
cd repository-name

# Check the remote
git remote -v
```

### Connecting Local Repo to GitHub

If you already have a local repo and want to connect it to GitHub:

```bash
# Add a remote repository (example URL - replace with actual)
git remote add origin https://github.com/username/your-repo-name.git

# Verify the remote was added
git remote -v
```

### Pushing Changes to GitHub

```bash
# First, make sure you have commits
git add .
git commit -m "Add new feature"

# Push to GitHub
git push origin main

# For the first push, you might need:
git push -u origin main
```

### Pulling Changes from GitHub

```bash
# Get latest changes from GitHub
git pull origin main

# Or simply (if you've set upstream):
git pull
```

## 🖥️ GitHub Web Interface Tour

### Repository Page Components

1. **Code Tab**: Browse files, see recent commits
2. **Issues**: Track bugs, features, and tasks
3. **Pull Requests**: Review and discuss code changes
4. **Actions**: Automated workflows (CI/CD)
5. **Settings**: Repository configuration

### Key Features to Know

- **Clone button**: Get the repository URL
- **README.md**: Displays on the main page
- **Commits history**: See all changes
- **Branches**: Switch between different versions
- **Contributors**: See who's working on the project

## 🎯 Practice Exercise 2: Your First GitHub Repo

### Part A: Using GitHub Web Interface

**Practice Repository**: https://github.com/LeoandTisha/tisha-git-practice

1. Navigate to the repository URL above
2. Click the green "Code" button
3. Copy the HTTPS URL

### Part B: Clone and Modify

```bash
# 1. Clone the repository
git clone https://github.com/LeoandTisha/tisha-git-practice.git
cd tisha-git-practice

# 2. Create a new file
echo "Hello from Tisha!" > tisha.txt

# 3. Add and commit
git add tisha.txt
git commit -m "Add Tisha's greeting file"

# 4. Push to GitHub
git push origin main
```

### Part C: Verify on GitHub

1. Go back to the GitHub repository page
2. Refresh the page
3. You should see your new file!

## 🔐 Authentication with GitHub

### Setting up Authentication

Since GitHub requires authentication for pushing:

```bash
# When you push, GitHub will ask for:
# Username: your-github-username
# Password: your-personal-access-token (NOT your password!)
```

For LeoLab repositories, we'll set you up with proper access.

## 📊 Understanding Git Push/Pull

### The Flow
```
Local Repo ← pull ← GitHub (Remote)
Local Repo → push → GitHub (Remote)
```

### Best Practices
1. **Always pull before starting work**: `git pull`
2. **Commit often, push regularly**: Don't wait too long
3. **Write clear commit messages**: Others will read them

## 🚨 Common GitHub Mistakes

1. **Forgetting to pull before pushing**
   - Can cause conflicts
   - Always: pull → work → commit → push

2. **Pushing to the wrong branch**
   - Double-check with `git branch`
   - We'll cover branches in detail next module

3. **Committing sensitive information**
   - NEVER commit passwords, tokens, or secrets
   - Use `.gitignore` for files that shouldn't be tracked

## 🔍 Troubleshooting

### "Repository not found" Error
- Check the URL is correct
- Verify you have access to the repository

### "Authentication failed"
- Make sure you're using a Personal Access Token, not your password
- Check your GitHub username is correct

### "Updates were rejected"
- Someone else pushed changes before you
- Solution: `git pull` first, then push again

## 📝 Module Summary

You've learned:
- ✅ The difference between Git and GitHub
- ✅ How to clone repositories
- ✅ How to push and pull changes
- ✅ Navigate GitHub's web interface
- ✅ Basic remote repository concepts

## 🚀 What's Next?

Module 3 will teach you the LeoLab-specific workflow:
- Our branching strategy
- Proper commit message format
- How we organize our projects

## 📖 Quick Reference

```bash
# Clone a repo
git clone <url>

# Add remote to existing repo
git remote add origin <url>

# Push changes
git push origin main

# Pull changes
git pull origin main

# Check remotes
git remote -v
```

## 🎉 Congratulations!

You can now:
- Work with both local and remote repositories
- Share your code on GitHub
- Collaborate with the LeoLab team

Practice by:
1. Creating your own repository on GitHub
2. Cloning it locally
3. Making changes and pushing them
4. Viewing your changes on GitHub.com

---

**Next Module**: Learn the LeoLab way of using Git and GitHub!