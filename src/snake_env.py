import random

class SnakeEnv:
    def __init__(self, width=30, height=30, max_idle_steps=100):
        self.width = width
        self.height = height
        self.max_idle_steps = max_idle_steps
        self.reset()

    def reset(self):
        self.snake = [(self.width // 2, self.height // 2)]   # head first
        self.direction = (0, 1)                               # (dx, dy), starts moving down
        self.score = 0
        self.steps = 0
        self.steps_since_food = 0
        self.food = self._place_food()
        self.alive = True

    def _place_food(self):
        # TODO: random grid cell that is not in self.snake
        pass

    def _turn(self, action):
        """action: 0 = straight, 1 = turn right, 2 = turn left. Returns the new (dx, dy)."""
        dx, dy = self.direction
        if action == 1:
            return (-dy, dx)
        if action == 2:
            return (dy, -dx)
        return (dx, dy)

    def _is_danger(self, cell):
        # TODO: True if cell is outside the grid or part of the snake body
        pass

    def step(self, action):
        # TODO:
        # 1. self.direction = self._turn(action)
        # 2. compute new head = old head + direction
        # 3. if self._is_danger(new_head): self.alive = False, return
        # 4. insert the new head; if it equals self.food: score += 1, place new food,
        #    steps_since_food = 0; else pop the tail and steps_since_food += 1
        # 5. steps += 1
        # 6. if steps_since_food > max_idle_steps: self.alive = False
        pass

    def get_state(self):
        # TODO: return a list of 11 numbers (0 or 1):
        # danger straight, danger right, danger left   (3)
        # direction is up, down, left, right           (4)
        # food is up, down, left, right of the head    (4)
        pass