import glove_signal_lib as gsl
from time import sleep
import sys;print(sys.version);print(sys.executable)

pulse_on_time = .5
pulse_off_time = .005
blink_on_time = .25
blink_off_time = .005
blink_fade_in_time = 0.0
blink_fade_out_time = 0.0
n = 1 # number of blinks
sleep_time = 1
# background defines whether a vibration request should, True, run in parallel as in vibrator A & B & C 
# or, False, run sequentially as in vibrator A then B then C
background = True

while True:

# Test Row and Column Signal Methods

    # gsl.Row1.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Row2.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Row3.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)

    # gsl.Row1.pulse(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Row2.pulse(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Row3.pulse(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Column1.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Column2.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Column3.blink(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)

    # gsl.Column1.pulse(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Column2.pulse(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Column3.pulse(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # Directional
    # gsl.Row1.blink_rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Row1.blink_leftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)

    # gsl.Row1.pulse_rightward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Row1.pulse_leftward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Row1.pulse_inward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Row1.pulse_outward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Row2.blink_rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Row2.blink_leftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)

    # gsl.Row2.pulse_rightward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Row2.pulse_leftward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Row2.pulse_inward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Row2.pulse_outward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Row3.blink_rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Row3.blink_leftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)

    # gsl.Row3.pulse_rightward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Row3.pulse_leftward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Row3.pulse_inward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Row3.pulse_outward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Column1.blink_upward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Column1.blink_downward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)

    # gsl.Column1.pulse_upward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Column1.pulse_downward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Column1.pulse_inward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Column1.pulse_outward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Column2.blink_upward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Column2.blink_downward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)

    # gsl.Column2.pulse_upward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Column2.pulse_downward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Column2.pulse_inward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Column2.pulse_outward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Column3.blink_upward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Column3.blink_downward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)

    # gsl.Column3.pulse_upward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Column3.pulse_downward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

    # gsl.Column3.pulse_inward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)
    # gsl.Column3.pulse_outward(pulse_on_time, pulse_off_time, n)
    # sleep(sleep_time)

# Test Arrow Signal Methods
    # Sequential
    # gsl.Arrow.upward_left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Arrow.downward_right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Arrow.upward_right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Arrow.downward_left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Arrow.upward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Arrow.downward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Arrow.leftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Arrow.rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    
#     # Parallel
#     blink_on_time = .5
#     blink_off_time = .5
#     sleep_time = 1
#     gsl.Arrow.out_left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
#     sleep(sleep_time)
#     gsl.Arrow.in_right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
#     sleep(sleep_time)
#     gsl.Arrow.out_right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
#     sleep(sleep_time)
#     gsl.Arrow.in_left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
#     sleep(sleep_time)
#     gsl.Arrow.up(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
#     sleep(sleep_time)
#     gsl.Arrow.down(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
#     sleep(sleep_time)
#     gsl.Arrow.left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
#     sleep(sleep_time)
#     gsl.Arrow.right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
#     sleep(sleep_time)

# Test Triangle Signal Methods
    # gsl.Triangle.up(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.down(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.upper_left(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.upper_right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.lowerleft(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.lower_right(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    
    # # # Sequential
    # gsl.Triangle.upward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.downward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.leftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.upper_leftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.upper_rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.lowerleftward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)
    # gsl.Triangle.lower_rightward(blink_on_time, blink_off_time, blink_fade_in_time, blink_fade_out_time, n)
    # sleep(sleep_time)

# Test Diagnal Signal Methods

# Test Box Signal Methods

