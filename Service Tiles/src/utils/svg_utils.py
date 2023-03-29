import sys
from xml.dom.minidom import Node, parseString

if sys.version_info[:2] >= (3, 8):
    from collections.abc import MutableMapping
else:
    from collections import MutableMapping

from utils.text_to_svg import get_text_to_svg
from svgpathtools import svgstr2paths, document

IS_BLACK_FILL = True

# def calc_x_percent(name_length):
#     default_x_percent = 44
#     character_delta = 3.5

#     remaining_length = name_length-3

#     return default_x_percent - remaining_length * character_delta

# def build_fill_html(service_name):
#     font_fill = 'black' if IS_BLACK_FILL == True else 'white'

#     x_percent = calc_x_percent(len(service_name))

#     # split into multiple lines if service name is long
#     text_attributes = f'xmlns="http://www.w3.org/2000/svg" text-anchor="middle" style="font-weight: bold;font: bold 6px sans-serif;fill:{font_fill};"'
#     if(len(service_name) > 20):
#         service_name_words = service_name.split(' ')
#         service_name_html = f'<text x="47%" y="65" {text_attributes}>{service_name_words[0]} {service_name_words[1]}</text>'
#         service_name_html += f'<text x="47%" y="75" {text_attributes}>{" ".join(word for word in service_name_words[2:])}</text>'
#     else:
#         service_name_html = f'<text x="47%" y="65" {text_attributes}>{service_name}</text>'

#     return service_name_html


# def translate_svg_text_path_tools(svg, service_name):
#     svg_group_id_index = svg.index('svgGroup')

#     x_offset, y_offset = derive_translate_coordinates(svg, service_name)

#     # , scale(0.75)
#     svg = svg[:svg_group_id_index+10] + \
#         f'transform="translate({x_offset}, {y_offset})" ' + svg[svg_group_id_index+10:]

#     return svg


# def translate_svg_text(svg, line_number, text_length):
#     g_index = svg.index('<g')

#     # pixel offset
#     # x_offset = 46

#     # if text_length > 2:
#     #     x_offset = x_offset - (text_length * 1.9)

#     # y_offset = 73 + (10 * line_number)

#     # view offset
#     x_offset = 33

#     if text_length > 20:
#         x_offset = 12

#     # match text_length:
#     #     case 20:
#     #         x_offset = 33
#     #     case 19:
#     #         x_offset = 33
#     #     case 17:
#     #         x_offset = 34
#     #     case 16:
#     #         x_offset = 35
#     #     case 15:
#     #         x_offset = 36
#     #     case 14:
#     #         x_offset = 37
#     #     case 13:
#     #         x_offset = 38
#     #     case 12:
#     #         x_offset = 39
#     #     case 11:
#     #         x_offset = 40
#     #     case 10:
#     #         x_offset = 22
#     #     case 9:
#     #         x_offset = 24.5
#     #     case 8:
#     #         x_offset = 25.5
#     #     case 7: # 3
#     #         x_offset = 28.5  # even to odd is bigger
#     #     case 6: # 3.5
#     #         x_offset = 32
#     #     case 5: # 2.5
#     #         x_offset = 34.5
#     #     case 4: # 3.5
#     #         x_offset = 38
#     #     case 3: # 1.5
#     #         x_offset = 40.5
#     #     case 2: # 3.5
#     #         x_offset = 44
#     #     case 1: # 2
#     #         x_offset = 46
#     #     case _:
#     #         x_offset = 33
#     y_offset = 70 + (10 * line_number)

#     #svg = svg[:g_index+3] + f'transform="translate({x_offset}, {y_offset})" ' + svg[g_index+3:]
#     svg = svg[:g_index+3] + \
#         f'transform="translate({x_offset}vw, {y_offset}vh)" ' + svg[g_index+3:]

#     return svg


# def derive_translate_coordinates(svg, service_name):
#     # create svgpathtools Path objects from an SVG file
#     # paths, attributes, dict_attr = #svg2paths(svg)
#     paths, attributes, dict_attr = svgstr2paths(svg,
#                                                 return_svg_attributes=True)

#     # text path is always the second element
#     svg_icon = paths[0]
    
