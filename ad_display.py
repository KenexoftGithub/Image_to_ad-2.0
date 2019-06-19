import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('out.csv')
#X = gender , y = age , z = images names , X1 = gender confidence , y1 = age confidence
z = dataset.iloc[:, 0].values
X = dataset.iloc[:, 1].values
X1 = dataset.iloc[:, 2].values
y = dataset.iloc[:, 3].values
y1 = dataset.iloc[:, 4].values
#age and gnder are lists to hold the values of age and gender after optimizing
age = []
gen = []
#flag variable is used when we have the case of an image having 2 confidence limits on age and gender
flag = 0
#removing the data based on confidence limits
for i in range(0,len(X)):
    #checking if the next frame is checked already
    if flag == 1:
        flag = 0
        continue
    if i != (len(X)-1):
        #checking if the next frame is same as the present frame
        if z[i] == z[i+1] :
            flag=1
            #checking the confidence limits of gender's
            if X1[i]<X1[i+1]:
                #print("entered for 2nd img great conf")
                #print(X1[i],X1[i+1],"\n")
                age.append(y[i+1])
                gen.append(X[i+1])
            elif X1[i]>X1[i+1]:
                age.append(y[i])
                gen.append(X[i])
            elif X1[i] == X1[i+1]:
                #checking the confidence limits of age's
                if y1[i]<y1[i+1]:
                    age.append(y[i+1])
                    gen.append(X[i+1])
                else:
                    age.append(y[i])
                    gen.append(X[i])
        else:
            age.append(y[i])
            gen.append(X[i])
    #checking the last frame if its already checked
    elif z[i] == z[i-1]:
        continue
    else:
        age.append(y[i])
        gen.append(X[i])
#print(y,age)


#to get the gender of the refined age as per the population and to et the exact age group whihc has the highest population
gender = []
reqage = 0
#array to get the highly populated age group
a=[0,0,0,0,0,0,0,0]
for i in age:
    #print("\ni=",i)
    if i == ' (0-2) ':
        a[0] = a[0] + 1
    elif i == ' (3-7) ':
        a[1] = a[1] + 1
    elif i == ' (8-12) ':
        a[2] = a[2] + 1
    elif i == ' (13-19) ':
        a[3] = a[3] + 1
    elif i == ' (20-30) ':
        a[4] = a[4] + 1
    elif i == ' (31-40) ':
        a[5] = a[5] + 1
    elif i == ' (41-59) ':
        a[6] = a[6] + 1
    elif i == ' (60-100) ':
        a[7] = a[7] + 1
print("\na=",a)
#print('age group = ',reqage)
temp = 0
#loop to get the highly populated age group
for i in range(8):
    if temp<a[i]:
        temp=a[i]
        pos=i
#to get the required age group of the highest populated age group
if pos == 0:
    reqage = ' (0-2) '
elif pos == 1:
    reqage = ' (3-7) '
elif pos == 2:
    reqage = ' (8-12) '
elif pos == 3:
    reqage = ' (13-19) '
elif pos == 4:
    reqage = ' (20-30) '
elif pos == 5:
    reqage = ' (31-40) '
elif pos == 6:
    reqage = ' (41-59) '
else:
    reqage = ' (60-100) '

#getting the genders of the highly populated age group
for i in range(len(age)):
    if age[i] == reqage:
        gender.append(gen[i])
print("gender = ",gender)
#variables to check the number of males and females
male=0
female=0
#checking the number of males and females
for i in gender:
    #print(i,"\t")
    if i == ' Male ':
        male = male + 1
    elif i == ' Female ':
        female = female + 1
    else:
        continue
print("males=",male,"\n females=",female)

print(pos)
#list of the groups through which ad's should be trigerred
ageList = ['(0-2)', '(3-7)', '(8-12)', '(13-19)', '(20-30)', '(31-40)', '(41-59)', '(60-100)']
print(ageList[pos],a[pos])

#playing the video based on the age groups highest occured population
import cv2 
#videos holds the list of ads to be played
videos = ['ads/advert1.mp4','ads/advert2.mp4','ads/advert3.mp4','ads/advert4.mp4','ads/advert5.mp4','ads/advert6.mp4','ads/advert7.mp4','ads/advert8.mp4']
   
# Create a VideoCapture object and read from input file 
cap = cv2.VideoCapture(videos[pos]) 
   
# Check if camera opened successfully 
if (cap.isOpened()== False):  
  print("Error opening video  file") 
   
# Read until video is completed 
while(cap.isOpened()): 
      
  # Capture frame-by-frame 
  ret, frame = cap.read() 
  if ret == True: 
   
    # Display the resulting frame 
    cv2.imshow('Frame', frame) 
   
    # Press Q on keyboard to  exit 
    if cv2.waitKey(25) & 0xFF == ord('q'): 
      break
   
  # Break the loop 
  else:  
    break
   
# When everything done, release  
# the video capture object 
cap.release() 
   
# Closes all the frames 
cv2.destroyAllWindows() 


