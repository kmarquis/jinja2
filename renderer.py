#! /usr/bin/env/python
import os
import sys
import yaml
from huepy import *
from jinja2 import Environment, FileSystemLoader

def main():
    data = yaml.load(open(sys.argv[1]))
    template_dir = FileSystemLoader(os.path.dirname(os.path.realpath(__file__)))
    env = Environment(loader=template_dir, trim_blocks=True, lstrip_blocks=True).get_template(sys.argv[2])
    print(env.render(data))

if __name__ == '__main__':
     if len(sys.argv) < 3:
         print(info(lightred('Please provide the following: "python3 {0} yaml_file j2_template"'.format(sys.argv[0]))))
         sys.exit(1)
     main()