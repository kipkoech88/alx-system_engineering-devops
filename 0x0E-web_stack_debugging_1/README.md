 # Webstack Debugging
<br> In this scenario, we are getting `curl: (7) Failed to connect to 0 port 80: Connection refused
` <br> And upon inspection, the first thing we will check is networking to see which service is running on port 80.
<br> Here we are going to install and use netstat. <be>
```sh sudo apt update && sudo apt install netstat```
 >br>
and then use netstat to check services running in different ports <br>
```sh netstat -lpdn``` <br>
```
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      10/sshd         
tcp6       0      0 :::22                   :::*                    LISTEN      10/sshd         
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path and we can see the results show two active services,
``` 
1. tcp which is on port 22 
2. tcp6 also on port 22
>br> Therefore nothing on port 80.
The next thing is to check if nginx is running <br>
and to do this, we will use ```sh sudo service nginx status``` <br>
and we get `nginx: unrecognized service`
 <br>
But again we see service nginx is not recognized =========================<br>
So we need to install and run the service
