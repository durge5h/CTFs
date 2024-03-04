from PIL import Image

def read_coordinates(file_path):
    with open(file_path, 'r') as f:
        coordinates = [tuple(map(int, line.strip('()\n').split(','))) for line in f]
    return coordinates

def draw_white_pixels(image_path, coordinates, output_path):
    img = Image.open(image_path)
    for coord in coordinates:
        img.putpixel(coord, (255, 255, 255))  # RGB value for white
    img.save(output_path)
	print(f"Done, check : {output_path}.")

image_path = './confidential.jpg'
file_path = './5ecr3t_c0de/5ecr3t_c0de.txt'
output_path = 'output_image.png'

coordinates = read_coordinates(file_path)
draw_white_pixels(image_path, coordinates, output_path)
