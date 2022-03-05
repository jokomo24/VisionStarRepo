from time import sleep
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

# fade_in_time = 0 
# fade_out_time = 0

# background defines whether a vibration request should, True, run in parallel as in vibrator A & B & C 
# or, False, run sequentially as in vibrator A then B then C
#background = False

class Vibrator:
    def A(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute in parallel
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def B(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute in parallel
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def C(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute in parallel
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def D(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute in parallel
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def E(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute in parallel
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def F(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute in parallel
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def G(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute in parallel
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def H(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute in parallel
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def I(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute in parallel
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)

class Row1:
    def blink(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute in parallel
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_rightward(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute sequentially
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_leftward(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute sequentially
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def pulse(on_time, off_time, n):
        background = True # execute in parallel
        vibrator_A.pulse(on_time, off_time, n, background)
        vibrator_B.pulse(on_time, off_time, n, background)
        vibrator_C.pulse(on_time, off_time, n, background)
    def pulse_rightward(on_time, off_time, n):
        background = False # execute sequentially
        vibrator_A.pulse(on_time, off_time, n, background)
        vibrator_B.pulse(on_time, off_time, n, background)
        vibrator_C.pulse(on_time, off_time, n, background)
    def pulse_leftward(on_time, off_time, n):
        background = False # execute sequentially
        vibrator_C.pulse(on_time, off_time, n, background)
        vibrator_B.pulse(on_time, off_time, n, background)
        vibrator_A.pulse(on_time, off_time, n, background)
    def pulse_inward(on_time, off_time, n):
        background = True # execute in parallel
        vibrator_A.pulse(on_time, off_time, n, background)
        vibrator_C.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_B.pulse(on_time, off_time, n, background)
    def pulse_outward(on_time, off_time, n):
        background = True # execute in parallel
        vibrator_B.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_A.pulse(on_time, off_time, n, background)
        vibrator_C.pulse(on_time, off_time, n, background)
    # Constant On/Off methods
    def on():
        vibrator_A.on()
        vibrator_B.on()
        vibrator_C.on()
    def off():
        vibrator_A.off()
        vibrator_B.off()
        vibrator_C.off()

class Row2:
    def blink(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute in parallel
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_rightward(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute sequentially
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_leftward(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute sequentially
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def pulse(on_time, off_time, n):
        background = True # execute in parallel
        vibrator_D.pulse(on_time, off_time, n, background)
        vibrator_E.pulse(on_time, off_time, n, background)
        vibrator_F.pulse(on_time, off_time, n, background)
    def pulse_rightward(on_time, off_time, n):
        background = False # execute sequentially
        vibrator_D.pulse(on_time, off_time, n, background)
        vibrator_E.pulse(on_time, off_time, n, background)
        vibrator_F.pulse(on_time, off_time, n, background)
    def pulse_leftward(on_time, off_time, n):
        background = False # execute sequentially
        vibrator_F.pulse(on_time, off_time, n, background)
        vibrator_E.pulse(on_time, off_time, n, background)
        vibrator_D.pulse(on_time, off_time, n, background)
    def pulse_inward(on_time, off_time, n):
        background = True # execute in parallel
        vibrator_D.pulse(on_time, off_time, n, background)
        vibrator_F.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_E.pulse(on_time, off_time, n, background)
    def pulse_outward(on_time, off_time, n):
        background = True # execute in parallel
        vibrator_E.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_D.pulse(on_time, off_time, n, background)
        vibrator_F.pulse(on_time, off_time, n, background)
    # Constant On/Off methods
    def on():
        vibrator_D.on()
        vibrator_E.on()
        vibrator_F.on()
    def off():
        vibrator_D.off()
        vibrator_E.off()
        vibrator_F.off()

class Row3:
    def blink(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute in parallel
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_rightward(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute sequentially
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_leftward(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute sequentially
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def pulse(on_time, off_time, n):
        background = True # execute in parallel
        vibrator_G.pulse(on_time, off_time, n, background)
        vibrator_H.pulse(on_time, off_time, n, background)
        vibrator_I.pulse(on_time, off_time, n, background)
    def pulse_rightward(on_time, off_time, n):
        background = False # execute sequentially
        vibrator_G.pulse(on_time, off_time, n, background)
        vibrator_H.pulse(on_time, off_time, n, background)
        vibrator_I.pulse(on_time, off_time, n, background)
    def pulse_leftward(on_time, off_time, n):
        background = False # execute sequentially
        vibrator_I.pulse(on_time, off_time, n, background)
        vibrator_H.pulse(on_time, off_time, n, background)
        vibrator_G.pulse(on_time, off_time, n, background)
    def pulse_inward(on_time, off_time, n):
        background = True # execute in parallel
        vibrator_G.pulse(on_time, off_time, n, background)
        vibrator_I.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_H.pulse(on_time, off_time, n, background)
    def pulse_outward(on_time, off_time, n):
        background = True # execute in parallel
        vibrator_H.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_G.pulse(on_time, off_time, n, background)
        vibrator_I.pulse(on_time, off_time, n, background)
    # Constant On/Off methods
    def on():
        vibrator_G.on()
        vibrator_H.on()
        vibrator_I.on()
    def off():
        vibrator_G.off()
        vibrator_H.off()
        vibrator_I.off()

class Column1:
    def blink(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute in parallel
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_upward(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute sequentially
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_downward(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute sequentially
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def pulse(on_time, off_time, n):
        background = True # execute in parallel
        vibrator_A.pulse(on_time, off_time, n, background)
        vibrator_D.pulse(on_time, off_time, n, background)
        vibrator_G.pulse(on_time, off_time, n, background)
    def pulse_upward(on_time, off_time, n):
        background = False # execute sequentially
        vibrator_G.pulse(on_time, off_time, n, background)
        vibrator_D.pulse(on_time, off_time, n, background)
        vibrator_A.pulse(on_time, off_time, n, background)
    def pulse_downward(on_time, off_time, n):
        background = False # execute sequentially
        vibrator_A.pulse(on_time, off_time, n, background)
        vibrator_D.pulse(on_time, off_time, n, background)
        vibrator_G.pulse(on_time, off_time, n, background)
    def pulse_inward(on_time, off_time, n):
        background = True # execute in parallel
        vibrator_A.pulse(on_time, off_time, n, background)
        vibrator_G.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_D.pulse(on_time, off_time, n, background)
    def pulse_outward(on_time, off_time, n):
        background = True # execute in parallel
        vibrator_D.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_A.pulse(on_time, off_time, n, background)
        vibrator_G.pulse(on_time, off_time, n, background)
    # Constant On/Off methods
    def on():
        vibrator_A.on()
        vibrator_D.on()
        vibrator_G.on()
    def off():
        vibrator_A.off()
        vibrator_D.off()
        vibrator_G.off()

class Column2:
    def blink(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute in parallel
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_upward(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute sequentially
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_downward(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute sequentially
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def pulse(on_time, off_time, n):
        background = True # execute in parallel
        vibrator_B.pulse(on_time, off_time, n, background)
        vibrator_E.pulse(on_time, off_time, n, background)
        vibrator_H.pulse(on_time, off_time, n, background)
    def pulse_upward(on_time, off_time, n):
        background = False # execute sequentially
        vibrator_H.pulse(on_time, off_time, n, background)
        vibrator_E.pulse(on_time, off_time, n, background)
        vibrator_B.pulse(on_time, off_time, n, background)
    def pulse_downward(on_time, off_time, n):
        background = False # execute sequentially
        vibrator_B.pulse(on_time, off_time, n, background)
        vibrator_E.pulse(on_time, off_time, n, background)
        vibrator_H.pulse(on_time, off_time, n, background)
    def pulse_inward(on_time, off_time, n):
        background = True # execute in parallel
        vibrator_B.pulse(on_time, off_time, n, background)
        vibrator_H.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_E.pulse(on_time, off_time, n, background)
    def pulse_outward(on_time, off_time, n):
        background = True # execute in parallel
        vibrator_E.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_B.pulse(on_time, off_time, n, background)
        vibrator_H.pulse(on_time, off_time, n, background)
    # Constant On/Off methods
    def on():
        vibrator_B.on()
        vibrator_E.on()
        vibrator_H.on()
    def off():
        vibrator_B.off()
        vibrator_E.off()
        vibrator_H.off()

class Column3:
    def blink(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute in parallel
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_upward(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute sequentially
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def blink_downward(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute sequentially
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def pulse(on_time, off_time, n):
        background = True # execute in parallel
        vibrator_C.pulse(on_time, off_time, n, background)
        vibrator_F.pulse(on_time, off_time, n, background)
        vibrator_I.pulse(on_time, off_time, n, background)
    def pulse_upward(on_time, off_time, n):
        background = False # execute sequentially
        vibrator_I.pulse(on_time, off_time, n, background)
        vibrator_F.pulse(on_time, off_time, n, background)
        vibrator_C.pulse(on_time, off_time, n, background)
    def pulse_downward(on_time, off_time, n):
        background = False # execute sequentially
        vibrator_C.pulse(on_time, off_time, n, background)
        vibrator_F.pulse(on_time, off_time, n, background)
        vibrator_I.pulse(on_time, off_time, n, background)
    def pulse_inward(on_time, off_time, n):
        background = True # execute in parallel
        vibrator_C.pulse(on_time, off_time, n, background)
        vibrator_I.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_F.pulse(on_time, off_time, n, background)
    def pulse_outward(on_time, off_time, n):
        background = True # execute in parallel
        vibrator_F.pulse(on_time, off_time, n, background)
        sleep(off_time)
        vibrator_C.pulse(on_time, off_time, n, background)
        vibrator_I.pulse(on_time, off_time, n, background)
    # Constant On/Off methods
    def on():
        vibrator_C.on()
        vibrator_F.on()
        vibrator_I.on()
    def off():
        vibrator_C.off()
        vibrator_F.off()
        vibrator_I.off()

class Arrow:
    # Define Arrow Pattern methods
    # Sequential
    def upward_left(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute arrow body sequentially
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        background = True # execute arrow wings in parallel
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def upward_right(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute arrow body sequentially
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        background = True # execute arrow wings in parallel
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def downward_right(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute arrow body sequentially
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        background = True # execute arrow wings in parallel
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def downward_left(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute arrow body sequentially
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        background = True # execute arrow wings in parallel
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def upward(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute arrow body sequentially
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        background = True # execute arrow wings in parallel
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def downward(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute arrow body sequentially
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        background = True # execute arrow wings in parallel
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def leftward(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute arrow body sequentially
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        background = True # execute arrow wings in parallel
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def rightward(on_time, off_time, fade_in_time, fade_out_time, n):
        background = False # execute arrow body sequentially
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        background = True # execute arrow wings in parallel
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    # Parallel
    def out_left(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute arrow body in parallel
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        sleep(off_time)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def out_right(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute arrow body in parallel
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        sleep(off_time)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def in_right(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute arrow body in parallel
        vibrator_A.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_I.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        sleep(off_time)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def in_left(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute arrow body in parallel
        vibrator_C.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_G.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        sleep(off_time)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def up(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute arrow body in parallel
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        sleep(off_time)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def down(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute arrow body in parallel
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        sleep(off_time)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def left(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute arrow body in parallel
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        sleep(off_time)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
    def right(on_time, off_time, fade_in_time, fade_out_time, n):
        background = True # execute arrow body in parallel
        vibrator_D.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_E.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_F.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        sleep(off_time)
        vibrator_B.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)
        vibrator_H.blink(on_time, off_time, fade_in_time, fade_out_time, n, background)

class Triangle:
    def up(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def down(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def upperleft(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_A.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def upperright(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_C.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def lowerleft(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_G.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def lowerright(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_I.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    # Sequential Functions
    def upward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        sleep(blink_on_time)
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def downward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        sleep(blink_on_time)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def leftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        sleep(blink_on_time)
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        sleep(blink_on_time)
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def upperleftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        sleep(blink_on_time)
        vibrator_A.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def upperrightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        sleep(blink_on_time)
        vibrator_C.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def lowerleftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        sleep(blink_on_time)
        vibrator_G.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def lowerrightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        sleep(blink_on_time)
        vibrator_I.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)

class Diagnal:
    def AEI(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_A.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_E.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_I.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def CEG(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_C.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_E.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_G.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def BF(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def DH(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def BD(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def FH(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def X(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_A.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_E.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_I.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_C.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_G.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)

class Box:
    def full(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_A.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_C.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_E.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_G.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_I.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def foursides(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_A.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_C.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_G.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_I.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def fourcorners(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_A.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_C.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_G.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_I.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def upperleft(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_A.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_E.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def upperright(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_C.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_E.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def lowerleft(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_E.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_G.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def lowerright(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_E.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_I.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def leftrect(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_A.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_E.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_G.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def rightrect(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_C.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_E.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_I.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def upperrect(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_A.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_E.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_C.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def lowerrect(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_E.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_G.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_I.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def diamond(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_E.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
    def diamondhollow(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n):
        background = True
        vibrator_D.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_B.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_H.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)
        vibrator_F.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n, background)

# Here we will describe signals using the previously defined ones
# based on a level of urgency defined below.
# 

# Here we establish three priority levels for the glove signals:
#   1. ALERT       - Three short blinks
#   2. ATTENTION   - Two short blinks
#   3. AKNOWLEDGE  - One short blink

class Alert:
    def Vibrator(which):
        if (which == "A"):
            Vibrator.A(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.A(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.A(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "B"):
            Vibrator.B(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.B(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.B(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "C"):
            Vibrator.C(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.C(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.C(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "D"):
            Vibrator.D(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.D(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.D(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "E"):
            Vibrator.E(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.E(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.E(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "F"):
            Vibrator.F(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.F(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.F(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "G"):
            Vibrator.G(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.G(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.G(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "H"):
            Vibrator.H(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.H(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.H(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "I"):
            Vibrator.I(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.I(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.I(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS) 
    def Row(rowNum):
        if (rowNum == 1):
            Row1.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Row1.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Row1.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (rowNum == 2):
            Row2.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Row2.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Row2.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (rowNum == 3):
            Row3.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Row3.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Row3.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Column(colNum):
        if (colNum == 1):
            Column1.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Column1.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Column1.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (colNum == 2):
            Column2.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Column2.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Column2.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (colNum == 3):
            Column3.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Column3.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Column3.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Triangle(direction):
        if (direction == "upward"):
            Triangle.upward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.upward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.upward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "downward"):
            Triangle.downward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.downward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.downward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "leftward"):
            Triangle.leftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.leftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.leftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "rightward"):
            Triangle.rightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.rightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.rightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "upperleftward"):
            Triangle.upperleftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.upperleftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.upperleftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "upperrightward"):
            Triangle.upperrightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.upperrightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.upperrightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "lowerrightward"):
            Triangle.lowerrightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.lowerrightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.lowerrightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "lowerleftward"):
            Triangle.lowerleftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.lowerleftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.lowerleftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Box(type):
        if (type == "full"):
            Box.full(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.full(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.full(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "foursides"):
            Box.foursides(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.foursides(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.foursides(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "fourcorners"):
            Box.fourcorners(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.fourcorners(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.fourcorners(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "upperleft"):
            Box.upperleft(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.upperleft(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.upperleft(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "upperright"):
            Box.upperright(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.upperright(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.upperright(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "lowerright"):
            Box.lowerright(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.lowerright(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.lowerright(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "lowerleft"):
            Box.lowerleft(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.lowerleft(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.lowerleft(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "leftrect"):
            Box.leftrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.leftrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.leftrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "rightrect"):
            Box.rightrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.rightrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.rightrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "upperrect"):
            Box.upperrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.upperrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.upperrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "lowerrect"):
            Box.lowerrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.lowerrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.lowerrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "diamond"):
            Box.diamond(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.diamond(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.diamond(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "diamondhollow"):
            Box.diamondhollow(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.diamondhollow(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.diamondhollow(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Above():
        Row1.blink_rightward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Row1.blink_leftward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Row1.blink_rightward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Row1.blink_leftward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Row1.blink_rightward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Row1.blink_leftward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Below():
        Row3.blink_rightward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Row3.blink_leftward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Row3.blink_rightward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Row3.blink_leftward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Row3.blink_rightward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Row3.blink_leftward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Left():
        Column1.blink_downward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Column1.blink_upward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Column1.blink_downward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Column1.blink_upward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Column1.blink_downward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Column1.blink_upward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Right():
        Column3.blink_downward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Column3.blink_upward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Column3.blink_downward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Column3.blink_upward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Column3.blink_downward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Column3.blink_upward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)

class Attention:
    def Vibrator(which):
        if (which == "A"):
            Vibrator.A(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.A(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "B"):
            Vibrator.B(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.B(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "C"):
            Vibrator.C(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.C(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "D"):
            Vibrator.D(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.D(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "E"):
            Vibrator.E(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.E(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "F"):
            Vibrator.F(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.F(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "G"):
            Vibrator.G(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.G(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "H"):
            Vibrator.H(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.H(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "I"):
            Vibrator.I(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Vibrator.I(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Row(rowNum):
        if (rowNum == 1):
            Row1.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Row1.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (rowNum == 2):
            Row2.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Row2.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (rowNum == 3):
            Row3.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Row3.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Column(colNum):
        if (colNum == 1):
            Column1.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Column1.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (colNum == 2):
            Column2.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Column2.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (colNum == 3):
            Column3.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Column3.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Triangle(direction):
        if (direction == "upward"):
            Triangle.upward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.upward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "downward"):
            Triangle.downward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.downward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "leftward"):
            Triangle.leftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.leftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "rightward"):
            Triangle.rightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.rightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "upperleftward"):
            Triangle.upperleftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.upperleftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "upperrightward"):
            Triangle.upperrightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.upperrightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "lowerrightward"):
            Triangle.lowerrightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.lowerrightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "lowerleftward"):
            Triangle.lowerleftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Triangle.lowerleftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Box(type):
        if (type == "full"):
            Box.full(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.full(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "foursides"):
            Box.foursides(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.foursides(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "fourcorners"):
            Box.fourcorners(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.fourcorners(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "upperleft"):
            Box.upperleft(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.upperleft(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "upperright"):
            Box.upperright(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.upperright(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "lowerright"):
            Box.lowerright(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.lowerright(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "lowerleft"):
            Box.lowerleft(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.lowerleft(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "leftrect"):
            Box.leftrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.leftrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "rightrect"):
            Box.rightrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.rightrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "upperrect"):
            Box.upperrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.upperrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "lowerrect"):
            Box.lowerrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.lowerrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "diamond"):
            Box.diamond(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.diamond(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "diamondhollow"):
            Box.diamondhollow(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
            sleep(const.SLEEP_TIME)
            Box.diamondhollow(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Above():
        Row1.blink_rightward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Row1.blink_leftward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Row1.blink_rightward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Row1.blink_leftward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Below():
        Row3.blink_rightward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Row3.blink_leftward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Row3.blink_rightward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Row3.blink_leftward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Left():
        Column1.blink_downward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Column1.blink_upward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Column1.blink_downward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Column1.blink_upward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Right():
        Column3.blink_downward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Column3.blink_upward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Column3.blink_downward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Column3.blink_upward(const.BLINK_ON/2, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)

class Acknowledge:
    def Vibrator(which):
        if (which == "A"):
            Vibrator.A(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "B"):
            Vibrator.B(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "C"):
            Vibrator.C(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "D"):
            Vibrator.D(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "E"):
            Vibrator.E(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "F"):
            Vibrator.F(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "G"):
            Vibrator.G(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "H"):
            Vibrator.H(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (which == "I"):
            Vibrator.I(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Row(rowNum):
        if (rowNum == 1):
            Row1.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (rowNum == 2):
            Row2.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (rowNum == 3):
            Row3.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Column(colNum):
        if (colNum == 1):
            Column1.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (colNum == 2):
            Column2.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (colNum == 3):
            Column3.blink(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Triangle(direction):
        if (direction == "upward"):
            Triangle.upward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "downward"):
            Triangle.downward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "leftward"):
            Triangle.leftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "rightward"):
            Triangle.rightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "upperleftward"):
            Triangle.upperleftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "upperrightward"):
            Triangle.upperrightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "lowerrightward"):
            Triangle.lowerrightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (direction == "lowerleftward"):
            Triangle.lowerleftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Box(type):
        if (type == "full"):
            Box.full(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "foursides"):
            Box.foursides(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "fourcorners"):
            Box.fourcorners(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "upperleft"):
            Box.upperleft(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "upperright"):
            Box.upperright(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "lowerright"):
            Box.lowerright(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "lowerleft"):
            Box.lowerleft(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "leftrect"):
            Box.leftrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "rightrect"):
            Box.rightrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "upperrect"):
            Box.upperrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "lowerrect"):
            Box.lowerrect(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "diamond"):
            Box.diamond(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        elif (type == "diamondhollow"):
            Box.diamondhollow(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Above():
        Row1.blink_rightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Row1.blink_leftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Below():
        Row3.blink_rightward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Row3.blink_leftward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Left():
        Column1.blink_downward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Column1.blink_upward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
    def Right():
        Column3.blink_downward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
        Column3.blink_upward(const.BLINK_ON, const.BLINK_OFF, const.BLINK_FADE_IN, const.BLINK_FADE_OUT, const.NUM_BLINKS)
