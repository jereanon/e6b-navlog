import math
import cmath


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
    pa = (29.92 - altimeter) * 1000 + elevation
    return int(round(pa, 0))


def density_altitude(elevation, celsius_temp, altimeter=29.92):
    da = pressure_altitude(elevation, altimeter) + (120 * (celsius_temp - isa_temp(elevation)))
    return int(round(da, 0))


def isa_temp(elevation):
    return ((elevation/1000) * 2 - 15) * -1


def wind_correction_angle(wind_direction, wind_speed, course, true_airspeed):
    wca = (180 / math.pi) * math.asin((wind_speed / true_airspeed) * math.sin(math.pi * (wind_direction - course) / 180))
    return int(round(wca, 0))


def true_airspeed(altitude, celsius_oat, indicate_airspeed):
    '''
    Calculate true airspeed given an altitude, outside air temp in celcius, and an indicated airspeed.

    Adapted from: https://github.com/bjoernffm/e6b

    :param altitude: the altitude
    :param celsius_oat: the outside air temp
    :param indicate_airspeed: indicate air speed
    :return: true air speed
    '''

    qnh = 1013.25
    lapse_rate = 0.0019812              # degrees / foot std. lapse rate C° in to K° result
    temperature_correction = 273.15     # deg Kelvin
    standard_temperature0 = 288.15      # deg Kelvin

    xx = qnh / 1013.25

    pa = altitude + 145442.2 * (1 - pow(xx, 0.190261))

    standard_temperature = standard_temperature0 - pa * lapse_rate
    temperature_ratio = standard_temperature / lapse_rate

    xx = standard_temperature / (celsius_oat + temperature_correction)  # for temp in deg C

    da = pa + temperature_ratio * (1 - pow(xx, 0.234969))

    a = da * lapse_rate                 # Calculate DA temperature
    b = standard_temperature0 - a       # Correct DA temp to Kelvin
    c = b / standard_temperature0       # Temperature ratio
    c1 = 1 / 0.234969                   # Used to find .235 root next
    d = pow(c, c1)                      # Establishes Density Ratio
    d = pow(d, .5)                      # For TAS, square root of DR
    e = 1 / d                           # For TAS 1 divided by above
    TAS = e * indicate_airspeed
    return round(TAS)


if __name__ == '__main__':
    print(pressure_altitude(5000, 29.45))
    print(density_altitude(5000, 35, 29.45))
    print(wind_correction_angle(240, 8, 320, 100))
    print(true_airspeed(5000, 22, 100))
