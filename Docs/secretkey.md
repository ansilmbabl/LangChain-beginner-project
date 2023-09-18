# Getting a Secret key of OpenAI API (2/5)
To interact with OpenAI LLM we need an API key, Follow these steps to obtain one:

## Obtaining an OpenAI API Key

1. Visit the OpenAI website [[1]](https://beta.openai.com/signup/).
2. Sign up for an account or log in if you already have one.
3. Navigate to the API section or API settings.
4. Create a new API key or copy an existing one.

**Important**: Keep your API key secure. Do not share it publicly or commit it to version control. Instead, store it in a separate `secret.py` file (as explained below). If you are uploading this to Github don't forget to add this file name in the `.gitignore` file [[2]](https://www.w3schools.com/git/git_ignore.asp)

## Using Your OpenAI API Key

To use your OpenAI API key with this application, follow these steps:

1. Create a `secret.py` file in the `Chains` directory.
2. Inside `secret.py`, store your API key as follows:

   ```python
   openai_api_key = "****************"
   ```
   replace "****************" with your actual OpenAI API key


## Conclusion
Now you have stored your API key safely. In the next guide, we'll explore creating the `Health` class and implementing its methods for fetching data. [click here](Docs\Health.md)