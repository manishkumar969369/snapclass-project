import streamlit as st

def header_home():

    logo_img="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvfnCVpVPUW5XUjxV8KA6RPE80wowio-7BUw&s"
  

    st.markdown(f"""
                <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:10px;">
                  <img src="{logo_img}" style="height:100px; border-radius:2rem">   
                  <h1 style='text-align:center; color:#E0E3FF'; >SNAP <br/> CLASS</h1>  
                </div>  
                    """,unsafe_allow_html=True)
    


def header_dashboard():

    logo_img="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvfnCVpVPUW5XUjxV8KA6RPE80wowio-7BUw&s"
  

    st.markdown(f"""
                <div style="display:flex; align-items:center; justify-content:center; gap:10px;">
                  <img src="{logo_img}" style="height:85px; border-radius:2rem">   
                  <h2 style='text-align:left; color:#5865F2';> SNAP <br/> CLASS</h2>  
                </div>  
                    """,unsafe_allow_html=True)