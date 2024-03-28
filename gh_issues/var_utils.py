
import configparser
import re
import subprocess
import tempfile

from os import environ
from pathlib import Path


def edit_content(initial_content=""):
    # Get the preferred editor from the environment variable, default to nano if not set
    editor = environ.get('EDITOR', 'vim')

    # Create a temporary file and write the initial content to it
    with tempfile.NamedTemporaryFile(mode='r+') as tmpfile:
        tmpfile.write(initial_content)
        tmpfile.flush()

        # Open the preferred editor to edit the temporary file
        subprocess.call([editor, tmpfile.name])

        # Move the cursor to the beginning of the file to read its content
        tmpfile.seek(0)

        # Read the modified content
        modified_content = tmpfile.read()

    return modified_content

def determine_git_info_from_pwd():
    cwd = Path.cwd()
    dotgit_path = cwd.joinpath(".git")

    if not dotgit_path.exists():
        return None

    git_config_path = dotgit_path.joinpath("config").resolve()
    config = configparser.ConfigParser()
    config.read(str(git_config_path))
    username_pattern = r"(?<=github\.com\/)[a-zA-Z0-9\-_]*"
    repo_pattern = r"(?<=\/)[a-zA-Z0-9\-_]*(?=.git)"

    url = config['remote "origin"']['url']
    username = re.findall(username_pattern, url).pop()
    repo = re.findall(repo_pattern, url).pop()
    return {
        "username": username,
        "repo": repo
    }
