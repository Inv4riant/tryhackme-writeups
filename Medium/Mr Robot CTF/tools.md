## Tools Used

---

#### gobuster
`gobuster - Directory/file & DNS busting tool written in Go`
```
gobuster dir -u <Target IP> -w /usr/share/wordlists/dirb/common.txt -s "200" -b ""
```

> dir - the classic directory brute-forcing mode

>-u, --url string  

>-w, --wordlist string

>-s string
>>Positive status codes (dir mode only) (default "200,204,301,302,307")

>-b 
>> blacklist (was removed but gobuster still expects it)

---

#### hashcat
`Crack password hashes using various methods`

```
hashcat -m 0 hash.txt /usr/share/wordlists/rockyou.txt
```

> -m, --hash-type=NUM
>> Hash-type ID (see hashcat --help for 350+ types like 0=MD5, 1000=NTLM)

---

#### hydra

`hydra - a very fast network logon cracker which supports many different services`

```
hydra -L sorted.dic -p teste <Target IP> http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^:F=Invalid username"
```

```
hydra -l ELLIOT -P sorted.dic <Target IP> http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^:F=The password you entered"
```
> -l LOGIN or -L FILE  
>>login with LOGIN name, or load several logins from FILE

>-p PASS
>>or -P FILE try password PASS, or load several passwords from FILE

---

#### nmap

`nmap - Network exploration tool and security / port scanner`
```
nmap <Target IP>
```

```
nmap -sV -sC <Target IP>
```

>-sC: equivalent to --script=default

>-sV: Probe open ports to determine service/version info

---