import streamlit as st
from Chains.chain import Health

st.title("Docto AI")

st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("https://github.com/ansilmbabl/LangChain-beginner-project/blob/master/Images/25757.jpg?raw=true");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

age = st.sidebar.number_input(
    "age",min_value=0, max_value=100, value=30)

sex = st.sidebar.selectbox(
    "Gender",['male','female'])

language = st.sidebar.selectbox(
    "Language",['English','French','German','Arabic','Malayalam','Hindi'],)

submit = st.sidebar.button('Confirm', type='primary')

if submit:
    health = Health(age, sex, language)
    response = health.healthTips()
    st.header(f'Health Tips for the age "{age}"')
    tips = response['health_tips'].strip().split('\n\n')
    for tip in tips:
        st.markdown(tip)
    
    st.subheader('Checkout this......',)
    urls = health.youtube()
    # Embed the video
    col = st.columns(len(urls))
    for i,url in enumerate(urls):
        with col[i]:
            st.video(url)