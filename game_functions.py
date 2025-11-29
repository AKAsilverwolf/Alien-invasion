import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
import random


def check_keydown_events(event, ai_settings, screen, ship, bullets, sound_manager):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets, sound_manager)
    elif event.key == pygame.K_q:
        sys.exit()
        

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, sound_manager):
    """响应按键和鼠标事件"""
    events = list(pygame.event.get())
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, sound_manager)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, 
                ship, aliens, bullets, mouse_x, mouse_y)
    return events
            

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, 
        bullets, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()
        
        # 隐藏光标
        pygame.mouse.set_visible(False)
        
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True
        
        # 重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        
        # 创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def fire_bullet(ai_settings, screen, ship, bullets, sound_manager):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        sound_manager.play_shoot()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 绘制背景
    if ai_settings.background_image:
        screen.blit(ai_settings.background_image, (0, 0))
    else:
        screen.fill(ai_settings.bg_color)
    
    # 重绘所有子弹，飞船和外星人
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    
    # 显示得分
    sb.show_score()
    
    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, sound_manager):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, sound_manager)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, sound_manager):
    """响应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
            sound_manager.play_explosion()
        check_high_score(stats, sb)
    
    if len(aliens) == 0:
        # 提升难度，不需要重新创建外星人群，因为会持续生成
        ai_settings.increase_speed()
        
        # 提高等级
        stats.level += 1
        sb.prep_level()
        
        # 添加一些额外外星人作为奖励
        for _ in range(3):
            alien = Alien(ai_settings, screen)
            aliens.add(alien)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2.5 * alien_width))
    return max(4, number_aliens_x)  # 至少4个，最多8个


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - 
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2.5 * alien_height))
    return max(2, min(4, number_rows))  # 2-4行


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建初始外星人群"""
    # 创建初始的几个外星人
    initial_count = 5
    for _ in range(initial_count):
        alien = Alien(ai_settings, screen)
        # 随机Y位置，但不要太靠下
        alien.rect.y = random.randint(-200, -50)
        alien.y = float(alien.rect.y)
        aliens.add(alien)


def spawn_alien(ai_settings, screen, aliens):
    """持续随机生成敌人"""
    # 如果达到最大数量，不再生成
    if len(aliens) >= ai_settings.max_aliens:
        return
        
    # 更新生成计时器
    ai_settings.alien_spawn_timer += 1
    
    # 达到生成间隔时生成新敌人
    if ai_settings.alien_spawn_timer >= ai_settings.alien_spawn_interval:
        alien = Alien(ai_settings, screen)
        aliens.add(alien)
        ai_settings.alien_spawn_timer = 0


# 保留这些函数以兼容现有代码，但功能简化
def check_fleet_edges(ai_settings, aliens):
    """检查是否有外星人到达边缘（已简化）"""
    pass


def change_fleet_direction(ai_settings, aliens):
    """改变外星人方向（已简化）"""
    pass


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, sound_manager):
    """响应飞船被外星人撞到"""
    # 如果飞船处于无敌状态，不处理碰撞
    if ship.invincible:
        return
    
    # 将ships_left减1
    stats.ships_left -= 1
    
    # 更新记分牌
    sb.prep_ships()
    
    # 播放爆炸音效
    sound_manager.play_explosion()
    
    # 检查是否还有生命
    if stats.ships_left > 0:
        # 让飞船进入无敌状态
        ship.make_invincible()
        
        # 短暂停顿
        sleep(0.5)
    else:
        # 游戏结束
        stats.game_active = False
        pygame.mouse.set_visible(True)
        sound_manager.play_game_over()


# 注意：check_aliens_bottom函数已移除，因为现在游戏失败只基于飞船被撞击


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, sound_manager):
    """
    更新外星人位置并持续生成新敌人
    """
    # 持续生成新敌人
    spawn_alien(ai_settings, screen, aliens)
    
    # 更新所有外星人位置
    aliens.update()
    
    # 移除超出屏幕底部的外星人（清理性能）
    screen_rect = screen.get_rect()
    for alien in aliens.copy():
        if alien.rect.top > screen_rect.bottom:
            aliens.remove(alien)
    
    # 检测外星人和飞船之间的碰撞（仅在非无敌状态）
    if not ship.invincible:
        if pygame.sprite.spritecollideany(ship, aliens):
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, sound_manager)


def check_high_score(stats, sb):
    """检查是否诞生了新的最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()