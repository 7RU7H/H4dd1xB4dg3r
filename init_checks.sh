#!/bin/bash
# Automate the testing 

mympy src
flake8 src
pytest
# tox will slow down testing as it tests on fresh env 
# tox 


# masscan --regres 
