import re
import os
from Chains.secretkey import openai_api_key

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.tools import YouTubeSearchTool


class Health:
    def __init__(self,age, sex, language) -> None:
        os.environ['OPENAI_API_KEY'] = openai_api_key
        self.llm = OpenAI(temperature=0.1, max_tokens=256)
        self.youtube_vid = YouTubeSearchTool()
        self.age = age
        self.sex = sex
        self.language = language

    def healthTips(self):
        #chain 1
        prompt = PromptTemplate(
            input_variables=['age'],
            template="categorize this person with {age} to one of this 'Infants (0-2 years)','Children (3-12 years)','Teenagers (13-19 years)','Adults (20-59 years)','Seniors (60+ years)'"
        )
        
        categ_name_chain = LLMChain(llm=self.llm, prompt=prompt, output_key='category_name')
        
        #chain 2
        prompt = PromptTemplate(
            input_variables=['category_name','age','sex','language'],
            template='give them 5 health tips for {sex} in {category_name} with age {age} in short and crisp in the language {language} with a welcome message like gald to help you, wihtout mentioning their category or age'
        )
        
        health_tips_chain = LLMChain(llm=self.llm, prompt=prompt, output_key='health_tips')
        
        chain = SequentialChain(
            chains=[categ_name_chain, health_tips_chain],
            input_variables=['age', 'sex', 'language'],
            output_variables=['category_name','health_tips']
        )
        
        response = chain({'age':self.age, 'sex':self.sex, 'language':self.language})
        return response

    def youtube(self):
        videos = self.youtube_vid.run(f"health tips for {self.sex} with age {self.age} in {self.language},3")
        urls = re.findall('watch\?v=[\w\-]+',videos)
        youtube_url = ["https://www.youtube.com/" + link for link in urls]
        return youtube_url
