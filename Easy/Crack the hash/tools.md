## Tools Used

---

#### hashcat


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
>> Specifies the hash algorithm by its ID number.

> -r, --rules-file=FILE
>> Loads a rules file to apply word‑mutation rules during dictionary attacks.


---
