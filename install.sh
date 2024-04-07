#!/bin/sh

user=$(whoami)

# =============================================
#   COLORS
# =============================================

bold="$(tput bold)"
black="$(tput setaf 0)"
red="$(tput setaf 1)"
green="$(tput setaf 2)"
yellow="$(tput setaf 3)"
blue="$(tput setaf 4)"
magenta="$(tput setaf 5)"
cyan="$(tput setaf 6)"
white="$(tput setaf 7)"
reset="$(tput sgr0)"

# =============================================
#   ENTER DIRS
# =============================================

cd /tmp
git clone https://github.com/wuX4an/Alitle
sleep 0.25
cd Alitle

# =============================================
#   ON ALITLE
# =============================================

sleep 0.25

# Create .ali dir
mkdir /home/$user/.ali
mkdir /home/$user/.ali/bin/
mkdir /home/$user/.ali/conf/
mkdir /home/$user/.ali/tools/

sleep 0.25
# Copy to .ali dir
cp ./setups/bin/* /home/$user/.ali/bin/
cp ./setups/conf/* /home/$user/.ali/conf/
cp ./setups/tools/* /home/$user/.ali/tools/

# =============================================
#   ON PYTHON ENVIROMENT
# =============================================
function question() {
    while true; do
    echo -e "You can edit the /tmp/base/ali/conf.py script to your preferences"
        read -p "Do you wish to continue? (E/y)? " input

    # Validate the input
        case "$input" in
            "" | "E" | "e")
            return 0
            ;;
            "Y" | "y")
            return 1
            ;;
            *)
            echo "No valid input"
            ;;
        esac
    done
}

function python() {

    python -m venv env
    source env/bin/activate

    if [[ "$PS1" == *"(env)"* ]]; then
        echo -e "${reset}${green}${bold}In the virtual environment."
        sleep 1
        pip install -r requirements.txt
        pyinstaller -F ali_utils.py ali.py conf.py
        mv dist/main ali
        sudo mv ali /bin
    else
        echo -e "${reset}${red}${bold}Not in a virtual environment. Try to do it manually."
        exit
    fi
}

#Obtain the response
question

if [ $? -eq 0 ]; then
    #Edit
    sleep 0.5
    nano /tmp/base/ali/conf.py
    python
else
    #Continue
    python
fi