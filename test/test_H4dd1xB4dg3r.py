from H4dd1xB4dg3r.H4dd1xB4dg3r import *
import pytest

# Have a nice list of functions for easy scripting to make this file, it will get big probably 
# To write a test copy the function below #####--WORKSPACE-- line

def test_workspace_management():

def test_branch_osmedeus():

def test_branch_reconftw():

def test_branch_nuclei():

def test_osint_tools():

def test_recon_tools():

def test_domain_tools():

def test_subdomain_tools():

def test_server_tools():

def test_wordlist_tools():

def test_util_*



# run all
# cat test/test_H4dd1xB4dg3r.py | awk '{print $2}'  | tr -d ":"
test_workspace_management()
test_branch_osmedeus()
test_branch_reconftw()
test_branch_nuclei()
test_osint_tools()
test_recon_tools()
test_domain_tools()
test_subdomain_tools()
test_server_tools()
test_wordlist_tools()
test_util_*

# Parametrize testing 
@pytest.mark.parametrize("test_input,expected_answer", [
    ('testinput', expected_answer),
])

# Skip a test - if not implemented copy above that test
@pytest.mark.skip(reason="Better be a good reason")

# The Programmer from HELL's favourite test @ScottWlaschin
@pytest.mark.xfail # if you know it'll fail but don't want the build to fail.. - not an except!

# if a lot of tests require the 
# conftest.py should contain these
# IF a test_*( CONTAINS argument_name
# Avoids boiler plate
@pytest.fixture(scope="")
def argument_name():
    with x as xy:
        yield xy # yield is better than return for teardown code that require a closing() - use yield



###########################-----WORKSPACE------##############################







