@echo off
chcp 65001 >nul 2>&1
title 外星人入侵 - 创建便携版

echo 🎮 创建便携版游戏...
echo ==================
echo.

REM 检查dist目录和exe文件
if not exist "dist\AlienInvasion.exe" (
    echo ❌ 错误: 未找到游戏程序!
    echo 请先运行 build_sound_fixed.bat 来生成exe文件
    pause
    exit /b
)

echo ✅ 找到游戏程序: dist\AlienInvasion.exe

REM 创建游戏文件夹
set GAME_FOLDER=AlienInvasion_Portable
if exist "%GAME_FOLDER%" rmdir /s /q "%GAME_FOLDER%"
mkdir "%GAME_FOLDER%"

echo 📁 创建游戏文件夹: %GAME_FOLDER%

REM 复制主程序
copy "dist\AlienInvasion.exe" "%GAME_FOLDER%\" >nul
echo ✅ 复制主程序

REM 复制图像文件夹
if exist "images" (
    xcopy "images" "%GAME_FOLDER%\images" /E /I /Y >nul
    echo ✅ 复制图像文件
)

REM 复制音效文件夹
if exist "sounds" (
    xcopy "sounds" "%GAME_FOLDER%\sounds" /E /I /Y >nul
    echo ✅ 复制音效文件
)

REM 复制数据文件
if exist "leaderboard.json" (
    copy "leaderboard.json" "%GAME_FOLDER%\" >nul
    echo ✅ 复制排行榜数据
)

REM 创建启动脚本
echo @echo off > "%GAME_FOLDER%\开始游戏.bat"
echo chcp 65001 ^>nul 2^>^&1 >> "%GAME_FOLDER%\开始游戏.bat"
echo title 外星人入侵 - 太空战争 >> "%GAME_FOLDER%\开始游戏.bat"
echo color 0A >> "%GAME_FOLDER%\开始游戏.bat"
echo echo. >> "%GAME_FOLDER%\开始游戏.bat"
echo echo     ╔══════════════════════════════════════╗ >> "%GAME_FOLDER%\开始游戏.bat"
echo echo     ║          外星人入侵 - 太空战争          ║ >> "%GAME_FOLDER%\开始游戏.bat"
echo echo     ║                                        ║ >> "%GAME_FOLDER%\开始游戏.bat"
echo echo     ║  🚀 正在启动游戏...                    ║ >> "%GAME_FOLDER%\开始游戏.bat"
echo echo     ╚══════════════════════════════════════╝ >> "%GAME_FOLDER%\开始游戏.bat"
echo echo. >> "%GAME_FOLDER%\开始游戏.bat"
echo echo 🎮 游戏控制 >> "%GAME_FOLDER%\开始游戏.bat"
echo echo ┌─────────────────────────────────────┐ >> "%GAME_FOLDER%\开始游戏.bat"
echo echo │ 方向键: 移动飞船            │ >> "%GAME_FOLDER%\开始游戏.bat"
echo echo │ 空格键: 发射子弹            │ >> "%GAME_FOLDER%\开始游戏.bat"
echo echo │ M键: 暂停/恢复音乐          │ >> "%GAME_FOLDER%\开始游戏.bat"
echo echo │ L键: 查看排行榜            │ >> "%GAME_FOLDER%\开始游戏.bat"
echo echo │ ESC键: 返回/退出             │ >> "%GAME_FOLDER%\开始游戏.bat"
echo echo └─────────────────────────────────────┘ >> "%GAME_FOLDER%\开始游戏.bat"
echo echo. >> "%GAME_FOLDER%\开始游戏.bat"
echo echo 🎵 音效说明 >> "%GAME_FOLDER%\开始游戏.bat"
echo echo • 背景音乐自动播放 >> "%GAME_FOLDER%\开始游戏.bat"
echo echo • 射击和爆炸音效完整 >> "%GAME_FOLDER%\开始游戏.bat"
echo echo • 游戏结束音效提示 >> "%GAME_FOLDER%\开始游戏.bat"
echo echo. >> "%GAME_FOLDER%\开始游戏.bat"
echo echo 🚀 启动游戏... >> "%GAME_FOLDER%\开始游戏.bat"
echo echo. >> "%GAME_FOLDER%\开始游戏.bat"
echo echo 💡 按任意键开始游戏... >> "%GAME_FOLDER%\开始游戏.bat"
echo pause ^> nul >> "%GAME_FOLDER%\开始游戏.bat"
echo start "" "AlienInvasion.exe" >> "%GAME_FOLDER%\开始游戏.bat"
echo echo. >> "%GAME_FOLDER%\开始游戏.bat"
echo echo 🎮 享受游戏时光! >> "%GAME_FOLDER%\开始游戏.bat"

echo ✅ 创建启动脚本

