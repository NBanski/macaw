import os

# Specify the products file path.
workingDirectory = os.path.dirname(__file__)
productsPath = os.path.normpath(os.path.join(workingDirectory, "..", "..", "config", "products.conf"))

# Specify the config file path.
workingDirectory = os.path.dirname(__file__)
configPath = os.path.normpath(os.path.join(workingDirectory, "..", "..", "config", "config.conf"))

def checkConfigFiles():
    print("")