import streamlit as st

def footer_home():

    logo_img="https://media.licdn.com/dms/image/v2/D4D12AQFbqvMuVEZH_Q/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1727686986781?e=2147483647&v=beta&t=e8pJxjAdIK3-vwu3gQ7SlcyvEj5e-1RwjusiQjo0fEQ"

    st.markdown(f"""
                <div style="display:flex; gap:6px; items-align:center; justify-content:center;">
                  <p style="font-weight:bold; color:#000000; margin:0;">Created by ❤️ Manish</p> 
                  <img src="{logo_img}" style="height:20px;">   
                </div>  
                    """,unsafe_allow_html=True)
    


def footer_dashboard():

    logo_img="https://media.licdn.com/dms/image/v2/D4D12AQFbqvMuVEZH_Q/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1727686986781?e=2147483647&v=beta&t=e8pJxjAdIK3-vwu3gQ7SlcyvEj5e-1RwjusiQjo0fEQ"

    st.markdown(f"""
                <div style="display:flex; gap:6px; items-align:center; justify-content:center;">
                 <p style="font-weight:bold; color:#000000; margin:0;">Created by ❤️ Manish</p>
                  <img src="{logo_img}" style="height:20px;">   
                </div>  
                    """,unsafe_allow_html=True)