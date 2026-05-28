from PIL import Image
import os
from colorama import Fore, init

init(autoreset=True)

print(Fore.CYAN + "=" * 55)
print(Fore.YELLOW + "- PIXEL ART GENERATOR")
print(Fore.GREEN + "- Created by: ABHIRAM")
print(Fore.MAGENTA + "- Instagram: themabhiram (https://www.instagram.com/themabhiram/)")
print(Fore.CYAN + "=" * 55)

while True:
    folder = input(Fore.WHITE + "\nEnter image folder path (or type 'exit'): ")

    if folder.lower() == "exit":
        print(Fore.YELLOW + "Exiting...")
        break

    if not os.path.exists(folder):
        print(Fore.RED + "Invalid folder path")
        continue

    # Get image files
    images = [f for f in os.listdir(folder)
              if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    if not images:
        print(Fore.RED + "No images found in folder")
        continue

    # Show images with index
    print(Fore.YELLOW + "\nAvailable Images:")
    for i, img in enumerate(images):
        print(Fore.CYAN + f"[{i}] {img}")

    # Select image
    try:
        index = int(input(Fore.WHITE + "\nEnter image index: "))
        selected_image = images[index]
    except:
        print(Fore.RED + "Invalid index")
        continue

    img_path = os.path.join(folder, selected_image)

    save_path = input(Fore.WHITE + "Enter folder path to save pixel image: ")

    if not os.path.exists(save_path):
        print(Fore.RED + "Invalid save path")
        continue

    try:
        size = int(input(Fore.WHITE + "Enter pixel size (e.g. 50): "))
    except:
        print(Fore.RED + "Invalid number")
        continue

    try:
        print(Fore.BLUE + "Processing image...")

        img = Image.open(img_path)

        small = img.resize((size, size), resample=Image.BILINEAR)
        pixel = small.resize(img.size, Image.NEAREST)

        output_name = f"pixel_{selected_image}"
        output_path = os.path.join(save_path, output_name)

        pixel.save(output_path)

        print(Fore.GREEN + f"Saved: {output_name}")

    except Exception as e:
        print(Fore.RED + f"Error: {e}")

input(Fore.MAGENTA + "\nPress Enter to exit...")