#!/usr/bin/python3
""" distributes an archive to your web servers, 
using the function do_deploy """

from datetime import datetime
from fabric.api import *
from split import shlex
import os

def do_deploy(archive_path):
    """ It does deploy in the webserver """
        if not os.path.exists("archive_path"):
            return False

        try:
            del_sp = archive.path.replace("/", " ")

        return True

    except:
        return None
