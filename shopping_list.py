# This program can definitely run much mnore efficiently with less lines of code, but this is what I was able to come up with for now. I would like to complete the same excercise but as a dictionary not a list.

groc_list = []

while True:
    food = input("What's on your shopping list?\nType 'q' when finished. ")
    if food == 'q':
        break
    else:
        groc_list.append(food)
           
while True:
    add_food = input("Add items here: \ntype 'q' when done. ")
    if add_food == 'q':
          break
    else:
          groc_list.append(add_food)

while True:
    less_food = input("list any items you'd like to remove from the list: \nType 'q' to view final shopping list. ")
    if less_food == 'q':
         break
    else:
        if less_food in groc_list:
            groc_list.remove(less_food) 
 
        
print(f"Here is your grocery list: {groc_list}")


           
    
    
