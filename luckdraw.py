# import streamlit as st
# import sqlite3
#
# def app():
#     # Create/connect to SQLite database
#     conn = sqlite3.connect('data.db')
#     c = conn.cursor()
#
#
#     # Function to create a table
#     def create_table():
#         c.execute('''CREATE TABLE IF NOT EXISTS users
#                      (name TEXT, location TEXT, coupan TEXT, number INTEGER, feedback TEXT)''')
#
#
#     # Function to insert data
#     def insert_data(name, location, coupan, number, feedback):
#         c.execute("INSERT INTO users (name, location, coupan, number, feedback) VALUES (?, ?, ?, ?, ?)",
#                   (name, location,coupan, number, feedback))
#         conn.commit()
#
#
#     # Streamlit app to collect data
#     st.title('🎁Application For Luckydraw')
#
#     # Collect user inputs
#     name = st.text_input('Enter your name:',value=None,placeholder=("Your Name..."))
#     location = st.text_input('Enter your Location:',value=None,placeholder=("Your Location..."))
#     coupan = st.text_input('Enter your coupan:',value=None,placeholder=("Your Coupan Code..."))
#     number = st.number_input('Enter Your Mobile Number:',value=None,placeholder=("Your Number"))
#     feedback = st.text_area('Please provide your feedback:')
#     submit = st.button('Submit')
#     # Submit button
#     if name and location and coupan and number and feedback and submit:
#     # Create table if it doesn't exist
#         create_table()
#
#         # Insert user data into database
#         insert_data(name, location,coupan, number, feedback)
#
#         st.success("✅Your Data Is Securely Collected")
#     elif submit:
#         st.markdown("🚨Please Fill The Above Information Properly")
#
#     # Close the connection
#     conn.commit()
#     conn.close()
#     conn.push()


import streamlit as st
from supabase import create_client, Client
#import re
def app():
    st.image('WhatsApp Image 2024-09-15 at 21.03.35_1abce9cd.jpg', width=600)

    # Supabase credentials
    SUPABASE_URL = "https://giwgxenhaiqzymegceoo.supabase.co"
    SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imdpd2d4ZW5oYWlxenltZWdjZW9vIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjY2NjM5MzIsImV4cCI6MjA0MjIzOTkzMn0.EPLvdofai5VjkB5AJ4QvNtWzdMS7ujqXXf6TKQAuW3o"
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


    # Function to add data to Supabase
    def insert_data(name, location, coupon_code, mobile_number, feedback):
        response = supabase.table("user_data").insert({
            "name": name,
            "location": location,
            "coupon_code": coupon_code,
            "mobile_number": mobile_number,
            "feedback": feedback
        }).execute()
        return response


    # Streamlit form
    st.title("🎁Apply For Luckydraw")

    with st.form(key='user_form'):
        name= st.text_input("Name:-",value=None,placeholder="Your Name...")
        location= st.text_input("Name Of Place Where You Live:-",value=None,placeholder="Your Location...")
        coupon_code= st.text_input("Coupon Code:-",value=None,placeholder="Your Coupan Code...")
        mobile_number= st.number_input("Mobile Number:-",value=None,placeholder="Your Mobile Number...")
        feedback= st.text_area("Feedback (About Our Shop):-",value=None,placeholder="Your Feedback...")


        # Validate form input (simple validation)


        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            if name and location and coupon_code and feedback:
                response = insert_data(name, location, coupon_code, mobile_number, feedback)
                st.markdown("✅Your Data Is Collected Securely")

            else:
                st.error("Please fill in all fields.")
    st.sidebar.markdown("⚙️Site Created By Siddhant....")
    # Display stored data (optional)
