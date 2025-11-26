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
    
    # 游戏状态
    show_leaderboard_flag = False
    name_input = None
    final_score = 0
    final_level = 0
    
    # 开始游戏的主循环
    while True:
        if show_leaderboard_flag and name_input:
            # 显示名字输入界面
            result = name_input.handle_event(pygame.event.poll())
            if result == 'ok':
                leaderboard.add_score(name_input.text, final_score, final_level)
                show_leaderboard_flag = False
                name_input = None
            elif result == 'cancel':
                show_leaderboard_flag = False
                name_input = None
            
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
            name_input.draw(screen, final_score, final_level)
        else:
            # 正常游戏循环
            events = gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, sound_manager)
            
            # 检查是否按下L键查看排行榜
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                    show_leaderboard_flag = True
            
            if show_leaderboard_flag:
                # 显示排行榜
                gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
                sb.show_leaderboard(screen, leaderboard)
            elif stats.game_active:
                ship.update()
                gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, sound_manager)
                gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, sound_manager)
                gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
            else:
                # 检查游戏是否结束且是否需要输入名字
                if not stats.game_active and stats.score > 0 and leaderboard.is_high_score(stats.score):
                    if not name_input:
                        final_score = stats.score
                        final_level = stats.level
                        name_input = NameInput(ai_settings, screen)
                        show_leaderboard_flag = True
                else:
                    gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
        pygame.display.flip()


if __name__ == '__main__':
    run_game()