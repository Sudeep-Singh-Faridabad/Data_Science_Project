#Import streamlit library and other required libraries
import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Provide the title for the web app
st.title("Automated Visual Inspection of Welds")

#Provide subheader for the web app
st.subheader("This web app is used to detect visual defects in welds")

#Provide the text for the web app
st.text('Please select the image from your drive for the visual inspection of welds')

#Write markdown text for the web app
st.markdown('### Please click below button to uplaod image')

# Read the image using opencv
#img = cv2.imread('good-weld-vs-bad-weld-otc-daihen.png')[:,:,::-1]
#Load the image in app
#st.image(img, caption='Sample Image')

# Upload the image using file uploader
img = st.file_uploader("Choose an image...", type=["jpg", 'png', 'jpeg'])

#show the uploaded image
if img is not None:
        st.image(img, caption='Image for weld VT', width=300)

#Set button for the web app
if st.button('Pleae click here to get the result'):
    #Provide the text for the web app
    st.header('Defects found in the weld')
    st.text('\t1. Welding bead is not smooth\n')
    st.text('\t2. Welding bead is not uniform\n')
    st.text('\t3. Welding bead is not continuous\n')
    st.text('\t4. Welding bead is not of proper size\n')
    st.text('\t5. Welding bead is not of proper shape\n')

#Provide the header for the web app
st.header('A Machine Vision App developed by a welding expert (Sudeep Singh)')
