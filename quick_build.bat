@echo off
chcp 65001 >nul
echo 🚀 快速打包游戏
echo ================

echo 📦 快速打包...
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build

pyinstaller --onefile --windowed --add-data "images;images" --add-data "sounds;sounds" --add-data "leaderboard.json;." alien_invasion.py

if exist "dist\alien_invasion.exe" (
    echo ✅ 快速打包完成!
    echo 📁 文件: dist\alien_invasion.exe
) else (
    echo ❌ 打包失败
)

pause