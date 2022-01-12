from statistics import mean
#imports mean from statistics to find average
MPH=[]
KPH=[]
print("Swallow Speed Analysis: Version 1.0")
while True:
    speed = (input("Enter speed:"))    #asks user to input speed
    if speed=="":
        if len(MPH +KPH)==0:           #it compares length of sum of both readings
            print("No readings entered. Nothing to do")
        break                          #the loop stops immediately if the sum of length flight speed is 0(i.e no readings)
        
    elif(speed[0].lower() == "u" or speed[0].lower()=="e") or speed[1:].isnumeric()== True:#it checks the value of u and e         
        if speed[0].lower()=="u":      #if first letter of the reading is u then adds the speed value i.e entered
            MPH.append(float(speed[1:]))
        else:
            MPH.append(float(speed[1:])*0.621371)            #it converts to KPH
            
    else:
        print("Invalid Input") 
        break
        
if len(MPH)!=0:                                              #if length of MPH is not equals to 0 then
    for i in MPH: 
        KPH.append(i*1.60934)                                #converts and adds MPH value into KPH
    print(f"\nResults Summary:")
    if len(MPH) ==1:
        print(len(MPH), "Reading analysis")
    else:
        print(len(MPH),"Readings analysis")      
    print(f"Maximum Speed: {max(MPH):.2f} MPH, {max(KPH):.2f} KPH")
    print(f"Minimum Speed: {min(MPH):.2f} MPH, {min(KPH):.2f} KPH")
    print(f"Average Speed: {mean(MPH):.2f} MPH, {mean(KPH):.2f} KPH")
    