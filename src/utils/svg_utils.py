from utils.text_to_svg import get_text_to_svg


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

def translate_svg_text(svg, line_number, text_length):
    g_index = svg.index('<g')

    ## pixel offset
    # x_offset = 46

    # if text_length > 2:
    #     x_offset = x_offset - (text_length * 1.9)

    # y_offset = 73 + (10 * line_number)


    ## view offset
    x_offset = 33
    if text_length > 9:
        x_offset = max(33 - (text_length * 2), 12)
    y_offset = 70 + (10 * line_number)

    #svg = svg[:g_index+3] + f'transform="translate({x_offset}, {y_offset})" ' + svg[g_index+3:]
    svg = svg[:g_index+3] + f'transform="translate({x_offset}vw, {y_offset}vh)" ' + svg[g_index+3:]

    return svg

def strip_get_g_tag(svg):
    g_start_index = svg.index('<g')
    g_end_index = svg.rindex('</g>')
    return svg[g_start_index:g_end_index+4]


def build_text_as_svg(service_name):
    #font_fill = 'black' if IS_BLACK_FILL == True else 'white'
    
    # split into multiple lines if service name is long
    text_line_1 = "" 
    text_line_2 = ""

    if len(service_name) > 20: 
        service_name_words = service_name.split(' ')
        if len(service_name_words) > 1:
            service_name_joined = f'{service_name_words[0]} {service_name_words[1]}'

            text_line_1 = get_text_to_svg(service_name_joined)
            text_line_1 = strip_get_g_tag(text_line_1)
            text_line_1 = translate_svg_text(text_line_1, 1, len(service_name_joined))

        if len(service_name_words) > 2:
            service_name_joined = " ".join(word for word in service_name_words[2:])

            text_line_2 = get_text_to_svg(service_name_joined)
            text_line_2 = strip_get_g_tag(text_line_2)
            text_line_2 = translate_svg_text(text_line_2, 2, len(service_name_joined))
    else:
        service_name_words = service_name.split(' ')
        if len(service_name_words) > 1:
            service_name_joined = " ".join(word for word in service_name_words[:])

            text_line_1 = get_text_to_svg(service_name_joined)
            text_line_1 = translate_svg_text(text_line_1, 1, len(service_name_joined))
        else:
            text_line_1 = get_text_to_svg(service_name)
            text_line_1 = translate_svg_text(text_line_1, 1, len(service_name))
        
        text_line_1 = strip_get_g_tag(text_line_1)
        
            
    return text_line_1 + text_line_2

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
        if(path_index < 0): #some svgs use polygons, not fixing now
            return svg
        
        #new = svg[:path_index + 6] + 'transform="translate(12.000000, 8.000000), scale(.65)" ' + svg[path_index + 6:]
        new = svg[:path_index + 6] + 'transform="translate(0vw, 0vh), scale(.65)" ' + svg[path_index + 6:]
    else:
        new = svg.replace("translate(8.000000, 8.000000)",
                          "translate(16, 8), scale(.65)")

    return new


def add_text_as_svg(svg, service_name):
    last_g_index = svg.rindex('</g>')
    new = svg[:last_g_index+4] + \
        build_text_as_svg(service_name) + svg[last_g_index+4:]

    return new


def remove_defs(svg):
    def_start_index = svg.find('<defs>')
    def_end_index = svg.find('</defs>')

    return svg[:def_start_index] + svg[def_end_index+7:]

def remove_rectangle(svg):
    """ rectangle is always second <g> tag in svgs """
    first_g_start_index = svg.find('<g')
    grect_start_index = svg.find('<g', first_g_start_index+1)
    if grect_start_index > -1:
        grect_end_index = svg.index('</g>', grect_start_index)
        return svg[:grect_start_index] + svg[grect_end_index+4:]
    
    return svg

def svg_edit(svg, service_name):
    # background set to transparent
    new = svg.replace(' fill="url(#linearGradient-1)"', "")
    if (IS_BLACK_FILL):
        new = new.replace(f' fill="#FFFFFF"', ' fill="#000000"')
    else:
        new = new.replace(f' fill="#000000"', ' fill="#FFFFFF"')

    new = remove_rectangle(new)
    new = translate_and_scale_icon(new)
    new = add_text_as_svg(new, service_name)
    new = remove_defs(new)

    return new


def svg_edit_resources(svg, service_name, unique_fill_list):
    # background set to transparent
    new = svg
    for fill in unique_fill_list:
        if (IS_BLACK_FILL):
            new = new.replace(f' fill="{fill}"', ' fill="#000000"')
        else:
            new = new.replace(f' fill="{fill}"', ' fill="#FFFFFF"')

    new = remove_rectangle(new)
    new = translate_and_scale_icon(new)
    new = add_text_as_svg(new, service_name)
    new = remove_defs(new)

    return new
