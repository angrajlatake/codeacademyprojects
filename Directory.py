'''Let’s say we have two lists that we want to combine into a dictionary, like a list of drinks and cafine amount:'''
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
"""You have two lists, representing some drinks sold at a coffee shop and the milligrams of caffeine in each. First, create a variable called zipped_drinks that is a zipped list of pairs between the drinks list and the caffeine list."""

drinks_to_caffeine  = {key:value for key, value in zipped_drinks}
"""Create a dictionary called drinks_to_caffeine by using a list comprehension that goes through the zipped_drinks list and turns each pair into a key:value item."""
print(zipped_drinks)

#new exercise

"""We are building a music streaming service. We have provided two lists, representing songs in a user’s library and the amount of times each song has been played.

Using a list comprehension, create a dictionary called plays that goes through zip(songs, playcounts) and creates a song:playcount pair for each song in songs and each playcount in playcounts."""
# this was given
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# my solution

amazing = zip(songs, playcounts)

plays = {key:value for key,value in amazing}
print(plays)

#After printing plays, add a new entry to it. The entry should be for the song "Purple Haze" and the playcount is 1

plays["Purple Haze"] : 1

#This user has caught Aretha Franklin fever and listened to “Respect” 5 more times. Update the value for "Respect" to be 94 in the plays dictionary.

plays["Respect"] : 94

'''Create a dictionary called library that has two key: value pairs:

key "The Best Songs" with a value of plays, the dictionary you created
key "Sunday Feelings" with a value of an empty dictionary'''

library = {"The Best Songs" : plays, "Sunday Feelings" : []}
print(library)

#get value of key

print(plays["Imagine"])

# new exercise

'''Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. If the key you are trying to .get() does not exist, it will return None by default:'''

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

#Use .get() to get the value of "teraCoder"‘s user ID, with 100000 as a default value if the user doesn’t exist. Store it in a variable called tc_id. Print tc_id to the console.

tc_id = user_ids.get("teraCoder", 100000)

print(tc_id)


#Use .get() to get the value of "superStackSmash"‘s user ID, with 100000 as a default value if the user doesn’t exist. Store it in a variable called stack_id. Print stack_id to the console.

stack_id = user_ids.get("superStackSmash", 100000)

print(stack_id)

'''We can use .pop() to return the value of key and remove it from the list at the same time'''

#new exercise
print("new exercise")
'''.
You are designing the video game Big Rock Adventure. We have provided a dictionary of items that are in the player’s inventory which add points to their health meter. In one line, add the corresponding value of the key "stamina grains" to the health_points variable and remove the item "stamina grains" from the dictionary. If the key does not exist, add 0 to health_points.'''

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)

print(health_points)
print(available_items)

#In one line, add the value of "power stew" to health_points and remove the item from the dictionary. If the key does not exist, add 0 to health_points.

health_points += available_items.pop("power stew", 0)

print(health_points)
print(available_items)

#In one line, add the value of "mystic bread" to health_points and remove the item from the dictionary. If the key does not exist, add 0 to health_points.

health_points += available_items.pop("mystic bread", 0)

print(health_points)
print(available_items)

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()

#Create a variable called lessons and assign it to be a dict_keys object of all of the keys of the num_exercises dictionary.

lessons = num_exercises.keys()

print(users)
print(lessons)
