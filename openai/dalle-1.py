import os
from dotenv import load_dotenv
from rich import print as pprint
import openai

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(
    api_key=OPENAI_API_KEY,
)

response = client.images.generate(
    model="dall-e-3",
    prompt="夕陽下駛過海邊的火車",
    n=1,
    quality="hd",
    size="1024x1024",
    style="natural"
)

pprint(response)