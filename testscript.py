import glove_signal_lib as gsl
from time import sleep

# while True:

pulse_on_time = .5
pulse_off_time = .5
blink_on_time = .05
blink_off_time = .05
n = 1
sleep_time = .5
# background defines whether a vibration request should, True, run in parallel as in vibrator A & B & C 
# or, False, run sequentially as in vibrator A then B then C
background = True

gsl.Row1.pulse(pulse_on_time, pulse_off_time, n, background)
sleep(sleep_time)
gsl.Row2.pulse(pulse_on_time, pulse_off_time, n, background)
sleep(sleep_time)
gsl.Row3.pulse(pulse_on_time, pulse_off_time, n, background)
sleep(sleep_time)

gsl.Column1.pulse(pulse_on_time, pulse_off_time, n, background)
sleep(sleep_time)
gsl.Column2.pulse(pulse_on_time, pulse_off_time, n, background)
sleep(sleep_time)
gsl.Column3.pulse(pulse_on_time, pulse_off_time, n, background)
sleep(sleep_time)

gsl.Row1.blink(blink_on_time, blink_off_time, n, background)
sleep(sleep_time)
gsl.Row2.blink(blink_on_time, blink_off_time, n, background)
sleep(sleep_time)
gsl.Row3.blink(blink_on_time, blink_off_time, n, background)
sleep(sleep_time)

gsl.Column1.blink(blink_on_time, blink_off_time, n, background)
sleep(sleep_time)
gsl.Column2.blink(blink_on_time, blink_off_time, n, background)
sleep(sleep_time)
gsl.Column3.blink(blink_on_time, blink_off_time, n, background)
sleep(sleep_time)

background = False

gsl.Row1.pulse(pulse_on_time, pulse_off_time, n, background)
sleep(sleep_time)
gsl.Row2.pulse(pulse_on_time, pulse_off_time, n, background)
sleep(sleep_time)
gsl.Row3.pulse(pulse_on_time, pulse_off_time, n, background)
sleep(sleep_time)

gsl.Column1.pulse(pulse_on_time, pulse_off_time, n, background)
sleep(sleep_time)
gsl.Column2.pulse(pulse_on_time, pulse_off_time, n, background)
sleep(sleep_time)
gsl.Column3.pulse(pulse_on_time, pulse_off_time, n, background)
sleep(sleep_time)

gsl.Row1.blink(blink_on_time, blink_off_time, n, background)
sleep(sleep_time)
gsl.Row2.blink(blink_on_time, blink_off_time, n, background)
sleep(sleep_time)
gsl.Row3.blink(blink_on_time, blink_off_time, n, background)
sleep(sleep_time)

gsl.Column1.blink(blink_on_time, blink_off_time, n, background)
sleep(sleep_time)
gsl.Column2.blink(blink_on_time, blink_off_time, n, background)
sleep(sleep_time)
gsl.Column3.blink(blink_on_time, blink_off_time, n, background)
sleep(sleep_time)