#     #svg_icon.transform = "translate(16,8)" ###TODO###
#     icon_xmin, icon_xmax, icon_ymin, icon_ymax = svg_icon.bbox()
#     svg_icon_width = icon_xmax - icon_xmin

#     #print(f'icon height: {icon_ymax - icon_ymin}')

#     icon_start = str(svg_icon.start)
#     svg_icon_x_start = float(icon_start[1:icon_start.index('+')-1])
#     print(f'icon start: {svg_icon_x_start}, icon width: {icon_xmax - icon_xmin}')

#     svg_text_path = paths[1]
#     xmin, xmax, ymin, ymax = svg_text_path.bbox()

#     #print(f'text height: {ymax - ymin}')

#     svt_text_start = str(svg_text_path.start)
#     svg_text_x_start = float(svt_text_start[1:svt_text_start.index('+')-1])
#     print(f'text start: {svg_text_x_start}, text width: {xmax - xmin}')

#     svg_text_width = xmax - xmin

#     #start_delta = abs(svg_icon_x_start - svg_text_x_start)
#     #x_offset = svg_icon_x_start - svg_icon_width / 2 - svg_text_x_start + svg_text_width / 2

#     icon_midpoint = svg_icon_x_start * .65 + svg_icon_width /2
#     #icon_midpoint = icon_midpoint - svg_text_x_start /2
#     x_offset = icon_midpoint - svg_text_width / 2 - svg_text_x_start #+ len(service_name) # 1.35 # text offset
    
#     # ChatGPT answer - Calculate the translation values for the second path element
#     # translate_x = (svg_width - path2_bbox.width) / 2 - path2_bbox.x
#     # translate_y = path1_bbox.y + path1_bbox.height - path2_bbox.y
    

#     print(f'X offset: {x_offset}')
#     #const finalTextAdjustedWidth = svgRect.width / 2 - svgTextWidth / 2;
#     #const finalTextAdjustedHeight = svgRect.height * .8; # 64 is .8 of 80

#     return x_offset, 74

# def strip_get_g_tag(svg):
#     g_start_index = svg.index('<g')
#     g_end_index = svg.rindex('</g>')
#     return svg[g_start_index:g_end_index+4]


# def build_text_as_svg(service_name):
#     #font_fill = 'black' if IS_BLACK_FILL == True else 'white'

#     # split into multiple lines if service name is long
#     text_line_1 = ""
#     text_line_2 = ""

#     if len(service_name) > 20:
#         service_name_words = service_name.split(' ')
#         if len(service_name_words) > 1:
#             service_name_joined = f'{service_name_words[0]} {service_name_words[1]}'

#             text_line_1 = get_text_to_svg(service_name_joined)
#             text_line_1 = strip_get_g_tag(text_line_1)
#             #text_line_1 = translate_svg_text(
#                 #text_line_1, 1, len(service_name_joined))

#         if len(service_name_words) > 2:
#             service_name_joined = " ".join(
#                 word for word in service_name_words[2:])

#             text_line_2 = get_text_to_svg(service_name_joined)
#             text_line_2 = strip_get_g_tag(text_line_2)
#             #text_line_2 = translate_svg_text(
#                 #text_line_2, 2, len(service_name_joined))
#     else:
#         service_name_words = service_name.split(' ')
#         if len(service_name_words) > 1:
#             service_name_joined = " ".join(
#                 word for word in service_name_words[:])

#             text_line_1 = get_text_to_svg(service_name_joined)
#             #text_line_1 = translate_svg_text(
#                 #text_line_1, 1, len(service_name_joined))
#         else:
#             text_line_1 = get_text_to_svg(service_name)
#             #text_line_1 = translate_svg_text(text_line_1, 1, len(service_name))

#         text_line_1 = strip_get_g_tag(text_line_1)

#     return text_line_1 + text_line_2


def find_fill(svg):
    fill_index = svg.rindex('fill="#')
    fill_index_end = svg.index('">', fill_index)
    fill_value = svg[fill_index+6:fill_index_end]

    fill_value = fill_value[:7]  # truncate to max-color length

    return fill_value


