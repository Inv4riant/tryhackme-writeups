## Commands Used

---

#### gobuster

```
gobuster dir -u <Target IP> -w /usr/share/wordlists/dirb/common.txt
```
> dir - Performs brute‑force discovery of directories and files on a web server.

>-u, --url string  

>-w, --wordlist string

---

#### netcat


```
nc -nvlp <Port>
```
> -l    Enables listening mode, allowing the tool to wait for incoming connections.

> -v     Produces more detailed output. Use it twice for extra verbosity.

> -n     Uses numeric IP addresses only, skipping DNS lookups.

> -p    port    Sets the local port to use. Accepts a single port or a range (lo–hi).

---

#### nmap


```
nmap <Target IP>
```
---

#### ssh

```
ssh -i id_rsa root@<Target IP>
```

> -i identity_file
>> Specifies which private key file to use for authentication.    
If the matching private key isn’t stored locally, SSH uses the corresponding key loaded in ssh-agent.
Defaults include: ~/.ssh/id_rsa, id_ecdsa, id_ecdsa_sk, id_ed25519, and id_ed25519_sk.    
Multiple -i options may be provided, and per‑host identity settings can also be defined in the SSH config.    
If no certificate is explicitly set, SSH will automatically look for a *-cert.pub file matching the identity.

---

