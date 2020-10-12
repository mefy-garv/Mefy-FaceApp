# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 07:12:28 2020

@author: Aruna
"""
import os
from flask import Flask, url_for, render_template, redirect, session,request                    
import cv2
import numpy as np
import base64

"""
Flask App:

login-if user identified, success
else: prompts to register webpage"""

import faceLoginApp
import facecode

app = Flask(__name__)
recognizer = faceLoginApp.UserLogin
captureface=facecode.FaceCapture

############################# HOME PAGE #######################################

@app.route('/', methods=['GET', 'POST'])
def home():
	""" Session control"""
	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		if request.method == 'POST':

			return render_template('index.html') 
		return render_template('index.html')
    
############################ LOGIN PAGE ########################################

@app.route('/login', methods=['GET', 'POST'])
def login():        
        ret = recognizer.captureAndCompare('aru')
        
        if ret==1:
            return("Sucessfully logged in. Welcome to MEFY")
        else:
            
            return redirect(url_for('register'))


########################## REGISTER PAGE ############################################


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['username']
        ret=captureface.FuncCap(name)
        if ret==1:
            return redirect(url_for('home'))
        else:
        
                return render_template('index.html')
    return render_template('register.html')

########################## LOGOUT PAGE (dormant) ###############################

@app.route("/logout")
def logout():
	"""Logout Form"""
	session['logged_in'] = False
	return redirect(url_for('home'))

#########################  MAIN FUNCTION ##################################


if __name__ == '__main__':
    app.run()
	#app.debug = True
	
