import os
import shutil
import numpy as np

rootdir = r'C:\Users\aboro\Documents\AI\CNNs\OneDrive_1_10-01-2025\Convolutional Neural Networks (CNNs)\training_set\Data_set'

categories = ['cats', 'dogs']
for category in categories:
    os.makedirs(os.path.join(rootdir, category), exist_ok=True)

all_files = os.listdir(rootdir)

for file in all_files:
    if file.lower() in categories or not os.path.isfile(os.path.join(rootdir, file)):
        continue
    if 'cat' in file.lower():
        shutil.move(os.path.join(rootdir, file), os.path.join(rootdir, 'cats', file))
    elif 'dog' in file.lower():
        shutil.move(os.path.join(rootdir, file), os.path.join(rootdir, 'dogs', file))

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

    for file in train_files:
        shutil.copy(os.path.join(source_dir, file), os.path.join(rootdir, 'train', category, file))

    for file in test_files:
        shutil.copy(os.path.join(source_dir, file), os.path.join(rootdir, 'test', category, file))











from PIL import Image
import os

# المسار الرئيسي للبيانات
rootdir = r'C:\Users\aboro\Documents\AI\CNNs\OneDrive_1_10-01-2025\Convolutional Neural Networks (CNNs)\training_set\Data_set\train'

# قائمة لتخزين خصائص الصور
image_properties = []

# قراءة كل الصور في المجلد الرئيسي
for file in os.listdir(rootdir):
    file_path = os.path.join(rootdir, file)
    if os.path.isfile(file_path) and file.lower().endswith(('.png', '.jpg', '.jpeg')):  # التأكد من أن الملف صورة
        try:
            with Image.open(file_path) as img:
                # خصائص الصورة
                width, height = img.size  # الأبعاد
                img_format = img.format  # الصيغة (JPEG, PNG, ...)
                img_mode = img.mode  # صيغة اللون (RGB, Grayscale, ...)
                
                # إضافة الخصائص إلى القائمة
                image_properties.append({
                    "file_name": file,
                    "width": width,
                    "height": height,
                    "format": img_format,
                    "mode": img_mode
                })
        except Exception as e:
            print(f"خطأ أثناء قراءة الصورة: {file}, {e}")

# عرض الخصائص
for prop in image_properties[:10]:  # عرض أول 10 صور
    print(prop)

# عدد الصور الإجمالي
print(f"عدد الصور الإجمالي: {len(image_properties)}")
