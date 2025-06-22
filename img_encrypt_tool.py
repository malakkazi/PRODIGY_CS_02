from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    try:
        img = Image.open(image_path)
        img_array = np.array(img).astype('int16')

        encrypted_array = (img_array + key) % 256
        encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))

        encrypted_image.save(output_path)
        print("Image encrypted and saved as:", output_path)
    except Exception as e:
        print("Error during encryption:", e)

def decrypt_image(image_path, key, output_path):
    try:
        img = Image.open(image_path)
        img_array = np.array(img).astype('int16')

        decrypted_array = (img_array - key) % 256
        decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))

        decrypted_image.save(output_path)
        print("Image decrypted and saved as:", output_path)
    except Exception as e:
        print("Error during decryption:", e)

def main():
    print("=== Image Encryption & Decryption Tool ===")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    image_path = input("Enter the path to the image file: ")
    key = int(input("Enter the encryption/decryption key (e.g., 10): "))
    output_path = input("Enter the output file name (with .png/.jpg extension): ")

    if choice == 'e':
        encrypt_image(image_path, key, output_path)
    elif choice == 'd':
        decrypt_image(image_path, key, output_path)
    else:
        print("Invalid choice. Please type 'e' or 'd'.")

if __name__ == "__main__":
    main()
