import pygame
from pygame.sprite import Sprite
from resource_manager import get_image_path


class Ship(Sprite):
    """管理飞船的类"""
    
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(get_image_path('ship.bmp'))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        # 无敌状态相关
        self.invincible = False
        self.invincible_timer = 0
        self.invincible_duration = 60  # 60帧 = 1秒（假设60FPS）
        
    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom - self.rect.height // 2
        
    def update(self):
        """根据移动标志调整飞船的位置，并处理无敌时间"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
            
        # 根据self.center更新rect对象
        self.rect.centerx = self.center
        self.rect.centery = self.centery
        
        # 处理无敌时间
        if self.invincible:
            self.invincible_timer -= 1
            if self.invincible_timer <= 0:
                self.invincible = False
    
    def make_invincible(self):
        """让飞船进入无敌状态"""
        self.invincible = True
        self.invincible_timer = self.invincible_duration
    
    def blitme(self):
        """在指定位置绘制飞船，无敌时闪烁显示"""
        if self.invincible:
            # 无敌时闪烁效果（每5帧闪烁一次）
            if self.invincible_timer % 10 < 5:
                self.screen.blit(self.image, self.rect)
        else:
            self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image, self.rect)