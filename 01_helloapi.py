from aidevs_key import key
import requests


def get_token():
    url = "https://zadania.aidevs.pl/token/helloapi"
    data = {"apikey": key}
    response = requests.post(url, json=data)
    return response.json()['token']


def get_task():
    url = f"https://zadania.aidevs.pl/task/{get_token()}"
    response = requests.get(url)
    task = response.json()
    return task['cookie']


def send_answer():
    url = f"https://zadania.aidevs.pl/answer/{get_task()}"
    answer = {"anser": get_task()}
    response = requests.post(url, json=answer)
    return response


get_token()
get_task()
send_answer()
