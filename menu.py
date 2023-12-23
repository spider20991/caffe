#drink menu
drinks = ['Cappuccino','Mocha latte','Pumpkin spice latte','Chai latte']
customer_basket = []

#Used enumerate to iterate over my list, going through 1 by 1
print("Welcome to my caffe!! We are having a sale- everything is £1!! Here's the menu: ")
for x, y in enumerate(drinks, start=1):
    print("\n" , x , ": "  , y)

while True:
    prompt = "Please choose between [1-4] to continue, 'checkout' = pay: , 'q' = exit: "
    answer = input("\n" + prompt)
    
    if answer == 'q': #quits
        break
    elif answer == 'checkout':
        if not customer_basket:
            print("You have nothing in your basket!!")   
        else:
            total_cost = len(customer_basket)
            print("\nYour basket contains :", ', ' .join(customer_basket)) #.join() - combines the items from 'list' to the string
            print("Total cost: £" , total_cost)
            question = input("What name would you like on your drink? ")
            print("\nHere you go " + question + ", have a lovely day!😊") 
        
    elif answer.isdigit(): #.isdigit() - check to see if answ input is a digit
        customer_choice = int(answer)
        if 1 <= customer_choice <= 4: #going through each value
            print("\nYou have choosen: " , drinks[customer_choice-1])
            customer_basket.append(drinks[customer_choice-1])
            print("Updated basket: " , ', ' .join(customer_basket))
        
    
    else:
        print("Invalid choice, chose between [1-4]")