import os
import shutil
import threading
from concurrent.futures import ThreadPoolExecutor


def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            process_file(root, file)


def process_file(folder_path, file_name):
    source_path = os.path.join(folder_path, file_name)
    extension = os.path.splitext(file_name)[1]
    destination_folder = os.path.join(folder_path, extension.strip('.').lower())

    os.makedirs(destination_folder, exist_ok=True)
    destination_path = os.path.join(destination_folder, file_name)

    shutil.move(source_path, destination_path)
    print(f"Moved {file_name} to {destination_path}")


def main():
    path = input("Write path to folder which we are sorting:")
    folder_to_process = path  # Replace with the path to your target folder
    num_threads = 4  # Number of threads to use

    if not os.path.exists(folder_to_process):
        return print(f"Folder '{folder_to_process}' does not exist.")
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.submit(process_folder, folder_to_process)


if __name__ == "__main__":
    main()
