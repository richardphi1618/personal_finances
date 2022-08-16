import pprint
import sys
from os import path

import yaml


def to_upper(oldList):
    newList = []
    for element in oldList:
        newList.append(element.upper())
    return newList

def find_key(input_dict, target):
    solutions = []
    for key, value in input_dict.items():
        for i in to_upper(value):
            if i in target.upper():
                solutions.append(key)
        
    return solutions

def read_yml_as_dict(file_path: str):
    if path.isfile(file_path):
        f = open(file_path, "r")
        input = f.read()
        f.close()
    
    try:
        output = yaml.safe_load(input)
    except Exception as e:
        print(str(e))
        sys.exit(1) 
    
    return output


if __name__=='__main__':
    categories = read_yml_as_dict('./categories.yml')

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(categories)

    print("\n --------------------------- \n")

    print(f'test1 = {find_key(categories, "Amazoncom611WF3KX3 Amzncombill WA")}')


    
