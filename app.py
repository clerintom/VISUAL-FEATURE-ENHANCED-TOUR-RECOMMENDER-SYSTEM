import pickle
import streamlit as st
import requests
import pandas as pd




#def fetch_poster(movie_id):
    #url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
   # data = requests.get(url)
   # data = data.json()
    #full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    #return full_path


def retrieve_most_similar_products(image_name , cos_similarities_df):
    closes_images_list=[]
    match_score = []
    nb_closest_images = 5 # number of most similar images to retrieve
    #original = load_img(given_img, target_size=(imgs_model_width, imgs_model_height))
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
       closes_images_list.append(index.replace('/content/drive/MyDrive/style/',''))
       match_score.append(value)


    return closes_images_list , match_score


st.header('Visual Similarity Based Recommender System')
cos_similarities_df = pickle.load(open('item_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

lst = ['0_0_004.png','0_0_005.png','0_0_006.png','0_0_007.png','0_0_008.png']
  
# Calling DataFrame constructor on list
df = pd.DataFrame(lst,columns=['name'])
#st.write(df)

uploaded_file = st.file_uploader("Upload an Image")

if uploaded_file:
   file_name = f"/content/drive/MyDrive/style/{uploaded_file.name}"
   print(f"file name = {file_name}")

if st.button('Show Recommendation'):
    closest_imgs = []
    images_lst  , match_score_lst  =retrieve_most_similar_products(file_name,cos_similarities_df)

    st.header("Uploaded image")
    st.image(f"style/{uploaded_file.name}")
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
        
