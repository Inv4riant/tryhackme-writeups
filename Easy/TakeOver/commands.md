## Commands Used

---

#### gobuster
`gobuster - Directory/file & DNS busting tool written in Go`
```
gobuster dir -u https://futurevera.thm -k -w /usr/share/wordlists/dirb/common.txt
```

```
gobuster vhost -u https://futureeva.thm --append-domain -k -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
```

> dir - Performs brute‑force discovery of directories and files on a web server.

>vhost - Attempts to identify virtual hosts by testing hostnames against the target.
(Different from DNS enumeration.)

>-u, --url string  

>-w, --wordlist string

>-k
>> Ignores TLS/SSL certificate validation.

>--append-domain, --ad
>> Adds the main domain from the target URL to each word in the wordlist.
Without this, the wordlist must contain full domain names. (Default: false)

---

#### nmap


```
nmap futurevera.thm
```

---

