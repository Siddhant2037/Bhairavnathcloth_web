import streamlit as st
import sqlite3

def app():
    # Create/connect to SQLite database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()


    # Function to create a table
    def create_table():
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (name TEXT, location TEXT, coupan TEXT, number INTEGER, feedback TEXT)''')


    # Function to insert data
    def insert_data(name, location, coupan, number, feedback):
        c.execute("INSERT INTO users (name, location, coupan, number, feedback) VALUES (?, ?, ?, ?, ?)",
                  (name, location,coupan, number, feedback))
        conn.commit()


    # Streamlit app to collect data
    st.title('🎁Application For Luckydraw')

    # Collect user inputs
    name = st.text_input('Enter your name:',value=None,placeholder=("Your Name..."))
    location = st.text_input('Enter your Location:',value=None,placeholder=("Your Location..."))
    coupan = st.text_input('Enter your coupan:',value=None,placeholder=("Your Coupan Code..."))
    number = st.number_input('Enter Your Mobile Number:',value=None,placeholder=("Your Number"))
    feedback = st.text_area('Please provide your feedback:')
    submit = st.button('Submit')
    # Submit button
    if name and location and coupan and number and feedback and submit:
    # Create table if it doesn't exist
        create_table()

        # Insert user data into database
        insert_data(name, location,coupan, number, feedback)

        st.success("✅Your Data Is Securely Collected")
    elif submit:
        st.markdown("🚨Please Fill The Above Information Properly")

    # Close the connection
    conn.commit()
    conn.close()

