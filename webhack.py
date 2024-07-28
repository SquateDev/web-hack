import argparse
import requests, json
import sys
from sys import argv
import os


api = "http://ip-api.com/json/"
data = requests.get(api).json();
print("Socket ", data['query'])

