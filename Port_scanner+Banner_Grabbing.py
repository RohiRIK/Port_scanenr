import socket
import subprocess
import sys
from datetime import datetime
from progress.spinner import MoonSpinner
from colorama import Fore, init
import random, time
import argparse
import pyfiglet


####################### Loding fun #######################

def loding():
    with MoonSpinner('Processing…') as bar:
        for i in range(100):
            time.sleep(0.02)
            bar.next()


def loding_less():
    with MoonSpinner('Processing…') as bar:
        for i in range(20):
            time.sleep(0.02)
            bar.next()


###################### One PORT SCANER FUN - TCP #######################

def open_port_scaner(ip, port):
    host_ip = socket.gethostbyname(ip)
    socket.setdefaulttimeout(1)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host_ip, port))
    sock.close()

    if result == 0:
        # machine_hostname = socket.gethostbyaddr(ip)
        # service = socket.getservbyport(port)
        print(f"{Fore.GREEN}[+] Port {port} is Open",Fore.RESET)
        return port
    else:
        print(f"{Fore.RED}[!] Port:  {port}  is   Close", Fore.RESET)
        return None


###################### Banner Grabing #######################


def bannergrabbing(ip, port):
    print(f"{Fore.GREEN}[+] Port:  {port}  is  Open", Fore.RESET)
    print(f"{Fore.MAGENTA}[*] Grabbing Banner...", Fore.RESET)
    time.sleep(3)
    socket.setdefaulttimeout(2)
    try:
        bannergrabber = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bannergrabber.connect((ip, port))
        bannergrabber.send('message.\r\n'.encode())
        banner = bannergrabber.recv(1245).decode()
        bannergrabber.close()
        print(f"{Fore.GREEN}[#] Banner Found: \n{Fore.BLUE}{banner}", Fore.RESET)
        print("-" * 60)
    except:
        print(f"{Fore.RED}[!] Can't Connect Port", Fore.RESET)
        print("-" * 60)
    # return banner


#
###################### Banner Data base #######################
#
# def banner_DB(banner): print(banner) if "vsFTPd" in banner: new_banner = banner.split(")") new_banner=new_banner[
# 0].split(" ") print(f"{Fore.GREEN}Ftp service is running",Fore.RESET) print(f"{Fore.GREEN}Additional data -\n
# Service Version : {new_banner[2]}",Fore.RESET) if "SSH" in banner: new_banner=banner.split("-") print(f"{
# Fore.GREEN}SSH service is running",Fore.RESET) print(f"{Fore.GREEN}Additional data -\nService Version : {
# new_banner[1]} \nOs version : {new_banner[-1]}",Fore.RESET) if "open  telnet" or "Linux telnetd" in banner: print(
# f"{Fore.GREEN}Telnet service is running",Fore.RESET) if "smtp" in banner: print(f"{Fore.GREEN}Smtp service is
# running",Fore.RESET) if "domain" in banner: print(f"{Fore.GREEN}Domain service is running",Fore.RESET) print(f"{
# Fore.GREEN}Additional data -\n    Service Version : {new_banner[1]} \n    Os version : {new_banner[-1]}",
# Fore.RESET) if "http" in banner: print(f"{Fore.GREEN}Http service is running",Fore.RESET)

###################### Mulitepal Ports Scanning #######################
#
def ports_scannr(ip, first_port, last_port, summ):
    open_ports = []
    for port in random.sample(range(first_port, last_port), summ):
        open_port = open_port_scaner(ip, port)
        if open_port is None:
            continue
        else:
            open_ports.append(open_port)
    return open_ports


###################### Multiple banner grabbing #######################

def get_service_banners_for_host(ip, portlist):
    for port in portlist:
        bannergrabbing(ip, port)

###################### MAIN FUN #######################


#
if __name__=='__main__':

### Aguments
    parser = argparse.ArgumentParser(description="Magical Port Scanner and Banner Grabbing.")
    parser.add_argument("host", help="Host to scan.")
    parser.add_argument("First_Port", help="First Port to Scan.")
    parser.add_argument("Last_Port", help="last Port to Scan.")

    args = parser.parse_args()
    host = args.host
    first_port = int(args.First_Port)
    last_port =int(args.Last_Port) + 1
### main
    print(pyfiglet.figlet_format(f"{Fore.MAGENTA}Megical {Fore.GREEN}Port {Fore.BLUE}Scanner"))
    sum = last_port - first_port
    loding()

    time_from_start = datetime.now()
    subprocess.call('clear', shell=True)
    host_ip = socket.gethostbyname(host)
    print(f"{Fore.MAGENTA}Start Scanning {host_ip} in meanwhile grab cup of coffee",Fore.RESET)
    print("-" * 60)
    get_service_banners_for_host(host, ports_scannr(host,first_port,last_port,sum))

    time_after_scann = datetime.now()
    total = time_after_scann - time_from_start
    print(f"{Fore.GREEN}Scanning Completed in: {total}",Fore.RESET)

