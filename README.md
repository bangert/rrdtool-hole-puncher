# rrdtool-hole-puncher

Modify XML data generated by `rrdtool dump` such that all values in the given
timespan are set to NaN.

Only one hole can be punched at a time. Call this script multiple times, to punch
multiple holes.

Be aware, that if your hole is smaller than the aggregation interval of
one of the aggregations, your data will not be erased from that aggregation.

This script is based upon work by RobM at http://stackoverflow.com/questions/10298484/remove-data-from-rrdtool

Sample usage:
```
    rrdtool dump foo.rrd \
       | python rrdtool-hole-puncher.py 1486335600 1486421700 \
       | rrdtool restore - foo_trimmed.rrd
```
