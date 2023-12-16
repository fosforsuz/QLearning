import numpy as np
import pandas as pd


class QLearning:
    def __init__(self, actions: [], learning_rate: float, reward_decay: float, e_greedy: float):
        self.actions = actions
        self.learning_rate = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)

    def choose_action(self, observation):
        self.check_state_exist(observation)
        if np.random.uniform() < self.epsilon:
            state_action = self.q_table.ix[observation, :]
            state_action = state_action.reindex(
                np.random.permutation(state_action.index))  # make sure to not pick always the first value
            action = state_action.idxmax()
        else:
            action = np.random.choice(self.actions)
        return action

    def learn(self, s, a, r, s_, done):
        self.check_state_exist(s_)
        # get the Q value of the action a at state s
        q_predict = self.q_table.ix[s, a]

        if not done:
            q_target = r + self.gamma * self.q_table.ix[s_, :].max()  # next state is not terminal
        else:
            q_target = r  # next state is terminal
        self.q_table.ix[s, a] += self.learning_rate * (q_target - q_predict)

    def check_state_exist(self, state):
        if state not in self.q_table.index:
            # append new state to q table
            self.q_table = self.q_table.append(
                pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )
