from tkinter import *
from PIL import ImageTk, Image
import get_data
import get_local_data
from io import BytesIO
from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
from PIL import ImageTk as itk

#main function that dictates the searches and images when 
#put into the searchbar

def main():
    local = False

    window = Tk()
    window.attributes('-type', 'dialog')
    window.title("Minecraft Recipes")
    window.geometry('800x800')
    canvas = Canvas(window, height = 300, width = 300)
    window.grid_columnconfigure((0, 1, 2), weight=1)
    #Create Textbox with specified size
    
    #Label
    a = Label(window, text ='Minecraft Recipes', font = "50") 
    #w.pack()
    
    #msg = Message(window, text = "A Minecraft Portal To Search For Recipes")
    #msg.pack()  
    a.config(font = ("Courier",14))
    a.grid(row = 0, column = 1, pady = 2)
    #a.pack()
    """
    img = ImageTk.PhotoImage(file = './assets/Minecraft.png')  
    logo = img._PhotoImage__photo.subsample(2)
    # logo = img.resize(700, 200)
    #resized_img = image.resize((100, 100))
    image = Label(window, image = logo)
    image.config(width = 700, height = 200)
    image.pack()
    """

    # Input
    item = Entry(window)
    item.grid(row = 1, column = 1, pady = 2)

    if local:
        #Initial Crafting Table
        img = PhotoImage(file = './assets/recipes/crafting-table-crafting.png')
        output = Label(height = 112, width = 204, image = img)
        output.grid(row = 3, column = 1, pady = 2)

    #Search Button
    if local:
        b1 = Button(window, text = "Search", command = lambda: getLocalRecipes(item.get(), output)) 
        b1.grid(row = 2, column = 1, pady = 2)
    else :
        b1 = Button(window, text = "Search", command = lambda: getRecipes(item.get()))
        b1.grid(row = 2, column = 1, pady = 2)

    window.mainloop()

#The function named getRecipie
def getRecipes(item):
    all_array = get_data.main(item)
    image_array = []
    y = 0
    for i in range(len(all_array)):
        req = Request(
            url = all_array[i], 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        u = urlopen(req)
        raw_data = u.read()
        u.close()
    
        im = Image.open(BytesIO(raw_data))
        image1 = itk.PhotoImage(im)

        output = Label(image = image1)
        output.photo = image1
        output.grid(row = i  + 4 - y%3, column = y % 3, pady = 2)
        y+=1
    
def getLocalRecipes(item, output):
    outputfilename = get_local_data.main(str(item))
    img2 = itk.PhotoImage(Image.open(outputfilename))
    output.configure(image = img2)
    output.image = img2

# Runs main function when file is run
if __name__ == '__main__':
    main()