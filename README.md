# Video Splitter

A simple python CLI program to split a video into segments based on user designated input. OpenCV is used to process the original video file and write the individual, segmented video files as `.mp4` into a specified directory. Each video will be at most the specified length in second; if the desired length of segments is not evenly divisable by the specified length, the final video segment will be the remainder. 

## Requirements
- Python 3.9
- OpenCV
- FFMPEG
- Pip

## Installation

1. Download project into desired directory.
2. Navigate to parent directory and run the following command to install dependencies.<br>
optional: Create virtual environment `python -m venv .env; source .env/bin/activate`<br>
`pip install -r requirements.txt`
3. To split a video provide the following arguments in the CLI specifying the source video, target directory for created segments, and the max length of each segment in seconds.

## Params
- `-s, --source_path`: path to source file to be split
- `-d, --segment_dest`: dir and destination for split segments
- `-l, --segment_length`: length of segments in seconds

### Possible Future Improvements
- add additional command line arg and update `build_segment_encoding` to allow user to specify saved segment encoding file type


