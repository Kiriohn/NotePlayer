# General configuration file
import os

# Define the path to the parent directory
FILE_PATH = os.path.abspath(__file__)
PARENT_PATH = os.path.join(os.path.dirname(FILE_PATH).replace("\\","/"), "..")

# Define the path to the icon
ICON = "assets/img/NP.ico"
ICON_PATH = os.path.join(PARENT_PATH, ICON)

