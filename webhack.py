import argparse
import requests, json
import sys
from sys import argv
import os


api = "https://www.ufamama.ru/Auth/ActivationByPhoneForm?phone=%2B"
phone_num = int(input("Введите Номер >> "));
data = requests.get(api+phone_num).json();
print("Socket ", data['query'])

