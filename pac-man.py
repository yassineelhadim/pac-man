import mazegenerator
import yaml
import argparse
import sys

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="I parse the command line.")
        parser.add_argument("path", help="the path of the config")
        args = parser.parse_args()
        if len(sys.argv) != 2:
            raise Exception("Error: There should be three arguments\
                in this order: python3 pac-man.py 'config file'")
        with open(args.path, "r") as f:
            input = yaml.safe_load(f)
    except Exception as e:
        print(f"Error: {e}")
    print(input)
