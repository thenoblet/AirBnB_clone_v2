#!/usr/bin/python3

"""This fabric script generates a .tgz archive from the contents of the
web_static folder of the AirBnB Clone repo."""

from fabric.operations import local
import os
from datetime import datetime


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
