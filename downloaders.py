import requests


def download_1(url):
    shortcode = url.removeprefix('https://')
    shortcode = shortcode.removeprefix('www.')
    shortcode = shortcode.removeprefix('instagram.com/reel/')
    shortcode = shortcode.split('/')[0]

    cookie = '''i18n_redirected=ru; _ym_uid=1697031040374332668; _ym_d=1697031495; _ga=GA1.1.1484787183.1697031495; _ym_isad=1; nuxt-session-id=s%3AuQL7w6GaR8BOjMtAh1JkFLw5jNtiH7y5.wegmNEpWWUVIfvLwNAKIlXP2XkCZy7aeKofo5iEICrY; conv_session={"start":1697031039,"shown":[],"startUrl":"https://instagramdownloads.com/ru/reels","referrer":"https://yandex.ru/clck/jsredir?from=yandex.ru%3Bsearch%2F%3Bweb%3B%3B&text=&etext=2202.1QZZBnJ4x-BlMD_iSrfOx4QqZX9XSF-WH3p48Mn1JWTUYkZOY9Iz7pjAyESP9ElcxOzJmbRHf4R7sx5SvAwoyXN5bmp1anRtYmZ5a3NhcmM.25b6a3d3f2e736db2c2c6dc49f29813452882792&uuid=&state=RsWHKQP_fPE,&&cst=AxbTlK7nwx6hOtlFEVBANt_aR1gsovU_ADRunyCNpBJmgpje2g3gpT5D3kgOA3lX8BOG3thm2e01OpNxr8DhEboaTMvNO9Fgc2W9krV1yXXCv3x0bwomeXw3cQRVK4nIPIT9iUxy6PYmAEExSAZTD5W2eLalbSMKHsLFy00UcAZQkdHkfaGJkSKCvM6In9mzRRYWDBt7lLYacXsG1WzzKtBAXjms6vC5dHRQ2-LUHtaeyy1lQhp0uWXmVZ2DX42lqDGLUuxn7gKXR8sslSoxOz_HSM6P6Ygx9o2UJcW2vh7lOd6iayIZNEMFkDjt_swhRdnwOEIpmwQxMlXA5cBRfzHXYfOf-kvFy3D2MRC1j2g1dKQRY_j2Xa964VyxgLibLsd13zn_drmKxW_OAeSP3zP12UnCEOlledE1vGoOVOCzcm0MGFUU61x0FcFT6ZYPzVy10LSvZFskmE3uxrfVRY3HoKh3tJBBydRST31kqReUmR4DM4z0cDB78zMYBVP1mO2y2P0yyqwT_iWRuskv20O6lzD_dmbr6Vwyo-HfOP8xGmMerJsNoFH3PK7SbPBxV70bCt9y96OsGLw7Gjop4S9Qtae0hSEeVK6UxsERmhbyPruLiP16ZalgROvne1DZGSDZg3-GJWd42D795pBFfRNoXcyXaNYyRV2Mo6Rv2O2qLWNsWso8h-pdiXWeW8u0EqN0j-iAiqJW3g6i9jQYM73QqRBzSrP-ZVrXjymgFbppu9tp8ySZMSbWFSZyct-reuh4TfgmpxmcdbNRxN6FaALxhSDdL6oGV0Gtaf1yKmqEkSPjwIhIP3qx4JY-dFy1INeGpK5y0cL0qlexyat3V5raoKLd6P1EIhTWpIU0QWOa0mSJyjVamDYpu87G3nTSYz89huB_mqFKf-iYYX1D-lkJ0gJ8wfsUcB6wLQr2uaNtgSXpS77b5IDjaUABpluilrFDMwSBZgOHY2mdMGrYu4Z8eE5wFF8gZgd1dZ_F--ueR71JfKkfd1J-aMitRmE_1i98r2NL6In7NAUNquH8K61GynXkSK4P0mLZhmltEb6QhOwn2pgVzaqtWdGF_S9uA-qULtPdklVmQU5wd0xM1B5KUVdJZ7kGMKma6cBBn8RI4DvDV4T-Gb_EbTxmfskxg6MzIIeTWOZA4D_MjcUvjxjP0SDDytXF7oQiBzczckgP_tqXnFIhrQ,,&data=VzFITjJTUER3MkI4MEY5djBaZUVGMS0yeVlOWXJfcUd6b1Q4NFJ3RU5KQ3hXSmJIQTdXZ0tBZjk0eFl4WlVxMG5HLU55OTFneWhvOXU5bUJyc1JVZFVrRDlXLUZacS1VQUVyLWYyb2xlNXdRQjdxR0RBUUZvUXA4TGZqS2FJVzQ,&sign=a29010f5b4a99f4dd07de36278ff5957&keyno=WEB_0&b64e=2&ref=mag21uLwzH-iqa6a9U6fw6sBTXI61vrcLrAj4_J9mG4gqc4FvTfx3R4bK-4G_3WoCtJdEdQ5v3xIWssdU_HsRpURtvsKnWTPeGfBFMz9P4xqD6R86skbLEc-vijeTwzJI-ur6dHHi0oMlSup2snGAYS5wBBkGBByALwgKRK27uWYsFQaL-9sXYo76NZWd9KS7ZLtvsNdtPwQl7JmpnowwM0GhYCSyd7sdOava5zboNY,&l10n=ru&cts=1697031037587%40%40events%3D%5B%7B%22event%22%3A%22click%22%2C%22id%22%3A%222_6ttew06-00%22%2C%22cts%22%3A1697031037587%2C%22fast%22%3A%7B%22organic%22%3A1%7D%2C%22service%22%3A%22web%22%2C%22event-id%22%3A%22lnlsgp03he%22%2C%22data%22%3A%7B%22pageX%22%3A397%2C%22pageY%22%3A812%7D%7D%5D&mc=3.121928094887362&hdtime=3058.1","expires":1697033295,"isNew":false,"pageViews":3,"ab":[200075]}; _ga_2SJ1KKW4EV=\''''

    resp = requests.post(
        'https://instagramdownloads.com/api/post',
        json={
            'shortcode': shortcode
        },
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.717 Yowser/2.5 Safari/537.36',
            'Cookie': cookie,
            'Content-Type': 'application/json',
            'X-Sign': '1ff2575e4b2032bffeaf851084aeea0d'
        },
    )
    video_url = resp.json()['video_versions'][1]['url']

    resp = requests.get(
        'https://instagramdownloads.com/api/proxy',
        params={
            'url': video_url
        }
    )

    with open('video.mp4', 'wb') as f:
        f.write(
            resp.content
        )


