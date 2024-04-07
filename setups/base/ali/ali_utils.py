import os
from . import conf
from time import sleep

# =============================================
#   FIND CHAIN
# =============================================

def find_chain(log_path, key, error, loading_message, finish_message, error_message, animation):
    symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    a = 0
    while True:
        #Animation
        if animation == True:
            a = (a + 1) % len(symbols)
            print(f'\r\033[K%s {loading_message}...' % symbols[a], flush=True, end='')
            sleep(0.1)
        #Read
        with open(log_path, "r") as f:
            lines = f.readlines()
        #Find
        find = False
        for i, line in enumerate(lines):
            if error in line:
                os.system('clear')
                print(f"\n{error_message}\n")
                find = True
            elif key in line and find == False:
                #print(f"\n\nline {i + 1}: {line}")
                os.system('clear')
                print(f"\n{finish_message}\n")
                find = True
        if find == True:
            break

# =============================================
#   CREATE
# =============================================

def create(username, password, alpine_version):

    #Install src
    os.system('touch /tmp/install.sh')
    conf.install_scr = "\n".join(conf.install_scr)
    with open("/tmp/install.sh", "w") as install:
        install.write(conf.install_scr)
    #Docker src
    os.system('touch /tmp/docker_cmd.sh')
    conf.docker_cmd = "\n".join(conf.docker_cmd)
    with open("/tmp/docker_cmd.sh", "w") as docker:
        docker.write(conf.docker_cmd)
    
    ## RUN ##
    os.system("nohup sh -c 'chmod +x /tmp/docker_cmd.sh && . /tmp/docker_cmd.sh' > log 2>&1&")
    find_chain("log", "***","permission denied", "Creating", "Creation Complete", "Something Went Wrong", True)
    

# =============================================
#   SHELL
# =============================================

def shell(username):
    os.system("nohup sh -c 'docker start alitle' > /dev/null 2>&1&")
    os.system(f'docker exec -it alitle su {username}')

# =============================================
#   START
# =============================================

def start():
    os.system("nohup sh -c 'docker start alitle' > log 2>&1&")
    find_chain("log", "alitle", "No such container", "Starting", "The container started", "The Container no Exist", True)

# =============================================
#   STOP
# =============================================

def stop():
    #os.system('docker stop alitle')
    os.system("nohup sh -c 'docker stop alitle' > log 2>&1&")
    find_chain("log", "alitle","No such container", "Stopping", "The container stopped", "The Container no Exist", True)

# =============================================
#   CREATE RESTART
# =============================================

def restart():
    os.system("nohup sh -c 'docker restart alitle' > log 2>&1&")
    find_chain("log", "alitle","No such container", "Restarting", "The container as been restarted", "The Container no Exist", True)

# =============================================
#   DELETE
# =============================================

def delete():
    os.system("nohup sh -c 'docker stop alitle && docker rm alitle' > log 2>&1&")
    find_chain("log", "alitle","No such container", "Removing", "The container as been removed", "The Container no Exist", True)

# =============================================
#   STATUS
# =============================================

def status():
    os.system('docker stats alitle')

# =============================================
#   UNISTALL
# =============================================

def uninstall():
    os.system('echo -e "***\e[31m Uninstall \e[0m***"')
    os.system('sudo rm /bin/ali')