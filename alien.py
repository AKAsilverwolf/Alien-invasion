import pygame
from pygame.sprite import Sprite
import random


class Alien(Sprite):
    """表示单个外星人的类"""
    
    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # 随机在屏幕顶端位置
        self.rect.x = random.randint(self.rect.width, 
                                    ai_settings.screen_width - self.rect.width)
        self.rect.y = -self.rect.height  # 从屏幕顶端外开始
        
        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # 随机速度设置
        self.speed_x = random.uniform(ai_settings.alien_speed_min, 
                                     ai_settings.alien_speed_max)
        self.speed_y = random.uniform(ai_settings.alien_speed_min * 0.3, 
                                     ai_settings.alien_speed_max * 0.5)
        
        # 随机初始运动方向
        self.direction_x = random.choice([-1, 1])
        self.direction_y = 1  # 默认向下移动
        
    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        hit_edge = False
        
        if self.rect.right >= screen_rect.right:
            self.direction_x = -1
            hit_edge = True
        elif self.rect.left <= 0:
            self.direction_x = 1
            hit_edge = True
            
        return hit_edge
            
    def update(self):
        """随机移动外星人，碰到边缘会反弹"""
        # 更新位置
        self.x += self.speed_x * self.direction_x
        self.y += self.speed_y * self.direction_y
        
        # 更新rect位置
        self.rect.x = self.x
        self.rect.y = self.y
        
        # 检查边缘碰撞并反弹
        self.check_edges()
        
        # 随机改变水平方向（小概率）
        if random.random() < 0.005:  # 0.5%概率改变方向
            self.direction_x *= -1
        
    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)