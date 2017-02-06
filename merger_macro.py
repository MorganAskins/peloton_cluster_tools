#!/usr/bin/env python

import os
import argparse
from subprocess import call

'''
Create a rat macro which merges a list of root files with rat
'''

# Too many files crashes rat
file_limit = 100

def inroots(flist):
    textstring = []
    for fname in flist:
        textstring.append('/rat/inroot/load %s' % fname)
    return '\n'.join(textstring)

def body(outfile):
  textstring = """
/run/initialize
/rat/proc count
/rat/procset update 10
/rat/proclast outroot
/rat/procset file \"%s\"
/rat/inroot/read
exit """ % (outfile)

  return textstring

def main():
  args = get_args()
  blocks = 1 + int(len(args.files)/file_limit)
  base_root_name = (args.outfile.replace('.root', ''))
  base_mac_name = (args.macro.replace('.mac', ''))
  for blk in range(blocks):
      subfiles = args.files[(blk*file_limit):((blk+1)*file_limit)]
      header = inroots(subfiles)
      outfile = '%s_%i.root' % (base_root_name, blk)
      footer = body(outfile)
      macro = '%s_%i.mac' % (base_mac_name, blk)
      with open(macro, 'w') as mac:
          mac.write(header)
          mac.write(footer)

def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('outfile', type=str)
  parser.add_argument('-m', '--macro', type=str, default='merger.mac')
  parser.add_argument('-f', '--files', nargs='+', type=str)
  return parser.parse_args()

if __name__ == '__main__':
  main()
