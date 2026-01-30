import streamlit as st
from supabase import create_client, Client

def app():
    #st.set_page_config(page_title="Lucky Draw", page_icon="🎁")
    #st.header("Lucky Draw")
    st.title("🎁 LuckyDraw")

    # Supabase connection
    supabase: Client = create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )

    st.title("🎁 Application For Lucky Draw")

    # ---- Form ----
    with st.form("luckydraw_form"):
        name = st.text_input("Enter your name", placeholder="Your Name...")
        location = st.text_input("Enter your location", placeholder="Your Location...")
        coupon = st.text_input("Enter your coupon code", placeholder="Your Coupon Code...")
        mobile = st.text_input("Enter your mobile number", placeholder="Your Mobile Number...")
        feedback = st.text_area("Please provide your feedback")

        submit = st.form_submit_button("Submit")

    # ---- Handle Submit ----
    if submit:
        if not all([name, location, coupon, mobile, feedback]):
            st.error("🚨 Please fill all the fields")
            return

        supabase.table("Lucky Draw").insert({
            "name": name,
            "location": location,
            "coupon": coupon,
            "mobile": mobile,
            "feedback": feedback
        }).execute()

        st.success("✅ Your data is securely collected")
        st.balloons()

    st.sidebar.markdown("⚙️ Site Created By Siddhant")

if __name__ == "__main__":
    app()
