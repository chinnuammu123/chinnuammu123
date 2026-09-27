# GitHub Basics – A Beginner's Guide

## 1. The key words
| Word | Meaning |
|------|---------|
| **Git** | A tool on your computer that records the history of your files. |
| **GitHub** | A website that stores Git projects online so you can share them. |
| **Repository (repo)** | A project folder tracked by Git – like this one. |
| **Commit** | A saved snapshot of your changes, with a message describing them. |
| **Branch** | A separate line of work. `main` is the default; you make new branches to try things safely. |
| **Push** | Upload your commits from your computer to GitHub. |
| **Pull** | Download new commits from GitHub to your computer. |
| **Clone** | Copy a GitHub repo to your computer for the first time. |
| **Pull Request (PR)** | A request to merge one branch into another, where others can review the changes. |
| **Fork** | Your own copy of someone else's repo, so you can change it. |
| **Issue** | A to-do item, bug report, or idea tracked on GitHub. |

## 2. One-time setup
```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
```

## 3. The everyday workflow
```bash
git clone https://github.com/chinnuammu123/chinnuammu123.git   # 1. copy the repo (first time only)
cd chinnuammu123

git checkout -b my-new-feature      # 2. make a branch for your work
# ...edit files...
git status                          # 3. see what changed
git add .                           # 4. stage the changes
git commit -m "Add calculator project"   # 5. save a snapshot
git push -u origin my-new-feature   # 6. upload to GitHub
```
7. On GitHub, click **"Compare & pull request"**, write what you changed, and create the PR.
8. Review it, then click **"Merge pull request"**. Your change is now on `main`.
9. Back on your computer: `git checkout main && git pull`.

## 4. Useful commands
```bash
git log --oneline      # show history
git diff               # show unsaved changes
git branch             # list branches
git restore file.txt   # throw away changes to a file
```

## 5. No terminal? Use the website
- **Add file → Create new file** to write a file right in the browser.
- **Add file → Upload files** to drag and drop files.
- Every save in the browser is a commit.

## 6. Practice exercises
1. Edit this README on GitHub and commit the change.
2. Create an **Issue** called "Build a calculator" and add a checklist to it.
3. Make a branch, add a project, and open a **Pull Request** that says `Closes #1` –
   merging it closes the issue automatically.
4. Turn on **GitHub Pages** (Settings → Pages) to host an HTML project for free.
5. Star ⭐ and fork a beginner-friendly repo, such as `firstcontributions/first-contributions`,
   and follow its steps to make your first open-source contribution.
