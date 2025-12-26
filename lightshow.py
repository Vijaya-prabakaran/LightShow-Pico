import machine
import utime
pin_numbers = [0, 1, 2, 3, 4, 6, 8, 10, 12, 13]
pins = [machine.Pin(p, machine.Pin.OUT) for p in pin_numbers]
while True:
    #forward direction
    for pin in pins:
        pin.on()
        utime.sleep(0.05)
        pin.off()  
    #reverse direction
    #first and last LED is skipped to avoid double blink
    for pin in pins[-2:0:-1]:
        pin.on()
        utime.sleep(0.05)
        pin.off()
