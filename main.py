import pgzrun
import math
import random
from pygame import Rect

hero = Actor("player/tile000", (400, 300))

sprites = []
for i in range(72):
        sprites.append(f"player/tile{i:03}")

current_frame = 0
frame_counter = 0
frame_duration = 10

def draw():
    screen.clear()
    hero.draw()

def update():
    global current_frame
    global frame_counter
    if frame_counter < frame_duration:
        frame_counter += 1
    else:
        frame_counter = 0
        current_frame = (current_frame + 1) % len(sprites)
    hero.image = sprites[current_frame]

pgzrun.go()