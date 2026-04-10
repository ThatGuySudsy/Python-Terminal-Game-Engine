import render as r
from time import sleep

def main_loop(userUpdateFunc = None, tps = 10):
    while True:
        r.render()
        userUpdateFunc()
        sleep(1/tps)