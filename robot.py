def fillBox():
    fullbox = 0
    items = 0

    items = int(input("Enter the numbers of items to go into box. 60 max")) 

    if items < 60:
        
        print("add test")
    elif items == 60:
        fullbox += 1
        
        print("The number is", fullbox)
        items = 60
        print("The number is", items)
    else:
        fullbox += 1
        items -= 60
        print("This many boxs where made", fullbox)
        print("This is ow many items are left", items)
        

fillBox()
