from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import os
from dotenv import load_dotenv
import random
load_dotenv()

model = LiteLlm(
    model="groq/llama3-8b-8192",
    api_key = os.getenv("GROQ_API_KEY") 
)

def get_bad_joke():
    "A function which returns a bad joke."
    return random.choice([
        "Why did the chicken cross the road? To get to the other side!",
        "What do you call a belt made of watches? a waist of time.",
        "What do you call fake spaghetti? An impasta!",
        "Why did THE SCARECROW win an award? BEcoz he was outstanding in his field"
    ])

root_agent = Agent(
    model=model,
    name='litellm_agent',
    description='.Dad joke agent',
    instruction='A helpful assistant that can tell dad jokes. Only use the get_bad_joke function to get jokes if user asks for a joke',
    tools=[get_bad_joke],
)
