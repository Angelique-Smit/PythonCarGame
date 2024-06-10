# Import necessary modules
import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("2 Player Racing Game")
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Create the racetrack
racetrack = turtle.Turtle()
racetrack.shape("square")
racetrack.color("black")
racetrack.shapesize(stretch_wid=4, stretch_len=50)

# Create the finish line
finish_line = turtle.Turtle(visible=False)
finish_line.shape("square")
finish_line.color("yellow")
finish_line.shapesize(stretch_wid=4, stretch_len=1)
finish_line.penup()
finish_line.goto(screen.window_width() / 2.80 - 2 / 2, -2 / 2)
finish_line.pendown()
finish_line.showturtle()

# Car class
class Car:
    def __init__(self, brand, color, color2, acceleration, max_speed):
        # Initialize car attributes
        self.brand = brand        
        self.color = color
        self.color2 = color2
        self.acceleration = acceleration
        self.max_speed = max_speed
        self.speed = 0
        self.position = -screen.window_width() / 1.8  # Start at the left side
        self.timeout = 0  # Timeout counter

        # Initialize Turtle graphics for the car
        self.visual = turtle.Turtle(visible=False)
        self.visual.shape("square")
        self.visual.color(color)
        self.visual.shapesize(stretch_wid=1, stretch_len=3)
        self.visual.penup()
        self.visual.goto(self.position, -1)
        self.visual.pendown()
        self.visual.showturtle()

        # Additional visual component for the car
        self.visual2 = turtle.Turtle(visible=False)
        self.visual2.shape("square")
        self.visual2.color(color2)
        self.visual2.shapesize(stretch_wid=0.5, stretch_len=1)
        self.visual2.penup()
        self.visual2.goto(self.position, -1)
        self.visual2.pendown()
        self.visual2.showturtle()

    def accelerate(self):
        # Increase car speed up to the maximum speed
        self.speed = min(self.speed + self.acceleration, self.max_speed)

    def decelerate(self):
        # Decrease car speed with adjusted deceleration for smooth slowing down
        deceleration = 0.3 * self.max_speed
        self.speed = max(0, self.speed - deceleration)

    def move(self):
        # Move the car based on its current speed
        if self.timeout > 0:
            # Timeout in progress, decrement the counter
            self.timeout -= 1
            return

        self.position += self.speed
        self.visual.setx(self.position)
        self.visual2.setx(self.position)

    def check_speed_timeout(self):
        # Check if the car is speeding and apply a timeout if necessary
        if self.speed > 15 and self.timeout == 0:
            print(f"{self.brand} is speeding! Timeout for 3 seconds.")
            self.timeout = 180  # 3 seconds at 60 FPS (180 frames)
            self.speed = 0

# Create players' cars
player1 = Car("toyota", "blue", "red",  4, 20) 
player2 = Car("tesla","red", "blue", 2, 15)

# Keyboard bindings
screen.listen()
screen.onkeypress(player1.accelerate, "a")
screen.onkeyrelease(player1.decelerate, "z")  # 'z' for deceleration
screen.onkeypress(player2.accelerate, "k")
screen.onkeyrelease(player2.decelerate, "m")  # 'm' for deceleration

# Main game loop
while True:
    player1.check_speed_timeout()
    player2.check_speed_timeout()

    player1.move()
    player2.move()

    # Check if any player has crossed the finish line
    if player1.position > 285:
        print("Player 1 wins!")
        break
    elif player2.position > 285:
        print("Player 2 wins!")
        break
    screen.update()

# Close the Turtle graphics window
turtle.done()
