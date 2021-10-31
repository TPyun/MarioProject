import game_framework
import pico2d
import monsters


import start_state

pico2d.open_canvas()
game_framework.run(start_state)
somemonsters = [ monsters.Monster() for i in range(10)]
pico2d.close_canvas()
