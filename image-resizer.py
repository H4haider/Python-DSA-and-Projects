import PIL as pil

input_path = 'image path here'
destination_path = 'destination path here'
width = int(input("Enter the new width: "))
height = int(input("Enter the new height: "))

try:
 image = pil.Image.open(input_path)
 resized_image = image.resize((width, height))
 resized_image.save(destination_path)
 print("Image Resized Successfully")

except FileNotFoundError:
    print("Error: The input image file was not found.")

except ValueError:
    print("Error: Please enter valid integers for width and height.")

