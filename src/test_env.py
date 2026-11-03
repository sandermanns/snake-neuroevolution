import random, time
from snake_env import SnakeEnv

env = SnakeEnv()
start = time.time()
scores = []
for _ in range(1000):
    env.reset()
    while env.alive:
        env.step(random.choice([0, 1, 2]))
    scores.append(env.score)
print("avg score:", sum(scores) / len(scores), "max:", max(scores))
print("time:", round(time.time() - start, 2), "seconds")