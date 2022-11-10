# OsmCleaner

This project is a utility for bulk data quality analysis of
OpenStreetMap data. It's primary purpose it to find bad data, and
produce output files so problems can be fixed with JOSM.

As OpenStreetMap data files are often large, this program takes a
multipolygon boundary file to limit the size of the data extract. If
you want to chop a Tasking Manager project up into little tiles, it'll
be faster to extract the TM project boundary first, and then the use
that as the input file for the many small tasks.


# Checks

When implemented, this program will check for bad tag values,
building geometry, and duplicate buildings.

