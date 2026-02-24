## Tools Used

---

#### gobuster

```
gobuster dir -u <Target IP> -w /usr/share/wordlists/dirb/common.txt -s "200" -b ""
```

> dir - Performs brute‑force discovery of directories and files on a web server.

>-u, --url string  

>-w, --wordlist string

>-s string
>>Specifies which HTTP status codes should be treated as valid hits in directory mode.
(Default: "200,204,301,302,307")

>-b 
>> blacklist (was removed but gobuster still expects it)

---

#### hashcat


```
hashcat -m 0 hash.txt /usr/share/wordlists/rockyou.txt
```

> -m, --hash-type=NUM
>> Specifies the hash algorithm by its ID number.

---

#### hydra



```
hydra -L sorted.dic -p teste <Target IP> http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^:F=Invalid username"
```

```
hydra -l ELLIOT -P sorted.dic <Target IP> http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^:F=The password you entered"
```
> -l LOGIN or -L FILE  
>>Use a single username, or load a list of usernames from a file

>-p PASS
>>Try one specific password, or supply a file containing multiple passwords.

---

#### nmap


```
nmap <Target IP>
```

```
nmap -sV -sC <Target IP>
```

>-sC: Runs the default script set (same as --script=default).

>-sV: Examines open ports to identify the service and version running on them.


---
