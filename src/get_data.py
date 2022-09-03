from bs4 import BeautifulSoup
import requests
import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO

def main(item_name):
    parameters = item_name.split(" ")
    root = tk.Tk()
    url = 'https://minecraftcraftingguide.net/'
    source_html = requests.get(url)
    soup_page = BeautifulSoup(source_html.content,'html.parser')

    all_items = soup_page.find_all(height='112')
    
    urls = []
    for x in all_items:
        reformated = str(x)
        if check(parameters, reformated):
            urls.append( 'https://' + reformated[reformated.find("src=") + 7 : reformated.find("style=") - 2])
     
    return urls

def check(parameters, name):
    for stuff in parameters:
        if stuff not in name:
            return False

    return True