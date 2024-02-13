import requests
from colorama import Fore, init
from pystyle import Write, Colors, Box, Center
import time
import os


Write.Print(Center.XCenter("\n[-] Welcome to IP Lookup."), Colors.blue_to_purple, interval=0.015)
time.sleep(0.9)
Write.Print(("\n[-] Enter the IP to scan: "), Colors.blue_to_purple, interval=0.015)
ip = input()

if len(ip) == 0 or len(ip) > 16 or len(ip) < 7:
    Write.Print("\n[*] Please, enter a valid IP, closing...", Colors.red, interval=0.015)
    time.sleep(5)
    exit()

elif isinstance(ip, str):
    url = f"http://www.ip-api.com/json/{ip}"
    Write.Print(f"\n[*] Connecting to API... ", Colors.blue_to_purple, interval=0.025)
    time.sleep(1)
    response = requests.get(url)
    if response.status_code != 200:
        Write.Print(f"\n[*] Unexcpected Error | Status Code of the request: {response.status_code}", Colors.red, interval=0.015)

    elif response.status_code == 200:
        status_code = response.status_code
        Write.Print(f"\n[*] Succesfully connected to API | Status Code: ", Colors.blue_to_purple, interval=0.015)
        Write.Print(str(status_code), Colors.white, interval=0.015)
        Write.Print(f"\n[*] Scrapping data of: ", Colors.blue_to_purple, interval=0.015)
        Write.Print(ip, Colors.white, interval=0.015)
        time.sleep(2)
        
        data = response.json()
        Write.Print(f"\n\n[*] Data Scrapped | Do you want an extensive (E) or simple (S) report?: ", Colors.blue_to_purple, interval=0.015)
        report_type = input("")
        if report_type.lower() == "e" or report_type.lower() == "extensive":
            Write.Print(f"\n[*] Generating extensive report... ", Colors.blue_to_purple, interval=0.015)
            time.sleep(2)
            os.system("cls")
            time.sleep(2)

            Write.Print(Center.XCenter("\n[-] Data Report of: "), Colors.cyan, interval=0.015)
            print(ip)

            Write.Print((f"\n[-] Country: "), Colors.cyan, interval=0.005)
            Write.Print(f"{data.get('country')} | {data.get('countryCode')}", Colors.white, interval=0.005)

            Write.Print((f"\n[-] Region: "), Colors.cyan, interval=0.005)
            Write.Print(f"{data.get('regionName')} | {data.get('region')}", Colors.white, interval=0.005)

            Write.Print((f"\n[-] City: "), Colors.cyan, interval=0.005)
            Write.Print(f"{data.get('city')}", Colors.white, interval=0.005)

            Write.Print((f"\n[-] Postal Code: "), Colors.cyan, interval=0.005)
            Write.Print(f"{data.get('zip')}", Colors.white, interval=0.005)

            Write.Print((f"\n[-] Timezone: "), Colors.cyan, interval=0.005)
            Write.Print(f"{data.get('timezone')}", Colors.white, interval=0.005)

            Write.Print((f"\n[-] ISP: "), Colors.cyan, interval=0.005)
            Write.Print(f"{data.get('isp')}", Colors.white, interval=0.005)

            Write.Print((f"\n[-] ORG: "), Colors.cyan, interval=0.005)
            Write.Print(f"{data.get('org')}", Colors.white, interval=0.005)

            Write.Print((f"\n[-] AS: "), Colors.cyan, interval=0.005)
            Write.Print(f"{data.get('as')}", Colors.white, interval=0.005)

            time.sleep(1000)

        elif report_type.lower() == "s" or report_type.lower() == "simple":
            Write.Print(f"\n[*] Generating simply report... ", Colors.blue_to_purple, interval=0.015)
            time.sleep(2)
            os.system("cls")
            time.sleep(2)

            Write.Print((f"\n[-] Country: "), Colors.cyan, interval=0.005)
            Write.Print(f"{data.get('country')} | {data.get('countryCode')}", Colors.white, interval=0.005)

            Write.Print((f"\n[-] City: "), Colors.cyan, interval=0.005)
            Write.Print(f"{data.get('city')}", Colors.white, interval=0.005)

            Write.Print((f"\n[-] Postal Code: "), Colors.cyan, interval=0.005)
            Write.Print(f"{data.get('zip')}", Colors.white, interval=0.005)

            time.sleep(1000)

        else:
            Write.Print("\n[*] Please, enter a valid report type, closing...", Colors.red, interval=0.015)
            time.sleep(5)
            exit()