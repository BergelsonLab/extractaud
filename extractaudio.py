import csv
import os
import sys
import subprocess as sp


def extract_audio(out_dir, file_in):
    command = [
        'ffmpeg',
        '-i',
        entry[0],
        '-vn',
        '-acodec',
        'pcm_s16le',
        '-ar',
        '44100',
        '-ac',
        '2',
        '{}.wav'.format(os.path.join(out_dir, file_in[:-4]))
    ]

    sp.call(command)


def walk_tree(start_dir, out_dir):
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith(".mp4"):
                extract_audio(out_dir, os.path.join(root, file))


def extract_times(timestamps, out_dir):
    for entry in timestamps:
        filename = os.path.basename(entry[0][:-4]).replace("video", "")
        command = [
            'ffmpeg',
            '-ss',
            entry[1],
            '-i',
            entry[0],
            '-t',
            '{}'.format(int(entry[2])-int(entry[1])),
            '-vn',
            '-acodec',
            'pcm_s16le',
            '-ar',
            '44100',
            '-ac',
            '2',
            '{}_{}-{}.wav'.format(os.path.join(out_dir, filename),
                                  entry[1],
                                  entry[2])
        ]

        sp.call(command)


def read_timestamps(input):
    timestamps = []
    with open(input, "rU") as filein:
        reader = csv.reader(filein)
        for row in reader:
            timestamps.append(row)
    return timestamps


if __name__ == "__main__":

    first_arg = sys.argv[1]
    out_dir = sys.argv[2]

    if first_arg.endswith(".csv"):
        timestamps = read_timestamps(first_arg)
        extract_times(timestamps, out_dir)
    else:
        walk_tree(first_arg, out_dir)
