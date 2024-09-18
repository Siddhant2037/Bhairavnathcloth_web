import streamlit as st
from streamlit_lottie import st_lottie
import json

def app():
    st.title("✨Click Below Button To Visit Saree Section")
    st.markdown("""
    <style>
    .stButton>button {
        background-color: #ff0000; /* Blue*/
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 10px;
        border: 2px solid #FF5733;
    }

    .stButton>button:hover {
        background-color: white;
        color: #FF5733;
        border: 2px solid #FF5733;
    }
    </style>
    """, unsafe_allow_html=True)

    # Create the functional button
    if st.button("👰‍♀️Saree Section"):

        st.image('sr30.jpg')
        st.image(["sr1.jpg","sr2.jpg","sr3.jpg","sr4.jpg","sr5.jpg",
                  "sr6.jpg","sr7.jpg","sr8.jpg","sr9.jpg","sr10.jpg",
                  "sr11.jpg","sr12.jpg","sr13.jpg","sr14.jpg","sr15.jpg",
                  "sr16.jpg","sr17.jpg","sr18.jpg","sr19.jpg","sr20.jpg",
                  "sr21.jpg","sr22.jpg","sr23.jpg","sr24.jpg","sr25.jpg",
                  "sr26.jpg","sr27.jpg","sr28.jpg","sr29.jpg","sr30.jpg",
                  "sr31.jpg","sr32.jpg",
                  ])
    st.title("✨Click Below Button To Visit Womens Dress Section:-")

    st.markdown("""
        <style>
        .stButton>button {
            background-color: #ff0000; /* Blue*/
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 10px;
            border: 2px solid #FF5733;
        }

        .stButton>button:hover {
            background-color: white;
            color: #FF5733;
            border: 2px solid #FF5733;
        }
        </style>
        """, unsafe_allow_html=True)

    # Create the functional button
    if st.button("👗Dress Section"):
        st.image(["dr1.jpg","dr2.jpg","dr3.jpg","dr4.jpg","dr5.jpg","dr6.jpg",
                  "dr7.jpg","dr8.jpg","dr9.jpg","dr10.jpg","dr11.jpg","dr12.jpg",
                  "dr13.jpg","dr14.jpg","dr15.jpg","dr16.jpg","dr17.jpg","dr18.jpg",
                  "dr19.jpg","dr20.jpg","dr21.jpg","dr22.jpg","dr23.jpg"])


    st.sidebar.markdown("⚙️Site created by Siddhant....")

    # Load Lottie animations

    # def load_lottie_json(path: str):
    #     with open(path, "r") as f:
    #         return json.load(f)

    # def main():
    #     st.title("Select one ot the following catogrires")
    #
    #     # Load your JSON animations
    #     animation_1 = load_lottie_json("Animation - 1726314383121.json")
    #     animation_2 = load_lottie_json("Animation - 1726314407127.json")
    #     animation_3 = load_lottie_json("Animation - 1726314282958.json")
    #
    #     # Arrange animations using Streamlit columns
    #     col1, col2, col3 = st.columns(3)
    #
    #     with col1:
    #         st_lottie(animation_1, height=200, key="animation1")
    #         button = st.button("Click to get all latest offers related to jeans")
    #
    #     with col2:
    #         st_lottie(animation_2, height=200, key="animation2")
    #         button = st.button("Click to get all latest offers related to Hoodies")
    #         if button:
    #             st.image("1629362802-Neeraj Chopra.jpg")
    #
    #     with col3:
    #         st_lottie(animation_3, height=200, key="animation3")
    #         button = st.button("Click to get all latest offers related to Shirts")
    #         if button:
    #             st.image("1629362802-Neeraj Chopra.jpg")
    # return(main())


