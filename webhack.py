import argparse
import requests, json
import sys
from sys import argv
import os
from colorama import Fore, Style


api = "https://www.ufamama.ru/Auth/ActivationByPhoneForm?phone=%2B79016929013"
data = requests.get(api);
print(Fore.RED+"Done Sms"+Fore.WHITE+"...");
