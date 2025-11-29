#!/usr/bin/env python3
"""
快速修复音效问题并重新打包
"""

import os
import subprocess
import shutil

def main():
    print("🔧 快速修复音效问题...")
    
    # 步骤1: 清理之前的打包
    print("🗑️ 清理旧的打包文件...")
    for folder in ['dist', 'build']:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"  清理 {folder} 文件夹")
    
    # 步骤2: 检查所有必要文件
    print("📋 检查必要文件...")
    required_files = {
        'alien_invasion.py': '主程序',
        'resource_manager.py': '资源管理器',
        'sound_manager.py': '音效管理器',
        'ship.py': '飞船类',
        'alien.py': '外星人类',
        'settings.py': '设置类',
        'leaderboard.py': '排行榜类',
        'leaderboard.json': '排行榜数据',
        'images/ship.bmp': '飞船图像',
        'images/alien.bmp': '外星人图像',
        'images/background.bmp': '背景图像',
        'sounds/shoot.wav': '射击音效',
        'sounds/explosion.wav': '爆炸音效',
        'sounds/BGM.mp3': '背景音乐'
    }
    
    missing_files = []
    for file_path, description in required_files.items():
        if os.path.exists(file_path):
            print(f"  ✅ {description}: {file_path}")
        else:
            print(f"  ❌ {description}: {file_path}")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n💔 缺少以下文件: {missing_files}")
        return False
    
    # 步骤3: 创建一个spec文件确保所有资源都被包含
    spec_content = '''
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['alien_invasion.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('images', 'images'),
        ('sounds', 'sounds'),
        ('leaderboard.json', '.'),
    ],
    hiddenimports=['pygame', 'numpy', 'json', 'time', 'random', 'os', 'sys'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='AlienInvasion',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
'''
    
    with open('AlienInvasion_fixed.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    print("📝 创建修复版spec文件")
    
    # 步骤4: 使用spec文件打包
    print("📦 开始修复打包...")
    try:
        result = subprocess.run(['pyinstaller', 'AlienInvasion_fixed.spec', '--clean'], 
                          capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ 打包成功!")
            
            # 检查生成的文件
            exe_path = os.path.join('dist', 'AlienInvasion.exe')
            if os.path.exists(exe_path):
                size_mb = os.path.getsize(exe_path) / (1024 * 1024)
                print(f"📁 生成的文件: {exe_path}")
                print(f"📏 文件大小: {size_mb:.1f} MB")
                
                # 创建测试说明
                with open(os.path.join('dist', 'README.txt'), 'w', encoding='utf-8') as f:
                    f.write('外星人入侵游戏 - 打包版本\n')
                    f.write('=======================\n\n')
                    f.write('使用方法:\n')
                    f.write('1. 双击 AlienInvasion.exe 启动游戏\n')
                    f.write('2. 如果无法运行，请安装 Visual C++ Redistributable\n')
                    f.write('3. 游戏包含背景音乐和完整音效\n\n')
                    f.write('控制说明:\n')
                    f.write('- 方向键: 移动飞船\n')
                    f.write('- 空格键: 发射子弹\n')
                    f.write('- M键: 暂停/恢复背景音乐\n')
                    f.write('- L键: 查看排行榜\n')
                    f.write('- ESC键: 返回/退出\n\n')
                    f.write('祝你游戏愉快!\n')
                
                print("📄 创建使用说明文件")
                return True
            else:
                print("❌ 未找到生成的exe文件")
                return False
        else:
            print("❌ 打包失败:")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ 打包过程出错: {e}")
        return False

if __name__ == '__main__':
    success = main()
    if success:
        print("\n🎉 修复成功! 游戏已打包在 dist/AlienInvasion.exe")
        print("💡 建议先运行一次测试是否正常工作")
    else:
        print("\n💔 修复失败，请检查上述错误信息")
    
    input("\n按任意键退出...")