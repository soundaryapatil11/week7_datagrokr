# Week 7 Mini Project: Full Gitflow Simulation

A beginner-friendly Git/GitHub mini project that demonstrates:

- `git init`, clone, add, commit, push, and pull
- Feature branches and Pull Requests (PRs)
- `develop`, `release`, and `hotfix` branches
- Merge commits and conflict resolution
- Git stash (`push`, `pop`, `apply`)
- Rebase vs merge, interactive rebase, and cherry-pick
- A pre-commit Git hook
- GitHub Actions CI to run tests automatically

The sample application is a tiny **Task Tracker** written in Python. The main learning goal is Git workflow, not Python complexity.

## 1. Requirements

Install:
- Git
- Python 3.10 or newer
- A GitHub account
- VS Code (recommended)

Verify installations:

```bash
git --version
python --version
```

## 2. Create your GitHub repository

1. On GitHub, create a **new empty repository** named `week7-gitflow-simulation`.
2. Do not initialize it with a README or `.gitignore` (this project already has those files).
3. Download and extract this project ZIP.
4. Open the extracted `week7_gitflow_simulation` folder in VS Code.

## 3. Initialize and push `main`

Run these commands in the project folder:

```bash
git init
git branch -M main
git add .
git commit -m "chore: initialize task tracker project"
git remote add origin https://github.com/YOUR-USERNAME/week7-gitflow-simulation.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

Set up the included pre-commit hook:

```bash
git config core.hooksPath .githooks
```

The hook blocks commits if Python files have syntax errors or trailing whitespace. If Git does not execute the hook on Windows, run Git Bash or ensure `.githooks/pre-commit` is executable in your environment.

## 4. Create the long-lived `develop` branch

```bash
git switch -c develop
git push -u origin develop
```

For this exercise, `main` represents production and `develop` is where completed features are integrated.

## 5. Feature branch → Pull Request → merge

Create a feature branch:

```bash
git switch develop
git pull
git switch -c feature/add-priority
```

Edit `app.py` and add a priority field to task creation, or use the included feature example below. Then:

```bash
git add app.py
git commit -m "feat: add task priority"
git push -u origin feature/add-priority
```

On GitHub:
1. Open a Pull Request from `feature/add-priority` **into `develop`**.
2. Review the diff and wait for the GitHub Actions check.
3. Merge the PR.
4. Delete the feature branch on GitHub if prompted.

Back in your terminal:

```bash
git switch develop
git pull
```

If you are completing this as a solo exercise, you can still create and merge your own PR. The purpose is to practice the review workflow.

## 6. Practice a merge conflict

Create a branch and edit the same line differently on two branches:

```bash
git switch develop
git switch -c feature/change-welcome
```

Change the welcome message in `app.py`, then commit:

```bash
git add app.py
git commit -m "feat: update welcome message"
git switch develop
```

Now change that same welcome-message line differently on `develop` and commit it. Then merge the feature branch:

```bash
git add app.py
git commit -m "docs: adjust welcome message on develop"
git merge feature/change-welcome
```

Git may report a conflict. Open the file and look for:

```text
<<<<<<< HEAD
your develop version
=======
your feature version
>>>>>>> feature/change-welcome
```

Edit the file to keep the desired final version and remove all conflict markers, then:

```bash
git add app.py
git commit
```

If no conflict occurs, make sure both branches changed the **same line** before trying again.

## 7. Practice stash

Make an uncommitted change in `app.py`, then run:

```bash
git stash push -m "work in progress"
git status
git stash list
git stash apply
```

`apply` restores the change but keeps the stash entry. To restore and remove the entry instead, use `git stash pop`. To discard the stash after checking it, use `git stash drop`.

## 8. Release branch → merge to `main` and `develop`

Start a release branch from `develop`:

```bash
git switch develop
git pull
git switch -c release/1.0.0
```

Update the version in `app.py` from `0.1.0` to `1.0.0`, run the tests, and commit:

```bash
python -m unittest discover -s tests -v
git add app.py
git commit -m "chore: prepare release 1.0.0"
git push -u origin release/1.0.0
```

Open a PR from `release/1.0.0` to `main` and merge it. Then tag the release:

```bash
git switch main
git pull
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

Merge the release changes back into `develop` so both branches contain the release version:

```bash
git switch develop
git pull
git merge --no-ff release/1.0.0 -m "merge: release 1.0.0 back into develop"
git push
```

## 9. Hotfix branch → merge back to both branches

Simulate a production bug fix:

```bash
git switch main
git pull
git switch -c hotfix/1.0.1
```

Make a small bug fix in `app.py` (for example, improve input validation), update the version to `1.0.1`, test, and commit:

```bash
python -m unittest discover -s tests -v
git add app.py
git commit -m "fix: validate task title and prepare 1.0.1"
git push -u origin hotfix/1.0.1
```

Open a PR from `hotfix/1.0.1` to `main`, then merge it. Tag the patch release:

```bash
git switch main
git pull
git tag -a v1.0.1 -m "Hotfix version 1.0.1"
git push origin v1.0.1
```

Merge the hotfix back into `develop`:

```bash
git switch develop
git pull
git merge --no-ff hotfix/1.0.1 -m "merge: hotfix 1.0.1 back into develop"
git push
```

## 10. Rebase vs merge

On a disposable branch, create a commit and rebase it on the latest `develop`:

```bash
git switch develop
git switch -c practice/rebase
# Make and commit a small change
git switch develop
git switch practice/rebase
git rebase develop
```

- **Merge** preserves the branch history and may create a merge commit.
- **Rebase** replays commits on top of another base and creates new commit IDs.
- Avoid rebasing shared/public branches unless the team has agreed on it.

## 11. Interactive rebase and cherry-pick

On a temporary branch, make two or three small commits, then:

```bash
git rebase -i HEAD~3
```

In the editor, try `reword`, `squash`, or `fixup`. Save and close the editor. Only do this on your own unshared practice branch.

To apply one specific commit from another branch:

```bash
git log --oneline
git cherry-pick COMMIT_HASH
```

Replace `COMMIT_HASH` with the actual commit ID. If conflicts occur, resolve them, `git add` the fixed files, and run `git cherry-pick --continue`.

## 12. GitHub Actions CI

The workflow at `.github/workflows/tests.yml` runs Python unit tests when code is pushed or a Pull Request is opened against `main` or `develop`. A green check means the tests passed; it does not replace code review.

## 13. Useful verification commands

```bash
git status
git branch -a
git log --oneline --graph --decorate --all
git remote -v
git tag
python -m unittest discover -s tests -v
python app.py
```

## Expected Gitflow diagram

```text
main      ─────────●──────────────●────────────●── (v1.0.0, v1.0.1)
                    \ release/1.0.0 \ hotfix/1.0.1
develop   ──●──●─────●──────────────●────────────●──
              \ feature/add-priority
```

## Submission checklist

- [ ] Repository pushed to GitHub
- [ ] `main` and `develop` branches exist
- [ ] Feature branch and PR merged into `develop`
- [ ] Release PR merged into `main`
- [ ] `v1.0.0` tag created
- [ ] Hotfix PR merged into `main`
- [ ] `v1.0.1` tag created
- [ ] Release and hotfix merged back into `develop`
- [ ] Pre-commit hook enabled
- [ ] GitHub Actions test workflow passes
- [ ] Screenshot of branch graph and merged PRs saved for submission
