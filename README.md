# WxSatConjunctionFinder
A quick and dirty python script that finds when NOAA 15, 18, 19, Meteor M2-2, MetOp-B, and MetOp-C are within 5 degrees of a Geostationary weather satellite, as viewed from your location.

To put it another way: it finds when a POES and GOES satellite are "in line" with your dish.

## Using the script
WxSatConjunctionFinder.py script depends on SkyField. To install it, run `pip install skyfield`.

To use WxSatConjunctionFinder.py, edit the script and set (at the top): 

- A Geostationary weather satellite
- Your latitude and longitude to 6 decimal places
- The number of days out to forecast conjunctions

This script is anything but efficient - calculating conjunctions within the next 30 days takes 7GB of RAM or more, and several minutes to complete. Conjunct at your own risk!

*Dates and times are in UTC*

## Why is this useful?
Many people have stationary satellite dishes pointed at Geostationary weather satellites to pick up their L-Band transmissions. The GOES HRIT is one common examples of this.

The same dishes, amplifiers, and SDRs can also be used to pick up the (A)HRPT transmissions of Polar-Orbiting satellites, except for one thing: how are you going to track the satellites as they mode across the sky? Some people put their dish on a rotor to track polar satellites, or hand track it, but what if you want to keep your stationary dish stationary for one reason or another?

If you don't care about image height or frequency of captures, WxSatConjunctionFinder solves the problem by letting you know when a polar orbiting satellite will be within the current beamwidth of the dish you're using for Geostationary satellite reception. You can then temporarily switch over to decoding HRPT at the right time and get a < 1 minute high-res recording from a LEO satellite - all from your stationary dish.

There are lots of problems with this approach:
- Your captures will only ever be so tall since they're limited by the beamwidth of your dish
- This happens infrequently - all HRPT satellites taken into account, it only happens 2-3 times a week from my location. Depending on your position on earth, this will vary
- You'll only ever see (roughly) the same point on the ground from a given location, and unless you're near the equator, you'll never be able to see your own weather

But, it's good for some simple, no-extra-cost fun on a Saturday afternoon!

## Example images captured from my stationary dish during conjenctions with GOES-16:

### NOAA-18 HRPT
![avhrr_3_rgb_Natural_Color_corrected](https://user-images.githubusercontent.com/24253715/215290038-b0a23c2f-c899-4b56-a928-272b5f16337c.png)

### Meteor M2-2 HRPT
![msu_mr_composite](https://user-images.githubusercontent.com/24253715/215290073-d4cfdad6-474f-40b4-a7ae-a9e71ea309a0.png)
