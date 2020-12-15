import os

# Specify the config directory path.
workingDirectory = os.path.dirname(__file__)
directoryPath = os.path.normpath(os.path.join(workingDirectory, "..", "..", "config",))

# Specify the products file path.
workingDirectory = os.path.dirname(__file__)
securityPath = os.path.normpath(os.path.join(workingDirectory, "..", "..", "config", "security.conf"))

# Specify the config file path.
workingDirectory = os.path.dirname(__file__)
configPath = os.path.normpath(os.path.join(workingDirectory, "..", "..", "config", "config.conf"))

def createConfigFiles():
    # Check if directory itself exists/create it.
    if os.path.exists(directoryPath):
        print("Config directory exists.")
    else:
        print("Config directory does not exist. Creating...")
        os.makedirs(directoryPath)
    # Check if products.conf exists/create it.
    if os.path.exists(securityPath):
        print("Security configuration file exists.")
    else:
        print("Security configuration file does not exist. Creating...")
        with open(securityPath, "a"):
            os.utime(securityPath, None)
    # Check if products.conf exists/create it.
    if os.path.exists(configPath):
        print("Config configuration file exists.")
    else:
        print("Config configuration file does not exist. Creating...")
        with open(configPath, "a"):
            os.utime(configPath, None)