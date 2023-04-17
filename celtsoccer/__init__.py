# Do not modify this script!!!
from celtsoccer.parser import *
from celtsoccer.stats import *
from celtsoccer.viz import *
import turtle

hard_dependencies = ['turtle']
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)

    except ImportError as e:
        missing_dependencies.append(dependency)

if len(missing_dependencies) != 0:
    for dependency in missing_dependencies:
        raise ImportError("Missing required dependencies {0}".format(dependency))
    print('Missing packages error, make sure to install/import them')
    exit(-1)

