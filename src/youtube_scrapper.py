"""
    Creator: Yuri Mirchev
    Source: https://github.com/rg3/youtube-dl#embedding-youtube-dl
    Purpose: Download video and print its info
"""

import youtube_dl


def _get_youtube_video_info(url):
    ydl_opts = {
        'quiet': True,
        'skip_download': False,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(url)


def get_youtube_video_data(url):
    info = _get_youtube_video_info(url)
    print('Url:', url)
    print('Title:', info['title'])
    print('Upload date:', info['upload_date'])
    print('Average Rating:', info['average_rating'])


if __name__ == '__main__':
    url = 'http://www.youtube.com/watch?v=BaW_jenozKc'
    get_youtube_video_data(url)
