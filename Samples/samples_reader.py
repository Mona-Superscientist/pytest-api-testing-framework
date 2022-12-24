import json
from os import path


def get_sample(rel_path):
    abs_path = path.dirname(__file__)
    file_path = f'{abs_path}/{rel_path}'
    with open(file_path) as file:
        sample = json.load(file)
        return sample


def load_json_schema(schema_file_name):
    abs_path = path.dirname(__file__)
    file_path = f'{abs_path}/schemas/{schema_file_name}'
    with open(file_path) as schema_file:
        schema = json.load(schema_file)
        return schema