def translate_and_scale_icon(svg):
    # scale main icon

    translate_index = svg.find('translate(')

    if (translate_index < 0):
        path_index = svg.find('<path ')
        if (path_index < 0):  # some svgs use polygons, not fixing now
            return svg

        #new = svg[:path_index + 6] + 'transform="translate(12.000000, 8.000000), scale(.65)" ' + svg[path_index + 6:]
        new = svg[:path_index + 6] + \
            'transform="translate(0vw, 0vh), scale(.65)" ' + \
            svg[path_index + 6:] + '\n'
    else:
        new = svg.replace("translate(8.000000, 8.000000)", "translate(16, 8), scale(.65)")

    return new



# def add_text_as_svg(source, svg, service_name):
#     path_end_index = svg.index('</path>')
    
#     #new = svg[:last_g_index+4] + \
#         #build_text_as_svg(service_name) + svg[last_g_index+4:]

#     svg_text =  build_text_as_svg(service_name)
#     new = svg[:path_end_index+7] + \
#         svg_text + svg[path_end_index+7:]

#     # print(file_name)
#     with open(source + '/Editted/' + service_name + '_text.svg', "w") as svg_service_text_file:
#         svg_service_text_file.write(
#             "<svg viewBox=\"0 0 80 6\" xmlns=\"http://www.w3.org/2000/svg\">" +
#             svg_text +
#             "</svg>")

#     # try:
#     #     new = translate_svg_text_path_tools(new, service_name)
#     # except Exception as e:
#     #     print(f'Service: {service_name} failed to build svg text')
#     return svg


# def remove_defs(svg):
#     def_start_index = svg.find('<defs>')
#     def_end_index = svg.find('</defs>')
#
#    return svg[:def_start_index] + svg[def_end_index+7:]


# def remove_rectangle(svg):
#     """ rectangle is always second <g> tag in svgs """
#     first_g_start_index = svg.find('<g')
#     grect_start_index = svg.find('<g', first_g_start_index+1)
#     if grect_start_index > -1:
#         grect_end_index = svg.index('</g>', grect_start_index)
#         return svg[:grect_start_index] + svg[grect_end_index+4:]

#     return svg

def build_new_svg(svg):   
    doc = parseString(svg)
    
    # capture Icon path
    path = doc.getElementsByTagName('path')

    # set color to Black or White
    if (IS_BLACK_FILL):
        fill="#000000"
    else:
        fill="#FFFFFF"
    
    if hasattr(path[0]._attrs, 'fill'):
        path[0]._attrs['fill'].value=fill
    else:
        path[0].setAttribute('fill', fill)

    # build minimal svg
    new_svg = f"""<?xml version="1.0" encoding="UTF-8"?>
    <svg version="1.1" xmlns="http://www.w3.org/2000/svg">
       <g fill-rule="evenodd">
            {Node.toprettyxml(path[0])}
        </g>
    </svg>""".replace('\n', '')

    return new_svg

def svg_edit(svg, service_name):
    # background set to transparent
    #new = svg.replace(' fill="url(#linearGradient-1)"', "")
    # if (IS_BLACK_FILL):
    #     new = new.replace(f' fill="#FFFFFF"', ' fill="#000000"')
    # else:
    #     new = new.replace(f' fill="#000000"', ' fill="#FFFFFF"')

    #new = remove_rectangle(new)
    #new = translate_and_scale_icon(new)
    #new = add_text_as_svg(source, new, service_name)
    #new = remove_defs(new)

    try:
        return build_new_svg(svg)
    except Exception as e:
        print(service_name, e)
    
    return svg


def svg_edit_resources(svg, service_name, unique_fill_list):
    # background set to transparent
    #new = svg
    # for fill in unique_fill_list:
    #     if (IS_BLACK_FILL):
    #         new = new.replace(f' fill="{fill}"', ' fill="#000000"')
    #     else:
    #         new = new.replace(f' fill="{fill}"', ' fill="#FFFFFF"')

    #new = remove_rectangle(new)
    #new = translate_and_scale_icon(new)
    #new = add_text_as_svg(source, new, service_name)
    #new = remove_defs(new)
    
    try:
        return build_new_svg(svg)
    except Exception as e:
        print(service_name, e)
    
    return svg

