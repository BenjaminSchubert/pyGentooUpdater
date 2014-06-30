#!/usr/bin/python3
#! -*- Coding: UTF-8 -*-

__author__ = 'tellendil'

import subprocess
from gi.repository import Notify

def check_updates():
    pr = subprocess.Popen(["emerge", "-uDNpq", "world"], stdout=subprocess.PIPE)
    output = pr.stdout.read()
    if not pr.wait():
        return output.decode("UTF-8").split("\n")
    else:
        return ""


def parse_packages(pa):
    packages  = [x[x.find("]") + 1:].split("/")[1].split(" ")[0].replace("-", " ") for x in pa if "]" in x]
    return packages


def display(packages):
    message = "\n".join(packages)
    title="New updates"
    Notify.init(title)
    send = Notify.Notification.new(title, message, "software-update-available")
    send.set_urgency(1)
    send.set_timeout(60000)
    send.show()

def main():
    packages_to_update = check_updates()
    if packages_to_update != "":
        packages = parse_packages(packages_to_update)
    display(packages)
    return 0


if __name__ == "__main__":
    main()