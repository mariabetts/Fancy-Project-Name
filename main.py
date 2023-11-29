import streamlit as st
from streamlit_option_menu import option_menu
import about, account, home, transactionmapping
import firebase_admin
from firebase_admin import credentials



class MultiApp:

    def __init__(self):
        self.apps = []


    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            app_choice = option_menu(
                menu_title='Options ',
                options=['Home', 'Account', 'Transaction Mapping', 'About'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app_choice == "Home":
            home.app()
        elif app_choice == "Transaction Mapping":
            transactionmapping.app()
        elif app_choice == 'Account':
            account.app()
        elif app_choice == 'About':
            about.app()
            
# Create an instance of MultiApp
multi_app = MultiApp()

# Add your apps to the MultiApp instance
multi_app.add_app("Home", home.app)
multi_app.add_app("Transaction Mapping", transactionmapping.app)
multi_app.add_app("Account", account.app)
multi_app.add_app("About", about.app)

# Run the MultiApp
multi_app.run()



