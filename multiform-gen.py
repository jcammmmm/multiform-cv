from unittest import main
import pyjson5 as json
import yaml
from types import SimpleNamespace
from pprint import pprint as print

def main():
    data = open('cv-data.yml', 'r').read()
    from yaml import load, dump
    try:
        from yaml import CLoader as Loader, CDumper as Dumper
    except ImportError:
        from yaml import Loader, Dumper

    data = load(data, Loader=Loader)
    print(data)
    
if __name__ == '__main__':
    main()