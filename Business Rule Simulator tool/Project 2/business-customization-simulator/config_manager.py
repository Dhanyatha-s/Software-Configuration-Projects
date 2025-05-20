import json
import os

def load_config(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config file not found: {file_path}")
    
    if file_path.endswith('.json'):
        with open(file_path, 'r') as f:
            return json.load(f)
    else:
        raise ValueError("Unsupported file format. Only .json is allowed.")

        

def save_config(data, file_path):
    # file_path = r'config_templates/hr_config_template.json'
    if file_path.endswith('.json'):
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
    else:
        print("Unsupported file format.")
        return
        
    print(f"Configuration saved to {file_path}")



    

