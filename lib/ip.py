#!/usr/bin/env python3

import json
import requests
import socket


class Ip:
    def __init__(self):
        self.session = requests.session()

    def get_public_ip_info(self):
        url = "https://ipv4.geojs.io/v1/ip/geo.json"
        req = self.session.get(url)

        if not req or req.status_code != 200:
            return

        return req.json()

    def get_local_ip(self):
        return (([
            ip for ip in socket.gethostbyname_ex(
                socket.gethostname())[2]
            if not ip.startswith("127.")
        ]
            or [[
                (s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close())
                for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
            ][0][1]]) + ["no IP found"])[0]
