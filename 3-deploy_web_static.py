#!/usr/bin/python3

"""This fabric script generates a .tgz archive from the contents of the
web_static folder of the AirBnB Clone repo."""

import os
from datetime import datetime
from fabric.operations import local, put, run, env

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
    # print(f"Archive created successfully: {archive_path}")
    return archive_path


def do_deploy(archive_path: str) -> bool:
    """Distributes an archive to your web servers."""
    if not archive_path:
        return False

    if os.path.exists(archive_path) is False:
        return False

    archive_name = archive_path.split("/")[-1]
    archive_name_no_ext = archive_name.split(".")[0]

    put(archive_path, "/tmp/")
    run(f"mkdir -p /data/web_static/releases/{archive_name_no_ext}/")
    run(
        f"tar -xzf /tmp/{archive_name} -C "
        f"/data/web_static/releases/{archive_name_no_ext}/"
    )
    run(f"rm /tmp/{archive_name}")
    run(
        f"mv /data/web_static/releases/{archive_name_no_ext}/web_static/* "
        f"/data/web_static/releases/{archive_name_no_ext}/"
    )
    run(f"rm -rf /data/web_static/releases/{archive_name_no_ext}/web_static")
    run("rm -rf /data/web_static/current")
    run(
        f"ln -s /data/web_static/releases/{archive_name_no_ext}/ "
        "/data/web_static/current"
    )

    print("New version deployed!")
    return True


def deploy():
    """Creates and distributes an archive to your web servers."""
    if not archive_path:
        return False

    return do_deploy(archive_path)


archive_path = do_pack()
