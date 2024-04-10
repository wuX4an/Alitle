# Alitle

Alitle is Alpine Linux on Docker. It is intended for those who want to use Docker as small virtual machines. I created it to become the container that everyone wanted but no one asked for.
<br>



<p align="center">
	<a href="https://github.com/wux4an/alitle/stargazers">
		<img alt="Stargazers" src="https://img.shields.io/github/stars/wux4an/alitle?style=for-the-badge&logo=starship&color=C9CBFF&logoColor=D9E0EE&labelColor=302D41"></a>
	<a href="https://github.com/wux4an/alitle/releases/latest">
		<img alt="Releases" src="https://img.shields.io/github/release/wux4an/alitle.svg?style=for-the-badge&logo=github&color=F2CDCD&logoColor=D9E0EE&labelColor=302D41"/></a>
</p>

---

<img src="https://raw.githubusercontent.com/wuX4an/wuX4an/main/assets/logo/alpine-poster.png" class="center">


<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

</div>


---

<br>

## Installation

<h3><details>
    <summary><b>System Requirements</b></summary>
<h6> 

- Docker 🐳
- Git 🌿
- Python 🐍
- Binutils 🛠️

</h6>

</details></h3>


<h3><details>
    <summary><b>Prerequisites</b></summary>

<h6>1. Add your user to docker group</h6>
<h6><pre><code>sudo usermod -aG docker $USER</code></pre></h6>

</details></h3>

---

### Install:
```console
git clone https://github.com/wuX4an/alitle
cd alitle
chmod +x install.sh
./install.sh
```
---

<h3><details>
    <summary><b>How to use</b></summary>

#### Setup:
<h6>1. Create a virtual environment with python:</h6>
<h6><pre><code>python3 -m venv env</code></pre></h6>

<h6>2. Install dependencies:</h6>

#### Usage:
<h6>1. For help type:</h6>
<h6><pre><code>python3 setups/base/ali/ali.py --help</code></pre></h6>

<h6>2. You can modify to your taste setups/base/ali/conf.py</h6>
<h6><pre><code>python3 -m venv env</code></pre></h6>

</details></h3>

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
