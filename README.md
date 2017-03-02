# extractaud


A script for pulling out the audio stream from video files.

## usage

#### all the audio, all the files
To pull out all the audio from all the files in a directory:

```
$: python  extractaudio.py  input_directory  output_directory
```

#### specific timestamps, specified files
If you only want to pull out specified timestamps within a video file,
pass in a csv file with filenames/onset_ms/offset_ms timestamps:

```
$ python extract_audio.py  timestamps.csv  output_directory
```

The csv file should be in this form:

|filepath             |onset_ms|offset_ms|
|---------------------|--------|---------|
|input/01_06_video.mp4|13292   | 18983|
|input/09_08_video.mp4|25292   | 41983|
|input/15_12_video.mp4|71222   | 103951|

You will end up with .wav files in the output directory, named after the
original video it came from, with the timestamps included in the filename.



## dependencies

This script depends on FFmpeg, which you can get [here](https://www.ffmpeg.org/). Make sure the binary is somewhere in your $PATH.
