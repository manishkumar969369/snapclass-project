import streamlit as st
from src.components.header_home import header_home
from src.ui.base_layout import style_base_layout, style_background_home
from src.components.footer import footer_home


def home_screen():

    header_home()
    style_base_layout()
    style_background_home()

    col1, col2 = st.columns(2,gap='large')

    with col1:
        st.header("I'm Student")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMwn_ZRz_FPX6Eolz0uMuK-Zp51-NZQuRXiBH7zThzDC8dgkWh", width=120,)
        if st.button('Teacher Portal', type='primary',icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='teacher'
            st.rerun()
    with col2:
        st.header("I'm Teacher")
        st.image("https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSSinkx4QEhM61APF2_gb_Y9uQkmoBLmE4XfeuoKyxGAZ2qln7D",width=140)
        if st.button('Student Portal',type='primary',icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='student'
            st.rerun()

    footer_home()