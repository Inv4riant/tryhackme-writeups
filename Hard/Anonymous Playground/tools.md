## Tools Used

---

#### gobuster



```
gobuster -dir -u <Target IP> -w /usr/share/wordlists/dirb/big.txt
```
> dir - Performs brute‑force discovery of directories and files on a web server.

>-u, --url string  

>-w, --wordlist string

---

#### nmap



```
nmap <Target IP>
```

---
#### radare2



```
r2 ./hacktheworld
```

> aaa 
>> Performs an in‑depth analysis of the binary.

> aaaa
>> Extends aaa with additional, more experimental analysis passes.

> afl
>> Lists all detected functions within the binary.

> axt
>> Shows code or data references that point to the specified address.

> pdf
>> Disassembles the current function in a straightforward, linear format.

> s < addr>
>> Moves the seek pointer to the given address.


---
