import Stats
import random
import numpy as np


class Solver:
    def __init__(self, width: int, height: int):
        self.actions = [Stats.Action.MOVE_LEFT_UP, Stats.Action.MOVE_UP, Stats.Action.MOVE_RIGHT_UP,
                        Stats.Action.MOVE_LEFT, Stats.Action.MOVE_RIGHT,
                        Stats.Action.MOVE_LEFT_DOWN, Stats.Action.MOVE_DOWN, Stats.Action.MOVE_RIGHT_DOWN]
        self.number_of_actions = len(self.actions)
        self.width = width
        self.height = height
        # Create Random hells in the maze
        self.hells = np.array([])
        for i in range(0, 5):
            np.append(self.hells, [random.randint(0, self.width - 1), random.randint(0, self.height - 1)])

        self.goal = np.array([width - 1, height - 1])
        self.agent = np.array([0, 0])

    def reset(self):
        self.agent = np.array([0, 0])
        return self.agent

    def step(self, action: Stats.Action):
        agent = self.agent
        base_action = self.action_step(action, agent)
        self.agent = agent + base_action
        reward, done = self.reward()
        return self.agent, reward, done

    def action_step(self, action: Stats.Action, state: []):
        base_action = np.array([0, 0])
        if action == Stats.Action.MOVE_LEFT_UP:
            if state[0] > 0 and state[1] > 0:
                base_action[0] -= 1
                base_action[1] -= 1
        elif action == Stats.Action.MOVE_UP:
            if state[1] > 0:
                base_action[1] -= 1
        elif action == Stats.Action.MOVE_RIGHT_UP:
            if state[0] < self.width - 1 and state[1] > 0:
                base_action[0] += 1
                base_action[1] -= 1
        elif action == Stats.Action.MOVE_RIGHT:
            if state[0] < self.width - 1:
                base_action[0] += 1
        elif action == Stats.Action.MOVE_RIGHT_DOWN:
            if state[0] < self.width - 1 and state[1] < self.height - 1:
                base_action[0] += 1
                base_action[1] += 1
        elif action == Stats.Action.MOVE_DOWN:
            if state[1] < self.height - 1:
                base_action[1] += 1
        elif action == Stats.Action.MOVE_LEFT_DOWN:
            if state[0] > 0 and state[1] < self.height - 1:
                base_action[0] -= 1
                base_action[1] += 1
        elif action == Stats.Action.MOVE_LEFT:
            if state[0] > 0:
                base_action[0] -= 1

        return base_action

    def reward(self):
        if np.array_equal(self.agent, self.goal):
            r = 1
            done = True
        elif self.actor_is_in_hell(self.agent):
            r = -1
            done = True
        else:
            r = 0
            done = False
        return r, done

    def actor_is_in_hell(self, state):
        for i in range(len(self.hells)):
            if state[0] == self.hells[i][0] and state[1] == self.hells[i][1]:
                return True
        return False
