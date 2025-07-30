import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(full_path)
    absolute_path_cwd = os.path.abspath(working_directory)
    if not absolute_path.startswith(absolute_path_cwd):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(absolute_path):
        return f'Error: "{directory}" is not a directory'
    
    contents = os.listdir(absolute_path)
    list_of_strings_to_print = []
    for thing in contents:
        full_path_thing = os.path.join(absolute_path, thing)
        size_thing = os.path.getsize(full_path_thing)
        check_dr_thing = os.path.isdir(full_path_thing)
        thing_to_append = f"- {thing}: file_size={size_thing} bytes, is_dir={check_dr_thing}"
        list_of_strings_to_print.append(thing_to_append)

    return "\n".join(list_of_strings_to_print)
