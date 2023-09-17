# LangChain Beginner Project
Creating a web app to suggest health tips using Language Models (LLMs) like OpenAI.

![English](Images/English.png)

A beginner-friendly project to understand how to use Language Models (LLMs) with LangChain and integrate the power of other LangChain tools like Google search, YouTube videos, etc.

## Try the Web App Locally

1. Open the command prompt in the desired location.
2. Clone the project using the following command:
    ```bash
    git clone https://github.com/ansilmbabl/LangChain-beginner-project.git
    ```
3. Install the dependencies by running the command:
    ```bash
    pip install -r requirements.txt
    ```
4. Create a file named `secretkey.py` inside the `Chains` folder and save your [OPENAI_API_KEY](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key) like this:
    ```python
    openai_api_key = "sk-****************************"
    ```
5. Run the following command in the command prompt to host the web app on your browser:
    ```bash
    streamlit run app.py
    ```

## Documentation

Explore these steps to understand the implementation idea behind this project and get started with LangChain with this project:

* [Building the Frontend of a Streamlit Application](Docs/streamlit.md)
* [Getting a Secret Key for the OpenAI API](Docs/secretkey.md)
* [Creating the `Health` Class](Docs/Health.md)
* [Fetching Health Tips with the `healthTips` Method](Docs/health_tips.md)
* [Fetching YouTube Video Recommendations with the `youtube` Method](Docs/youtube_video.md)

Feel free to navigate through these guides to gain a deeper understanding of how LangChain can be used in your projects.

Happy coding!

## Connect
📫 Reach me via [linkedIn](Linkedin.com/in/ansilmbabl/) <br>
📧 Mail me at ansilproabl@gmail.com