# Fetching Health Tips with the `healthTips` Method (4/5)

In this guide, we'll dive into the `healthTips` method within the `Health` class. This method is responsible for fetching health tips based on user input parameters, such as age, gender, and language. Let's break down the code step by step:

## Understanding the `healthTips` Method

### Chain 1: Categorization
```python
def healthTips(self):
    # Chain 1: Categorization
    prompt = PromptTemplate(
        input_variables=['age'],
        template="categorize this person with {age} to one of these categories: 'Infants (0-2 years)', 'Children (3-12 years)', 'Teenagers (13-19 years)', 'Adults (20-59 years)', 'Seniors (60+ years)'"
    )

    categ_name_chain = LLMChain(llm=self.llm, prompt=prompt, output_key='category_name')

    # Chain 2: Generating Health Tips
    # ...

    # Sequential Chain : Chaining together
    # ...

```


- The `healthTips` method begins by setting up a categorization chain using LangChain. This chain categorizes the user's age into one of the following categories: 'Infants (0-2 years)', 'Children (3-12 years)', 'Teenagers (13-19 years)', 'Adults (20-59 years)', or 'Seniors (60+ years)'.
- It creates a `PromptTemplate` with an input variable `age` and a template string that uses this input to generate the prompt. [[1]](https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/#prompt-template)
- A `LLMChain` (Language Model Chain) is then created with the specified LangChain language model (`llm`) and the prompt. [[2]](https://python.langchain.com/docs/modules/chains/foundational/llm_chain)

### Chain 2: Generating Health Tips

```python
def healthTips(self):
    # Chain 1: Categorize age group
    # ...

    # Chain 2: Generating Health Tips
    prompt = PromptTemplate(
        input_variables=['category_name', 'age', 'sex', 'language'],
        template='give them 5 health tips for {sex} in {category_name} with age {age} in short and crisp in the language {language} with a welcome message like glad to help you, without mentioning their category or age'
    )

    health_tips_chain = LLMChain(llm=self.llm, prompt=prompt, output_key='health_tips')

    # Sequential Chain : Chaining together
    # ...

```
- After categorization, the method sets up another chain to generate health tips. This chain considers the user's age category (`category_name`), age, gender (`sex`), and language (`language`) to generate health tips.
- Similar to Chain 1, a `PromptTemplate` is created with input variables and a template string for generating the prompt.
- A new `LLMChain` is created to execute this chain. The output of this chain will be the `health_tips`.

### SequentialChain

```python
def healthTips(self):
    # Chain 1: Categorize age group
    # ...

    # Chain 2: Generating Health Tips
    # ...

    chain = SequentialChain(
        chains=[categ_name_chain, health_tips_chain],
        input_variables=['age', 'sex', 'language'],
        output_variables=['category_name', 'health_tips']
    )

    response = chain({'age': self.age, 'sex': self.sex, 'language': self.language})
    return response
```
- The `SequentialChain` is a way to structure these two chains in sequence. First, Chain 1 (categorization) is executed, and its output (`category_name`) is then used as input for Chain 2 (health tips generation). This is how integreate different prompts given to the LLM. [[3]](https://python.langchain.com/docs/modules/chains/foundational/sequential_chains#sequential-chain)
- Input and output variables are specified to ensure data flow between the chains.

### Fetching and Returning the Response

- The `response` variable holds the result of executing the SequentialChain with the user's age, gender, and language as inputs.
- The response contains the ouput given by the LLM model using the information from both the chains.

## Conclusion

The `healthTips` method is a critical part of the `Health` class. It utilizes LangChain to categorize users based on age and generate personalized health tips. By understanding how this method works, you'll gain insights into how the project provides users with valuable health information.

In the next guide, we will explore another method within the `Health` class used to provide some youtube reference links, [click here](Docs\youtube_video.md)
