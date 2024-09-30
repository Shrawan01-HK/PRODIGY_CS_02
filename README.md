# Pixel-Manipulation-for-Image-Encryption
# Image Encryption Tool

This repository features a Python tool for encrypting and decrypting images using a simple XOR operation. The tool leverages the Pillow (PIL) library to manipulate image pixels, allowing users to secure their images with a specified encryption key.

## Overview

The tool provides an easy interface to either encrypt an image by modifying its pixel values or decrypt an encrypted image back to its original form. The XOR operation is used for both processes, ensuring that the same key can be used for encryption and decryption.

### Key Features

- **Image Encryption**: Secure an image by performing an XOR operation on each pixel using a user-defined key.
- **Image Decryption**: Restore the original image using the same key with the decryption process.
- **User-Friendly Interface**: A command-line interface allows users to choose between encrypting or decrypting images easily.
- **Error Handling**: The tool checks for valid image paths and handles errors gracefully, providing informative feedback.

## How It Works

1. **Encrypt Image**:
   - The `encrypt_image` function reads the image from the specified path, applies the XOR operation to each pixel using the provided key, and saves the result as "encrypted_image.png".

2. **Decrypt Image**:
   - The `decrypt_image` function reads the encrypted image, applies the XOR operation with the same key to retrieve the original image, and saves it as "decrypted_image.png".

3. **Main Function**:
   - The `main` function facilitates user interaction, prompting for image paths and keys while managing encryption and decryption options.

## Example Usage

To encrypt an image:
```
Choose an option: 1
Enter the path to the image file: path/to/image.png
Enter the encryption key: 123
Image encrypted successfully!
```

To decrypt an image:
```
Choose an option: 2
Enter the path to the encrypted image file: encrypted_image.png
Enter the decryption key: 123
Image decrypted successfully!
```

## Requirements

- Python 3.x
- Pillow library (`pip install Pillow`)

## License

This project is open-source and available under the MIT License. Contributions and improvements are welcome!
