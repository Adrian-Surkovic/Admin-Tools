[ ] Test restore point
[ ] Add auto‑update setting (default off)
[ ] Add backup location setting
[ ] Implement optional auto update via ```bash git pull```



Pipeline for tags:
```bash
git add .
git commit -m "vX.X.X"
git tag vX.X.X
git push
git push --tags
```