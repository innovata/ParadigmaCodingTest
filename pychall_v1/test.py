
from subprocess import run


# run("python -m unittest pychall/test/psql.py", shell=True, check=True)
# run("python -m unittest pychall/test/models.py", shell=True, check=True)
run("python -m unittest pychall/test/initdb.py", shell=True, check=True)
