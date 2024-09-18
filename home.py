import streamlit as st
import json
from streamlit_lottie import st_lottie


def app():
    st.image('blue logo.jpg')
    # p1=st.Page(
    #     "pages/Offers_for_mens.py",
    #     title="Offers for Mens",
    #     icon=":material/query_stats:"
    # )
    # p2=st.Page(
    #     "pages/Offers_for_ Womens.py",
    #     title="Offers for Womens"
    # )
    #
    # pg = st.navigation([p1,p2])
    # pg.run()

    st.header("Welcome to.....\n")
    st.title("\nBhairavnath cloth stores")
    st.text(f"Chief Owner:-Mayur Bhairavnath Tak")
    st.text(f"CO.Owner:-Kumudini Tak")
    st.markdown("""
                <a href="https://www.google.com/maps/place/Bhairavnath+Cloth+Stores/@19.6785797,74.0860829,17z/data=!3m1!4b1!4m6!3m5!1s0x3bdda9175d0bf28b:0xf6965d9ab60a7ae4!8m2!3d19.6785797!4d74.0886578!16s%2Fg%2F11g71c">
                    <button style="background-color:blue; border-radius:10px; padding:5px; border:none;">
                        🚗Track our Shop now
                    </button>
                </a>
                """, unsafe_allow_html=True)

    def load_lottie_json(path: str):
        with open(path, "r") as f:
            return json.load(f)

    animation_1 = load_lottie_json("Animation - 1726307387181.json")
    st_lottie(animation_1, height=500, width=500, key="animation1")
    st.header("Bhairavnath Cloth Stores in Chas,Nashik")
    st.markdown(
        "\tThe craze for readymade garments in India has witnessed an unprecedented surge, reflecting a dynamic shift towards convenience, style, and a rapidly evolving fashion culture. With a blend of traditional and contemporary designs, readymade garments have become a fashion staple, catering to the diverse tastes of the Indian populace.Selecting the right provider for readymade garments is crucial for meeting diverse fashion needs with quality and reliability. In the realm of readymade garments, Bhairavnath Cloth Stores emerges as a symbol of excellence, dedicated to delivering top- notch services for various fashion requirements. With a rich history dating back to 1985, they have been an integral part of numerous success stories, offering high-quality readymade garments tailored to diverse preferences. Their commitment to perfection and years of experience ensure that your quest for reliable readymade garments concludes here. Whether you are looking for everyday wear, special occasion outfits, or custom designs, trust Bhairavnath Cloth Stores to provide the best-in- class readymade garment solutions.")
    st.header("📍Location and Overview")
    st.markdown(
        "Situated in Nashik, Bhairavnath Cloth Stores is strategically located in the heart of Chas. With a track record dating back to 1985, Bhairavnath Cloth Stores has earned a trusted reputation for delivering readymade garment solutions that meet the highest industry standards.")
    st.header("🧑‍🔧Services Offered")
    st.markdown(
        "At Bhairavnath Cloth Stores, a diverse range of readymade garments tailored to various fashion needs is offered. While providing various types of products, their specialisation lies in Shop In Store. With a commitment to quality and innovation, Bhairavnath Cloth Stores has been a trusted provider in the industry for years. Their team of experienced professionals ensures that each garment is precisely designed and crafted to complement specific preferences. The style and performance of Bhairavnath Cloth Stores readymade garments make them the preferred choice for customers. With a focus on customer comfort and satisfaction, these amenities are thoughtfully curated to elevate your interaction with their services.")
    st.header("🤔Why Choose Bhairavnath Cloth Stores?")
    st.markdown(
        "Bhairavnath Cloth Stores's profound understanding of the intricacies of diverse fashion preferences sets them apart in the field of readymade fashion. They consistently demonstrate their commitment to ensuring that every detail of the readymade garments is meticulously crafted to perfection, meeting and exceeding the expectations of their clients. Bhairavnath Cloth Stores's remarkable reputation, with a rating of, is a testament to the unwavering satisfaction of their clients. Their dedication to maintaining the highest standards of product quality and service is unwavering, guaranteeing garment solutions that exceed your expectations. In the intricate world of readymade garments, Bhairavnath Cloth Stores emerges as a trusted partner, a beacon of reliability, and a guarantor of fashion solutions that meet your diverse needs. Their prime location, coupled with their wealth of experience and unwavering commitment to perfection, makes them the ideal choice to fulfil your readymade garment needs.")
    st.header("⭐Click Options to know more about us")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("""
            <a href="https://www.justdial.com/Nashik/Bhairavnath-Cloth-Stores-Chas/0253PX253-X253-180321070918-X7J3_BZDET" target="_blank">
                <button style="background-color:red; border-radius:10px; padding:5px; border:black;">
                   ℹ️ Go to Just Dial
                </button>
            </a>
            """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <a href="https://www.google.com/maps/place/Bhairavnath+Cloth+Stores/@19.6785797,74.0860829,17z/data=!3m1!4b1!4m6!3m5!1s0x3bdda9175d0bf28b:0xf6965d9ab60a7ae4!8m2!3d19.6785797!4d74.0886578!16s%2Fg%2F11g71c">
                <button style="background-color:blue; border-radius:10px; padding:5px; border:none;">
                    🚗Track our Shop now
                </button>
            </a>
            """, unsafe_allow_html=True)
    st.header("")
    st.image('WhatsApp Image 2024-09-15 at 21.03.35_1abce9cd.jpg',caption='Visit Our Shop')
    st.sidebar.markdown("⚙️Site created by Siddhant.....")

    # botton3 = st.sidebar.markdown("""
    #             <button style="background-color:red; border-radius:10px; padding:5px; border:black;">
    #                Offers For Men
    #             </button>
    #         </a>
    #         """, unsafe_allow_html=True)

    # streamlit run About__Shop.py


