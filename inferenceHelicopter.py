import tensorflow
import tensorflow as tf
import random, pygame, signal, time
from ple.games.pixelcopter import Pixelcopter
from ple import PLE
from pygame.constants import K_w, K_s
import numpy as np
from collections import deque
from tensorflow.python.keras import backend as K

from collections import deque
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout
from tensorflow.python.keras.optimizers import Adam

from tensorflow.python.keras.backend import manual_variable_initialization
manual_variable_initialization(True)

class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = 0.0004
        self.model = self._build_model()

    def _build_model(self):
        # Ensure to use same model architecture as that was trained and loaded
        model = Sequential()
        model.add(Dense(32, input_dim=self.state_size, activation='relu'))
        model.add(Dense(48, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(16, activation='relu'))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(self.action_size)) # default is linear activation
        model.compile(loss='mse',
                      optimizer=Adam(lr=self.learning_rate))
        return model

    def act(self, state):
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])  # returns action

    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        self.model.save_weights(name)

def resetEnv(ple_env):
    ple_env.reset_game()
    return getCurrentState(ple_env)

def getCurrentState(ple_env):
    state_dict = ple_env.getGameState()
    state = [state_dict[i] for i in state_dict]
    return np.reshape(state, [1, len(state)])

action_map = [K_w, K_s]
def actInEnv(ple_env, action_num):
    reward = ple_env.act(action_map[action_num])
    state = getCurrentState(ple_env)
    done = ple_env.game_over()
    action = action_map[action_num]
    return state, reward, done, action
    
EPISODES = 15000
starting_episode = 1
stop_flow = False


def sigint_handler(signum, frame):
    global stop_flow
    print('Going to stop the flow after the current episode terminates...')
    stop_flow = True
    
# To capture Ctrl-C events and stop gracefully
# Source: https://pythonadventures.wordpress.com/2012/11/21/handle-ctrlc-in-your-script/
signal.signal(signal.SIGINT, sigint_handler)

if __name__ == "__main__":
    #tf.keras.backend.clear_session()
    game = Pixelcopter(512, 512)
    p = PLE(game, fps=20, force_fps=False, display_screen=True)
    p.init()
    state_size = 7 # Don't hardcode?
    action_size = 2 # Up and No-op
    agent = DQNAgent(state_size, action_size)
    agent.load("./weights/heli-dqn-6000.h5")
    done = False

    for e in range(starting_episode, EPISODES):
        state = resetEnv(p)
        total_reward = 0.0
        done = False
        while True:
            action = agent.act(state)
            next_state, reward, done, _ = actInEnv(p, action)
            reward = reward if not done else -10
            total_reward += reward
            state = next_state
            if done:
                print("episode: {} - score: {}"
                      .format(e, total_reward))
                break
            
        if stop_flow:
            break
        
