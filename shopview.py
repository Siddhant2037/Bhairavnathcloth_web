import streamlit as st
def app():
    st.title("🤵Mens Wear")
    st.header("⭐Total of 4000 sq.feats area is covered by mega Showroom")
    col1,col2,col3=st.columns([1,1,1])
    with col1:
        st.image('g5.jpg')
    with col2:
        st.image('g2.jpg')
    with col3:
        st.image('g3.jpg')
    col4, col5= st.columns([1, 1])
    with col4:
        st.image('g1.jpg')
    with col5:
        st.image('g4.jpg')
    st.image('g5.jpg')
    st.image('g6.jpg')
    st.image('g7.jpg')
    st.image('g8.jpg')
    st.image('g9.jpg')
    st.image('g10.jpg')
    st.image('g11.jpg')
    st.image('g12.jpg')
    st.sidebar.markdown("⚙️Site created by Siddhant.....")
    st.title("👰‍♀️Womens Wear")
    st.image('w1.jpg')
    st.image('w2.jpg')
    st.image('w3.jpg')
    st.image('w4.jpg')
    st.image('w5.jpg')
    st.image('w6.jpg')
    st.image('w7.jpg')
    st.image('w8.jpg')
    st.image('w9.jpg')
