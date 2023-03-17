from enums.icon_types import IconType
from folder_work import walk_folder, walk_category_folder, walk_resource_folder
from svg_work import walk_architecture_svg, walk_architecture_svg, walk_category_svg, walk_resource_svg
from enum import Enum

path_root = '/Users/ethan.bowen/Documents/Git/ethan/archi-crate/AWS Arch Icons/'

dirs = [
    'Architecture-Service-Icons',
    'Category-Icons',
    'Resource-Icons'
]


def organize_cleanup_and_create_svgs(directory, icon_type: IconType):
    """Rename folder and files, Delete non SVG files, Build new SVGs"""
    full_path = path_root + directory
    walk_folder(full_path)

    if icon_type == IconType.Architecture:
        #walk_architecture_folder(full_path)
        walk_architecture_svg(full_path)
    elif icon_type == IconType.Category:
        walk_category_folder(full_path)
        walk_category_svg(full_path)
    elif icon_type == IconType.Resource:
        walk_resource_folder(full_path)
        walk_resource_svg(full_path)

organize_cleanup_and_create_svgs(dirs[0], IconType.Architecture)
organize_cleanup_and_create_svgs(dirs[1], IconType.Category)
organize_cleanup_and_create_svgs(dirs[2], IconType.Resource)

# Folder Reorganization

# Architecture Icons
#walk(path_root + child_dirs[0])

# Category Icons
#walk(path_root + child_dirs[1])
#walk_category(path_root + child_dirs[1])

# Resource Icons
#walk(path_root + child_dirs[2])
#walk_resource(path_root + child_dirs[2])

# Svg Reorganization

#walk_arch(path_root + child_dirs[0])
#walk_category(path_root + child_dirs[1])
#walk_resource(path_root + child_dirs[2])



# # Process AWS Architecture Icons
# * Rename Files for easier understanding
# * Transform SVGs
#   * Make Background transparent
#   * Move Icon up and scale down
#   * Add text of Service Name below Icon
#     * Call text-to-svg local server.  See [https://github.com/ethanabowen/text-to-svg](https://github.com/ethanabowen/text-to-svg) 