# Test Urgency Signal Methods
#    Test Acknowledge
    # gsl.Acknowledge.Vibrator("A")
    # sleep(sleep_time)
    # gsl.Acknowledge.Vibrator("B")
    # sleep(sleep_time)
    # gsl.Acknowledge.Vibrator("C")
    # sleep(sleep_time)
    # gsl.Acknowledge.Vibrator("D")
    # sleep(sleep_time)
    # gsl.Acknowledge.Vibrator("E")
    # sleep(sleep_time)
    # gsl.Acknowledge.Vibrator("F")
    # sleep(sleep_time)
    # gsl.Acknowledge.Vibrator("G")
    # sleep(sleep_time)
    # gsl.Acknowledge.Vibrator("H")
    # sleep(sleep_time)
    # gsl.Acknowledge.Vibrator("I")
    # sleep(sleep_time)

    # gsl.Acknowledge.Row(1)
    # sleep(sleep_time)
    # gsl.Acknowledge.Row(2)
    # sleep(sleep_time)
    # gsl.Acknowledge.Row(3)
    # sleep(sleep_time)
    # gsl.Acknowledge.Column(1)
    # sleep(sleep_time)
    # gsl.Acknowledge.Column(2)
    # sleep(sleep_time)
    # gsl.Acknowledge.Column(3)
    # sleep(sleep_time)

    # gsl.Acknowledge.Triangle("upward")
    # sleep(sleep_time)
    # gsl.Acknowledge.Triangle("downward")
    # sleep(sleep_time)
    # gsl.Acknowledge.Triangle("leftward")
    # sleep(sleep_time)
    # gsl.Acknowledge.Triangle("rightward")
    # sleep(sleep_time)
    # gsl.Acknowledge.Triangle("upperleftward")
    # sleep(sleep_time)
    # gsl.Acknowledge.Triangle("upperrightward")
    # sleep(sleep_time)
    # gsl.Acknowledge.Triangle("lowerrightward")
    # sleep(sleep_time)
    # gsl.Acknowledge.Triangle("lowerleftward")
    # sleep(sleep_time)

    # gsl.Acknowledge.Box("full")
    # sleep(sleep_time)
    # gsl.Acknowledge.Box("foursides")
    # sleep(sleep_time)
    # gsl.Acknowledge.Box("fourcorners")
    # sleep(sleep_time)
    # gsl.Acknowledge.Box("upperleft")
    # sleep(sleep_time)
    # gsl.Acknowledge.Box("upperright")
    # sleep(sleep_time)
    # gsl.Acknowledge.Box("lowerright")
    # sleep(sleep_time)
    # gsl.Acknowledge.Box("lowerleft")
    # sleep(sleep_time)
    # gsl.Acknowledge.Box("leftrect")
    # sleep(sleep_time)
    # gsl.Acknowledge.Box("rightrect")
    # sleep(sleep_time)
    # gsl.Acknowledge.Box("upperrect")
    # sleep(sleep_time)
    # gsl.Acknowledge.Box("lowerrect")
    # sleep(sleep_time)
    # gsl.Acknowledge.Box("diamond")
    # sleep(sleep_time)
    # gsl.Acknowledge.Box("diamondhollow")
    # sleep(sleep_time)

    gsl.Acknowledge.Above()
    sleep(sleep_time)
    gsl.Acknowledge.Below()
    sleep(sleep_time)
    gsl.Acknowledge.Left()
    sleep(sleep_time)
    gsl.Acknowledge.Right()
    sleep(sleep_time)

    # # Test Attention
    # gsl.Attention.Vibrator("A")
    # sleep(sleep_time)
    # gsl.Attention.Vibrator("B")
    # sleep(sleep_time)
    # gsl.Attention.Vibrator("C")
    # sleep(sleep_time)
    # gsl.Attention.Vibrator("D")
    # sleep(sleep_time)
    # gsl.Attention.Vibrator("E")
    # sleep(sleep_time)
    # gsl.Attention.Vibrator("F")
    # sleep(sleep_time)
    # gsl.Attention.Vibrator("G")
    # sleep(sleep_time)
    # gsl.Attention.Vibrator("H")
    # sleep(sleep_time)
    # gsl.Attention.Vibrator("I")
    # sleep(sleep_time)

    # gsl.Attention.Row(1)
    # sleep(sleep_time)
    # gsl.Attention.Row(2)
    # sleep(sleep_time)
    # gsl.Attention.Row(3)
    # sleep(sleep_time)
    # gsl.Attention.Column(1)
    # sleep(sleep_time)
    # gsl.Attention.Column(2)
    # sleep(sleep_time)
    # gsl.Attention.Column(3)
    # sleep(sleep_time)

    # gsl.Attention.Triangle("upward")
    # sleep(sleep_time)
    # gsl.Attention.Triangle("downward")
    # sleep(sleep_time)
    # gsl.Attention.Triangle("leftward")
    # sleep(sleep_time)
    # gsl.Attention.Triangle("rightward")
    # sleep(sleep_time)
    # gsl.Attention.Triangle("upperleftward")
    # sleep(sleep_time)
    # gsl.Attention.Triangle("upperrightward")
    # sleep(sleep_time)
    # gsl.Attention.Triangle("lowerrightward")
    # sleep(sleep_time)
    # gsl.Attention.Triangle("lowerleftward")
    # sleep(sleep_time)

    # gsl.Attention.Box("full")
    # sleep(sleep_time)
    # gsl.Attention.Box("foursides")
    # sleep(sleep_time)
    # gsl.Attention.Box("fourcorners")
    # sleep(sleep_time)
    # gsl.Attention.Box("upperleft")
    # sleep(sleep_time)
    # gsl.Attention.Box("upperright")
    # sleep(sleep_time)
    # gsl.Attention.Box("lowerright")
    # sleep(sleep_time)
    # gsl.Attention.Box("lowerleft")
    # sleep(sleep_time)
    # gsl.Attention.Box("leftrect")
    # sleep(sleep_time)
    # gsl.Attention.Box("rightrect")
    # sleep(sleep_time)
    # gsl.Attention.Box("upperrect")
    # sleep(sleep_time)
    # gsl.Attention.Box("lowerrect")
    # sleep(sleep_time)
    # gsl.Attention.Box("diamond")
    # sleep(sleep_time)
    # gsl.Attention.Box("diamondhollow")
    # sleep(sleep_time)

    gsl.Attention.Above()
    sleep(sleep_time)
    gsl.Attention.Below()
    sleep(sleep_time)
    gsl.Attention.Left()
    sleep(sleep_time)
    gsl.Attention.Right()
    sleep(sleep_time)

    # # Test Alert
    # gsl.Alert.Vibrator("A")
    # sleep(sleep_time)
    # gsl.Alert.Vibrator("B")
    # sleep(sleep_time)
    # gsl.Alert.Vibrator("C")
    # sleep(sleep_time)
    # gsl.Alert.Vibrator("D")
    # sleep(sleep_time)
    # gsl.Alert.Vibrator("E")
    # sleep(sleep_time)
    # gsl.Alert.Vibrator("F")
    # sleep(sleep_time)
    # gsl.Alert.Vibrator("G")
    # sleep(sleep_time)
    # gsl.Alert.Vibrator("H")
    # sleep(sleep_time)
    # gsl.Alert.Vibrator("I")
    # sleep(sleep_time)

    # gsl.Alert.Row(1)
    # sleep(sleep_time)
    # gsl.Alert.Row(2)
    # sleep(sleep_time)
    # gsl.Alert.Row(3)
    # sleep(sleep_time)
    # gsl.Alert.Column(1)
    # sleep(sleep_time)
    # gsl.Alert.Column(2)
    # sleep(sleep_time)
    # gsl.Alert.Column(3)
    # sleep(sleep_time)

    # gsl.Alert.Triangle("upward")
    # sleep(sleep_time)
    # gsl.Alert.Triangle("downward")
    # sleep(sleep_time)
    # gsl.Alert.Triangle("leftward")
    # sleep(sleep_time)
    # gsl.Alert.Triangle("rightward")
    # sleep(sleep_time)
    # gsl.Alert.Triangle("upperleftward")
    # sleep(sleep_time)
    # gsl.Alert.Triangle("upperrightward")
    # sleep(sleep_time)
    # gsl.Alert.Triangle("lowerrightward")
    # sleep(sleep_time)
    # gsl.Alert.Triangle("lowerleftward")
    # sleep(sleep_time)

    # gsl.Alert.Box("full")
    # sleep(sleep_time)
    # gsl.Alert.Box("foursides")
    # sleep(sleep_time)
    # gsl.Alert.Box("fourcorners")
    # sleep(sleep_time)
    # gsl.Alert.Box("upperleft")
    # sleep(sleep_time)
    # gsl.Alert.Box("upperright")
    # sleep(sleep_time)
    # gsl.Alert.Box("lowerright")
    # sleep(sleep_time)
    # gsl.Alert.Box("lowerleft")
    # sleep(sleep_time)
    # gsl.Alert.Box("leftrect")
    # sleep(sleep_time)
    # gsl.Alert.Box("rightrect")
    # sleep(sleep_time)
    # gsl.Alert.Box("upperrect")
    # sleep(sleep_time)
    # gsl.Alert.Box("lowerrect")
    # sleep(sleep_time)
    # gsl.Alert.Box("diamond")
    # sleep(sleep_time)
    # gsl.Alert.Box("diamondhollow")
    # sleep(sleep_time)

    gsl.Alert.Above()
    sleep(sleep_time)
    gsl.Alert.Below()
    sleep(sleep_time)
    gsl.Alert.Left()
    sleep(sleep_time)
    gsl.Alert.Right()
    sleep(sleep_time)