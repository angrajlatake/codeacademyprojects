'''In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.

There are many ways you can extend this project on your own if you finish and want to get more practice!'''

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#We have provided you with two lists, letters and points. We would like to combine these two into a dictionary that would map a letter to its point value.

#Using a list comprehension and zip, create a dictionary called letter_to_points that has the elements of letters as the keys and the elements of points as the values.

lettrs_to_points = {key:value for key, value in zip(letters,points)}

#Our letters list did not take into account blank tiles. Add an element to the letter_to_points dictionary that has a key of " " and a point value of 0.

lettrs_to_points[" "] = 0

#We want to create a function that will take in a word and return how many points that word is worth.

#Define a function called score_word that takes in a parameter word.

#Inside score_word, create a variable called point_total and set it to 0.

def score_word(word):
    points_total = 0
    for char in word:
        points_total += lettrs_to_points.get(char, 0)
    return points_total



#Create a dictionary called player_to_words that maps players to a list of the words they have played. This table represents the data to transcribe into your dictionary:

player_to_word = {"player1" : ["BLUE, TENNIS, EXIT"], "wordNerd" : ["EARTH", "EYES", "MACHINE"], "Lexi Con" : ["ERASER", "BELLY", "HUSKY"], "Prof Reader" : ["ZAP", "COMA", "PERIOD"]}

#Create an empty dictionary called player_to_points.

player_to_point = {}

#player_to_points should now contain the mapping of players to how many points they’ve scored. Print this out to see the current standings for this game!

#If you’ve calculated correctly, wordNerd should be winning by 1 point.

def update_total_score() :
    for player, words in player_to_word.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)

            player_to_point[player] = player_points

update_total_score()
print(player_to_point)
# give option to enter the words and add it to the directory. Once the word is added update the score.
#every player will get 2 chances

count = 0
while count != 2 :

    for player, word in player_to_word.items():
        word =input(player +" Please enter your word :")
        player_to_word[player].append(word.upper())
    update_total_score()
    print(player_to_point)
    count+=1

print(player_to_word)


