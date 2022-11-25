# Clear file
gif = open("timer.gif", "w")
gif.close()

gif = open("timer.gif", "ab")

# tag file as gif with version
GIF89a = b'\x47\x49\x46\x38\x39\x61'
gif.write(GIF89a)

# width and height
width = b'\x02\x00'
height = b'\x02\x00'
gif.write(width)
gif.write(height)

global_color_table_info = b'\xF1'
gif.write(global_color_table_info)

background_color = b'\x00'
gif.write(background_color)

default_pixel_aspect_ratio = b'\x00'
gif.write(default_pixel_aspect_ratio)

global_color_table = b'\xFF\x00\x00\x80\x00\x00\x00\xFF\x00\x00\x00\xFF'
gif.write(global_color_table)

# Application Extension
application_extension = b'\x21\xFF'
gif.write(application_extension)

block_size = b'\x0B'
gif.write(block_size)

app_name = b'\x4E\x45\x54\x53\x43\x41\x50\x45\x32\x2E\x30'
gif.write(app_name)

num_bytes = b'\x03'
gif.write(num_bytes)

index_of_the_data = b'\x01'
gif.write(index_of_the_data)

repetitions = b'\x00\x00'
gif.write(repetitions)

end_block = b'\x00'
gif.write(end_block)

# Graphic Control Extension 
graphic_control_extension = b'\x21\xF9'
gif.write(graphic_control_extension)

block_size = b'\x04'
gif.write(block_size)

packed_fields = b'\x04'
gif.write(packed_fields)

animation_delay =  b'\x64\x00'
gif.write(animation_delay)

color_number_of_transparent_pixel = b'\x00'
gif.write(color_number_of_transparent_pixel)

block_terminator = b'\x00'
gif.write(block_terminator)


# Image frame
image_descriptor = b'\x2C'
gif.write(image_descriptor)

north_west_corner_pos = b'\x00\x00\x00\x00'
gif.write(north_west_corner_pos)

gif.write(width)
gif.write(height)

packed_fields = b'\x00'
gif.write(packed_fields)

minimum_LZW_code = b'\x07'
gif.write(minimum_LZW_code)

# Number of bytes, clear code, image data
image_data = b'\x05\x80\x00\x02\x02\x03'
gif.write(image_data)

end_image_block = b'\x00'
gif.write(end_image_block)


# Graphic Control Extension 
graphic_control_extension = b'\x21\xF9'
gif.write(graphic_control_extension)

block_size = b'\x04'
gif.write(block_size)

packed_fields = b'\x04'
gif.write(packed_fields)

animation_delay =  b'\x64\x00'
gif.write(animation_delay)

color_number_of_transparent_pixel = b'\x00'
gif.write(color_number_of_transparent_pixel)

block_terminator = b'\x00'
gif.write(block_terminator)


# Image frame
image_descriptor = b'\x2C'
gif.write(image_descriptor)

north_west_corner_pos = b'\x00\x00\x00\x00'
gif.write(north_west_corner_pos)

gif.write(width)
gif.write(height)

packed_fields = b'\x00'
gif.write(packed_fields)

minimum_LZW_code = b'\x07'
gif.write(minimum_LZW_code)

image_data = b'\x05\x80\x03\x00\x00\x02'
gif.write(image_data)

end_image_block = b'\x00'
gif.write(end_image_block)

# End file
end_file = b'\x3B'
gif.write(end_file)

gif.close()