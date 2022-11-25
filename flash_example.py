from gif import *

SIZE = 64
LOOP_NUMBER = 8 * SIZE

def main():

    gif("flash")

    GIF89a()

    width(SIZE)
    height(SIZE)

    # Packed Fields
    global_color_table_flag(True)
    color_resolution(7)
    table_sort_flag(False)
    size_of_global_color_table(1)

    background_color_index(0)

    pixel_aspect_ratio(0)

    # Add colors to the color table
    global_color_table_color((255, 0, 0))
    global_color_table_color((0, 255, 0))
    global_color_table_color((0, 0, 255))
    global_color_table_color((255, 0, 255))

    # Application Extension
    application_extension()

    block_size(11)

    application_name("NETSCAPE2.0")

    block_size(3)

    index_of_block(1)

    # 0 for infinite
    number_of_repetitions(0)

    end_block()

    # Graphic Control Extension
    graphic_control_extension()

    block_size(4)

    # Packed Byte Field
    reserved(0)
    disposal_method(1)
    user_input_flag(False)
    transparent_color_flag(False)

    # Hundreds of seconds
    delay_time(100)

    transparent_color_index(0)

    end_block()

    # Image frame
    image_separator()

    image_top_left(0)
    image_top_right(0)

    width(SIZE)
    height(SIZE)

    # Packed Byte Field
    local_color_table_flag(False)
    interlace_flag(False)
    sort_flag(False)
    reserved(0)
    size_of_local_color_table(0)

    LZW_minimum_code_size(7)

    COLOR_CODE = 0 
    for i in range(LOOP_NUMBER):
        block_size(9)
        clear_command()
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)

    end_block()

    # Graphic Control Extension
    graphic_control_extension()

    block_size(4)

    # Packed Byte Field
    reserved(0)
    disposal_method(1)
    user_input_flag(False)
    transparent_color_flag(False)

    # Hundreds of seconds
    delay_time(100)

    transparent_color_index(0)

    end_block()

    # Image frame
    image_separator()

    image_top_left(0)
    image_top_right(0)

    width(SIZE)
    height(SIZE)

    # Packed Byte Field
    local_color_table_flag(False)
    interlace_flag(False)
    sort_flag(False)
    reserved(0)
    size_of_local_color_table(0)

    LZW_minimum_code_size(7)

    COLOR_CODE = 1
    for i in range(LOOP_NUMBER):
        block_size(9)
        clear_command()
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        
    end_block()

    # Graphic Control Extension
    graphic_control_extension()

    block_size(4)

    # Packed Byte Field
    reserved(0)
    disposal_method(1)
    user_input_flag(False)
    transparent_color_flag(False)

    # Hundreds of seconds
    delay_time(100)

    transparent_color_index(0)

    end_block()

    # Image frame
    image_separator()

    image_top_left(0)
    image_top_right(0)

    width(SIZE)
    height(SIZE)

    # Packed Byte Field
    local_color_table_flag(False)
    interlace_flag(False)
    sort_flag(False)
    reserved(0)
    size_of_local_color_table(0)

    LZW_minimum_code_size(7)

    COLOR_CODE = 2
    for i in range(LOOP_NUMBER):
        block_size(9)
        clear_command()
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        
    end_block()

# Graphic Control Extension
    graphic_control_extension()

    block_size(4)

    # Packed Byte Field
    reserved(0)
    disposal_method(1)
    user_input_flag(False)
    transparent_color_flag(False)

    # Hundreds of seconds
    delay_time(100)

    transparent_color_index(0)

    end_block()

    # Image frame
    image_separator()

    image_top_left(0)
    image_top_right(0)

    width(SIZE)
    height(SIZE)

    # Packed Byte Field
    local_color_table_flag(False)
    interlace_flag(False)
    sort_flag(False)
    reserved(0)
    size_of_local_color_table(0)

    LZW_minimum_code_size(7)

    COLOR_CODE = 3
    for i in range(LOOP_NUMBER):
        block_size(9)
        clear_command()
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        color_lookup_value(COLOR_CODE)
        
    end_block()

    end_file()

main()