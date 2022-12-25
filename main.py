import openai as openai
import requests
import shutil
from PIL import Image

openai.api_key = "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"


def createImageWithText(keyword, search_key, size):
    for i in range(0, 100):
        response = openai.Image.create(
            prompt=keyword,
            n=1,
            size=size
        )
        image_url = response['data'][0]['url']
        print(image_url)

        file_name = f"{search_key}-{i}.png"

        res = requests.get(image_url, stream=True)

        if res.status_code == 200:
            with open(f"src/{file_name}", 'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ', file_name)
        else:
            print('Image Couldn\'t be retrieved')


if __name__ == '__main__':
    keyword = input("Please enter a few words: ")
    search_key = input("Please enter your keyword(to save): ")
    size = input("Please enter your image size(e.g 1024x1024):")
    createImageWithText(keyword, search_key, size)