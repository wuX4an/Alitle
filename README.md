# Alitle

Alitle is Alpine Linux on Docker. It is intended for those who want to use Docker as small virtual machines. I created it to become the container that everyone wanted but no one asked for.

<img src="https://raw.githubusercontent.com/wuX4an/wuX4an/main/assets/logo/alpine-poster.png">



### **Requirements**
* #### docker
* #### git
* #### python
* #### pip

### **Recommendations**

* [lazydocker](https://github.com/jesseduffield/lazydocker)

---

<br>

### Install
#### NOTE: you must have port 2022 unoccupied, if not you must change it in ali(bin) and sshd_conf
```
https://raw.githubusercontent.com/wuX4an/Alitle/main/install.sh
```

---

### After Install
#### To enter to the container type
```
ali shell
```
#### I recommend change the default password, The default password is "alabama"
```
passwd <your-user-name>
```

---

### Features
* #### Install automatically the basic tools 
* #### Your user now create and configure automatically
* #### Fish is now your default shell
* #### Don't use neofetch now use ufetch 

---

### Possible Futures updates
* #### A little package manager
* #### A repository with useful and basic helper-type tools written in ash or fish
* #### And probably all the mini projects are compatible with this repository
* #### A bash script that you can install on your base system to get into the container more easily with you user (beta)
* #### User add user profiles setup tool and use with the custom future repository

---

### Note: everything is a beta, everything could change drastically at some point

---

## Credit

- [jschx (ufetch) ](https://gitlab.com/jschx/ufetch)
