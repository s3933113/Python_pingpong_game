Python Ping Pong Game
A classic two-player Ping Pong game built with Python using the turtle graphics library. This project was built as a practice project to apply Object-Oriented Programming (OOP) principles in Python.

How to Install & Run
Requirements
Python 3.x
Windows OS (required for winsound sound effects)
Steps
Clone or download this repository

git clone https://github.com/your-username/Python_pingpong_game.git
Navigate into the project folder

cd Python_pingpong_game
Run the game

python src/main.py
No external packages are needed. The game uses only Python's built-in turtle and winsound libraries.

How to Play / Controls
The game is Player vs AI. Player 1 controls the left paddle manually while Player 2 is controlled by the computer.

Player	Action	Key
Player A (Left)	Move Up	W
Player A (Left)	Move Down	S
Player B (Right)	Controlled by AI	—
Rules
The ball bounces off the top and bottom walls
If the ball passes the right wall, Player A scores a point
If the ball passes the left wall, Player B scores a point
The score is displayed at the top of the screen
Project Structure
Python_pingpong_game/
│
├── src/
│   ├── main.py       # Game entry point — window setup, game loop, collision logic
│   ├── ball.py       # Ball class — movement and position
│   └── paddle.py     # Paddle class — player and AI paddle
│
└── README.md
File Descriptions
File	Responsibility
main.py	Sets up the window, creates all objects, runs the game loop, handles scoring and collisions
ball.py	Defines the Ball class with position and movement methods
paddle.py	Defines the Paddle class with move up/down methods and position getter
OOP Design
This project applies core Object-Oriented Programming principles:

Classes
Ball — ball.py
Represents the game ball.

Attribute / Method	Description
self.dx / self.dy	Ball speed in x and y direction
xcor()	Returns current x position
ycor()	Returns current y position
setx(x)	Sets x position
sety(y)	Sets y position
goto(x, y)	Moves ball to a position (used on reset)
Paddle — paddle.py
Represents a paddle (used for both Player A and AI).

Attribute / Method	Description
__init__(x)	Creates a paddle at the given x position
move_up()	Moves the paddle up by 20 units
move_down()	Moves the paddle down by 20 units
ycor()	Returns current y position (used for collision detection)
OOP Principles Applied
Principle	How it's used
Encapsulation	Ball and Paddle hide their internal turtle.Turtle() object — outside code only calls the class methods
Abstraction	main.py doesn't need to know how the ball or paddle draws itself — it just calls move_up(), setx(), etc.
Reusability	The same Paddle class is used for both Player A (Paddle(-350)) and the AI (Paddle(350))
