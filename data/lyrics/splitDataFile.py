"""
Used to split the giant lyrics.csv into multiple csv's.

May not be useful after we initially split the file, but just in case we want to tweak or reuse for another dataset...
"""
import csv
import sys
import os
import time

BIGFILE = "lyrics.csv"
NUMFILES = 10 # the number of mini-files to split the big file into
LOGGINGPERIOD = 50000 # number of writes to do between logs

basepath = "" if os.path.isfile(BIGFILE) else "./data/lyrics/"
smallfile_names = ["lyrics_" + str(n) + ".csv" for n in range(NUMFILES)]

if not os.path.isfile(basepath + BIGFILE):
    # dump some common sense info and exit
    print sys.path
    print os.getcwd()
    print "\n\nCouldn't find the file:", basepath + BIGFILE
    sys.exit(1)

start_time = time.time()
with open(basepath + BIGFILE, "r") as f:
    outfiles = [open(basepath + sf_name, "w") for sf_name in smallfile_names]
    csv_writers = [csv.writer(outfile) for outfile in outfiles]
    # skip first line, since it's the header row and we don't need that
    next(f)
    c = 0
    period_start = time.time() # let's track how long each period takes
    for row in csv.reader(f):
        csv_writers[c % NUMFILES].writerow(row)
        if (c + 1) % LOGGINGPERIOD == 0: # periodic logging
            pt = str(time.time() - period_start)
            print "Wrote songs", str(c - LOGGINGPERIOD + 1), "through", str(c), "to split files in", pt, "sec"
            period_start = time.time()
        c += 1
    [outfile.close() for outfile in outfiles]

print "\n\ndonezo; split", basepath + BIGFILE, "into", NUMFILES, "files in", str(time.time() - start_time), "seconds"
