# Module 1: Git Fundamentals

## 🎯 Learning Objectives

By the end of this module, you will:
- Understand what Git is and why we use it at LeoLab
- Know the difference between Git and GitHub
- Understand core concepts: repositories, commits, branches
- Be able to use essential Git commands
- Have created your first local repository

## 📚 What is Git?

Git is a **version control system** - think of it as a powerful "save game" system for your code. Just like in a video game where you can save your progress and go back to earlier saves, Git lets you:

- Save snapshots of your work (called "commits")
- Go back to any previous version
- Work on different features without breaking the main code
- Collaborate with others without conflicts

### Why LeoLab Uses Git

1. **Track Changes**: Every change is recorded with who made it and why
2. **Collaboration**: Multiple people can work on the same project
3. **Backup**: Your code is safe even if your computer crashes
4. **Experimentation**: Try new ideas without breaking working code
5. **Accountability**: Know exactly what changed and when

## 🔑 Core Concepts

### Repository (Repo)
A repository is like a project folder that Git tracks. It contains:
- All your project files
- The complete history of changes
- Information about branches and commits

### Commit
A commit is a snapshot of your project at a specific point in time. Think of it as:
- A "save point" in your project
- Contains: what changed, who changed it, when, and why
- Has a unique ID (hash) like `a3f4b7c`

### Branch
A branch is an independent line of development. Imagine:
- The main branch (`main`) is your stable, working code
- Feature branches are where you develop new features
- You can switch between branches instantly

## 💻 Essential Git Commands

### Setting Up Git

First, tell Git who you are:
```bash
git config --global user.name "Tisha"
git config --global user.email "tisha@leoandtisha.net"
```

**Note**: Your Vault access has already been set up. You'll learn more about using Vault for secrets in Module 5.

### Creating Your First Repository

```bash
# Create a new directory for your project
mkdir my-first-repo
cd my-first-repo

# Initialize Git in this directory
git init

# You should see: "Initialized empty Git repository"
```

### Basic Workflow Commands

```bash
# 1. Check the status of your repository
git status

# 2. Add files to staging area (prepare to commit)
git add filename.txt
# Or add all files:
git add .

# 3. Commit your changes with a message
git commit -m "Add initial project files"

# 4. View your commit history
git log
# Or a simplified view:
git log --oneline
```

## 🎯 Practice Exercise 1: Your First Repository

Let's create a simple project to practice:

```bash
# 1. Create a new directory
mkdir tisha-practice
cd tisha-practice

# 2. Initialize Git
git init

# 3. Create a README file
echo "# Tisha's Git Practice" > README.md

# 4. Check status (file should be untracked)
git status

# 5. Add the file to staging
git add README.md

# 6. Check status again (file should be staged)
git status

# 7. Commit the file
git commit -m "Initial commit: Add README"

# 8. View your commit
git log
```

## 🚨 Common Mistakes to Avoid

1. **Forgetting to add files before committing**
   - Always run `git status` to check what will be committed

2. **Committing too much at once**
   - Make small, focused commits
   - Each commit should do one thing

3. **Bad commit messages**
   - ❌ "fixed stuff"
   - ✅ "Fix login error when password contains special characters"

## 📊 Understanding Git Status

When you run `git status`, files can be in different states:

- **Untracked**: New files Git doesn't know about yet
- **Modified**: Files that have changed since last commit
- **Staged**: Files ready to be committed
- **Committed**: Files safely stored in Git history

## 🔍 Checking Your Understanding

### Quick Quiz
1. What command initializes a new Git repository?
2. What's the difference between `git add` and `git commit`?
3. How do you check which files have been modified?

### Answers
1. `git init`
2. `git add` stages changes (prepares them), `git commit` saves them permanently
3. `git status`

## 📝 Module Summary

You've learned:
- ✅ What Git is and why we use it
- ✅ Core concepts: repositories, commits, branches
- ✅ Essential commands: init, add, commit, status, log
- ✅ How to create your first repository

## 🚀 What's Next?

In Module 2, you'll learn about GitHub and how to work with remote repositories. Before moving on:

1. Practice creating at least 2 more repositories
2. Make multiple commits in each
3. Get comfortable with `git status` and `git log`

## 📖 Additional Resources

- [Official Git Tutorial](https://git-scm.com/docs/gittutorial)
- [Visual Git Reference](https://marklodato.github.io/visual-git-guide/index-en.html)
- Ask Leo if you get stuck!

---

**Remember**: Git might feel confusing at first, but with practice it becomes second nature. Every developer started where you are now!