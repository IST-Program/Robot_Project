# CHP 1
name = "barry"
charge = int(100)
print("charge:", charge)
fullbox = 0
items = 0
def fillBox():
    

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

def palllet():
    pallets = 0

    while fullbox < 1:
        if fullbox == 6:


            def pickitems():
                Hardware = 0
                lumber = 0
                paint = 0
                Item_selection = input("Select Hardware, Lumber, Paint")
                Selection_number = int(input("How many of item"))


# CHP 3
def pickitem():
    hardware = 0
    lumber = 0
    paint = 0
    item_types = ['Hardware', 'Lumber', 'Paint']
    
    while True:
        
        print("This many boxs where made", item_types)
        data = input("Choose an item or press Enter to quit: ")
        
        
        if data == "":
            break
        
        
        if data == 'Hardware':
            hardware += 1
        elif data == 'Lumber':
            lumber += 1
        elif data == 'Paint':
            paint += 1
        else:
            print("Invalid option. Please try again.")
            continue
            
        print(f"Updated Counts: Hardware={hardware}, Lumber={lumber}, Paint={paint}")

# Call the function
pickitem()


# CHP 4
def outputOrderAuto(fname):
    # read file
    with open(fname, mode='r') as csvfile:
        # read the file lines
        lines = csvfile.readlines()

        # remove the header
        lines.pop(0)

        # initialize a list to store the items
        items = {"Hardware": 0, "Lumber": 0, "Paint": 0}

        # reads each line
        for line in lines:
            # split lines into columns
            columns = line.strip().split(',')

            # give the robot each number of items in this specific order
            items["Hardware"] += int(columns[0])
            items["Lumber"] += int(columns[1])
            items["Paint"] += int(columns[2])
        
        # outputs the items that the robot needs from the file
        print("Items to aquire: ")
        for item_t, quantity in items.items():
            print(f"{item_t}: {quantity}:")


def main():
    # file name
    fname = "robotOrder.csv"

    # calls the outputOrderAuto function with the csv file name
    outputOrderAuto(fname)

if __name__ == "__main__":
    main()