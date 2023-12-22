import streamlit as st
from streamlit_option_menu import option_menu
import blockchaindemo, account, address_book, transactionmapping, addressinfo, faqpage
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
                menu_title='Etherview',
                options=['Login/Register', 'Address Book','Address Information/Insights','Graphing and Visualizing Transactions', 'Demo of a Blockchain', 'FAQ Page'],
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )
        if app_choice == 'Address Book':
            address_book.app()
        elif app_choice == "Login/Register":
            account.app()
        elif app_choice == "Graphing and Visualizing Transactions":
            transactionmapping.app()
        elif app_choice == "Address Information/Insights":
            addressinfo.app()
        elif app_choice == 'Demo of a Blockchain':
            blockchaindemo.app()
        elif app_choice == 'FAQ Page':
            faqpage.app()

        
            
# Create an instance of MultiApp
multi_app = MultiApp()

# Add your apps to the MultiApp instance
multi_app.add_app("Login/Register", account.app)
multi_app.add_app("Address Book", address_book.app)
multi_app.add_app("Transaction Mapping", transactionmapping.app)
multi_app.add_app("Demo of a Blockchain", blockchaindemo.app)
multi_app.add_app("Address Information/Insights", addressinfo.app)
multi_app.add_app("FAQ Page", faqpage.app)
# Run the MultiApp
multi_app.run()


