import streamlit as st
from streamlit_option_menu import option_menu

import contact
import home
import offer2
import offers
import shopview
import updates
import luckdraw

st.set_page_config(
    page_title="Main Menu",initial_sidebar_state="expanded"
)


class MultiApp:

    def _init_(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run():
        # st.set_page_config(page_title=None,page_icon=None,initial_sidebar_state="auto",menu_items=None)

        with st.sidebar:
            app = option_menu(
                menu_title='Main Menu',
                options=['About Shop','Apply for Luckydraw', 'Offers For Men ', 'Offers For Women', 'Latest Updates','View our Shop','Contact Us',],
                icons=['cart-fill','gift-fill', 'person-standing', 'person-standing-dress', 'chat-fill', 'eye-fill', 'telephone-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"}, }
            )

        if app == 'About Shop':
            home.app()
        if app == 'Offers For Women':
            offer2.app()
        if app == 'Offers For Men ':
            offers.app()
        if app == 'Contact Us':
            contact.app()
        if app== 'View our Shop':
            shopview.app()
        if app=='Latest Updates':
            updates.app()
        if app=='Apply for Luckydraw':
            luckdraw.app()


    run()