import pygame
import sys
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from sound_manager import SoundManager
from leaderboard import Leaderboard
from name_input import NameInput


def show_leaderboard_screen(screen, ai_settings, stats, sb, ship, aliens, bullets, play_button, leaderboard):
    """显示排行榜界面（阻塞模式）"""
    clock = pygame.time.Clock()
    
    # 只绘制一次排行榜（包含完整的背景和内容）
    sb.show_leaderboard(screen, leaderboard)
    
    # 显示初始界面
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # 退出游戏
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return True  # 返回游戏
        
        # 只处理事件，不重新绘制界面
        clock.tick(60)  # 60 FPS

def show_name_input_screen(screen, ai_settings, leaderboard, score, level):
    """显示名字输入界面（阻塞模式）"""
    name_input = NameInput(ai_settings, screen)
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # 退出游戏
            
            result = name_input.handle_event(event)
            if result == 'ok':
                leaderboard.add_score(name_input.text, score, level)
                return True  # 返回游戏
            elif result == 'cancel':
                return True  # 返回游戏
        
        # 绘制输入界面
        name_input.draw(screen, score, level)
        
        pygame.display.flip()
        clock.tick(60)  # 60 FPS

def run_game():
    """运行游戏的主函数"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")
    
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Start Game")
    
    # 创建音效管理器
    sound_manager = SoundManager()
    
    # 创建排行榜
    leaderboard = Leaderboard()
    
    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # 游戏主循环
    while True:
        # 检查游戏结束并需要输入名字的情况
        if not stats.game_active and stats.score > 0 and leaderboard.is_high_score(stats.score):
            result = show_name_input_screen(screen, ai_settings, leaderboard, stats.score, stats.level)
            if not result:  # 用户点击了关闭窗口
                pygame.quit()
                sys.exit()
            # 重置分数，避免重复显示输入界面
            stats.score = 0
        
        # 处理游戏事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    # 保存当前游戏状态
                    was_game_active = stats.game_active
                    stats.game_active = False  # 暂停游戏
                    
                    result = show_leaderboard_screen(screen, ai_settings, stats, sb, ship, aliens, bullets, play_button, leaderboard)
                    if not result:  # 用户点击了关闭窗口
                        pygame.quit()
                        sys.exit()
                    
                    # 恢复游戏状态
                    stats.game_active = was_game_active
                else:
                    gf.check_keydown_events(event, ai_settings, screen, ship, bullets, sound_manager)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                gf.check_play_button(ai_settings, screen, stats, sb, play_button, 
                    ship, aliens, bullets, mouse_x, mouse_y)
            elif event.type == pygame.KEYUP:
                gf.check_keyup_events(event, ship)
        
        # 更新游戏状态（只处理正常游戏和主菜单）
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, sound_manager)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, sound_manager)
        
        # 更新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        pygame.display.flip()


if __name__ == '__main__':
    run_game()