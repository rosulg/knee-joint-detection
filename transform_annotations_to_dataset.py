import json
import os
import shutil
from datetime import datetime

import cv2

COCO_FORMAT_ANNOTATIONS_PATH = "./annotations/via_project_4Dec2021_16h55m_coco.json"

# Create dataset structure
folder_name = datetime.now().strftime("knee-%d-%m-%Y-%H:%M:%S")
images_dir = folder_name + "/images/"
labels_dir = folder_name + "/labels/"
os.mkdir(folder_name)
os.mkdir(images_dir)
os.mkdir(labels_dir)

with open(COCO_FORMAT_ANNOTATIONS_PATH) as f:
    data = json.load(f)

    images = data["images"]
    annotations = data["annotations"]

    for annotation in annotations:
        bbox = annotation["bbox"]
        image_id = annotation["image_id"]

        # find corresponding image to annotation
        for image in images:
            if image["id"] == image_id:
                filename = image["file_name"]

                img_path = "./extracted_images/" + filename

                # convert to x, y to center x, y
                x, y, w, h = bbox
                bbox[0] = x + w / 2
                bbox[1] = y + h / 2

                # Normalize detection
                img = cv2.imread(img_path)
                width, height, _ = img.shape
                normalized_bbox = [round(bbox[i] / width, 5) if i % 2 == 0 else round(bbox[i] / height, 5) for i in
                                   range(len(bbox))]

                class_id = annotation["category_id"]
                entry = f"{class_id} " + " ".join(map(lambda j: str(j), normalized_bbox))

                # Create entry
                with open(labels_dir + filename[:-4] + ".txt", "a") as file:
                    file.write(entry + "\n")

                # Copy image that was annotated
                shutil.copyfile(img_path, images_dir + filename)
                break

print("Labels count:", len(os.listdir(labels_dir)))
print("Copied images count:", len(os.listdir(images_dir)))


