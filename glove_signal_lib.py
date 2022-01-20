import gpiozero
import constants as const

# Grid Layout Naming Convention
#         1      2     3
#      ____________________
#  1  |   A  |   B  |  C   |
#     |______|______|______|
#  2  |   D  |   E  |  F   |
#     |______|______|______|
#  3  |   G  |   H  |  I   |
#     |______|______|______|

# Initialize Vibrators - https://gpiozero.readthedocs.io/en/stable/api_output.html#pwmoutputdevice
active_high = True
initialVal = 0.0
freq = 100
pin_factory = None

vibrator_A = gpiozero.PWMOutputDevice(const.GPIO_A, active_high, initialVal, freq, pin_factory)
vibrator_B = gpiozero.PWMOutputDevice(const.GPIO_B, active_high, initialVal, freq, pin_factory)
vibrator_C = gpiozero.PWMOutputDevice(const.GPIO_C, active_high, initialVal, freq, pin_factory)
vibrator_D = gpiozero.PWMOutputDevice(const.GPIO_D, active_high, initialVal, freq, pin_factory)
vibrator_E = gpiozero.PWMOutputDevice(const.GPIO_E, active_high, initialVal, freq, pin_factory)
vibrator_F = gpiozero.PWMOutputDevice(const.GPIO_F, active_high, initialVal, freq, pin_factory)
vibrator_G = gpiozero.PWMOutputDevice(const.GPIO_G, active_high, initialVal, freq, pin_factory)
vibrator_H = gpiozero.PWMOutputDevice(const.GPIO_H, active_high, initialVal, freq, pin_factory)
vibrator_I = gpiozero.PWMOutputDevice(const.GPIO_I, active_high, initialVal, freq, pin_factory)

# |********************************************************************|
# | Here, we wish to define a set of Classes. Each Class will define a |
# | Haptic Signal Pattern. Each pattern will use 1 or more vibrators   |
# | with methods that define the style and feel of each particular     |
# | haptic message. Later, we will use these functions in our main app |
# | to interface with the camera and build logic to control the glove. |
# |********************************************************************|

# Define Classes for Column and Row patterns 

fade_in_time = 0 
fade_out_time = 0

# background defines whether a vibration request should, True, run in parallel as in vibrator A & B & C 
# or, False, run sequentially as in vibrator A then B then C
#background = False

class Row1:
    # Define vibration pattern/behavior with Class methods
    def blink(on_time, off_time, n, background):
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def pulse(on_time, off_time, n, background):
        vibrator_A.pulse(on_time, off_time, n, background)
        vibrator_B.pulse(on_time, off_time, n, background)
        vibrator_C.pulse(on_time, off_time, n, background)
    def on():
        vibrator_A.on()
        vibrator_B.on()
        vibrator_C.on()
    def off():
        vibrator_A.off()
        vibrator_B.off()
        vibrator_C.off()

class Row2:
    def blink(on_time, off_time, n, background):
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def pulse(on_time, off_time, n, background):
        vibrator_D.pulse(on_time, off_time, n, background)
        vibrator_E.pulse(on_time, off_time, n, background)
        vibrator_F.pulse(on_time, off_time, n, background)
    def on():
        vibrator_D.on()
        vibrator_E.on()
        vibrator_F.on()
    def off():
        vibrator_D.off()
        vibrator_E.off()
        vibrator_F.off()

class Row3:
    def blink(on_time, off_time, n, background):
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def pulse(on_time, off_time, n, background):
        vibrator_G.pulse(on_time, off_time, n, background)
        vibrator_H.pulse(on_time, off_time, n, background)
        vibrator_I.pulse(on_time, off_time, n, background)
    def on():
        vibrator_G.on()
        vibrator_H.on()
        vibrator_I.on()
    def off():
        vibrator_G.off()
        vibrator_H.off()
        vibrator_I.off()

class Column1:
    def blink(on_time, off_time, n, background):
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def pulse(on_time, off_time, n, background):
        vibrator_A.pulse(on_time, off_time, n, background)
        vibrator_D.pulse(on_time, off_time, n, background)
        vibrator_G.pulse(on_time, off_time, n, background)
    def on():
        vibrator_A.on()
        vibrator_D.on()
        vibrator_G.on()
    def off():
        vibrator_A.off()
        vibrator_D.off()
        vibrator_G.off()

class Column2:
    def blink(on_time, off_time, n, background):
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def pulse(on_time, off_time, n, background):
        vibrator_B.pulse(on_time, off_time, n, background)
        vibrator_E.pulse(on_time, off_time, n, background)
        vibrator_H.pulse(on_time, off_time, n, background)
    def on():
        vibrator_B.on()
        vibrator_E.on()
        vibrator_H.on()
    def off():
        vibrator_B.off()
        vibrator_E.off()
        vibrator_H.off()

class Column3:
    def blink(on_time, off_time, n, background):
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def pulse(on_time, off_time, n, background):
        vibrator_C.pulse(on_time, off_time, n, background)
        vibrator_F.pulse(on_time, off_time, n, background)
        vibrator_I.pulse(on_time, off_time, n, background)
    def on():
        vibrator_C.on()
        vibrator_F.on()
        vibrator_I.on()
    def off():
        vibrator_C.off()
        vibrator_F.off()
        vibrator_I.off()