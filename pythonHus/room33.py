from . import room

from easygui import *
import sys


def do():
	th = room.grunnur(33)
	th.info = msgbox("Þú gengur inn í herbergi sem virðist tómt.")
