import streamlit as st
def app():
    st.image('WhatsApp Image 2024-09-15 at 21.03.35_1abce9cd.jpg', width=600)

    st.markdown("""
                <a href="tel:+1234567890" target="_blank">
                    <button style="background-color:blue; border-radius:10px; padding:5px; border:black;">
                       📞Call Us
                    </button>
                </a>
                """, unsafe_allow_html=True)

    st.write("Or call us directly at:- 9850114367")
    st.text("")
    st.header("📍Track Our Shop Now:-")
    st.markdown("""
                <a href="https://www.google.com/maps/place/Bhairavnath+Cloth+Stores/@19.6785797,74.0860829,17z/data=!3m1!4b1!4m6!3m5!1s0x3bdda9175d0bf28b:0xf6965d9ab60a7ae4!8m2!3d19.6785797!4d74.0886578!16s%2Fg%2F11g71c">
                    <button style="background-color:green; border-radius:10px; padding:5px; border:none;">
                        🚗Track our Shop now
                    </button>
                </a>
                """, unsafe_allow_html=True)
    st.sidebar.markdown("⚙️Site created by Siddhant....")