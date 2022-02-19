class Settings:
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """Инициалищирует настройки игры."""
        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_limit = 3
        
        # Параметры снаряда
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Настройки пришельцев
        self.fleet_drop_speed = 10

        # Темп ускорения игры
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialyze_dynamic_settings()

    def initialyze_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        self.fleet_direction = 1
        # 1 - вправо, -1 - влево

        # Подсчет очков
        self.alien_points = 50
        
    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)