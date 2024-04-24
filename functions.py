# returns the text of template 1 fullfilled
# with the information user wrote in input fields
def generate_and_display_story1():
    number = input("Input a number(greater than 1): ")
    measure_of_time = input("Input a measure of time(plural): ")
    mode_of_transportation = input(
        "Input a mode of transportation: ")
    adjective = input("Input an adjective: ")
    adjective2 = input("Input an adjective: ")
    noun = input("Input a noun(plural): ")
    color = input("Input a color: ")
    part_of_the_Body = input("Input a part of body(plural): ")
    verb1 = input("Input a verb: ")
    number2 = input("Input a number(greater than 1): ")  # plural issue 9
    noun2 = input("Input a noun(plural): ")  # plural issue arms
    noun3 = input("Input a noun: ")
    part_of_the_Body_2 = input("Input a part of body(plural): ")
    verb2 = input("Input a verb: ")
    noun4 = input("Input a noun: ")
    adjective3 = input("Input an adjective: ")
    silly_Word = input("Input a silly word: ")
    noun5 = input("Input a noun: ")
    return f"""
            It was about {number} {measure_of_time} ago when I arrived at the hospital
            in a/an {mode_of_transportation}. The hospital is a/an {adjective} place,
            there are a lot of {adjective2} {noun} here. There are nurses here who have 
            {color} {part_of_the_Body}. If someone wants to come into my room I told them that they have to 
            {verb1} first. I’ve decorated my room with {number2} {noun2}. "
            Today I talked to a doctor and they were wearing a {noun3} on their {part_of_the_Body_2}. 
            I heard that all doctors {verb2} {noun4} every day for breakfast. "
            The most {adjective3} thing about being in the hospital is the {silly_Word} {noun5} !"""


# returns the text of template 2 fullfilled
# with the information user wrote in input fields
def generate_and_display_story2():
    person_name_2 = input("Input a person's name: ")
    noun1_2 = input("Input a noun: ")
    adjective1_2 = input("Input an adjecitve(feeling): ")
    verb1_2 = input("Input a verb: ")
    adjective2_2 = input("Input an adjective(feeling): ")
    animal1_2 = input("Input an animal: ")
    verb2_2 = input("Input a verb: ")
    color1_2 = input("Input a color: ")
    verb_ing_2 = input("Input a verb ending in 'ing': ")
    adverb_ly_2 = input("Input an adverb ending in 'ly': ")
    number1_2 = input("Input a number(greater than 1): ")
    measure_of_time_2 = input("Input measure of time(plural): ")
    color2_2 = input("Input a color: ")
    animal2_2 = input("Input an animal:")
    number2_2 = input("Input a number(greater than 1): ")
    silly_word_2 = input("Input a silly word: ")
    noun2_2 = input("Input a noun: ")
    return f"""
                This weekend I am going camping with {person_name_2}. I packed my lantern, sleeping bag, and {noun1_2}.
                I am so {adjective1_2} to {verb1_2} in a tent. I am {adjective2_2} we might see a(n) {animal1_2}, I hear they’re kind of dangerous. 
                While we’re camping, we are going to hike, fish, and {verb2_2}. I have heard that the {color1_2} lake is great for {verb_ing_2}.
                Then we will {adverb_ly_2} hike through the forest for {number1_2} {measure_of_time_2}.
                If I see a {color2_2} {animal2_2} while hiking, I am going to bring it home as a pet! 
                At night we will tell {number2_2} {silly_word_2} stories and roast {noun2_2} around the campfire!!"""


# returns the text of template 3 fullfilled
# with the information user wrote in input fields
def generate_and_display_story3():
    persons_name_3 = input("Input a person's name: ")
    adjective1_3 = input("Input an adjective: ")
    color1_3 = input("Input a color: ")
    animal1_3 = input("Input an animal: ")
    place1_3 = input("Input a place: ")
    adjective2_3 = input("Input an adjective: ")
    magical_creature_plural1_3 = input("Input a magical creature(plural): ")
    adjective3_3 = input("Input and ajdective: ")
    magical_creature_plural2_3 = input("Input a magical creature(plural): ")
    room_in_house_3 = input("Input room in a house: ")
    noun1_3 = input("Input a noun: ")
    noun2_3 = input("Input a noun: ")
    noun3_3 = input("Input nouns(plural): ")
    adjective4_3 = input("Input an adjective: ")
    noun4_3 = input("Input a noun: ")
    number_3 = input("Input number(plural): ")
    measure_of_time_3 = input("Input measure of time(plural): ")
    verb_ing_3 = input("Input a verb ending in 'ing': ")
    adjective5_3 = input("Input an adjective: ")
    noun5_3 = input("Input a noun: ")

    return f"""
                Dear {persons_name_3}, I am writing to you from a/an {adjective1_3} castle in an enchanted forest. 
                I found myself here one day after going for a ride on a {color1_3} {animal1_3} in {place1_3}. 
                There are {adjective2_3} {magical_creature_plural1_3} and {adjective3_3} {magical_creature_plural2_3} here! 
                In the {room_in_house_3} there is a pool full of {noun1_3}. 
                I fall asleep each night on a {noun2_3} of {noun3_3} and dream of {adjective4_3} {noun4_3}. 
                It feels as though I have lived here for {number_3} {measure_of_time_3}. 
                I hope one day you can visit, although the only way to get here now is {verb_ing_3} on a {adjective5_3} {noun5_3}!!"""
