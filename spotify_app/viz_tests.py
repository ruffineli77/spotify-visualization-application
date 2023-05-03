
import os
import json
# import pandas as pd
from pathlib import Path


# Temporary path to the spotify data json files.
temp_data_folder = ("temporary_data/eli_data2")


# This function is for unzipping
def unzip_files():
    pass


# this function looks through unzipped spotify data folder, finds all
# StreamingData files, and returns a tuple of filepaths.
def collect_streamingdata():
    streamingHistory_json_files = []

    for file in os.listdir(temp_data_folder):
        if "StreamingHistory" in file:
            desired_filepath = os.path.join(temp_data_folder, file)
            # print("StreamingHistory file found!")
            # print(desired_file)
            streamingHistory_json_files.append(desired_filepath)

        else:
            # print(f"{file} does not contain streaming history data.")
            pass

    return tuple(streamingHistory_json_files)


# decodes the json files so the data can be used in a dataframe.
def decode_json_files(encoded_jsons):
    decoded_files = []

    for json_file in encoded_jsons:
        # print(json_file)
        # print(type(json_file))

        with open(json_file, encoding="utf-8") as opened_json:
            # print(opened_json)
            data = json.load(opened_json)
            # print(type(data))
            # print(data)
            # decoded_files.append(data)
            # decoded_files.extend adds the items in each list to the main list
            # rather than adding each list to the main list with .append()
            decoded_files.extend(data)

    # print(len(decoded_files)) # total number of songs played
    return tuple(decoded_files)


# this function extracts one column of values from the decoded json files.
def extract_trackNames(data_files_dict: dict, desired_value: str):
    extracted_data = []

    try:
        for dict in data_files_dict:
            extracted_data.append(dict[desired_value])

    except KeyError as ke:
        print(f"{ke}\n{desired_value} is not found in the json file.")

    # print(tuple(extracted_data))
    return tuple(extracted_data)


def create_dataframe(data_files):
    dataframe = {}

    # I only need song names so the second parameter for extract_trackNames()
    # will be "trackName". To get different data I just have to call the
    # function with a different second parameter.
    extracted_trackNames = extract_trackNames(data_files, "trackName")

    for song in extracted_trackNames:
        dataframe[song] = dataframe.get(song, 0) + 1

    # print(dataframe)
    return dataframe  # a dict. Keys are song names values are number of plays.


# played_songs = create_dataframe(decode_json_files(collect_streamingdata()))

# for song in played_songs.items():
#     print(song)
