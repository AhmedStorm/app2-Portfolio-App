import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv",sep=";")
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)



with col1:
    st.image("images/photo.png")
with col2:
    st.title("Ahmed Barhoma")
    st.info("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
    dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
    commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
    pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
    laborum.""")


st.write("Below you can find some of the apps i have built in python, Feel free to contact me")
col3,empty, col4 = st.columns([1.5,0.5,1.5])

with col3:
    for index,item in df[:10].iterrows():
        st.title(item['title'])
        st.write(item['description'])
        st.image(f"images/{item['image']}")
        st.write(f"[Source Code]({item['url']})")

with col4:
    for index,item in df[10:].iterrows():
        st.title(item['title'])
        st.write(item['description'])
        st.image(f"images/{item['image']}")
        st.write(f"[Source Code]({item['url']})")
