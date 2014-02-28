from fabric.api import task, local
from platform import system
from fabric.context_managers import lcd


@task
def test():
    local("python test.py")

@task
def build_doc():
    with lcd("docs"):
        if system() == 'Windows':
            local("make.bat html")
        else:
            local("make html")