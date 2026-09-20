from pydantic import BaseModel, field_validator, ValidationError, ConfigDict
from typing import Any, Dict, Optional, List

class PacConfig():
    # this is a class that works as a template
    # of an object that will be used later in 
    # the code for easy access to the config
    pass

class GameConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    highscore_filename: str
    seed: int
    lives: int
    pacgum: int
    points_per_pacgum: int
    points_per_super_pacgum: int
    points_per_ghost: int
    level_max_time: int

    @field_validator
    def highscore_filename_validate(self):
        pass


class LevelConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    levels: List[Dict]
    width: int
    hight: int
    pass


def parser(config_dict: Dict) -> PacConfig:
    pass