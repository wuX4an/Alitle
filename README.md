# Alitle

Alitle is a Linux Alpine on Docker. It is intended for those who want to use Docker as small virtual machines. I created it to become the container that everyone wanted but no one asked for.

<img src="https://raw.githubusercontent.com/wuX4an/wuX4an/main/assets/logo/alpine.png">



### **Requirements**
* #### docker
* #### git

### **Recomendations**

* [lazydocker](https://github.com/jesseduffield/lazydocker)

---

<br>

### Install
```
git clone https://github.com/wuX4an/Alitle.git
```
```
cd Alitle
```
```
chmod +x setup.sh && chmod +x alitle
```
```
./setup.sh
```

---

### After Install
```
alitle
```

```
passwd <your-user-name>
```
#### I recommend before this step to log in with your user and not create directories in Alitle as the root user
```
sudo su <your-user-name>
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
* #### A bash script that you can install on your base system to get into the container more easily with you user(is the next project)

---

<br>


##### Help:
###### I need ```export PF_INFO="ascii os kernel uptime memory palette" ``` to be executed every time it boots.