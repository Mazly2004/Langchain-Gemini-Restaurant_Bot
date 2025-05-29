<<<<<<< HEAD
import streamlit as st
import utils

st.title("Mazly Restaurant Generator")

chosen_cuisine = st.sidebar.selectbox("Select Cuisine", ("Indian", "Chinese", "Mexican", "Italian", "Japanese", "Thai",
                                         "French", "Greek", "American", "Mediterranean", "Spanish", "Korean",
                                         "Vietnamese", "Ethiopian", "Middle Eastern", "Brazilian", "German", 
                                         "Caribbean", "Peruvian", "Moroccan"))

if chosen_cuisine:
    answer  = utils.generate_name_and_items(chosen_cuisine=chosen_cuisine)
    st.header(answer["restaurant_name"].strip())

    menu_items = answer["menu_items"].strip().split(",")
    st.write("**Menu Items**")
    
    for item in menu_items:
=======
import streamlit as st
import utils

st.title("Mazly Restaurant Generator")

chosen_cuisine = st.sidebar.selectbox("Select Cuisine", ("Indian", "Chinese", "Mexican", "Italian", "Japanese", "Thai",
                                         "French", "Greek", "American", "Mediterranean", "Spanish", "Korean",
                                         "Vietnamese", "Ethiopian", "Middle Eastern", "Brazilian", "German", 
                                         "Caribbean", "Peruvian", "Moroccan"))

if chosen_cuisine:
    answer  = utils.generate_name_and_items(chosen_cuisine=chosen_cuisine)
    st.header(answer["restaurant_name"].strip())

    menu_items = answer["menu_items"].strip().split(",")
    st.write("**Menu Items**")
    
    for item in menu_items:
>>>>>>> 11ae12367cda390b83bebd879275fb72c1346f9d
        st.write("-",item)