import RPi.GPIO as GPIO
from hx711 import HX711

try:
    hx711 = HX711(
        dout_pin=5,
        pd_sck_pin=6,
        channel='A',
        gain=64
    )

    print("1")
    hx711.reset()   # Before we start, reset the HX711 (not obligate)
    print("2")
    measures = hx711.get_raw_data(num_measures=3)
    print("3")
finally:
    print("4")
    GPIO.cleanup()  # always do a GPIO cleanup in your scripts!

print("5")
print("\n".join(measures))