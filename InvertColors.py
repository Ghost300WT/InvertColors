from PIL import Image, ImageOps
import os

def invert_image_colors(input_path, output_path):
    image = Image.open(input_path)


    if image.mode == 'RGBA':
        r, g, b, a = image.split()
        rgb_image = Image.merge("RGB", (r, g, b))
        inverted_image = ImageOps.invert(rgb_image)
        r2, g2, b2 = inverted_image.split()
        final_image = Image.merge("RGBA", (r2, g2, b2, a))
    elif image.mode == 'RGB':
        final_image = ImageOps.invert(image)
    else:
        raise ValueError("Image format must be RGB or RGBA")

    final_image.save(output_path)


if __name__ == "__main__":
    input_file = input("Enter the path to the file: ")
    output_folder = input("Enter the path to save the file: ")

    if not os.path.isfile(input_file):
        print("This file does not exist.")
        exit(1)

    if not os.path.isdir(output_folder):
        print("This folder does not exist.")
        exit(1)

    filename = os.path.basename(input_file)
    output_file = os.path.join(output_folder, f"inverted_{filename}")

    invert_image_colors(input_file, output_file)
    print(f"The inverted image is saved in {output_file}")
    input("Press Enter to exit...")
