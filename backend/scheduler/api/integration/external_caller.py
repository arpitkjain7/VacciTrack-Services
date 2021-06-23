import os
import requests
import json
from client import config


class APIInterface:
    @staticmethod
    def post(route, data=None):
        # fcm_key = config.get("FCM").get("KEY")
        fcm_key = "AAAAZiDMEfw:APA91bGbgxNujBdVt52r0R_FmhcS9qalGMzWHJSCl-SX_g96Wktu9QHQGdj9Jv4Ok81Ti-96bo0I9GN9V3tnVTwTRmmT11jX-x5BKjfkAj-DD-zx-koQC15-KnyRiRJqaliOfU4r_O6U"
        url = route
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"key={fcm_key}",
        }
        response = requests.post(url, json=data, headers=headers)
        if response.status_code != 200:
            raise Exception(
                f"Call to {route} failed with {response.status_code} and response {response.text}"
            )
        return response.text

    @staticmethod
    def get(route, params=None):
        url = route
        # print(f"url = {url}, params = {params}")
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
        }
        response = requests.get(url, params=params, headers=headers)
        if response.status_code != 200:
            raise Exception(
                f"Call to {route} failed with {response.status_code} and response {response.text}"
            )
        return response.text

    @staticmethod
    def put(route, data=None):
        url = route
        # print(f"url = {url}, data = {data}")
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
        }
        response = requests.put(url, json=data, headers=headers)
        if response.status_code != 200:
            raise Exception(
                f"Call to {route} failed with {response.status_code} and response {response.text}"
            )
        return response.text
