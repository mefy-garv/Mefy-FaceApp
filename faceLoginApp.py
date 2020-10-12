# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 14:12:04 2020

@author: Aruna


"""

import face_recognition
import cv2
import pandas as pd
import os

############### FACE CAPTURE FOR LOGIN #################

class UserLogin:
    def captureAndCompare(name):
        vid = cv2.VideoCapture(0) 
          
        while(True): 
              
            # Capture the video frame by frame 
            ret, frame = vid.read() 
            font = cv2.FONT_HERSHEY_SIMPLEX 
            cv2.putText(frame,  
                'Existing User---Please Login---press q to capture',  
                (50, 50),  
                font,0.7,  
                (0, 0, 255),  
                1,  
                cv2.LINE_4) 
            cv2.imshow('frame', frame) 
              
            #'q' button is set as the quitting button----can be replaced by capture button on UI
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break
       
        vid.release() 
        # Destroy all the windows 
        cv2.destroyAllWindows()  
        
        
        ############### USING FACE ENCODINGS #########################
       
        users=[]
        unknown=[]
        
        face_encoding_to_check=face_recognition.face_encodings(frame)[0]        
        ##sizeOfUserDatabase=9###### change to dynamic and received from app database
        
        #Search for csv files to match encodings
        for file in os.listdir('./'):
            if file.endswith('.csv') and file != 'login.csv':
                users.append(file)
        print(users)
        
        
        ##checks if user matches to any existing database  and gives boolean decision

        result=[]        
        for user in users:
           
            col_list = ["colummn"]
            usercsv=pd.read_csv(user, usecols=col_list)
            userEncodings = usercsv.colummn.tolist()        
            unknown.append(userEncodings)   
            decision=face_recognition.compare_faces([userEncodings], face_encoding_to_check,tolerance=0.4)
            result.append(decision)
            print("Same?",decision)
            
        ###for 2 or more faces detected and matched in database, check which has closer match to its resp.matching face
        
        ct=0
        set=0
        
        for i in result:
            if i==[True]:
                eucli_dist=face_recognition.api.face_distance(face_encoding_to_check,unknown)
                print(eucli_dist)
                allow_user = min(eucli_dist) 
                index = [i for i, j in enumerate(eucli_dist) if j == allow_user] 
                set=1
                value=1
            elif i==[False] and set!=1:
                value=0
        if value==1:
                print("index :",index)
                print("Allow user with "+str(allow_user) +" eucli_dist")              
                ###display welcome

        else:
            print("denied")
            #display denied entry
            #Switches back to home page to allow user to register
               
            ct=ct+1
        return value


        
        
