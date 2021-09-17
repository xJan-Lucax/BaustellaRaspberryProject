from snappy_hx711 import *

CLOCK_PIN = 6
DATA_PIN = 7

@setHook(HOOK_INIT)

def init():
    # Must be called before making measurements:
    hx711_begin(CLOCK_PIN, DATA_PIN)

def take_a_measurement():
    # Returns a 3-byte string:
    return hx711_read()

init()
while True:
    take_a_measurement()
    print("I DO")
