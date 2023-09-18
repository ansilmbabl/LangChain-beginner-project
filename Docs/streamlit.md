# Building the Frontend of a Streamlit Application (1/5)

In this guide, we'll explore how to create the frontend of a Streamlit application for health tips and YouTube video recommendations. We'll break down the code provided and explain each step in detail.

Note: Additional reference links are provided like this [[1]]() on respective fields if you need further clarification

## Prerequisites

Before you begin, ensure you have the following:

- Python installed on your system (Python 3.6 or higher recommended).
- A code editor of your choice (e.g., Visual Studio Code, PyCharm).
- Basic knowledge of Python and Streamlit.

## Getting Started
This will be coded inside file `app.py` which will be called by `streamlit run app.py` to run the web app.

### Importing Required Libraries

The first step is to import the necessary libraries for your Streamlit application:

```python
import streamlit as st
from Chains.chain import Health
```

- `streamlit` is the main library for creating the user interface. [[1]](https://docs.streamlit.io/)
- `Health` It is the class we use to fetch health tips and YouTube video recommendations. We will see the details about this [here]() later

### Setting the Application Title and Background Image

```python
st.title("Docto AI") # Give a name you like

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
```

- `st.title("Docto AI")` sets the title of your Streamlit application to "Docto AI." [[2]](https://docs.streamlit.io/library/api-reference/text/st.title)
- `st.markdown` allows you to apply custom CSS styling to the app. In this case, it sets a background image. [[3]](https://docs.streamlit.io/library/api-reference/text/st.markdown)

### Sidebar Inputs

```python
age = st.sidebar.number_input(
    "Age", min_value=0, max_value=100, value=30)

sex = st.sidebar.selectbox(
    "Gender", ['Male', 'Female'])

language = st.sidebar.selectbox(
    "Language", ['English', 'French', 'German', 'Arabic', 'Malayalam', 'Hindi'])
```

- `st.sidebar` is a container for adding input widgets to the sidebar. [[4]](https://docs.streamlit.io/library/api-reference/layout/st.sidebar)
- `number_input` and `selectbox` are used to create input fields for age, gender, and language, respectively. [[5]](https://docs.streamlit.io/library/api-reference/widgets)

### Submit Button

```python
submit = st.sidebar.button('Confirm', type='primary')
```

- `st.sidebar.button` adds a "Confirm" button to the sidebar. [[6]](https://docs.streamlit.io/library/api-reference/widgets/st.button)

### Data Processing and Display

```python
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
    for i, url in enumerate(urls):
        with col[i]:
            st.video(url)
```

- When the "Confirm" button is clicked (`submit` is True), the user's input (age, gender, and language) is processed.
- The `Health` class is used to fetch health tips and YouTube video recommendations based on the user's input.
- The health tips are displayed as markdown text, and the YouTube videos are embedded for the user to watch.

## Conclusion

This guide has provided an in-depth explanation of the frontend part of your Streamlit application. You can follow these steps to create the user interface for your health tips and YouTube video recommendation app. Customize and expand upon it to enhance the functionality and user experience as needed.

Now Let's see how to create an API key needed for this project, [click here](Docs\secretkey.md)