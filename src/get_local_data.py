import os.path
def main(item_name):
    #format the request to be useable
    # item_name.replaceAll(" ", "-")
    item_name = "-".join(item_name.split(" "))
    #for u in item_name.split(" "):

    item_name = item_name+"-crafting"
    #os.path.exists('/recipes')
    #check if the file exists under diffrent type if so return that filename
    if os.path.exists('./assets/recipes/'+item_name+'.png'):
        return './assets/recipes/'+item_name+'.png'
    elif os.path.exists('./assets/recipes/'+item_name+'.gif'):
        return './assets/recipes/'+item_name+'.gif'
    #if the images isnt found return logo
    else:
        return './assets/recipes/crafting-table-crafting.png'
    
if __name__ == '__main__':
    main('aa')     