import numpy as np
from pynput import keyboard
from threading import Thread
import time, pygame, sys
from ple.games.pixelcopter import Pixelcopter
from ple import PLE
from pygame.constants import K_w, K_s

stop_render = False
ready = False
total_reward = 0.0
debug_logs = False
action = K_s
prev_action = K_w
frame_skip = 1

def start_listen():
	## Listen for keypresses to control game via Terminal. Inspired from: https://pypi.python.org/pypi/pynput
	global action, ready, stop_render

	def on_press(key):
		global action, ready, stop_render
		if key == keyboard.Key.up:
			action = K_w
		elif key == keyboard.Key.space:
		    ready = True
		elif key == keyboard.Key.esc:
			stop_render = True
			sys.exit(0)
		else: action = K_s

	def on_release(key):
		global action
		action = K_s

	# Collect events until released
	with keyboard.Listener(
			on_press=on_press,
			on_release=on_release) as listener:
		listener.join()

print("Creating Environment..")
game = Pixelcopter(512, 512)
p = PLE(game, fps=25, force_fps=False, display_screen=True)
p.init()

t = Thread(target=start_listen) # Start listening to key presses and update actions
t.start()

print("Start playing..... :)")
while True:

	r = 0.0
	for _ in range(frame_skip):
		observation = p.getGameState()
		prev_action = action
		action = K_s # A bad hack to get things go smooth
		reward = p.act(prev_action)
		r += reward
		if p.game_over(): break
	
	total_reward += r
	if p.game_over():
		p.reset_game()
		reset = False
		print("Total reward in episode:"+str(total_reward))
		total_reward = 0.0
		ready = False
		#p.init()
		
	if stop_render:
		break

print("That's it")
