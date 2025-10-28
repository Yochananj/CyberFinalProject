import platformdirs

# Constants:

# Project Constants
app_name = "CryptDrive"
app_author = "YochananJulian"


# Flags
seperator = "|||"
end_flag = b"||| END |||"


# Server Constants
server_address = "127.0.0.1"
server_port = 8080
host_addr = (server_address, server_port)
server_storage_path = platformdirs.user_data_path(app_name)

# Numerical Constants
buffer_size = 1024
