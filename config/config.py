import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", "")

DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "90000000")
)

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "200")
)

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "˹● 𝑻𝑶𝑴 ✘ 𝑱𝑬𝑹𝑹𝒀 𝑴𝑼𝑺𝑰𝑪 ●˼™")

OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5555422614").split())
)

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/dattuxd/BK-OP-TOM",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/Our_Groupps")
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/MUSICAL_BEATSZ")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "6"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://telegra.ph/file/f338b00f339561eb475e1.mp4")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "8"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "10")
)

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "1048579999999600")
)

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741829999999994")
)
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "anonxlogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = [
    "https://graph.org/file/63984c9d93a3d1696a173.jpg"
    "https://telegra.ph/file/c7b551119ea15dc365f68.jpg",
    "https://telegra.ph/file/1d19bdc70cb7ef3d60001.jpg",
    "https://telegra.ph/file/cb746616b6189e00fec71.jpg",
    "https://telegra.ph/file/71f57ec08d362b2247c6b.jpg",
    "https://telegra.ph/file/aef32840b7c2943031ad6.jpg",
    "https://telegra.ph/file/005f3268e52de060eab78.jpg",
    "https://telegra.ph/file/c04036447f2936ee4dd75.jpg",
    "https://telegra.ph/file/5cf94672c06083e36773f.jpg",
    "https://telegra.ph/file/952bac570b471a4243c8d.jpg",
    "https://telegra.ph/file/661da902ca073202ad4ba.jpg",
    "https://telegra.ph/file/89b49320d979989548003.jpg",
    "https://telegra.ph/file/01a5eab9744506eff3f83.jpg",
    "https://telegra.ph/file/eb38913e41771d1a16847.jpg",
    "https://telegra.ph/file/26f34e070431a858d31f5.jpg",
    "https://telegra.ph/file/e0c01f79896a32022c6ca.jpg",
    "https://telegra.ph/file/d424fcf4a72ec8e1a28c7.jpg",
    "https://telegra.ph/file/922e7ce9c5e0bafafeb34.jpg",
    "https://telegra.ph/file/f82d044b2f3133cec48c2.jpg",
    "https://telegra.ph/file/0f424d0824900939bb32a.jpg",
    "https://telegra.ph/file/0e84310ec975e8e6ebca9.jpg",
    "https://telegra.ph/file/1646ddc99a7c77f51b3a0.jpg",
    "https://telegra.ph/file/3c5ac8d87b622260445be.jpg",
    "https://telegra.ph/file/dfa43563bd68849a46a39.jpg",
    "https://telegra.ph/file/4506a375b415971355ff2.jpg",
    "https://telegra.ph/file/0d0cdfda3b9dac9730476.jpg",
    "https://telegra.ph/file/4d2c9229c567f9416143f.jpg",
    "https://telegra.ph/file/77ba544ccfb6bf8ba7b03.jpg",
    "https://telegra.ph/file/0387d64a44d76e0d53deb.jpg",
    "https://telegra.ph/file/9e346de01cb863b30367f.jpg",
    "https://telegra.ph/file/26a0d446102c63a1bbcca.jpg",
]

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://graph.org/file/5b5803b02a24b043fc6d0.jpg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "assets/Playlist.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "assets/Global.jpeg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "assets/Stats.jpeg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "assets/Audio.jpeg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "assets/Video.jpeg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "assets/Stream.jpeg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "assets/SpotifyPlaylist.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()
