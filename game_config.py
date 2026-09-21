from parser import MainConfig, LevelConfig
from typing import List, Dict, Any, Optional


class PacConfig():
    def __init__(self, main_config: MainConfig,
                 lvl_config: LevelConfig) -> None:
        self.highscore_filename = main_config.highscore_filename
        self.seed = main_config.seed
        self.lives = main_config.lives
        self.pacgum = main_config.pacgum
        self.points_per_pacgum = main_config.points_per_pacgum
        self.points_per_super_pacgum = main_config.points_per_super_pacgum
        self.points_per_ghost = main_config.points_per_ghost
        self.level_max_time = main_config.level_max_time
        self.levels = lvl_config.levels