####list programme

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
print(available_toppings)

requested_topping = input("What topping you want?" )
if requested_topping in available_toppings:
    print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza with "+ requested_topping )

else:
    print("Sorry, we don't have " + requested_topping + ".")
    print("\nFinished making your pizza without topping ")
        
