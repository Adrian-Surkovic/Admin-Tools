1. [x] Set up modules
2. [X] Set up main services
3. [X] Add FixWin11Audio to SystemRepair
4. [ ] Ensure system clean does not loop DISM percentages
5. [X] Ensure modular structure not compromised
6. [ ] Avoid unnecessary optimizations
7. [ ] Test backup
8. [ ] Add settings.json
9. [ ] Add auto‑update setting (default off)
10. [ ] Implement optional auto update via ```bash git pull```
10. [ ] Implement version tags for rollback
11. [ ] Show enabled/disabled status for startup apps

Pipeline for 7:
```bash
git add .
git commit -m "vX.X.X"
git tag vX.X.X
git push
git push --tags
```