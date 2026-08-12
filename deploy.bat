@echo off
git add .
set /p msg="更新内容: "
git commit -m "%msg%"
git push origin main
echo ===== 更新已推送到 GitHub，Cloudflare 正在部署中... =====
pause