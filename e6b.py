import math


def degrees_to_radians(degrees):
    return math.radians(degrees)


def radians_to_degrees(radians):
    return math.degrees(radians)


def celsius(temp):
    return (temp - 32) * .5556


def farenheit(temp):
    return temp * 1.8 + 32


def mph(knots):
    return knots * 1.15078


def knots(mph):
    return mph * 0.868976


def pressure_altitude(elevation, altimeter=29.92):
    return (29.92 - altimeter) * 1000 + elevation


def density_altitude(elevation, celsius_temp, altimeter=29.92):
    return pressure_altitude(elevation, altimeter) + (120 * (celsius_temp - isa_temp(elevation)))


def isa_temp(elevation):
    return ((elevation/1000) * 2 - 15) * -1


def wind_correction_angle(wind_direction, wind_speed, course, true_airspeed):
    wca = (180 / math.pi) * math.asin((wind_speed / true_airspeed) * math.sin(math.pi * (wind_direction - course) / 180))
    return round(wca, 0)


if __name__ == '__main__':
    print(pressure_altitude(5000, 29.45))
    print(density_altitude(5000, 35, 29.45))
    print(wind_correction_angle(240, 8, 320, 100))
