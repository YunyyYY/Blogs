---
layout: review
permalink: /:categories/:title/
category: Notes
tag: 笔记
---

#### 1. get host address on virtual machine

Use one of the following three commands to get the information of interface parameters.

```shell
$ hostname -i
$ ifconfig
$ ip addr
```

If using the second or third command, look at the number after `inet`. The result would be a sequence like `xx.xx.x.x`.



#### 2. enable sharing

In setting, enagle remote login, and also confirm the computer name.

![](/assets/p1.png)


#### 3. connect with `ssh`

On the local terminal, use `ssh` to login and enter the user's password.

```shell
$ ssh <user_id>@<host_addr>
```



#### 4. deployment on Clion

In `Tools` choose `deployment` -> `configuration`.

![](/assets/p2.png)

Click `+` to create a new configuration. Choosing protocol type as `SFTP`.

Enter host name as provided by the virtual machine, and choose `Password` as the authentication method. Select `Save password` for convenience of future use.

Use `Autodetect` to find root path, and set up deployment path in `mapping`.

![](/assets/p3.png)

Click `OK`, and the configuration is completed. To add remote terminal to workspace, click `Tools` -> `Start SSH session`. Click `Deployment` -> `Browse Remote Host` to see remote directories.

![](/assets/p4.png){:height="100px"}

![](/assets/p5.png){:height="100px"}
