from pydantic import (BaseModel, field_validator,
ValidationError, ConfigDict, ValidationInfo)

from typing import Any, Dict, Optional, List


class MainConfig(BaseModel):
    model_config = ConfigDict(extra="ignore")
    highscore_filename: Any
    seed: Any
    lives: Any
    pacgum: Any
    points_per_pacgum: Any
    points_per_super_pacgum: Any
    points_per_ghost: Any
    level_max_time: Any

    @field_validator("highscore_filename")
    @classmethod
    def highscore_filename_validate(cls, value: str) -> str:
        if not isinstance(value, str):
            value = "highscore.json"
        if value.strip() == "":
            print("The highscore file name is empty " + 
                  "therefore we will use a default value.")
            value = "highscore.json"
        if value.split(".")[-1] != "json":
            print("The highscore file name should be a .json")
            value = "highscore.json"
        return value

    @field_validator("points_per_pacgum", "lives", "pacgum", 
                     "points_per_ghost", "level_max_time",
                     "points_per_super_pacgum")
    @classmethod
    def validate_positive_config(cls, value: int, info: ValidationInfo) -> int:
        if value == None or not isinstance(value, int) or value <= 0:
            print(f'The value of {info.field_name} ' +
                                         "must be a positive integer.")
            if info.field_name == "lives":
                value = 3
            elif info.field_name == "pacgum":
                value = 42
            elif info.field_name == "points_per_pacgum":
                value = 10
            elif info.field_name == "points_per_super_pacgum":
                value = 50
            elif info.field_name == "points_per_ghost":
                value == 200
            elif info.field_name == "level_max_time":
                value = 90
        return value

    @field_validator("seed", mode="after")
    @classmethod
    def validate_seed(cls, value: int) -> int:
        if value == None or not isinstance(value, int) or value < 0:
            print("The seed should be 0 or more.")
            value = 42
        return value
    

class LevelConfig(BaseModel):
    model_config = ConfigDict(extra="ignore")
    levels: List[Dict]

    @field_validator("levels", mode="after")
    @classmethod
    def levels_validation(cls, value: List[Dict]):
        result = True
        def checker(value: List[Dict]) -> None:
            nonlocal result
            if value != None:
                for lvl in value:
                    if (
                        lvl["width"] < 0
                        or lvl["height"] < 0
                        or not isinstance(lvl["width"], int)
                        or not isinstance(lvl["height"], int)
                    ):
                        result = False
                        break
            elif value == None:
                result = False
        checker(value)
        if result == False:
            print("The width and the height" +
                  " must be positive integers")
            value = [
                    {"width": 21, "height": 21},
                    {"width": 21, "height": 21},
                    {"width": 25, "height": 25},
                    {"width": 25, "height": 25},
                    {"width": 25, "height": 25},
                    {"width": 29, "height": 29},
                    {"width": 29, "height": 29},
                    {"width": 29, "height": 29},
                    {"width": 33, "height": 33},
                    {"width": 33, "height": 33},
                ]
        return value

from game_config import PacConfig
def the_parser(config: Dict) -> PacConfig | None:
    if not isinstance(config, dict):
        raise TypeError("The config should be a Dictionary.")
    initial_config = {k: config[k] for k in config if k != "levels"}
    main_config = MainConfig.model_validate(config)
    lvl_config = LevelConfig.model_validate(config)
    pac_config = PacConfig(main_config, lvl_config)
    # print(main_config)
    # print(f'\n\n {lvl_config}')
    # print(f"\n\n\n the pac config is: \n {pac_config}")
    return pac_config