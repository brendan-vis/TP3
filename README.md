## TP3 DEV : Premiers pas Python

### I. Ping

🌞 ping_simple.py


[ping simple](./ping_simple.py)
```
python .\ping_simple.py

Envoi d’une requête 'Ping'  8.8.8.8 avec 32 octets de données :
Réponse de 8.8.8.8 : octets=32 temps=18 ms TTL=114
Réponse de 8.8.8.8 : octets=32 temps=16 ms TTL=114
```

🌞 ping_arg.py

[ping arg](./ping_arg.py)
```
python ping_arg.py 8.8.8.8

Envoi d’une requête 'Ping'  8.8.8.8 avec 32 octets de données :
Réponse de 8.8.8.8 : octets=32 temps=16 ms TTL=114
Réponse de 8.8.8.8 : octets=32 temps=17 ms TTL=114
```

🌞 is_up.py

[is_up](./is_up.py)
```
python is_up.py 8.8.8.8
UP !
```

### II. DNS
🌞 lookup.py

[lookup](./lookup.py)
```
python lookup.py ynov.com
172.67.74.226
```

### III. Get your IP

🌞 get_ip.py

[get_ip.py](./get_ip.py)
```
python .\get_ip.py
192.168.1.87/24
256 adresses
```

### IV. Mix

🌞 network.py

[network.py](./network.py)
```
python network.py lookup thinkerview.com
188.114.96.2

python network.py ping 8.8.8.8          
UP !

python network.py ip                    
192.168.1.87/24
256 adresses
```

### V. Logs

🌞 Continuez sur le script précédent network.py

[network.py](./network.py)
```
python network.py lookup thinkerview.com
python network.py ip
python network.py ping 8.8.8.8
python network.py lookup ddfvbn

2024-10-11 10:25:01 [INFO] Command lookup called successfully with argument thinkerview.com.
2024-10-11 10:25:05 [INFO] Command ip called successfully.
2024-10-11 10:25:09 [INFO] Command ping called successfully with argument 8.8.8.8.
2024-10-11 10:54:51 [ERROR] Command lookup called with bad arguments : ddfvbn.
```

### VI. Deploy

🌞 Déployez-moi ça dans une VM Rocky

```
[brendan@localhost ~]$ sudo dnf install git
[brendan@localhost ~]$ git clone https://github.com/brendan-vis/TP3..git
```