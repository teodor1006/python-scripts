def update_server_config(file_path, key, value):
    # Read the existing config file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Update the config value for the specified key
    with open(file_path, 'w') as file:
        for line in lines:
            if key in line:
                # Update the line with the new value
                updated_line = f"{key}={value}\n"
                file.write(updated_line)
            else:
                # Keep the existing line as it is
                file.write(line)

if __name__ == "__main__":
   
   server_config_file = r'C:\Users\Teodor\Desktop\Coding\PythonScripts\UpdateServer\server.conf'
   key_to_update = 'PORT'
   new_value = '5000'  

   update_server_config(server_config_file, key_to_update, new_value)
