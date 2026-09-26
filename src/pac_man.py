from mazegenerator import MazeGenerator
import yaml
import argparse
from parser import the_parser
from maze.draw_maze import MazeDrawer
from game_config import PacConfig

if __name__ == "__main__":
    try:
        ps = argparse.ArgumentParser(description="I parse the command line.")
        ps.add_argument("path", help="the path of the config")
        args = ps.parse_args()
        with open(args.path, "r") as f:
            input = yaml.safe_load(f)
        config: PacConfig = the_parser(input)
        generated_maze = MazeGenerator((config.levels[0]["width"],\
            config.levels[0]["height"]), seed=42)
        height = config.levels[0]["height"]
        width = config.levels[0]["width"]
        maze_drawer = MazeDrawer(width, height, generated_maze.maze)
    except Exception as e:
        print(f"Error: {e}")
    
