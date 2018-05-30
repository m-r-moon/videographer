#!/usr/bin/python

import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('totalLength', help='Specify total length (s, m, h)')
  parser.add_argument('frequency', help='Specify photo frequency (s, m, h)')
  parser.add_argument('project', help='Specify project name')
  args = parser.parse_args()

  if args.totalLength and args.frequency and args.project:
    print 'start taking photos...'
    # start taking photos
  else:
    print parser.usage
    exit(0)

if __name__ == '__main__':
  main()
