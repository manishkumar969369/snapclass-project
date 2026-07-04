import streamlit as st



def style_background_home():
    st.markdown("""

        <style>
                
                # .stApp {
                #     background: #5865F2 !important;
                # }

                # .stApp div[data-testid="stColumn"]{
                #     background-color:#E0E3FF !important;
                #     padding:2rem !important;
                #     border-radius: 5rem !important;
                # }
                .stApp{
                    background:#E0E3FF !important;
                    color:black !important;
                }

                h1,h2,h3,h4,h5,h6,p,span,label,div{
                    color:black !important;
                }
        </style>

                """
                    ,unsafe_allow_html=True)





def style_background_dashboard():
    st.markdown("""

        <style>
                
                .stApp {
                    background: #E0E3FF !important;
                }
        </style>

                """
                    ,unsafe_allow_html=True)
    


def style_base_layout():
    st.markdown("""

        <style>
           @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
           @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
            
                
                /* hide top streamlit bar*/

                #MainMenu, footer, header{
                    visibility:hidden;
                }

                .block-container{
                    padding-top:1.5rem !important;
                }

                h1{
                    font-family:'Climate Crisis',sans-serif !important;
                    font-size:2.5rem !important;
                    line-height:1.1 !important;
                    margin-bottom:0rem !important;
                }
                h2{
                    font-family:'Climate Crisis',sans-serif !important;
                    font-size:2rem !important;
                    line-height:1.1 !important;
                    margin-bottom:0rem !important;
                    margin-left:20px !important;
                     
                }

               h3 , h4, p{
                    font-family:'Outfit',sans-serif;
                }

                button {
                    background-color: #5865F2 !important;
                    color: white !important;
                    border: none !important;
                    border-radius: 25px !important;
                    padding: 10px 20px !important;
                    transition: all 0.3s ease !important;
                }

                button:hover {
                    background: #4652d9 !important;   /* slightly darker blue */
                    transform: scale(1.05);
                }
                button[kind="secondary"]{
                    border-radius:1.5rem !important;
                    background-color:#EB459E !important;
                    padding: 10px 20px !important;
                    border:none !important;
                    transition: transform 0.25s ease-in-out !important;
                }
                button[kind="tertiary"]{
                    border-radius:1.5rem !important;
                    background-color:#000000 !important;
                    padding: 10px 20px !important;
                    border:none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button:hover{
                    transform: scale(1.05)
                }
                 
                 

        </style>

                """
                    ,unsafe_allow_html=True)