import re, socket, sys

def gethostbyname(r):
    if re.match(r'^([A-Za-z0-9-]{1,63}\.)[A-Za-z]{2,6}$', r):
        print(f"{socket.gethostbyname(r)}")
    else: 
        print(f"invalid : {r}")

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Usage: python lookup.py <nom de domaine>")
    else:
        gethostbyname(sys.argv[1])