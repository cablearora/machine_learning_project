from setuptools import setup
from typing import List



def get_requirements_list()->List[str]:
    """
    Description: This functon is going to return a list of requirements
    mentioned in the requirements.txt file

    return This is function is going to return a list which contains name
    of libraries mentioned in the requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readline()

# Declaring variables for setuo functions
PROJCT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Praveen"
DESCRIPTION = "This is my first end to end project"
PACKGES = ["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

setup(
    name=PROJCT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKGES,
    install_requires=get_requirements_list(),

)


