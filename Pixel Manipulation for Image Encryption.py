from PIL import Image
import os

def encrypt_image(image_path, key):
    """
    Encrypts an image by performing XOR operation on each pixel.

    Args:
        image_path (str): The path to the image file.
        key (int): The encryption key.

    Returns:
        None
    """
    if not os.path.exists(image_path):
        raise ValueError("Image path does not exist")

    image = Image.open(image_path)
    width, height = image.size
    pixels = image.load()

    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            encrypted_pixel = (pixel[0] ^ key, pixel[1] ^ key, pixel[2] ^ key)
            pixels[x, y] = encrypted_pixel

    image.save("encrypted_image.png")

def decrypt_image(image_path, key):
    """
    Decrypts an image by performing XOR operation on each pixel.

    Args:
        image_path (str): The path to the encrypted image file.
        key (int): The decryption key.

    Returns:
        None
    """
    if not os.path.exists(image_path):
        raise ValueError("Image path does not exist")

    image = Image.open(image_path)
    width, height = image.size
    pixels = image.load()

    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            decrypted_pixel = (pixel[0] ^ key, pixel[1] ^ key, pixel[2] ^ key)
            pixels[x, y] = decrypted_pixel

    image.save("decrypted_image.png")

def main():
    print("Image Encryption Tool")
    print("---------------------")

    while True:
        print("Options:")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            image_path = input("Enter the path to the image file: ")
            key = int(input("Enter the encryption key: "))
            try:
                encrypt_image(image_path, key)
                print("Image encrypted successfully!")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '2':
            image_path = input("Enter the path to the encrypted image file: ")
            key = int(input("Enter the decryption key: "))
            try:
                decrypt_image(image_path, key)
                print("Image decrypted successfully!")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
