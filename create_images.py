import pygame
import os

def create_ship_image():
    """创建一个简单的飞船图像"""
    pygame.init()
    
    # 创建一个60x48的图像
    image = pygame.Surface((60, 48), pygame.SRCALPHA)
    image.fill((0, 0, 0, 0))  # 透明背景
    
    # 绘制简单的飞船形状
    # 主体（蓝色矩形）
    pygame.draw.rect(image, (0, 100, 255), (15, 10, 30, 25))
    # 顶部三角（船头）
    pygame.draw.polygon(image, (0, 150, 255), [(30, 0), (15, 10), (45, 10)])
    # 底部三角（船尾）
    pygame.draw.polygon(image, (0, 50, 255), [(20, 35), (25, 47), (40, 47), (35, 35)])
    # 窗户
    pygame.draw.rect(image, (200, 200, 255), (25, 15, 10, 8))
    
    # 保存图像
    pygame.image.save(image, 'images/ship.bmp')
    print("飞船图像已创建: images/ship.bmp")

def create_alien_image():
    """创建一个简单的外星人图像"""
    pygame.init()
    
    # 创建一个50x40的图像
    image = pygame.Surface((50, 40), pygame.SRCALPHA)
    image.fill((0, 0, 0, 0))  # 透明背景
    
    # 绘制简单的外星人形状
    # 身体（绿色椭圆形状）
    pygame.draw.ellipse(image, (0, 255, 0), (5, 10, 40, 25))
    # 眼睛
    pygame.draw.circle(image, (255, 0, 0), (15, 18), 4)
    pygame.draw.circle(image, (255, 0, 0), (35, 18), 4)
    # 触角
    pygame.draw.line(image, (0, 200, 0), (12, 10), (8, 0), 2)
    pygame.draw.line(image, (0, 200, 0), (38, 10), (42, 0), 2)
    
    # 保存图像
    pygame.image.save(image, 'images/alien.bmp')
    print("外星人图像已创建: images/alien.bmp")

def create_background():
    """创建星空背景"""
    pygame.init()
    
    # 创建与屏幕大小相同的背景
    image = pygame.Surface((1200, 800))
    
    # 深蓝色背景
    image.fill((0, 0, 40))
    
    # 添加星星
    import random
    random.seed(42)  # 固定随机种子，确保星星位置一致
    
    for _ in range(200):
        x = random.randint(0, 1200)
        y = random.randint(0, 800)
        size = random.randint(1, 3)
        brightness = random.randint(150, 255)
        color = (brightness, brightness, brightness)
        pygame.draw.circle(image, color, (x, y), size)
    
    # 添加一些大的亮星
    for _ in range(20):
        x = random.randint(0, 1200)
        y = random.randint(0, 800)
        size = random.randint(3, 5)
        pygame.draw.circle(image, (255, 255, 200), (x, y), size)
    
    # 保存背景图像
    pygame.image.save(image, 'images/background.bmp')
    print("背景图像已创建: images/background.bmp")

if __name__ == '__main__':
    # 确保images目录存在
    if not os.path.exists('images'):
        os.makedirs('images')
    
    create_ship_image()
    create_alien_image()
    create_background()
    print("所有游戏图像已创建完成！")