## Tools Used

---

#### gobuster

`gobuster - Directory/file & DNS busting tool written in Go`

```
gobuster -dir -u <Target IP> -w /usr/share/wordlists/dirb/big.txt
```
> dir - the classic directory brute-forcing mode

>-u, --url string  

>-w, --wordlist string

---

#### nmap

`nmap - Network exploration tool and security / port scanner`

```
nmap <Target IP>
```

---
#### radare2

`Reverse engineer and analyze binaries`

```
r2 ./hacktheworld
```

> aaa 
>> preform deeper analysis, most common use

> aaaa
>> same as aaa but adds a bunch of experimental iterations

> afl
>> list funcions

> axt
>> find data/code rferences to this address

> pdf
>> disassmeble function in a linear way (see pdfr)

> s < addr>
>> seek to address

---