@echo off
chcp 65001 >nul
echo 🔧 音效修复版打包
echo ==================
echo.

echo 📦 清理旧文件...
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build

echo 📝 使用修复版主程序打包...
pyinstaller --onefile --windowed --add-data "images;images" --add-data "sounds;sounds" --add-data "leaderboard.json;." --name "AlienInvasion" alien_invasion_fixed.py

echo.
echo 🎉 打包完成!
echo 📁 文件位置: dist\AlienInvasion.exe
echo 📏 文件大小:

if exist "dist\AlienInvasion.exe" (
    for %%F in ("dist\AlienInvasion.exe") do echo    %%~zF KB
    echo.
    echo ✅ 修复说明:
    echo    1. 使用多重路径检测资源文件
    echo    2. 详细的错误报告和调试信息
    echo    3. 异常安全处理
    echo.
    echo 🔊 测试音效:
    echo    - 空格键: 应该听到射击声
    echo    - 击中敌人: 应该听到爆炸声
    echo    - 启动后: 应该听到背景音乐
    echo    - M键: 可以暂停/恢复音乐
    echo.
) else (
    echo ❌ 打包失败，请检查错误信息
)

echo 💡 运行测试:
echo    双击 dist\AlienInvasion.exe
echo.

pause