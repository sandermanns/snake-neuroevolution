# snake-neuroevolution
Learning project: Snake played by NumPy neural networks that evolve over generations. Work in progress.

Snake Neuroevolution

A Snake game in Python where a neural network learns to play through evolution, built from scratch with NumPy. No machine learning libraries, no backpropagation.

Status: work in progress. The playable game is finished. The neural network and evolution are next.

Why this project

I wanted to understand how a neural network actually works, so I'm building one myself instead of using a framework. Watching AI learn Snake through evolution is what got me interested in the first place.

How it will work
A population of snakes, each controlled by a randomly generated neural network.
Every snake plays a game and gets a fitness score based on survival time and food eaten.
The best snakes are selected, combined (crossover) and slightly changed (mutation) to create the next generation.
Repeat for many generations until the snakes play well.

Planned network: 11 inputs (danger ahead/left/right, current direction, food direction), one hidden layer, 3 outputs (turn left, go straight, turn right).

Run the game

Requires Python 3.

bash
git clone https://github.com/<your-username>/snake-neuroevolution.git
cd snake-neuroevolution
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/snake_game.py

Controls

Key	Action
W / A / S / D	Move up / left / down / right
R	Restart after game over
Q	Quit after game over

In snake_game.py, set teleport_walls = False to make the walls deadly.

Project structure
snake-neuroevolution/
├── README.md
├── requirements.txt
├── src/
│   └── snake_game.py
└── images/
Roadmap
 Playable Snake game with pygame
 Separate game logic from drawing so games can run without a window
 Neural network (forward pass) in NumPy
 Fitness function
 Genetic algorithm: selection, crossover, mutation
 Plot fitness per generation
 Save and replay the best snake
 Record a demo GIF and add results to this README
What I'm learning
Python and pygame
How neural networks make decisions (matrices, activation functions)
Evolutionary algorithms
Git and GitHub
Credits

Learning resources I'm using:

3Blue1Brown, Neural Networks (YouTube)
Daniel Shiffman, The Nature of Code
pygame documentation
Author

Sander Sorholt, cybersecurity student.
