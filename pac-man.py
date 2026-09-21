import mazegenerator
import yaml
import argparse
import sys
from parser import the_parser
from game_config import PacConfig

if __name__ == "__main__":
    try:
        ps = argparse.ArgumentParser(description="I parse the command line.")
        ps.add_argument("path", help="the path of the config")
        args = ps.parse_args()
        with open(args.path, "r") as f:
            input = yaml.safe_load(f)
            print(args.path)
        config: PacConfig = the_parser(input)
    except Exception as e:
        print(f"Error: {e}")
    
