import pico2d
import character
import monsters
import terrain
import ui


def show():
    print(character.realXLocation, monsters.Monster().monsterX + character.leftEndMove + character.x, character.jumpHeight, character.Mario().die)