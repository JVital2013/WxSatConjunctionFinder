#!/usr/bin/python3
from skyfield.api import load, wgs84
from skyfield.searchlib import find_discrete
from datetime import timedelta
import sys

geosat = "GOES 16"
lat = 42.188724
lon = -78.839104
forecastDays = 14

print("LEO WxSat Conjunctions with " + geosat)
print("Your Location: " + str(lat) + ", " + str(lon))
print("Calculating " + str(forecastDays) + " days")

#N-day window starting from now
ts = load.timescale()
t1 = ts.now()
t2 = ts.utc(t1.utc_datetime() + timedelta(days=forecastDays))

#Update these coordinates to your exact location
planets = load('de421.bsp')
qth = planets['earth'] + wgs84.latlon(lat, lon)

#Satellite info
satellites = load.tle_file('http://celestrak.com/NORAD/elements/weather.txt')
by_name = {sat.name: sat for sat in satellites}
GEOSAT = planets['earth'] + by_name[geosat]
NOAA15 = planets['earth'] + by_name['NOAA 15']
NOAA18 = planets['earth'] + by_name['NOAA 18']
NOAA19 = planets['earth'] + by_name['NOAA 19']
METEORM22 = planets['earth'] + by_name['METEOR-M2 2']
METOPB = planets['earth'] + by_name['METOP-B']
METOPC = planets['earth'] + by_name['METOP-C']

#Define approach checkers
#Resolution = 8.64 seconds
def geosat_noaa15_quadrature(t):
    q = qth.at(t)
    g = q.observe(GEOSAT).apparent()
    n = q.observe(NOAA15).apparent()
    return g.separation_from(n).degrees <= 5
geosat_noaa15_quadrature.step_days = 0.0001

def geosat_noaa18_quadrature(t):
    q = qth.at(t)
    g = q.observe(GEOSAT).apparent()
    n = q.observe(NOAA18).apparent()
    return g.separation_from(n).degrees <= 5
geosat_noaa18_quadrature.step_days = 0.0001

def geosat_noaa19_quadrature(t):
    q = qth.at(t)
    g = q.observe(GEOSAT).apparent()
    n = q.observe(NOAA19).apparent()
    return g.separation_from(n).degrees <= 5
geosat_noaa19_quadrature.step_days = 0.0001

def geosat_meteorm22_quadrature(t):
    q = qth.at(t)
    g = q.observe(GEOSAT).apparent()
    n = q.observe(METEORM22).apparent()
    return g.separation_from(n).degrees <= 5
geosat_meteorm22_quadrature.step_days = 0.0001

def geosat_metopb_quadrature(t):
    q = qth.at(t)
    g = q.observe(GEOSAT).apparent()
    n = q.observe(METOPB).apparent()
    return g.separation_from(n).degrees <= 5
geosat_metopb_quadrature.step_days = 0.0001

def geosat_metopc_quadrature(t):
    q = qth.at(t)
    g = q.observe(GEOSAT).apparent()
    n = q.observe(METOPC).apparent()
    return g.separation_from(n).degrees <= 5
geosat_metopc_quadrature.step_days = 0.0001

#Perform Calculations and outout results
print("\nCalculating conjuctions for NOAA-15...", end="\r")
times,values = find_discrete(t1, t2, geosat_noaa15_quadrature)
sys.stdout.write("\033[K")
print("NOAA 15 within 5deg of " + geosat)
print("------------------------------")
for ti, vi in zip(times, values):
    if(vi == 1):
        print("Start: ", ti.utc_strftime('%Y-%m-%d %H:%M:%S'))
    else:
        print("End: ", ti.utc_strftime('%Y-%m-%d %H:%M:%S'))

print("\nCalculating conjuctions for NOAA-18...", end="\r")
times,values = find_discrete(t1, t2, geosat_noaa18_quadrature)
sys.stdout.write("\033[K")
print("NOAA 18 within 5deg of " + geosat)
print("------------------------------")
for ti, vi in zip(times, values):
    if(vi == 1):
        print("Start: ", ti.utc_strftime('%Y-%m-%d %H:%M:%S'))
    else:
        print("End: ", ti.utc_strftime('%Y-%m-%d %H:%M:%S'))

print("\nCalculating conjuctions for NOAA-19...", end="\r")
times,values = find_discrete(t1, t2, geosat_noaa19_quadrature)
sys.stdout.write("\033[K")
print("NOAA 19 within 5deg of " + geosat)
print("------------------------------")
for ti, vi in zip(times, values):
    if(vi == 1):
        print("Start: ", ti.utc_strftime('%Y-%m-%d %H:%M:%S'))
    else:
        print("End: ", ti.utc_strftime('%Y-%m-%d %H:%M:%S'))

print("\nCalculating conjuctions for METEOR M2-2...", end="\r")
times,values = find_discrete(t1, t2, geosat_meteorm22_quadrature)
sys.stdout.write("\033[K")
print("METEOR M2-2 within 5deg of " + geosat)
print("----------------------------------")
for ti, vi in zip(times, values):
    if(vi == 1):
        print("Start: ", ti.utc_strftime('%Y-%m-%d %H:%M:%S'))
    else:
        print("End: ", ti.utc_strftime('%Y-%m-%d %H:%M:%S'))
        
print("\nCalculating conjuctions for MetOp-B...", end="\r")
times,values = find_discrete(t1, t2, geosat_metopb_quadrature)
sys.stdout.write("\033[K")
print("MetOp-B within 5deg of " + geosat)
print("----------------------------------")
for ti, vi in zip(times, values):
    if(vi == 1):
        print("Start: ", ti.utc_strftime('%Y-%m-%d %H:%M:%S'))
    else:
        print("End: ", ti.utc_strftime('%Y-%m-%d %H:%M:%S'))
        
print("\nCalculating conjuctions for MetOp-C...", end="\r")
times,values = find_discrete(t1, t2, geosat_metopc_quadrature)
sys.stdout.write("\033[K")
print("MetOp-C within 5deg of " + geosat)
print("----------------------------------")
for ti, vi in zip(times, values):
    if(vi == 1):
        print("Start: ", ti.utc_strftime('%Y-%m-%d %H:%M:%S'))
    else:
        print("End: ", ti.utc_strftime('%Y-%m-%d %H:%M:%S'))