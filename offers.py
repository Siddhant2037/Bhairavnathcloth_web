import streamlit as st
from streamlit_lottie import st_lottie
import json


def app():
    st.image('WhatsApp Image 2024-09-15 at 21.03.35_1abce9cd.jpg',width=600)
    st.sidebar.markdown("⚙️Site created by Siddhant....")
    # Load Lottie animations
    def load_lottie_json(path: str):
        with open(path, "r") as f:
            return json.load(f)

    # Layout and Lottie animations
    def main():
        st.title("Select one ot the following catogrires")

        # Load your JSON animations
        animation_1 = load_lottie_json("Animation - 1726314383121.json")
        animation_2 = load_lottie_json("Animation - 1726314407127.json")
        animation_3 = load_lottie_json("Animation - 1726314282958.json")

        # Arrange animations using Streamlit columns
        col1, col2, col3 = st.columns(3)

        with col1:
            st_lottie(animation_1, height=200,key="animation1")
            button1=st.button("Click to get all latest offers related to jeans")
            if button1:
                video_file = open('WhatsApp Video 2024-09-14 at 21.47.02_06f81cbd.mp4', 'rb')
                video_bytes = video_file.read()
                st.video(video_bytes, loop=True,
                         autoplay=True)
        with col2:
            st_lottie(animation_2, height=200, key="animation2")
            button2 = st.button("Click to get all latest offers related to Hoodies")
            if button2:
                video_file1 = open('WhatsApp Video 2024-09-14 at 22.51.51_16df28e3.mp4', 'rb')
                video_bytes1 = video_file1.read()
                st.video(video_bytes1, loop=True,
                         autoplay=True)

        with col3:
            st_lottie(animation_3, height=200, key="animation3")
            button3= st.button("Click to get all latest offers related to Shirts")
            if button3:
                video_file1 = open('WhatsApp Video 2024-09-15 at 19.42.44_2be5bd50.mp4', 'rb')
                video_bytes1 = video_file1.read()
                st.video(video_bytes1, loop=True,
                         autoplay=True
                             )




    def main2():

        # Load your JSON animations
        animation_4 = load_lottie_json("Animation - 1726314484672.json")
        animation_5 = load_lottie_json("Animation - 1726314461844.json")

        # Arrange animations using Streamlit columns
        col4, col5,= st.columns(2)

        with col4:
            st_lottie(animation_4, height=200,key="animation4")
            button4=st.button("Click to get all latest offers related to Undergarments",use_container_width=False)
            if button4:
                video_file1 = open('Macroman.mp4', 'rb')
                video_bytes1 = video_file1.read()
                st.video(video_bytes1, loop=True,
                         autoplay=True
                         )


        with col5:
            st_lottie(animation_5, height=200, key="animation5")
            button5= st.button("Click to get all latest offers related to Sando")
            if button5:
                video_file1 = open('Ramraj.mp4', 'rb')
                video_bytes1 = video_file1.read()
                st.video(video_bytes1, loop=True,
                         autoplay=True)

    return(main(),main2())

        #with col6:
            #button2 = st.button("Click to get all latest offers related to Sirts")
            #if button2:
             #   st.image("1629362802-Neeraj Chopra.jpg")


    # if __name__ == "__main__":
    #     main()
    #     main2()

        # Load Lottie animations
        # if button:
        #     st.image("1629362802-Neeraj Chopra.jpg")