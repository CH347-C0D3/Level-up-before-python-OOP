fruits = ["apple", "banana", "pineapple", "orange", "avacado", "tomato", "cucumber"]    # a list of fruits, yes, tomato and cucumber are scientifically considered fruits

vegatables = ["tomato", "spinach", "potato", "bitter melon", "cucumber"]    # list of vegetables, tomato and cucumber are again considered vegetables in culinary

nveg = ["chicken", "pork", "beef", "mutton", "egg", "fish"]      # I like bitter melons but I'm not a vegan either

hfood = fruits + vegatables + nveg   # list supports a feature called concatenation which adds all other lists

filtered_data = set(hfood)  # converting the final list into a set to remove duplicates formed in the list. A set by default removes the duplicates inside it.

print("This is the list of healthy foods: ")

for item in filtered_data:
    print(item)
