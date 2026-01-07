## Commands Used

---

#### gobuster
`gobuster - Directory/file & DNS busting tool written in Go`
```
gobuster dir -u <Target IP> -w /usr/share/wordlists/dirb/common.txt
```
> dir - the classic directory brute-forcing mode

>-u, --url string  

>-w, --wordlist string

---

#### netcat

`nc - TCP/IP swiss army knife`
```
nc -lvnp <Port>
```
> -l    listen mode, for inbound connects

> -v     verbose [use twice to be more verbose]

> -n     numeric‐only IP addresses, no DNS

> -p    port    local port number (port numbers can be individual or ranges: lo‐hi [inclusive])

---

#### nmap

`nmap - Network exploration tool and security / port scanner`
```
nmap <Target IP>
```
---

#### ssh
`ssh — OpenSSH remote login client`
```
ssh -i id_rsa root@<Target IP>
```

> -i identity_file
>> Selects a file from which the identity (private key) for public key authentication is read. You can also specify a public key file to use the corresponding private key that is loaded in ssh-agent(1) when the private key file is not present locally.     
The default is ~/.ssh/id_rsa, ~/.ssh/id_ecdsa, ~/.ssh/id_ecdsa_sk, ~/.ssh/id_ed25519 and ~/.ssh/id_ed25519_sk.      
Identity files may also be specified on a per-host basis in the configuration file. It is possible to have multiple -i options (and multiple identities specified in configuration files).      
If no certificates have been explicitly specified by the CertificateFile directive, ssh will also try to load certificate information from the filename obtained by appending -cert.pub to identity filenames.
---