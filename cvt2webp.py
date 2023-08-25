from PIL import Image
import os

def convert_to_webp(input_path, output_path):
    try:
        image = Image.open(input_path)
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

    for root, _, files in os.walk(input_folder):
        for filename in files:
            if any(filename.lower().endswith(format) for format in image_formats):
                input_path = os.path.join(root, filename)
                relative_path = os.path.relpath(input_path, input_folder)
                output_path = os.path.join(output_folder, os.path.splitext(relative_path)[0] + ".webp")
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                convert_to_webp(input_path, output_path)

if __name__ == "__main__":
    main()
