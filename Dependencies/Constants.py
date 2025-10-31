import os
import platformdirs

# Constants:

# Project Constants
app_name = "CryptDrive"
app_author = "YochananJulian"
crypt_drive_blue = "#3043FB"


# Flags
seperator = "|||"
end_flag = b"||| END |||"


# Server Constants
server_address = "127.0.0.1"
server_port = 8080
host_addr = (server_address, server_port)
server_storage_path = platformdirs.user_data_path(app_name)


# Server Keys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # directory of this Constants.py file
PUBLIC_KEY_PATH = os.path.join(BASE_DIR, "public.pem")
PRIVATE_KEY_PATH = os.path.join(BASE_DIR, "private.pem")

with open(PUBLIC_KEY_PATH, "r") as file:
    public_key = file.read()

with open(PRIVATE_KEY_PATH, "r") as file:
    private_key = file.read()

# Numerical Constants
buffer_size = 1024
