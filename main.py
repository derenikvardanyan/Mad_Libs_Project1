from functions import generate_and_display_story1, generate_and_display_story2, \
                      generate_and_display_story3

#a built-in module that can be used to make random numbers
import random

# randint() method returns an integer number
# selected element from range 1-3(included)
template_for_inputs = random.randint(1,3)

if template_for_inputs == 1:
    print(f"Template Number {template_for_inputs}")
    # prints the story in template1
    print(generate_and_display_story1())
elif template_for_inputs == 2:
    print(f"Template Number {template_for_inputs}")
    # prints the story in template2
    print(generate_and_display_story2())
elif template_for_inputs == 3:
    print(f"Template Number {template_for_inputs}")
    # prints the story in template3
    print(generate_and_display_story3())
else:
    print("There was no generated text.")
