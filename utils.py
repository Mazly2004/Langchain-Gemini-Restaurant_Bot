import os
from dotenv import load_dotenv
import getpass
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough , RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def generate_name_and_items(chosen_cuisine):
        
    if "GOOGLE_API_KEY" not in os.environ:
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")


    llm = ChatGoogleGenerativeAI(
        model = "gemini-2.5-flash-preview-04-17",
        temperature = 0.6,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    ) 

    output_parser = StrOutputParser()

    prompt = ChatPromptTemplate.from_messages([
        ("system" , "You are a helpful assistant that suggests a single fancy restaurant name."),
        ("human" , "I want to open a restaurant for {cuisine} food.")
    ])

    chain_1 = prompt | llm | output_parser

    prompt_2 = ChatPromptTemplate.from_messages([
        ("system" , "You are a helpful assistant that suggests menu items for a given restaurant that doesnt exist on earth."),
        ("human" , "Give me items for {restaurant} restaurant as comma seperated list.")
    ])

    chain_2 = prompt_2 | llm | output_parser

    step_1 = RunnablePassthrough.assign(
        restaurant = chain_1   
    )

    step_2 = RunnableParallel(
        restaurant_name = (lambda x : x["restaurant"]),
        menu_items = chain_2 ,

    )

    overall_chain = step_1 | step_2  

    response2 = overall_chain.invoke({
        "cuisine" : "Mexican",
    })

    return response2