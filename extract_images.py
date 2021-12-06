import os
import shutil


BASE_DIRECTORY = "./Package_1194002/results/P001/0.C.2"
DESTINATION = "./extracted_images"

for subdir, dirs, files in os.walk(BASE_DIRECTORY):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".jpg"):
            identification = "".join(filepath.split(BASE_DIRECTORY)[1]).split("/")[1]
            print("Copying file at:", filepath, "...")
            new_file_name = identification + "_" + file
            shutil.copyfile(filepath, DESTINATION + "/" + new_file_name)

