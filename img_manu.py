from PIL import Image

def rotate_image(image_path, degrees):
    try:
        with Image.open(image_path) as img:
            rotated_img = img.rotate(degrees, expand=True)
            rotated_img.show()
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    image_path = input("Enter the path to the image file: ")
    degrees = int(input("Enter the rotation angle in degrees: "))

    rotate_image(image_path, degrees)

