from gif import *

def main():

    gif("example")

    GIF89a()

    width(4)
    height(4)

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

    width(4)
    height(4)

    # Packed Byte Field
    local_color_table_flag(False)
    interlace_flag(False)
    sort_flag(False)
    reserved(0)
    size_of_local_color_table(0)

    LZW_minimum_code_size(7)

    block_size(5)
    clear_command()
    color_lookup_value(0)
    color_lookup_value(0)
    color_lookup_value(0)
    color_lookup_value(0)

    block_size(5)
    clear_command()
    color_lookup_value(1)
    color_lookup_value(1)
    color_lookup_value(1)
    color_lookup_value(1)

    block_size(5)
    clear_command()
    color_lookup_value(2)
    color_lookup_value(2)
    color_lookup_value(2)
    color_lookup_value(2)

    block_size(5)
    clear_command()
    color_lookup_value(3)
    color_lookup_value(3)
    color_lookup_value(3)
    color_lookup_value(3)

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

    width(4)
    height(4)

    # Packed Byte Field
    local_color_table_flag(False)
    interlace_flag(False)
    sort_flag(False)
    reserved(0)
    size_of_local_color_table(0)

    LZW_minimum_code_size(7)

    block_size(5)
    clear_command()
    color_lookup_value(3)
    color_lookup_value(3)
    color_lookup_value(3)
    color_lookup_value(3)

    block_size(5)
    clear_command()
    color_lookup_value(0)
    color_lookup_value(0)
    color_lookup_value(0)
    color_lookup_value(0)

    block_size(5)
    clear_command()
    color_lookup_value(1)
    color_lookup_value(1)
    color_lookup_value(1)
    color_lookup_value(1)

    block_size(5)
    clear_command()
    color_lookup_value(2)
    color_lookup_value(2)
    color_lookup_value(2)
    color_lookup_value(2)

    end_block()

    end_file()

main()