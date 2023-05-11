
from pathlib import Path


# iterate over a dir and all subdirs and return all files in a dict.
# key names are dir names, values are lists of files.
# add optional arguments to add certain file extensions to each list.
def one_folder(one_dir:str):
  aa = Path(one_dir)
  # print(aa.parts[-1])
  # print(aa.parents[0])

  all_videos = {aa.parts[-1]:[]}
  for video in aa.iterdir():
    # print(video)
    if video.suffix in [".mp4", "mov", "mp3", "wav", "jpg", "png"]:
      all_videos[aa.parts[-1]].append(video.stem)

  return all_videos


# iterate over a dir and all subdirs and return all files in a dict.
# key names are dir names, values are lists of files.
# add optional arguments to add certain file extensions to each list
def many_folders(many_dirs:str):
  all_videos = {}
  aa = Path(many_dirs).iterdir()

  for subdir_path in aa:
    video_parent_dir = str(subdir_path.parts[-1])
    # print(video_parent_dir)
    all_videos[video_parent_dir] = []
    # print(subdir_path)
    for video in subdir_path.iterdir():
      # print(video.stem)
      if video.suffix in [".mp4", "mov", "mp3", "wav", "jpg", "png"]:
        all_videos[video_parent_dir].append(video.stem)


  return all_videos
