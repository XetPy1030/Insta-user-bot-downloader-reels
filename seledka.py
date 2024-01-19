import os

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


def get_video_url(url):
    options = webdriver.FirefoxOptions()
    options.headless = True
    options.add_argument('headless')
    print(os.listdir('.'))
    browser = webdriver.Firefox(
        service=Service(
            executable_path='./geckodriver'
        ),
        options=options
    )
    try:
        browser.get(url)
        browser.implicitly_wait(5)
        elem = browser.find_element(By.TAG_NAME, 'video')
        video_url = elem.get_attribute('src')
        return video_url
    finally:
        browser.quit()


def download_video(video_url):
    resp = requests.get(video_url, stream=True)
    with open('video.mp4', 'wb') as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)


if __name__ == '__main__':
    vid_url = get_video_url('https://www.instagram.com/reel/C2KVKh8MKYg/')
    download_video(vid_url)
