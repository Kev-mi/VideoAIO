import tkinter
import requests
import time

HEADERS = {'client-id': 'kimne78kx3ncx6brgo4mv6wki5h1ko' }
GQL_QUERY = """ query($login: String) { user(login: $login) { stream { id } } } """


def isLive(username):
    QUERY = {'query': GQL_QUERY, 'variables': {'login': username}}
    response = requests.post('https://gql.twitch.tv/gql', json=QUERY, headers=HEADERS)
    dict_response = response.json()
    return True if dict_response['data']['user']['stream'] is not None else False


if __name__ == '__main__':
    while True:
        time.sleep(5)
        with open("streamers.txt", 'r') as f:
            streamer_list = [line.strip() for line in f]
        for streamer in streamer_list:
            IS_LIVE = isLive(streamer)
            if IS_LIVE:
                print(f'User {streamer} live: {IS_LIVE}')



