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
    
if __name__ == "__main__":
    
    json_data = '{"name": "Bogdan", "age": 30, "city": "Sofia"}'
    
    yaml_result = convert_json_to_yaml(json_data)

    if yaml_result is not None:
        print("Converted JSON to YAML:")
        print(yaml_result)
  