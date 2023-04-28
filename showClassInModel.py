def showClass(names:dict):
    mes=""
    for i,name in names.items():
        mes+=f"{name}\n"
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

def showDatainFile():
    classList=[]
    try:
        with open("coco.txt","r") as r:
            data=r.read()
            classList=data.split("\n")
    except FileNotFoundError:
        print("The 'docs' directory does not exist")
        
    return classList