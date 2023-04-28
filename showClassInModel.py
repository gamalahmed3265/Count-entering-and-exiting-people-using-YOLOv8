def showClass(names:dict):
    mes=""
    for i,name in names.items():
        mes+=f"{i} -> {name}\n"
    saveInFile(mes)
    
    
def saveInFile(text:str):
    """_summary_

    Args:
        text (_type_): _description_
    show Class In Model ans save theme in file named cocos
    """
    try:
        with open('coco.txt', 'w') as f:
            f.write(text)
    except FileNotFoundError:
        print("The 'docs' directory does not exist")
