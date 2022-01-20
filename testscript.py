import glove_signal_lib as gsl
from time import sleep

# while True:

on_time = .05
off_time = .05
n = 1
sleep_time = .5

gsl.Row1.pulse(on_time, off_time, n)
sleep(sleep_time)
gsl.Row2.pulse(on_time, off_time, n)
sleep(sleep_time)
gsl.Row3.pulse(on_time, off_time, n)
sleep(sleep_time)

gsl.Column1.pulse(on_time, off_time, n)
sleep(sleep_time)
gsl.Column2.pulse(on_time, off_time, n)
sleep(sleep_time)
gsl.Column3.pulse(on_time, off_time, n)
sleep(sleep_time)

gsl.Row1.blink(on_time, off_time, n)
sleep(sleep_time)
gsl.Row2.blink(on_time, off_time, n)
sleep(sleep_time)
gsl.Row3.blink(on_time, off_time, n)
sleep(sleep_time)

gsl.Column1.blink(on_time, off_time, n)
sleep(sleep_time)
gsl.Column2.blink(on_time, off_time, n)
sleep(sleep_time)
gsl.Column3.blink(on_time, off_time, n)
sleep(sleep_time)
