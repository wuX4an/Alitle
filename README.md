# Alitle

Alitle is Alpine Linux on Docker. It is intended for those who want to use Docker as small virtual machines. I created it to become the container that everyone wanted but no one asked for.

<img src="https://raw.githubusercontent.com/wuX4an/wuX4an/main/assets/logo/alpine.png">



### **Requirements**
* #### docker
* #### git

### **Recomendations**

* [lazydocker](https://github.com/jesseduffield/lazydocker)

---

<br>

### Install
#### NOTE: you must have port 2022 unoccupied, if not you must change it in alitle(bin) and sshd_conf
```
git clone https://github.com/wuX4an/Alitle.git
```
```
cd Alitle
```
```
chmod +x /setups/base/ali
```
```
./setups/base/ali
```

```
sudo mv /setups/base/ali /bin
```

---

### After Install
#### The default password is "ali"
```
ali shell
```
#### I recomend change the deafault password 
```
passwd <your-user-name>
```

---

### Install theme for you shell
#### First install oh my fish
```
curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish
```


#### You can install a theme for your shell with omf, I recommend batman. select your favorite theme [here](https://github.com/oh-my-fish/oh-my-fish/blob/master/docs/Themes.md)
```
omf install batman 
```

---

### Features
* #### Install automatically the basic tools 
* #### Your user now create and configure automatically
* #### Fish is now your default shell
* #### Dont use neofetch now use pfetch 

---

### Possible Futures updates
* #### A little package manager
* #### A repository with useful and basic helper-type tools written in ash or fish
* #### And probably all the mini projects are compatible with this repository
* #### A bash script that you can install on your base system to get into the container more easily with you user (beta)

---

### Note: everything is a beta, everything could change drastically at some point

---
<br>


##### Help:
###### I need ```export PF_INFO="ascii os kernel uptime memory palette" ``` to be executed every time it boots.
