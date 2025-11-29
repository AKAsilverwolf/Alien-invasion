import os
import sys

def resource_path(relative_path):
    """获取资源的绝对路径，支持开发环境和打包后的环境
    
    Args:
        relative_path: 相对路径，如 'images/ship.bmp'
    
    Returns:
        str: 资源的绝对路径
    """
    try:
        # PyInstaller创建临时文件夹，将路径存储在_MEIPASS中
        base_path = sys._MEIPASS
        print(f"PyInstaller环境，基础路径: {base_path}")
    except AttributeError:
        # 开发环境中，使用当前文件所在目录
        base_path = os.path.abspath(".")
        print(f"开发环境，基础路径: {base_path}")
    except Exception as e:
        print(f"获取基础路径时出错: {e}")
        base_path = os.path.abspath(".")
    
    full_path = os.path.join(base_path, relative_path)
    print(f"资源完整路径: {full_path}")
    return full_path

def get_image_path(image_name):
    """获取图像文件的完整路径"""
    return resource_path(os.path.join('images', image_name))

def get_sound_path(sound_name):
    """获取音效文件的完整路径"""
    return resource_path(os.path.join('sounds', sound_name))

def get_data_path(data_name):
    """获取数据文件的完整路径"""
    return resource_path(data_name)