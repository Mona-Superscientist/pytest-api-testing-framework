import json
from os import path


def get_sample(rel_path):
    abs_path = path.dirname(__file__)
    file_path = f'{abs_path}/{rel_path}'
    with open(file_path) as file:
        sample = json.load(file)
        return sample


