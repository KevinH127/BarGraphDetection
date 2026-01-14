import os
import random
import shutil

# -------------------------------
# Configuration
# -------------------------------

dataset_root = 'DataPreprocessingScripts/dataunpacked'
images_directory = os.path.join(dataset_root, "images/")
labels_directory = os.path.join(dataset_root, "labels/")

train_split_ratio = 0.9  # 80% training, 20% validation
random_seed = 42

image_extensions = ".png"

# -------------------------------
# Output Directories
# -------------------------------

train_images_directory = "TrainingImages/BusyEnvBarGraphs/Labelled/data/train/images"
val_images_directory = "TrainingImages/BusyEnvBarGraphs/Labelled/data/val/images"

train_labels_directory = "TrainingImages/BusyEnvBarGraphs/Labelled/data/train/labels"
val_labels_directory = "TrainingImages/BusyEnvBarGraphs/Labelled/data/val/labels"

# -------------------------------
# Collect Image Files
# -------------------------------

all_image_filenames = [
    filename for filename in os.listdir(images_directory)
    if filename.lower().endswith(image_extensions)
]

random.seed(random_seed)
random.shuffle(all_image_filenames)

split_index = int(len(all_image_filenames) * train_split_ratio)

training_images = all_image_filenames[:split_index]
validation_images = all_image_filenames[split_index:]

# -------------------------------
# Helper Function
# -------------------------------

def copy_image_and_label(
    image_filename,
    destination_images_directory,
    destination_labels_directory
):
    image_source_path = os.path.join(images_directory, image_filename)
    label_filename = os.path.splitext(image_filename)[0] + ".txt"
    label_source_path = os.path.join(labels_directory, label_filename)

    shutil.copy(image_source_path, destination_images_directory)

    if os.path.exists(label_source_path):
        shutil.copy(label_source_path, destination_labels_directory)
    else:
        print(f"Warning: Missing label for {image_filename}")

# -------------------------------
# Copy Training Files
# -------------------------------

for image_filename in training_images:
    copy_image_and_label(
        image_filename,
        train_images_directory,
        train_labels_directory
    )

# -------------------------------
# Copy Validation Files
# -------------------------------

for image_filename in validation_images:
    copy_image_and_label(
        image_filename,
        val_images_directory,
        val_labels_directory
    )

print("Dataset successfully split into training and validation sets.")
