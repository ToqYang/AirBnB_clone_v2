#!/usr/bin/python3
""" Write a Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone repo,
using the function do_pack. """

from datetime import datetime
from fabric.api import *
import os


def do_pack():
    """ Do the pack to Fabric """
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")

        dat = datetime.now()
        dat = dat.strftime("%Y%m%d%H%M%S")

        new_mar = "versions/web_static_" + dat + ".tgz"

        local("tar -cvzf {} web_static".format(new_mar))
        return new_mar

    except:
        return None
