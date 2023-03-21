import os
import shutil
from pathlib import Path

from utils.folder_utils import create_editted_directory

path_root = '/Users/ethan.bowen/Documents/Build Projects/ArchiCrate/AWS Arch Icons/'

child_dirs = [
    'Architecture-Service-Icons',
    'Category-Icons',
    'Resource-Icons'
]


def move_files(source, destination):
    allfiles = os.listdir(source)

    for f in allfiles:
        if '.svg' in f:
            src_path = os.path.join(source, f)
            dst_path = os.path.join(destination, f)
            os.rename(src_path, dst_path)


def rename_dirs(path):
    for (root, dirs, file) in os.walk(path):
        for dir in dirs:  # rename dirs
            if not 'Editted' in dir:
                new_name = dir.replace('Arch_', '')
                new_name = new_name.replace('Res_', '')
                new_name = new_name.replace('48_', '')
                new_name = new_name.replace('-', ' ')
                new_name = new_name.replace('_', ' ')

                if dir != new_name:
                    print(f'Renaming directory {dir} to {new_name}')
                    os.rename(root + '/' + dir, root + '/' + new_name)


def rename_or_delete_files(path):
    for (root, dirs, file) in os.walk(path):
        for f in file:
            if '.png' in f:  # remove pngs
                os.remove(root + '/' + f)
            else:
                # remove prefix
                new_name = f.replace('Arch_Amazon-', '')
                new_name = new_name.replace('Arch-Category_', '')
                new_name = new_name.replace('Res_Amazon-', '')
                new_name = new_name.replace('Arch_AWS-', '')
                new_name = new_name.replace('Arch_', '')
                new_name = new_name.replace('-', ' ')
                new_name = new_name.replace('_', ' ')

                # remove suffix
                new_name = new_name.replace('_64', '')

                if f != new_name:
                    print(f'Renaming file {f} to {new_name}')
                    os.rename(root + '/' + f, root + '/' + new_name)


# needs edits if direct from source, run "walk" first
def walk_category_folder(path):
    create_editted_directory(path)

    rename_or_delete_files(path)


# needs edits if direct from source, run "walk" first
def walk_resource_folder(path):
    rename_dirs(path)

    rename_or_delete_files(path)


def walk_folder(path):
    print('Walking: ' + path)
    for (root, dirs, file) in os.walk(path):
        for dir in dirs:
            dir_path = root + '/' + dir
            if not 'Editted' in dir:
                rename_or_delete_files(dir_path)
                if '16' in dir or '32' in dir or ('48' in dir and not 'Res_'):
                    shutil.rmtree(dir_path)
                elif '64' in dir:
                    move_files(dir_path, root)

                    # delete now empty folder
                    shutil.rmtree(dir_path)
                else:
                    walk_folder(dir)

    rename_dirs(path)


# Process section

# Architecture Icons
#walk(path_root + child_dirs[0])

# Category Icons
#walk(path_root + child_dirs[1])
#walk_category(path_root + child_dirs[1])

# Resource Icons
#walk(path_root + child_dirs[2])
#walk_resource(path_root + child_dirs[2])
