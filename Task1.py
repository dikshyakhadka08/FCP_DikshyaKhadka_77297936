print("Stop! Who would cross the Bridge of Death \nMust answer me these questions three, 'ere the other side he see.\n")
name = input("What is your name? ")                          #asks user to enter a name
if "arthur" in name.lower():                                 #takes input in small or capital letter
    print("My liege! You may pass!")
else: 
    quest = input("What do you seek? ")
    if "grail" in quest.lower():                             #if condition with in operator checks if input exists grail in  it or not
        print("Ok!Now last question")
        color=input("What is your favourite color? ")
        print("You may pass!" if name[0].upper() in color[0].upper() else"Incorrect! You must now face the Gorge of Eternal Peril.")#use of ternery 
                                                              #it checks the first letter if color and name and returns value accordingly
    else:
        print("Only those who seek the Grail may pass.")      
       