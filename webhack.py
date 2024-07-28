import argparse
import requests, json
import sys
from sys import argv
import os


api = "https://www.ufamama.ru/Auth/ActivationByPhoneForm?phone=%2B79016929013"
data = requests.get(api).json();
print("Socket ", data['query'])

