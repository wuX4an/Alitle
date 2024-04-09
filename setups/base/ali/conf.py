import os

# =============================================
#   SETTINGS
# =============================================

settings = {
  "username": os.environ["USER"],
  "password": "alabama",
  "alpine_version": "3.19"
}

username = settings.get("username")
password = settings.get("password")
alpine_version = settings.get("alpine_version")


# =============================================
#   CREATE VARIABLES
# =============================================

install_scr=[
  "#!/bin/sh",
  "#Install base",
  "apk add curl wget git nano fish shadow sudo openssh-server openrc",
  "#Setup ssh",
  "mv sshd_config /etc/ssh",
  "ssh-keygen -A",
  "rc-status",
  "touch /run/openrc/softlevel",
  "/etc/init.d/sshd start",
  "rc-update add ssh default",
  "#Setup user",
  "echo '%wheel ALL=(ALL) ALL' > /etc/sudoers.d/wheel",
  f"adduser -h /home/{username} -D {username}",
  f"echo {username}:{password} | chpasswd",
  f"usermod -aG wheel {username}",
  f"chown {username} /sali",
  "#Setup shell",
  "chsh root -s /usr/bin/fish",
  f"chsh {username} -s /usr/bin/fish",
  f"mkdir /home/{username}/.config/fish/",
  "cp /sali/conf/fish/* /home/$USER/.config/fish/ && chown /home/$USER/.config/fish"
  "sleep 0.25",
  "#Remove shits",
  "rm install.sh",
  "#Finishing",
  "echo -e 'Instalation Complete ***' "]

docker_cmd=[
  f"docker pull alpine:{alpine_version}",
  f"docker create -v /home/{username}/.ali/:/sali --name alitle --network='host' -i alpine:{alpine_version} /bin/ash",
  "docker start alitle",
  "#Share",
  "docker cp /tmp/install.sh alitle:/",
  f"docker cp /tmp/fish_theme.sh alitle:/",
  f"docker cp /home/{username}/.ali/conf/sshd_config alitle:/",
  f"docker cp /home/{username}/.ali/bin/ufetch alitle:/bin",
  "docker exec alitle chmod +x install.sh",
  "rm /tmp/install.sh",
  "rm /tmp/docker_cmd.sh"]