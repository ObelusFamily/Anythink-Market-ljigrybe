import os
import requests
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

async def image_from_description(description: str)-> str:
    # return "https://w7.pngwing.com/pngs/921/644/png-transparent-smiley-emojicon-smiley-computer-icons-emoticon-scalable-graphics-icon-smiley-miscellaneous-desktop-wallpaper-circle.png"

    response = openai.Image.create(
        prompt=description,
        n=1,
        size="256x256"
    )
    if not response or not 'data' in response:
        raise Exception("Could not create image")
    return response['data'][0]['url']


