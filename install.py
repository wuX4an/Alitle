import os

username = os.environ("USER")

# =============================================
#   CREATE .ali DIR
# =============================================
os.system(f'mkdir -p /home/{username}/.ali')
os.system(f'mkdir -p /home/{username}/.ali/bin/')
os.system(f'mkdir -p /home/{username}/.ali/conf/')
os.system(f'mkdir -p /home/{username}/.ali/tools/')

# =============================================
#   COPY THE DEPENDENCIES 
# =============================================
os.system(f'cp -r ./setups/bin/* /home/{username}/.ali/bin/')
os.system(f'cp -r ./setups/conf/* /home/{username}/.ali/conf/')
os.system(f'cp -r ./setups/tools/* /home/{username}/.ali/tools/')