import re, socket, sys, os, ipaddress, psutil, datetime

fonction = sys.argv[1]

TEMP_DIR = os.path.join(os.getenv('LOCALAPPDATA'), 'Temp', 'network_tp3')
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)
LOG_FILE = os.path.join(TEMP_DIR, 'network.log')

with open(LOG_FILE, 'a') as file:
    pass


def write_log(command, success=True, args=sys.argv[-1]):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if success:
        log_line = f"{timestamp} [INFO] Command {command} called successfully"
        if len(sys.argv) == 3:
            log_line += f" with argument {args}."
        else:
            log_line += "."
    else:
        log_line = f"{timestamp} [ERROR] Command {command} called with bad arguments : {args}."
    
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(log_line + '\n')

def lookup(r):
    if re.match(r'^([A-Za-z0-9-]{1,63}\.)[A-Za-z]{2,6}$', r):
        try:
            print(f"{socket.gethostbyname(r)}")
            write_log(fonction, success=True, args=sys.argv[-1])
        except socket.gaierror as e:
            print("domain invalid")
        except:
            print("Uncaught exception.")

    else: 
        write_log(fonction, success=False, args=sys.argv[-1])
        if len(sys.argv) !=3:
            print("Usage: python lookup.py <nom de domaine>")
        
        


def ping():
    response = os.system ("ping -n  1 "+ sys.argv[2] + " > nul")

    if not re.search (r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", sys.argv[2]):
        print("addresse ip pas bonne")
        write_log(fonction, success=False, args=sys.argv[-1])
    elif response == 0:
        print(f"UP !")
        write_log(fonction, success=True, args=sys.argv[-1])
    else:
        print(f"DOWN !")
        write_log(fonction, success=False, args=sys.argv[-1])

    
def ip():
    res = psutil.net_if_addrs()['Wi-Fi']
    for infos in res:
        if infos.family == socket.AddressFamily.AF_INET:
            ip = infos.address
            netmask = infos.netmask
            cidr = ipaddress.IPv4Network(f"0.0.0.0/{netmask}").prefixlen
            nb_adr = 2**(32-cidr)
            print(f"{ip}/{cidr}")
            print(f"{nb_adr} adresses")
            write_log(fonction, success=True, args=sys.argv[-1])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <fonction> <argument>")
    else:        
        if fonction == "lookup":
            lookup(sys.argv[2])
        elif fonction == "ping":
            ping()
        elif fonction == "ip":
            ip()


# write_log(fonction, success=True, args=sys.argv[-1])

