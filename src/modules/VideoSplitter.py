#!/usr/bin/env python

"""
Video Splitter Class
"""

import os
import math

import cv2

class VideoSplitter:
  
  def __init__(self, source_path, segment_dest, segment_length):
    """
    param:
      source_path -> str: path to source file to be split
      segment_dest -> str: dir and destination for split segments
      segment_length -> int: length of segments in seconds
    """
    self.source_path = source_path
    self.segment_dest = segment_dest
    self.segment_length = int(segment_length)
    self.fps = 0
    self.frame_count = 0
    self.frame_size = (0, 0)
    
  def analyse_video(self):
    """
    Set or fetch analytics for video to use in segmentation.
    """
    
    vid_cap = cv2.VideoCapture(self.source_path)
    if not vid_cap.isOpened():
      print(f'Error opening video file.')
    else:
      print(f'Retrieving Video Analytics:')
      
      self.fps = round(vid_cap.get(cv2.CAP_PROP_FPS))
      print(f'FPS: {self.fps}')
      
      self.frame_count = int(vid_cap.get(cv2.CAP_PROP_FRAME_COUNT))
      print(f'Frame Count: {self.frame_count}')
      
      self.frame_size = (int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
      print(f'Frame Size (Width, Height): {self.frame_size}')
      
      vid_cap.release()
    
  def split_video(self):
    """
    Calculate segment dimension based on video analytics and user imput. Create segments of video. 
    """
    if self.fps == 0 or self.frame_count == 0 or self.frame_size == (0, 0):
      self.analyse_video()
    
    frames_per_segment = self.fps * self.segment_length
    print(f'Frames per Segment: {frames_per_segment}')
    
    segment_count = math.ceil(self.frame_count / frames_per_segment)
    print(f'Number of segments to create: {segment_count}')
    
    segments = [(i * frames_per_segment, (i + 1) * frames_per_segment if (i + 1) * frames_per_segment <= self.frame_count else self.frame_count) 
                for i in range(segment_count)]
    [print(f'Segment {int(start / frames_per_segment)} => {start}-{end}') for start, end in segments]
    
    fourcc = self.build_segment_encoding()
    writers = [
      cv2.VideoWriter(f'{self.segment_dest}/{segment[0]}thFrame.mp4', fourcc, self.fps, self.frame_size)
      for segment in segments
    ]
    
    self.write_segments(frames_per_segment, writers)

  def build_segment_encoding(self):
      """
      Set up indidual VideoWriters for each segment to be created.
      Future Improvement: add param to accept command line arg to allow user to specify segment encoding type
      """
      fourcc = cv2.VideoWriter_fourcc(*'mp4v')
      return fourcc

  def write_segments(self, frames_per_segment, writers):
    """
    param:
      frames_per_segment -> int: number of frames to be included in each segment pre-calculated in parent function.
      writers -> List: list of writers created for each segment in parent function.
      
    Read video into VideoCapture object. Iterate through frames, use floor of current frame divided by frames per segment to
    calculate which VideoWriter to use.
    
    Ensure each VideoWriter and the VideoCapture is closed after all the frames have been processed.
    """
  
    # create VideoCapture object for video
    vid_cap = cv2.VideoCapture(self.source_path)
    ret, frame = vid_cap.read()
    f = 0
    while ret:
      writers[math.floor(f/frames_per_segment)].write(frame)
      f += 1
      ret, frame = vid_cap.read()
      
    print('VideoWriters Closed')
    for writer in writers:
      writer.release()
      
    vid_cap.release()
    print('VideoCapture Closed')
    