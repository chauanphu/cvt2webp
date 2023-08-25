import os
import shutil

def delete_contents(folder):
    for root, dirs, files in os.walk(folder, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            os.rmdir(dir_path)

def main():
    input_folder = "input"
    output_folder = "output"

    delete_contents(input_folder)
    delete_contents(output_folder)

if __name__ == "__main__":
    main()
