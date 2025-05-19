import json
# import yaml
import os

def load_config(file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'r') as f:
            return json.load(f)
    # elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
    #     with open(file_path, 'r') as f:
    #         return yaml.safe_load(f)
    else:
        raise ValueError('Unsupported file format.')
    
def save_config(data, file_path):
    if file_path.endswith('.json'):
        with open(file_path,'w') as f:
            json.dump(data, f, indent=4)
    # elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
    #     with open(file_path, 'w') as f:
    #         yaml.dump(data, f)