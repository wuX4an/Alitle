import os



settings = {
  "username": os.environ["USER"],
  "password": "alabama",
  "alpine_version": "3.19"
}



username = settings.get("username")
password = settings.get("password")
alpine_version = settings.get("alpine_version")