#!/usr/bin/python3
from skyfield.api import load, wgs84
from skyfield.searchlib import find_discrete
from datetime import timedelta
import sys

#######################
# START UPDATING HERE #
#######################

geosat = "GOES 16"
leosats = ["NOAA 15", "NOAA 18", "NOAA 19", "METEOR-M2 2", "METOP-B", "METOP-C"]
lat = 42.188724
lon = -78.839104
forecastDays = 14
#logfile = "conjunctions.txt"

######################
# STOP UPDATING HERE #
######################

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
weatherSats = load.tle_file('http://celestrak.com/NORAD/elements/weather.txt')
geoSats = load.tle_file('http://celestrak.com/NORAD/elements/geo.txt')
satellites = set(weatherSats + geoSats)
by_name = {sat.name: sat for sat in satellites}

geosatData = planets['earth'] + by_name[geosat]

#Log if configured
if 'logfile' in locals():
    logFileHandle = open(logfile, "w")

#Loop through all LEO Satellites
for leosat in leosats:
    leosatData = planets['earth'] + by_name[leosat]
    def geosat_leosat_quadrature(t):
        q = qth.at(t)
        g = q.observe(geosatData).apparent()
        n = q.observe(leosatData).apparent()
        return g.separation_from(n).degrees <= 5
    geosat_leosat_quadrature.step_days = 0.0001
    
    print("\nCalculating conjunctions for " + leosat + "...", end="\r")
    times,values = find_discrete(t1, t2, geosat_leosat_quadrature)
    
    sys.stdout.write("\033[K")
    print(leosat + " within 5deg of " + geosat + "\n------------------------------")
    
    if 'logfile' in locals():
        logFileHandle.write(leosat + " within 5deg of " + geosat + "\n------------------------------")
    
    for ti, vi in zip(times, values):
        if(vi == 1):
            print("Start: ", ti.utc_strftime('%Y-%m-%d %H:%M:%S'))
            if 'logfile' in locals():
                logFileHandle.write("\n" + "Start: " + ti.utc_strftime('%Y-%m-%d %H:%M:%S'))
        else:
            print("End: ", ti.utc_strftime('%Y-%m-%d %H:%M:%S'))
            if 'logfile' in locals():
                logFileHandle.write("\n" + "End: " + ti.utc_strftime('%Y-%m-%d %H:%M:%S'))
            
    if 'logfile' in locals():
        logFileHandle.write("\n\n")

#Close the log
if 'logfile' in locals():
    logFileHandle.close()
