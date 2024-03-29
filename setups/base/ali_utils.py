import os

def uninstall():
    os.system('echo -e "***\e[31m Uninstall \e[0m***"')
    os.system('sudo rm /bin/ali')
    

def create(username, password, alpine_version):
    
    install_scr=[
        "#!/bin/ash",
        "#Install base",
        "apk add curl wget git nano fish shadow sudo openssh-server openrc",
        "#Setup ssh",
        "mv sshd_config /etc/ssh",
        "ssh-keygen -A",
        "rc-status",
        "touch /run/openrc/softlevel",
        "/etc/init.d/sshd start",
        "rc-update add ssh default",
        "#Setup user (deafult passwd is ali)",
        "echo '%wheel ALL=(ALL) ALL' > /etc/sudoers.d/wheel",
        f"adduser -h /home/{username} -D {username}",
        f"echo {username}:{password} | chpasswd",
        f"usermod -aG wheel {username}",
        f"chown {username} /sali",
        "#Setup shell",
        "chsh root -s /usr/bin/fish",
        f"chsh {username} -s /usr/bin/fish",
        "sleep 0.25",
        "#Remove shits",
        "rm install.sh",
        "#Finishing",
        "echo -e '*** Instalation Complete ***' "]
    #print("\n".join(install_scr))
    
    docker_cmd=[
        f"docker pull alpine:{alpine_version}",
        f"docker create -v /home/$USER/.ali/:/sali --name alitle --network='host' -i alpine:{alpine_version} /bin/ash",
        "docker start alitle",
        "#Share",
        "docker cp /tmp/install.sh alitle:/",
        "docker cp /home/$USER/.ali/conf/sshd_config alitle:/",
        "docker cp /home/$USER/.ali/bin/pfetch alitle:/bin",
        "docker exec alitle chmod +x install.sh",
        "docker exec alitle ./install.sh",
        "rm /tmp/install.sh",
        "rm /tmp/docker_cmd.sh"]
    
    ## LOGIC ##
    
    #Install src
    os.system('touch /tmp/install.sh')
    install_scr = "\n".join(install_scr)
    with open("/tmp/install.sh", "w") as install:
        install.write(install_scr)
    #Docker src
    os.system('touch /tmp/docker_cmd.sh')
    docker_cmd = "\n".join(docker_cmd)
    with open("/tmp/docker_cmd.sh", "w") as docker:
        docker.write(docker_cmd)
    
    ## RUN ##
    os.system("nohup sh -c 'chmod +x /tmp/docker_cmd.sh && . /tmp/docker_cmd.sh' > log 2>&1&")
    



def shell(username):
    os.system('docker start alitle')
    os.system(f'docker exec -it alitle su {username}')



def start():
    os.system('docker start alitle')



def stop():
    os.system('docker stop alitle')



def status():
    os.system('docker status alitle')



def restart():
    os.system('docker restart alitle')



def delete():
    os.system('docker stop alitle')
    os.system('docker rm alitle')
