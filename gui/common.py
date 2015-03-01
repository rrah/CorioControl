from math import sqrt, log

def fade_speed_to_seconds(fade_speed):
    
    return 2.9 * (1/sqrt(2)) ** fade_speed

def seconds_to_fade_speed(time):
    
    fade_speed = int(2 * log(2.9 / time) / log(2))
    if fade_speed > 25:
        return 25
    elif fade_speed < 1:
        return 1
    else:
        return fade_speed
    
if __name__ == '__main__':
    print fade_speed_to_seconds(1)