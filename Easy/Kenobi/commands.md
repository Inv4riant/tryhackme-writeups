## Commands Used

---
#### enum4linux

`Enumerate information from Windows and Samba systems`

```
enum4linux -S <Target IP>
```

> -S
>> Enumerate shared resources (shares) on the target.


---

#### netcat

`nc - TCP/IP swiss army knife`

```
nc <Target IP> <FTP Port>
```

---

#### nmap

`nmap - Network exploration tool and security / port scanner`
```
nmap <Target IP>
```

```
nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse <Target IP>
```

```
nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount <Target IP>
```

```
nmap -p 111 --script=nfs-showmount <Target IP>
```

>-p (port_range)
>> Port specification: Specifies which ports to scan (e.g., -p 80,443, -p 1-1024, -p- for all ports).

> --script <script_name|category|directory>
>> Nmap Scripting Engine: Runs specific Nmap scripts or categories of scripts (e.g., --script http-enum, --script default, --script vuln).

---
#### searchploit

`SearchSploit ‐ Exploit Database Archive Search`

```
searchploit proftpd <Service Version>
```

---