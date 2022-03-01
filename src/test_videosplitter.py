import pytest
import cv2
from modules.VideoSplitter import VideoSplitter


VIDEO_SPLITTER = VideoSplitter(source_path='data/airshow.mp4',
                               segment_dest='data/segments',
                               segment_length='60')


def test_VideoSplitter1_analysevideo1():
  VIDEO_SPLITTER.analyse_video()
  assert VIDEO_SPLITTER.fps == 30, f'FPS Test Failed: {VIDEO_SPLITTER.fps}'
  assert VIDEO_SPLITTER.frame_count == 9287, f'Frame Count Test Failed: {VIDEO_SPLITTER.frame_count}'
  assert VIDEO_SPLITTER.frame_size == (1280, 720), f'Frame Size Test Failed: {VIDEO_SPLITTER.frame_size}'
  
def test_VideoSplitter1_buildsegmentencoding1():
  fourcc = VIDEO_SPLITTER.build_segment_encoding()
  assert fourcc == cv2.VideoWriter_fourcc(*'mp4v'), f'Encoding Builder Failed Non mp4 encoding type: {fourcc}'