#!/usr/bin/env python

import os
import argparse
from subprocess import call

'''
This script is meant as a general purpose rat macro creator / runner, in order
to run the same macro many times, over many files in batch
'''

def body(infile):
  outfile = infile.split('.root')[0] + '_dc.root'
  textstring = """
/rat/inroot/load %s
/run/initialize
/rat/proc outroot
/rat/procset file \"%s\"
/rat/proc count
/rat/procset update 10
/rat/proclast datacleaning
/rat/procset mask "default"
/rat/inroot/read\n
exit """ % (infile, outfile)

  return textstring

def main():
  args = get_args()
  for fname in args.files:
    macname = fname.split('.root')[0]+'.mac'
    with open(macname, 'w') as mac:
      mac.write(body(fname))
    call(["rat", macname])
    os.remove(macname)


def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-f', '--files', nargs='+', type=str)
  return parser.parse_args()

if __name__ == '__main__':
  main()
