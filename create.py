import cv2
import os


img = "mcdonalds.jpg"

im = cv2.imread(img)
im = cv2.resize(im, (100,100))
cv2.imwrite("mcdonalds.jpg",im)


def create_file():

    for file_type in ['neg']:
        for im in os.listdir(file_type):
            if file_type == "neg":
                line = "/home/csimmons155/Documents/CustomHaar2/" + file_type + "/"+im+"\n"
                with open("bg.txt", "a") as f:
                    f.write(line)

#uncomment to run 
#create_file()
