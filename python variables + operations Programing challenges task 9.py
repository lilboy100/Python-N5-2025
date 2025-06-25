#Task 9: Recipe Scaler
#Write a program that:

#Stores ingredients for a chocolate chip cookie recipe that serves 4 people 
#(flour in grams, butter in grams, sugar in grams, number of eggs, chocolate chips in grams, vanilla in teaspoons)
#Work out the scaling factor as the user wants to cook for 6 people instead
#Scale all ingredients proportionally using the calculated factor
#Display the new ingredient amounts

flour = 200
butter = 100
sugger = 150
eggs = 2
chocolate_chips = 100
vanilla = 1

original_servings = 4
new_servings = 6

scaling_factor = new_servings / original_servings 

flour_new = flour *  scaling_factor
butter_new = butter * scaling_factor
sugger_new = sugger * scaling_factor
eggs_new = eggs * scaling_factor 
chocolate_chips_new = chocolate_chips * scaling_factor
vanilla_new = vanilla * scaling_factor

print("ingreedients for new_servings servings")
print("flour:",flour_new)
print("butter:",butter_new)
print("sugger:",sugger_new)
print("eggs:",eggs_new)
print("chocolate_chips:",chocolate_chips_new)
print("vanilla:",vanilla_new)