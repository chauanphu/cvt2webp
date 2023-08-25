from PIL import Image
import os

def convert_to_webp(input_path, output_folder):
    try:
        image = Image.open(input_path)
        output_filename = os.path.splitext(os.path.basename(input_path))[0] + ".webp"
        output_path = os.path.join(output_folder, output_filename)
        image.save(output_path, "webp")
        print(f"Converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

def main():
    input_folder = "input"
    output_folder = "output"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_formats = [".png", ".jpg", ".jpeg"]

    for filename in os.listdir(input_folder):
        if any(filename.lower().endswith(format) for format in image_formats):
            input_path = os.path.join(input_folder, filename)
            convert_to_webp(input_path, output_folder)

if __name__ == "__main__":
    main()
