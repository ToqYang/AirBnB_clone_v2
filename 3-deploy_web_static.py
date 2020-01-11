#!/usr/bin/python3
""" Write a Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone repo,
using the function do_pack. """

from datetime import datetime
from fabric.api import *
import os


env.hosts = ['34.73.238.143', '35.229.20.11']
env.user = "ubuntu"


def do_pack():
    """ Do the pack to Fabric """
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")

        dat = datetime.now()
        dat = dat.strftime("%Y%m%d%H%M%S")

        new_mar = "versions/web_static_{}.tgz".format(dat)
        local("tar -cvzf {} web_static".format(new_mar))
        return new_mar

    except:
        return None


def do_deploy(archive_path):
    """ It does deploy in the webserver """
    if not os.path.exists("archive_path"):
        return False

    try:

        fil_tgz = os.path.basename(archive_path)
        fol_des = fil_tgz.replace(".tgz", "")
        path = "/data/web_static/releases/"

        put(archive_path, "/tmp/")

        run("mkdir -p {}{}/".format(path, fol_des))
        run("tar -xzf /tmp/{} -C {}{}/".format(fil_tgz, path, fol_des))
        run("rm /tmp/{}".format(fil_tgz))
        run("mv {}{}/web_static/* {}{}/".format(path, fol_des, path, fol_des))
        run("rm -rf {}{}/web_static".format(path, fol_des))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, fol_des))

        print("New version deployed!")

        return True

    except:
        return None


def deploy():
    """ Deploy the functions """
    mypack = do_pack
    if not mypack:
        return False
    mydeploy = do_deploy(archive_path)
    return (mydeploy)

