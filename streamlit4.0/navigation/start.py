import streamlit as st
# from my_fuction import *
# import hydralit_components as hc
# import requests
# import pandas as pd
# import altair as alt
# import math
# import pickle


over_theme = {'txc_inactive': 'black', 'menu_background': '#D6E5FA', 'txc_active': 'white', 'option_active': '#749BC2'}
font_fmt = {'font-class': 'h3', 'font-size': '50%'}

def start_page():
    col1_1, col1_2 = st.columns(2)

    with col1_1:
        person_select = st.selectbox("选择您要转换的角色", ["Adele", "Taylor", "Justin", "Trump", "小组成员"], index=2)
        input_audio = st.file_uploader("请输入您要转换的音乐", type=["mp3", "wav"])
        st.markdown("请您在上传音频完成后再选择输出路径哦 输出路径请不要含有中文等字符哦，否则会刷新失败！！！")

        # if st.button("Start SingHeart 之旅"):
        #     state.text(update_start(input_audio))

    with col1_2:
        st.markdown(
            """
            # 转换成功的音频
            因上传到云端，云端处理，云端上传皆比较耗时，请耐心等待...
            """
        )
        if input_audio is not None:
            output_audio = start_process(person_select, input_audio)
            if output_audio:
                st.audio(output_audio)
                # state.text(update_trans_success())
        else:
            st.audio(None)