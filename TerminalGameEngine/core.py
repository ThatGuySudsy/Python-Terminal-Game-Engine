import render as r
from time import sleep

tps = 60

def main_loop(userUpdateFunc):
    r.render()
    userUpdateFunc()
    sleep(1/tps)