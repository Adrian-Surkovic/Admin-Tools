[ ] Test restore point
[ ] Add auto‑update setting (default off)
[ ] Add backup location setting
[ ] Implement optional auto update via ```bash git pull```
[ ] Implement version tags for rollback
[x] Restored cls
[x] Added UI restart module
[x] Layed groundwork for update command and auto update setting
[x] Tested file backup

Pipeline for tags:
```bash
git add .
git commit -m "vX.X.X"
git tag vX.X.X
git push
git push --tags
```