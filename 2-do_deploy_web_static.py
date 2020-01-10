#!/usr/bin/python3
""" distributes an archive to your web servers,
using the function do_deploy """
from datetime import datetime
from fabric.api import *
from split import shlex
import os


def do_deploy(archive_path):
    """ It does deploy in the webserver """
    env.hosts = [
        '34.73.238.143'
        '35.229.20.11'
    ]

    env.user = "ubuntu"
    env.use_ssh_config = True
    env.ssh_config_path = '~/.ssh/ssh_config'
    env.key_filename = '~/.ssh/holberton'

    if not os.path.exists("archive_path"):
        return False

    try:

        fil_tgz = os.path.basename(archive_path)
        fol_des = fil_tgz.replace(".tgz", "")
        path = "/data/web_static/releases/"

        put(nam_fil, "/tmp/{}".format(fil_tgz))
        run("mkdir -p {}{}/".format(path, fol_des))
        run("tar -xzf /tmp/{} -C {}{}/".format(fil_tgz, path, fol_des))
        run("rm /tmp/{}".format(fil_tgz))
        run("mv {}{}/web_static/* {}{}/".format(path, fol_des, path, fol_des))
        run("rm -rf {}{}/web_static".format(path, fol_des))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, fol_des))

        return True

    except:
        return None
