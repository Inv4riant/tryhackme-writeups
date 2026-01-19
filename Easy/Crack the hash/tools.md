## Tools Used

---

#### hashcat
`Crack password hashes using various methods`

```
hashcat -m 0 hash.txt /usr/share/wordlists/SecLists/Passwords/Leaked-Databases/rockyou.txt
```

```
hashcat -m 100 hash.txt /usr/share/wordlists/SecLists/Passwords/Leaked-Databases/rockyou.txt
```

```
hashcat -m 1400 hash.txt /usr/share/wordlists/SecLists/Passwords/Leaked-Databases/rockyou.txt
```

```
hashcat -m 3200 hash.txt rockyou-4.txt
```

```
hashcat -m 900 hash.txt /usr/share/wordlists/SecLists/Passwords/Leaked-Databases/rockyou.txt -r /usr/share/hashcat/rules/best64.rule
```

```
hashcat -m 1400 hash.txt /usr/share/wordlists/SecLists/Passwords/Leaked-Databases/rockyou.txt
```

```
hashcat -m 1000 hash.txt /usr/share/wordlists/SecLists/Passwords/Leaked-Databases/rockyou.txt
```

```
hashcat -m 1800 hash.txt rockyou-6.txt
```

```
hashcat -m 160 hash.txt /usr/share/wordlists/SecLists/Passwords/Leaked-Databases/rockyou.txt
```


> -m, --hash-type=NUM
>> Hash-type ID (see hashcat --help for 350+ types like 0=MD5, 1000=NTLM)

> -r, --rules-file=FILE
>> Load rules from FILE for mutations

---