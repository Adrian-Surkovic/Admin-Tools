[ ] Test backup
[ ] Add auto‑update setting (default off)
[ ] Implement optional auto update via ```bash git pull```
[ ] Implement version tags for rollback

Pipeline for 7:
```bash
git add .
git commit -m "vX.X.X"
git tag vX.X.X
git push
git push --tags
```