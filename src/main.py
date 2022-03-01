#!/usr/bin/python

import os
import pathlib
import sys
import argparse

from modules import VideoSplitter as vs


def build_argparser():
  parser = argparse.ArgumentParser(description='A simple python CLI program to split a video into segments based on user designated input. '\
                                              'OpenCV is used to process the original video file and write the individual, segmented '\
                                              'video files as .mp4 into a specified directory. Each video will be at most the specified '\
                                              'length in second; if the desired length of segments is not evenly divisable by the specified length, '\
                                              'the final video segment will be the remainder.')
  parser.add_argument('-s', '--source_path', type=str, required=True, help='path to the source file to be split')
  parser.add_argument('-d', '--segment_dest', type=pathlib.Path, required=True, help='dir and destination for the split segments')
  parser.add_argument('-l', '--segment_length', type=int, required=True, help='length of segments in seconds')
  
  return parser


if __name__ == '__main__':
  
  parser = build_argparser()
  args = parser.parse_args()
  if not (args.source_path and args.segment_dest and args.segment_length):
    print(parser.print_help(sys.stderr))
    sys.exit(1)
  else:  
    source_path = args.source_path
    segment_dest = args.segment_dest
    segment_length = args.segment_length
    
    print(f'Loading video: {source_path}')
    print(f'Segments Destination: {segment_dest}')
    print(f'Segment Length: {segment_length}')
    
    if not os.path.exists(segment_dest):
      print(f'Specified destination does not exist. Creating directory: {segment_dest}')
      os.makedirs(segment_dest)

    vs = vs.VideoSplitter(source_path=source_path,
                                      segment_dest=segment_dest,
                                      segment_length=segment_length)
    
    vs.split_video()
    sys.exit(0)