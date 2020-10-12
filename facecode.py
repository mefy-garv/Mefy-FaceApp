# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:54:05 2020

@author: Aruna

"""
"""

Register User using face capture

"""


import face_recognition
import cv2
import pandas as pd
import os


class FaceCapture:
    def FuncCap(username):
        
        ################# START VIDEO CAPTURE ###############################
        val=False
    
        vid = cv2.VideoCapture(0) 
          
        while(True): 
              
            # Capture the video frame by frame 
            ret, frame = vid.read() 
            font = cv2.FONT_HERSHEY_SIMPLEX 
            
            cv2.putText(frame,  
                'Not an existing user--PLEASE REGISTER--press q to capture ',  
                (50, 50),  
                font, 0.7,  
                (0, 255, 255),  
                1,  
                cv2.LINE_4) 
            
            # Display the resulting frame 
            cv2.imshow('Register Face ID', frame) 
              
            #'q' button is set as the quitting button----can be replaced by capture button on UI
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break

            file_name_path = './' + str(username) + '.png'
            cv2.imwrite(file_name_path, frame)
            login_user= face_recognition.load_image_file(str(username)+'.png')
            face_encoding_to_check=face_recognition.face_encodings(login_user)[0]
            df = pd.DataFrame(face_encoding_to_check, columns=["colummn"])
            df.to_csv(str(username)+'.csv', index=False)
        
        ##delete user png from database and keep only csv to save storage space
            
        for file in os.listdir('./'):
                if file.endswith('.png'):
                    os.remove(file) 
        
        val=True 
        
        vid.release() 
        # Destroy all the windows 
        cv2.destroyAllWindows()  
        return(val)
