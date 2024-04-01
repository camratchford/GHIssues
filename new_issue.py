import sys
import argparse
import json

from pathlib import Path
from os import environ

import urllib3

from rich.console import Console

from gh_issues import edit_content, determine_git_info_from_pwd



def new():
    gh_token = environ.get("GITHUB_TOKEN")
    gh_username = environ.get("GITHUB_USERNAME")
    gh_default_repo = environ.get("GITHUB_DEFAULT_REPO")

    parser = argparse.ArgumentParser()
    parser.add_argument('--user', type=str, default=gh_username, required=False)
    parser.add_argument('--token', type=str, default=gh_token)
    parser.add_argument('--repo', type=str, default=gh_default_repo, required=False)
    parser.add_argument('-t', '--title', type=str)
    parser.add_argument('-m', '--message', type=str, required=False)
    parser.add_argument('--pwd', action="store_true")
    args = parser.parse_args()

    console = Console()


    if not args.user and not args.pwd:
        console.print("no github username provided", style="red")
        sys.exit(1)
    user = args.user

    if not args.token:
        console.print("no github token provided", style="red")
        sys.exit(1)
    token = args.token

    if not args.repo and not args.pwd:
        console.print("no github repo provided", style="red")
        sys.exit(1)
    repo = args.repo

    if not args.title:
        console.print("no issue title provided", style="red")
        sys.exit(1)
    title = args.title

    # If we don't get the --message or -m option, open EDITOR and get it there
    message = args.message
    if not message:
        message = edit_content(f"# {title}\n")

    if args.pwd:
        pwd_args = determine_git_info_from_pwd()
        if not pwd_args:
            console.print("this directory is not a git repo", style="red")
            sys.exit(1)
        repo = pwd_args.get('repo')
        user = pwd_args.get('username')

    body_dict = {
        "title": title,
        "body": message
    }
    body = json.dumps(body_dict)

    issues_req = urllib3.request(
        method="POST",
        url=f"https://api.github.com/repos/{user}/{repo}/issues",
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.text+json",
            "X-GitHub-Api-Version": "2022-11-28"
        },
        body=body
    )
    style = "green"

    if issues_req.status > 299:
        style = "red"
    console.print(issues_req.reason, style=style)

if getattr(sys, 'frozen', False):
    new()
