import cv2
import os
import imageio


DETECTION_RESULTS = "./exp19"
ORIGINAL_IMAGES = "./test_set"

gif_images = []
for subdir, dirs, files in os.walk(DETECTION_RESULTS):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".jpg"):
            filepath_og = ORIGINAL_IMAGES + "/" + file
            image = cv2.imread(filepath_og)
            image = cv2.resize(image, (640, 640))

            detection_image = cv2.imread(filepath)
            detection_image = cv2.resize(detection_image, (640, 640))

            cv2.imshow(file, image)
            cv2.waitKey(100)
            cv2.imshow(file, detection_image)
            cv2.waitKey(100)

            gif_images.append(image)
            gif_images.append(detection_image)



cv2.destroyAllWindows()

imageio.mimsave('./movie.gif', gif_images, fps=3)