REM 创建说明文件
echo 外星人入侵 - 太空战争 > "%GAME_FOLDER%\游戏说明.txt"
echo ======================= >> "%GAME_FOLDER%\游戏说明.txt"
echo. >> "%GAME_FOLDER%\游戏说明.txt"
echo 🎮 运行方法: >> "%GAME_FOLDER%\游戏说明.txt"
echo 1. 双击 "开始游戏.bat" 启动游戏 >> "%GAME_FOLDER%\游戏说明.txt"
echo 2. 或者双击 "AlienInvasion.exe" 直接运行 >> "%GAME_FOLDER%\游戏说明.txt"
echo. >> "%GAME_FOLDER%\游戏说明.txt"
echo 📁 文件说明: >> "%GAME_FOLDER%\游戏说明.txt"
echo • AlienInvasion.exe - 主程序 >> "%GAME_FOLDER%\游戏说明.txt"
echo • images/ - 图像资源文件夹 >> "%GAME_FOLDER%\游戏说明.txt"
echo • sounds/ - 音效资源文件夹 >> "%GAME_FOLDER%\游戏说明.txt"
echo • leaderboard.json - 排行榜数据文件 >> "%GAME_FOLDER%\游戏说明.txt"
echo • 开始游戏.bat - 启动脚本 >> "%GAME_FOLDER%\游戏说明.txt"
echo. >> "%GAME_FOLDER%\游戏说明.txt"
echo 🎮 游戏控制: >> "%GAME_FOLDER%\游戏说明.txt"
echo • 方向键: 控制飞船四向移动 >> "%GAME_FOLDER%\游戏说明.txt"
echo • 空格键: 发射子弹 >> "%GAME_FOLDER%\游戏说明.txt"
echo • M键: 暂停/恢复背景音乐 >> "%GAME_FOLDER%\游戏说明.txt"
echo • L键: 打开排行榜查看 >> "%GAME_FOLDER%\游戏说明.txt"
echo • ESC键: 返回或退出 >> "%GAME_FOLDER%\游戏说明.txt"
echo. >> "%GAME_FOLDER%\游戏说明.txt"
echo 🎵 音效系统: >> "%GAME_FOLDER%\游戏说明.txt"
echo • 背景音乐: 游戏开始时自动播放 >> "%GAME_FOLDER%\游戏说明.txt"
echo • 射击音效: 空格键发射时播放 >> "%GAME_FOLDER%\游戏说明.txt"
echo • 爆炸音效: 击中敌人时播放 >> "%GAME_FOLDER%\游戏说明.txt"
echo • 游戏结束音效: 游戏结束时播放 >> "%GAME_FOLDER%\游戏说明.txt"
echo. >> "%GAME_FOLDER%\游戏说明.txt"
echo 🏆 游戏目标: >> "%GAME_FOLDER%\游戏说明.txt"
echo • 消灭尽可能多的外星人 >> "%GAME_FOLDER%\游戏说明.txt"
echo • 获得最高分 >> "%GAME_FOLDER%\游戏说明.txt"
echo • 生存更长时间 >> "%GAME_FOLDER%\游戏说明.txt"
echo. >> "%GAME_FOLDER%\游戏说明.txt"
echo 💡 提示: >> "%GAME_FOLDER%\游戏说明.txt"
echo • 游戏会自动保存你的分数 >> "%GAME_FOLDER%\游戏说明.txt"
echo • 排行榜文件会在同一目录创建 >> "%GAME_FOLDER%\游戏说明.txt"
echo • 3条生命，被击中后有1秒无敌时间 >> "%GAME_FOLDER%\游戏说明.txt"

echo ✅ 创建说明文件

REM 检查结果
set TOTAL_FILES=0
if exist "%GAME_FOLDER%\AlienInvasion.exe" set /a TOTAL_FILES+=1
if exist "%GAME_FOLDER%\images\ship.bmp" set /a TOTAL_FILES+=1
if exist "%GAME_FOLDER%\sounds\shoot.wav" set /a TOTAL_FILES+=1
if exist "%GAME_FOLDER%\leaderboard.json" set /a TOTAL_FILES+=1

echo.
echo 📊 便携版创建完成!
echo 📁 游戏文件夹: %GAME_FOLDER%
echo 📏 包含文件数量: %TOTAL_FILES%/4

if %TOTAL_FILES% GEQ 4 (
    echo ✅ 所有文件完整
    echo.
    echo 🎮 运行方法:
    echo   1. 进入 %GAME_FOLDER% 文件夹
    echo   2. 双击 "开始游戏.bat"
    echo.
    echo 📤 可以将整个 %GAME_FOLDER% 文件夹复制给朋友!
) else (
    echo ⚠️ 警告: 部分文件缺失
)

echo.
pause