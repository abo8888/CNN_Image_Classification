import os
import shutil
import numpy as np
from PIL import Image

# Define the root directory of the dataset
rootdir = r'C:\Users\aboro\Documents\AI\CNNs\OneDrive_1_10-01-2025\Convolutional Neural Networks (CNNs)\training_set\Data_set'

# Define image categories
categories = ['cats', 'dogs']

# Create category folders if they don't exist
for category in categories:
    os.makedirs(os.path.join(rootdir, category), exist_ok=True)

# Move images into their respective category folders
all_files = os.listdir(rootdir)

for file in all_files:
    file_path = os.path.join(rootdir, file)
    if file.lower() in categories or not os.path.isfile(file_path):
        continue
    if 'cat' in file.lower():
        shutil.move(file_path, os.path.join(rootdir, 'cats', file))
    elif 'dog' in file.lower():
        shutil.move(file_path, os.path.join(rootdir, 'dogs', file))

# Create training and testing folders
for category in categories:
    os.makedirs(os.path.join(rootdir, 'train', category), exist_ok=True)
    os.makedirs(os.path.join(rootdir, 'test', category), exist_ok=True)

    source_dir = os.path.join(rootdir, category)
    all_files = os.listdir(source_dir)

    np.random.shuffle(all_files)

    test_ratio = 0.25
    split_index = int(len(all_files) * (1 - test_ratio))

    train_files = all_files[:split_index]
    test_files = all_files[split_index:]

    # Copy training files
    for file in train_files:
        shutil.copy(os.path.join(source_dir, file), os.path.join(rootdir, 'train', category, file))

    # Copy testing files
    for file in test_files:
        shutil.copy(os.path.join(source_dir, file), os.path.join(rootdir, 'test', category, file))

# Analyze basic image properties
train_dir = os.path.join(rootdir, 'train')
image_properties = []

# Loop through all images in the training set
for category in categories:
    category_dir = os.path.join(train_dir, category)
    for file in os.listdir(category_dir):
        file_path = os.path.join(category_dir, file)
        if os.path.isfile(file_path) and file.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                with Image.open(file_path) as img:
                    width, height = img.size
                    img_format = img.format
                    img_mode = img.mode

                    image_properties.append({
                        "file_name": file,
                        "width": width,
                        "height": height,
                        "format": img_format,
                        "mode": img_mode
                    })
            except Exception as e:
                print(f"Error reading image: {file}, {e}")

# Display properties of first 10 images
for prop in image_properties[:10]:
    print(prop)

# Show total number of images analyzed
print(f"Total images analyzed: {len(image_properties)}")
