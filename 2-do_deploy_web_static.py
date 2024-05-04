#!/usr/bin/python3

"""This fabric script generates a .tgz archive from the contents of the
web_static folder of the AirBnB Clone repo."""

import os
from datetime import datetime
from fabric.operations import local, put, run, env, sudo

env.hosts = ["web-01.noblet.tech", "web-02.noblet.tech"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa.pub"


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    # Check if web_static folder exists
    if os.path.exists("web_static") is False:
        return None

    # Create versions folder if it doesn't exist
    if os.path.exists("versions") is False:
        local("mkdir -p versions")

    # Generate archive name using current date and time
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{timestamp}.tgz"

    # Use tar command to create the archive
    tar_command = f"tar -cvzf versions/{archive_name} web_static"
    result = local(tar_command, capture=True)

    # Check if archive was created successfully
    if result.failed:
        return None

    # Return path to the generated archive
    archive_path = os.path.join("versions", archive_name)
    return archive_path


def do_deploy(archive_path: str) -> bool:
    """Distributes an archive to web servers remotely"""
    # Check if the archive file exists
    if not archive_path or not os.path.exists(archive_path):
        return False

    # Upload the archive to /tmp/ directory on the web server
    put(archive_path, "/tmp/")

    # Extract the archive to /data/web_static/releases/ folder
    archive_filename = os.path.splitext(os.path.basename(archive_path))[0]

    release_folder = f"/data/web_static/releases/{archive_filename}"
    run(f"mkdir -p /data/web_static/releases/{archive_filename}/")
    run(f"tar -xzf /tmp/{archive_filename}.tgz -C {release_folder}")

    # Delete the archive from the web server
    run(f"rm /tmp/{archive_filename}.tgz")

    # Move the contents of the extracted folder to the release folder
    run(f"mv -f {release_folder}/web_static/* {release_folder}/")

    # Remove the now empty web_static folder
    run(f"rm -rf {release_folder}/web_static")

    # Delete the symbolic link /data/web_static/current
    run("sudo rm -rf /data/web_static/current")

    # Create a new symbolic link /data/web_static/current
    # linked to the new version
    run(f"sudo ln -s {release_folder} /data/web_static/current")
    run("sudo chown -R ubuntu:ubuntu /data/web_static/current")

    print("New version deployed successfully!")
    return True
