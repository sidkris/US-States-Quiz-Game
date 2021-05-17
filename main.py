import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"

screen.addshape(image)

guessed = []

states_data = pd.read_csv("50_states.csv")
states = states_data.state.to_list()

while (len(guessed) < 50):

  user_guess = screen.textinput(title = "{}/50 guesses correctly".format(len(guessed)), prompt = "Enter a state name : ")

  if (user_guess.title() in states) and (user_guess.title() not in guessed):
    t = turtle.Turtle()
    t.hideturtle() 
    t.penup() # so that the turtle doesnt draw
    loc = states_data[states_data.state == user_guess.title()]
    t.goto(int(loc.x), int(loc.y))
    t.write(user_guess.title())
    guessed.append(user_guess.title())

  elif user_guess == "exit":
    break

def endgame():
  missed = []
  for i in states:
    if i not in guessed:
      missed.append(i)
  if len(missed) > 0:
    print("you missed the following states: \n{}".format(missed))
  else:
    print("woohoo! you guessed all the states!")  
  print("thanks for playing! :)")

endgame()

screen.exitonclick()
