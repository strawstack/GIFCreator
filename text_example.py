from gif import *

SIZE = 64
LOOP_NUMBER = 8 * SIZE

def main():

    gif("text_example")

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

    # Plain Text Extension
    plain_text_label()

    block_size(12)

    text_grid_left(4)
    text_grid_top(4)

    width(SIZE - 8)
    height(SIZE - 8)

    character_cell_width(8)
    character_cell_height(8)

    text_foreground_color_index(1)
    text_background_color_index(3)

    block_size(7)

    characters("Richard")

    end_block()

    # Image frame
    image_separator()

    image_left(0)
    image_top(0)

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

    end_file()

main()