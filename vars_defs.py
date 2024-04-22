import json
import os

APPNAME = "PY_YT_DL"
DOWNLOAD_FOLDER = "PY_YT_DL_DOWNLOADS"
SETTINGS_FILE = "settings.json"


JSON_DATA = [
    {"id": 1, "name": "video_resolution", "content": ""},
    {"id": 2, "name": "video_filetype", "content": ""},
    {"id": 3, "name": "video_bitrate", "content": ""},
    {"id": 4, "name": "audio_filetype", "content": ""},
    {"id": 5, "name": "audio_bitrate", "content": ""},
    {"id": 6, "name": "_use_oauth", "content": ""},
    {"id": 7, "name": "allow_oauth_cache", "content": ""},
    {"id": 8, "name": "win_sound", "content": ""},
    {"id": 9, "name": "theme", "content": ""}
]


def get_json_data():
    if not os.path.exists(SETTINGS_FILE):
        raise FileNotFoundError(f"Settings file '{SETTINGS_FILE}' not found.")
    with open(SETTINGS_FILE, "r") as file:
        json_data = json.load(file)
    return json_data
