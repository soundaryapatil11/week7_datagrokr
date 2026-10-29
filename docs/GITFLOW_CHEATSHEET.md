# Gitflow Cheat Sheet

| Branch | Purpose | Typical destination |
|---|---|---|
| `main` | Production-ready code | Release / hotfix PRs |
| `develop` | Integration branch | Feature PRs |
| `feature/<name>` | New functionality | `develop` |
| `release/<version>` | Stabilize a release | `main`, then back to `develop` |
| `hotfix/<version>` | Urgent production fix | `main`, then back to `develop` |

## Core commands

```bash
git status
git switch -c feature/example
git add .
git commit -m "feat: describe change"
git push -u origin feature/example
git log --oneline --graph --decorate --all
git stash push -m "temporary work"
git stash pop
git merge --no-ff branch-name
git rebase develop
git cherry-pick COMMIT_HASH
git reflog
git bisect start
```

Use `git bisect` to find a bug-introducing commit:
1. `git bisect start`
2. `git bisect bad` (current broken commit)
3. `git bisect good GOOD_COMMIT_HASH`
4. Test each selected commit, then mark `git bisect good` or `git bisect bad`.
5. `git bisect reset` when finished.

Use `git reflog` to inspect recent movements of `HEAD` and recover a branch/commit reference when possible. Be careful with destructive commands.
