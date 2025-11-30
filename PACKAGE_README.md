# 📦 游戏打包指南

## 🎮 打包说明

本游戏已经配置好了自动打包脚本，可以轻松打包成独立的可执行文件，无需安装Python环境即可运行。

## 🚀 快速打包

### 🎯 方法一：Windows批处理脚本（推荐）
```bash
# 完整打包（音效修复版）
build_sound_fixed.bat

# 创建便携版
create_portable.bat
```

### 🐍 方法二：Python脚本（跨平台）
```bash
# 跨平台打包脚本
python build_game.py
```

### 🔧 方法三：手动使用PyInstaller
```bash
# 安装PyInstaller（如果未安装）
pip install pyinstaller

# 执行打包命令（包含背景音乐）
pyinstaller --onefile --windowed --add-data "images;images" --add-data "sounds;sounds" --add-data "leaderboard.json;." --name "AlienInvasion" alien_invasion.py
```

### 📋 工具选择建议

| 使用场景 | 推荐工具 | 命令 | 平台支持 |
|---------|---------|------|---------|
| **最终发布** | `build_sound_fixed.bat` | 一键完整打包 | Windows |
| **跨平台开发** | `build_game.py` | Python实现、详细错误处理 | Windows/macOS/Linux |
| **用户分发** | `create_portable.bat` | 便携版、启动脚本 | Windows |

## 📁 打包结果

打包成功后，会在项目目录下生成：
```
Alien-invasion/
├── dist/
│   └── AlienInvasion.exe    # 🎮 游戏可执行文件
├── build/                   # 构建缓存（可删除）
├── AlienInvasion.spec      # 打包配置文件
└── ...
```

### 便携版结构（使用create_portable.bat后）
```
AlienInvasion_Portable/
├── AlienInvasion.exe          # 🎮 主程序
├── 开始游戏.bat               # 🚀 启动脚本
├── 游戏说明.txt               # 📖 使用说明
├── images/                    # 🖼️ 图像资源
│   ├── ship.bmp              # 🚀 飞船图像
│   ├── alien.bmp             # 👾 外星人图像
│   └── background.bmp        # 🌌 星空背景
├── sounds/                    # 🔊 音效资源
│   ├── shoot.wav             # 💥 射击音效
│   ├── explosion.wav         # 💫 爆炸音效
│   └── BGM.mp3              # 🎵 背景音乐
└── leaderboard.json           # 🏆 排行榜数据
```

## 🎮 运行游戏

1. **找到可执行文件**: `dist/AlienInvasion.exe`
2. **双击运行**: 直接双击即可启动游戏

## 📋 系统要求


### 开发环境
- **Python**: 3.8+
- **PyInstaller**: 最新版本
- **依赖**: pygame, numpy

## 🔧 打包环境准备

### 1. 安装Python
```bash
# 从官网下载Python 3.8+: https://python.org
# 安装时勾选"Add Python to PATH"
```

### 2. 安装依赖
```bash
# 使用requirements.txt
pip install -r requirements.txt

# 或手动安装
pip install pygame numpy pyinstaller
```

### 3. 验证环境
```bash
# 检查Python版本
python --version

# 检查PyInstaller
pyinstaller --version

# 运行游戏测试
python alien_invasion.py
```


## 🔍 自定义打包选项

### 修改打包参数

如果需要自定义打包，可以修改以下参数：

```bash
# 基础命令结构
pyinstaller [选项] --name "输出名称" 主程序文件

# 常用选项
--onefile              # 打包为单个exe文件
--windowed             # 无控制台窗口（GUI程序）
--console              # 显示控制台窗口（调试用）
--add-data "源;目标"    # 包含数据文件
--icon "图标文件"      # 设置exe图标
--clean                # 清理临时文件
--noconfirm            # 覆盖输出不询问
```

## 📋 打包验证清单

### 打包前检查 ✅
- [ ] Python 3.8+ 已安装
- [ ] PyInstaller 已安装 (`pip install pyinstaller`)
- [ ] 游戏在开发环境正常运行 (`python alien_invasion.py`)
- [ ] 所有资源文件存在 (images/, sounds/, leaderboard.json)
- [ ] 依赖已安装 (`pip install -r requirements.txt`)

## 📚 相关文档
- 🎮 **[控制说明](CONTROLS.md)** - 游戏操作和控制键位
- 📁 **[文件说明](FILE_GUIDE.md)** - 每个文件的作用和重要性
- 📋 **[主文档](README.md)** - 游戏完整介绍
---