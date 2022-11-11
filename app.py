import pickle
import streamlit as st
import pandas as pd

from PIL import Image

def load_image(image_file):
	img = Image.open(image_file)
	return img

def retrieve_most_similar_products(image_name , cos_similarities_df):
    closes_images_list=[]
    match_score = []
    nb_closest_images = 5 # number of most similar images to retrieve
    closest_imgs = cos_similarities_df[image_name].sort_values(ascending=False)[1:nb_closest_images+1]
    closest_imgs_scores = cos_similarities_df[image_name].sort_values(ascending=False)[1:nb_closest_images+1]
    #st.write(closest_imgs)
    #st.write("test")
    #st.write(type(closest_imgs))
    #st.write(closest_imgs.index.tolist())
    #for i in range(0,len(closest_imgs)):
      #st.write(closest_imgs[i])
        
    #st.write(closest_imgs.tolist()) 
    for index, value in closest_imgs.items():
       #st.write(f"Index : {index}, Value : {value}")
       closes_images_list.append(index)
       match_score.append(value)

    return closes_images_list , match_score


st.header('Visual Similarity Based Recommender System')
cos_similarities_df = pickle.load(open('item_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

uploaded_file = st.file_uploader("Upload an Image",type=["png","jpg","jpeg"])

if uploaded_file:
   file_name = uploaded_file.name
   print(f"file name = {file_name}")

if st.button('Show Recommendation'):
    closest_imgs = []
    images_lst  , match_score_lst  =retrieve_most_similar_products(file_name,cos_similarities_df)

    st.header("Uploaded image")
    st.image(load_image(uploaded_file),width=250)
    st.header("Similar images based on recommendation")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(f"style/{images_lst[0]}")
        st.text(match_score_lst[0])
        
    with col2:
        st.image(f"style/{images_lst[1]}")
        st.text(match_score_lst[1])
        

    with col3:
        st.image(f"style/{images_lst[2]}")
        st.text(match_score_lst[3])
        
    with col4:
        st.image(f"style/{images_lst[3]}")
        st.text(match_score_lst[3])
        
    with col5:
        st.image(f"style/{images_lst[4]}")
        st.text(match_score_lst[4])
        
