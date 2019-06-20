import cv2
import numpy as np
import os
import csv

#folder to save the recorded video
if not os.path.exists('videos'):
    os.makedirs('videos')
#executing the video capture file
os.system('python3 record.py')

#executing the video to image file
os.system('python3 face_crop.py')

#creating a text file to get the age and gender of the images sent
file = open("out.txt", "w")


#passing each image to predict the age and gender which will be stored in a text file
people = [person for person in os.listdir("faces/")]
for i in people:
	os.system('python3 AgeGender.py --input '+'faces/'+i)

#converting the txt file to a csv file
with open('out.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('out.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('title', 'gender','gconf','age','aconf'))
        writer.writerows(lines)

#play video from the ages
os.system('python3 ad_display.py')