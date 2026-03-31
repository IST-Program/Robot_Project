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