def download_2(url):
    resp = requests.post(
        'https://bestsave.app/get-medias',
        json={"url": url,
              "needToLoadStories": False, "needToLoadAvatar": False},
        headers={
            'Cookie': '_ym_uid=1697035924523262159; _ym_d=1697035924; _ga=GA1.1.1667874667.1697035924; _ym_isad=1; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6IjFSWUJQV3dsZjFTbmdyQlF0bTM5MXc9PSIsInZhbHVlIjoiMFN3UDh3dHFXTnUvVGlMaHZoeTBoQmdnWkdTQXQ5d3RKWi9Uek1paDNNbUN2T1BTVXdNU3AyYnlRRXV5Y1d6ODBWZnZiY2VkckdQb00zaU9DMlBXdENZN3dPMG9nUVgvU2sramNkNmZNOEdlOTlCa2QzcDJaekEwb0ZxTkxGeXgiLCJtYWMiOiI4OGNkMmY0ODYyNWJkZDBiNDM2ODkzYjkzZjA2YWNhNGE0OTZiNTFhNGVmMDE3Y2E3YmU4YjkxZmFmMjY1MGM4IiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IlpIRE92andCbVpXTkJHRFBNU3lXZnc9PSIsInZhbHVlIjoibnFRYXB0azJmZ1ZlVmtkREFpV1RwK01zMDNuWDVlS1N2endJVmJjQjhtRTZ4TjZBekoyWi9HY1FDN2FhVWJnbExMcXltYmkwS1hsRDJOYlJrNkdTUEVLcGFaUTl5WkdaTFRFU3gzaGMyRzZMZXFtcU83aXhxNTJYV0lVMHhmWVEiLCJtYWMiOiJmYTk1YmE4MGZkOGE5ODJhZjNjM2JhMGJjOGRjYjE5MjkzNzEwNDAwOGVjNWVlMzZhZTNmYjRjM2Q4M2QzYmM1IiwidGFnIjoiIn0%3D; _ga_VM68HBTMJT=GS1.1.1697046362.2.1.1697046398.0.0.0',
            'X-Xsrf-Token': 'eyJpdiI6IjFSWUJQV3dsZjFTbmdyQlF0bTM5MXc9PSIsInZhbHVlIjoiMFN3UDh3dHFXTnUvVGlMaHZoeTBoQmdnWkdTQXQ5d3RKWi9Uek1paDNNbUN2T1BTVXdNU3AyYnlRRXV5Y1d6ODBWZnZiY2VkckdQb00zaU9DMlBXdENZN3dPMG9nUVgvU2sramNkNmZNOEdlOTlCa2QzcDJaekEwb0ZxTkxGeXgiLCJtYWMiOiI4OGNkMmY0ODYyNWJkZDBiNDM2ODkzYjkzZjA2YWNhNGE0OTZiNTFhNGVmMDE3Y2E3YmU4YjkxZmFmMjY1MGM4IiwidGFnIjoiIn0='
        }
    )

    video_chast = resp.json()[0]['url']
    video_url = f'https://video-cors.live/{video_chast}'
    resp = requests.get(video_url)
    with open('video.mp4', 'wb') as f:
        f.write(
            resp.content
        )


download_2('https://www.instagram.com/reel/Cxhi7mboOES')
