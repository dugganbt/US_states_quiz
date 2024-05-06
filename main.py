import turtle
import pandas as pd

# Create screen for game
screen = turtle.Screen()
screen.title("U.S. States Game")

# Using gif image as screen to play the quiz on
image_path = "blank_states_img.gif"
screen.addshape(image_path)  # load shape to screen to be able to use turtle
turtle.shape(image_path)  # change turtle to imagefile

# Load in the data
data = pd.read_csv("50_states.csv")

# Check if the guess is amongst the 50 states
correct_guesses = []
score = 0

while score < 50:
    # Pop up box to ask for the states from the user
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")

    # capitalize the first letter of each word in the string
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    # check if dataframe contains the state, and if state is already in the correct guess list
    if data["state"].str.contains(answer_state).any() and answer_state not in correct_guesses:
        # Get coordinates
        index_of_match = data.index[data["state"] == answer_state].max()
        coordinates = (data.iloc[index_of_match].x, data.iloc[index_of_match].y)

        # Write correct guess onto map
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(coordinates)
        writer.write(answer_state)

        # save correct guessand increa
        correct_guesses.append(answer_state)

        score = len(correct_guesses)

# Prepare a csv list of states that the player needs to learn
all_states = data.state.to_list()

# List comprehension to check which states are not in the guessed states
states_to_learn = [state for state in all_states if state not in correct_guesses]

# Save missing states list as csv file
states_to_learn_df = pd.DataFrame(states_to_learn, columns=['State'])
states_to_learn_df.to_csv('states_to_learn.csv')

turtle.mainloop()
