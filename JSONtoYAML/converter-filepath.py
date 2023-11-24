# pip install pyyaml
import json
import yaml

def convert_json_to_yaml(json_data):
    try:
        data = json.loads(json_data)
        yaml_data = yaml.dump(data, default_flow_style=False)
        return yaml_data
    
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def read_json_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            json_data = file.read()
        return json_data
    
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None

if __name__ == "__main__":

    # r'path/to/your/file.json' 
    json_file_path = r'C:\Users\Teodor\Desktop\Coding\PythonScripts\JSONtoYAML\taskdeffile.json'

    json_data_from_file = read_json_from_file(json_file_path)

    if json_data_from_file is not None:
        yaml_result = convert_json_to_yaml(json_data_from_file)

        if yaml_result is not None:
            print("Converted JSON to YAML:")
            print(yaml_result)
