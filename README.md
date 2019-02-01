# Helicopter Game - Reinforcement Learning

Ever played the classic helicopter game during your childhood?  
If you haven't, here's the flash game: [helicoptergame.net](https://www.helicoptergame.net/)

So, this repo contains the source for training a clone of that game using reinforcement learning. That is, the helicopter (agent) learns to play the game by itself by avoiding the obstacles and traveling maximum possible distance.

## Demo Video

[![Helicopter Game - Reinforcement Learning](https://j.gifs.com/mORJnO.gif)](https://www.youtube.com/watch?v=A73qsxWH3mY)

## Requirements

1. Tested on `Python 3.6` with `Tensorflow 1.12` and `Keras 2.1.6-tf`
2. `pip3 install numpy pygame pillow pynput matplotlib tensorflow keras tensorflow-gpu`
3. I trained on Google Colab, but the `.ipynb` notebook should work on Jupyter, etc.

## Testing the game environment

To play the game by yourself, enter in Terminal:
```
python3 pixelCopterHumanPlay.py
```

Press `Up` arrow key to make the helicopter move up.  
Press `Esc` key to quit the play.

## Training

Use the [Train_Helicopter_DQN_RL.ipynb](Train_Helicopter_DQN_RL.ipynb) notebook to train the model (without gameplay render)

Note: You have to execute each cells step by step from bottom to top as directed in the `.ipynb` file.

To visualize the reward plot and loss plot, use the `plotRewards.py` and `plotLoss.py` files respectively. (You can set the filename inside the code)

## Inference

Inference has to be done on computer with graphics display for rendering.

```
python3 inferenceHelicopter.py
```

This will load the saved model weights and show the gameplay inference. I have included a sample weights file in this repo that works well, but it's not fully trained.

(If you change the model architecture in the notebook, don't forget to alter the same in this code as well)

## Credits

This game was modified by me from the [PyGame Learning Environment (PLE)](https://github.com/ntasfi/PyGame-Learning-Environment)'s [PixelCopter game](https://pygame-learning-environment.readthedocs.io/en/latest/user/games/pixelcopter.html).

The instructions to use the environment can be found in their [docs](https://pygame-learning-environment.readthedocs.io/en/latest/). The training code was inspired from [this post](https://towardsdatascience.com/reinforcement-learning-w-keras-openai-dqns-1eed3a5338c).

## TODO

1. Add support for this environment to OpenAI Gym ;)
2. Include the graph plotting code as part of the training code instead of separate files.
3. Train using [this official example](https://github.com/ntasfi/PyGame-Learning-Environment/blob/master/examples/keras_nonvis.py).

Feel free to clone/contribute to the repo :)
