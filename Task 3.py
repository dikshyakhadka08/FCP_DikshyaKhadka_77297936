import random

def check_email(email,domain ='pop.ac.uk'):
    """This function checks the email."""
    flag = False
    if "@" in email:            #checks whether @ is in mail or not
        split_email= email.split("@")

        if len(split_email)==2 and len(split_email[0]) >= 2 and split_email[-1] == domain:
            flag = True
        else:
            print("Invalid email!")
            exit()
    else:
    
        print("Invalid email!")
        exit()      
    return flag
        
def reply(query,random_answers):
    """This function print the output"""
    query= query.lower()
    if "wifi" in query:          #checks whether the key values are in query or not
        print(respond['wifi'])
    elif "library" in query:
        print(respond['library'])
    elif "deadline" in query:
        print(respond['deadline'])
    elif "coffee" in query:
        print (respond['coffee'])
    elif "feebacks" in query:
        print (respond['feedbacks'])
    elif "SSD" in query:
        print(respond['SSD'])
    elif "bye" in query or "exit" in query:
        print(f"Thanks, {mail_name.capitalize()}!, for using PopChat. See you again soon!")
        exit()
    else:
        print(random.choice(random_answers))
        


respond={
        "wifi":"WiFi is excellent across the campus.",
         "library":'Sorry!The library is closed today',
         "coffee": "Cafe opens at 7 AM",
         "deadline": "Your deadline has been extended by two working days",
         "feedbacks": "You will get feebacks bu next week",
         "SSD": "SSD service is available 24 hour"
         }
random_answers =["Mmmm.","Oh, my","Oh,yes"," I see.","Tell me more."]  

print ("Welcome to Pop Chat !\nOne of our operators will be pleased to help you today. ")
names = ["Tony", "Marvel ", "Thor", "Blade", "Hulk"]
email = input ("Please enter your Poppleton email address: ")
if check_email (email) == True:          #it pass the email to check the email
    mail_name = email[0:email.index("@")]
    print(f"Hello, {mail_name.capitalize()}!  Thank you, and Welcome to PopChat!\n")
    print(f"My name is {random.choice(names)}, and it will be my pleasure to help you. ")
    if random.randint(0,10)>8:            # randomly inserts number and it checks the network error
            print("*** NETWORK ERROR ***") 
            print(f"Thanks,{mail_name.capitalize()}, for using PopChat. See you again soon!")
    else:
        while True:                       #it loops the code
            query = input(" Inquiry -----> ")
            reply(query,random_answers)
    
           
   

    