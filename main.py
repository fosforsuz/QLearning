import time
from solver import Solver
from rl import QLearning
from maze import Maze

EPISODE = 10_000
WIDTH = 10
HEIGHT = 10


def run_rl():
    start_time = time.time()
    for episode in range(EPISODE):
        observation = solver.reset()
        if episode % 500 == 0:
            print(str(float(episode) / EPISODE * 100) + "%")
        while True:
            maze.update_canvas(solver.agent)
            action = rl.choose_action(str(observation))
            observation_, reward, done = solver.step(action)
            rl.learn(str(observation), action, reward, str(observation_), done)
            observation = observation_
            if done:
                break
    # end of game
    print("My program took", time.time() - start_time, "to run")
    print('game over')


if __name__ == "__main__":
    solver = Solver(width=WIDTH, height=HEIGHT)
    maze = Maze(width=WIDTH, height=HEIGHT, scale=40, goal=solver.goal, hells=solver.hells)
    rl = QLearning(actions=solver.actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9)
    run_rl()
