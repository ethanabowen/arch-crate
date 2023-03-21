import os
import shutil
from pathlib import Path
from utils.folder_utils import create_editted_directory

from utils.svg_utils import find_fill, svg_edit, svg_edit_resources

path_root = '/Users/ethan.bowen/Documents/Build Projects/ArchiCrate/AWS Arch Icons/'

child_dirs = [
    'Architecture-Service-Icons',
    'Category-Icons',
    'Resource-Icons'
]

unique_fill_list = []


def build_unique_fill_list(source):
    all_source_files = os.listdir(source)

    for file_name in all_source_files:
        if '.svg' in file_name:
            with open(source + '/' + file_name, "r") as read_file:
                data = read_file.read()
                fill_value = find_fill(data)

                if not fill_value in unique_fill_list:
                    unique_fill_list.append(fill_value)


def svg_edit_all(source, destination):
    all_source_files = os.listdir(source)

    for file_name in all_source_files:
        if '.svg' in file_name:
            new_file = ''
            with open(source + '/' + file_name, "r") as read_file:
                old_file = read_file.read()

                service_name = file_name.replace('.svg', '')

                print(f'Processing: {service_name}')
                new_file = svg_edit(old_file, service_name)

            with open(destination + '/' + file_name, "w") as write_file:
                write_file.write(new_file)


def svg_edit_all_resources(source, destination):
    all_source_files = os.listdir(source)

    for file_name in all_source_files:
        if '.svg' in file_name:
            new_file = ''

            # print(file_name)
            with open(source + '/' + file_name, "r") as read_file:
                old_file = read_file.read()

                service_name = file_name.replace('.svg', '')
                new_file = svg_edit_resources(
                    old_file, service_name, unique_fill_list)

            with open(destination + '/' + file_name, "w") as write_file:
                write_file.write(new_file)


def walk_architecture_svg(path):
    print('Walking: ' + path)
    for (root, dirs, file) in os.walk(path):
        if not 'Editted' in dirs:
            for dir in dirs:
                dir_path = root + '/' + dir
                is_new_directory = create_editted_directory(dir_path)

                editted_directory = dir_path + '/Editted'
                svg_edit_all(dir_path, editted_directory)


def walk_category_svg(path):
    create_editted_directory(path)

    editted_directory = path + '/Editted'
    svg_edit_all(path, editted_directory)


def walk_resource_svg(path):
    for (root, dirs, file) in os.walk(path):
        if not 'Editted' in dirs:
            for dir in dirs:
                build_unique_fill_list(root + '/' + dir)

    print('Unique Fill List:', unique_fill_list)

    print('Walking: ' + path)
    for (root, dirs, file) in os.walk(path):
        if not 'Editted' in dirs:
            for dir in dirs:
                if not 'Light' in dir and not 'Dark' in dir:
                    dir_path = root + '/' + dir
                    # dark and white dirs
                    print(f"Walking {dir} Dark")
                    dark_dir = dir_path + '/Dark'
                    create_editted_directory(dark_dir)
                    editted_directory = dark_dir + '/Editted'
                    svg_edit_all_resources(dark_dir, editted_directory)

                    print(f"Walking {dir} Light")
                    light_dir = dir_path + '/Light'
                    create_editted_directory(light_dir)
                    editted_directory = light_dir + '/Editted'
                    svg_edit_all_resources(light_dir, editted_directory)


#walk_arch(path_root + child_dirs[0])
#walk_category(path_root + child_dirs[1])
#walk_resource(path_root + child_dirs[2])
