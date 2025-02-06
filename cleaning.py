import os

train_path = "C:\Users\aaron\OneDrive\Desktop\Projects\a-bit-too-handy\A-bit-too-Handy\archive (1)\train\train"
val_path = "C:\Users\aaron\OneDrive\Desktop\Projects\a-bit-too-handy\A-bit-too-Handy\archive (1)\val\val"
img_size = 224

print("Checking path:", train_path)
print("Folders inside train:", os.listdir(train_path))

for subfolder in os.listdir(train_path):
    subfolder_path = os.path.join(train_path, subfolder)

    if os.path.isdir(subfolder_path):  # Ensure it's a folder
        for image_file in os.listdir(subfolder_path):  # Iterate through images
            image_path = os.path.join(subfolder_path, image_file)
            print(f"Found image: {image_path}")  # Debugging output