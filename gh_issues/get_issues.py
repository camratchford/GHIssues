import argparse
from os import environ

import urllib3

from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.text import Text

from gh_issues import determine_git_info_from_pwd

def get():
    gh_token = environ.get("GITHUB_TOKEN")
    gh_username = environ.get("GITHUB_USERNAME")
    gh_default_repo = environ.get("GITHUB_DEFAULT_REPO")

    parser = argparse.ArgumentParser()

    parser.add_argument('--user', type=str, default=gh_username, required=False)
    parser.add_argument('--token', type=str, default=gh_token)
    parser.add_argument('--repo', type=str, default=gh_default_repo, required=False)
    parser.add_argument('--pwd', action="store_true")
    args = parser.parse_args()

    console = Console()

    if not args.user and not args.pwd:
        console.print("no github username provided", style="red")
        exit(1)
    user = args.user

    if not args.token:
        console.print("no github token provided", style="red")
        exit(1)
    token = args.token

    if not args.repo and not args.pwd:
        console.print("no github repo provided", style="red")
        exit(1)
    repo = args.repo

    if args.pwd:
        pwd_args = determine_git_info_from_pwd()
        if not pwd_args:
            console.print("this directory is not a git repo", style="red")
            exit(1)
        repo = pwd_args.get('repo')
        user = pwd_args.get('username')

    issues_req = urllib3.request(
        method="GET",
        url=f"https://api.github.com/repos/{user}/{repo}/issues",
        headers={
            "Authorization": f"token {token}",
            "X-GitHub-Api-Version": "2022-11-28"
        }
    )
    issues = issues_req.json()

    if not len(issues):
        console.print(f"No issues found for {user}/{repo}", style="yellow")
        exit(0)
    table = Table(title=Text(f"Github Issues for {user}/{repo}", style="bold white"), show_lines=True)
    tx_title = Text("Title", style="bold white")
    tx_body = Text("Notes", style="bold white")
    table.add_column(tx_title, style="bold white", no_wrap=True)
    table.add_column(tx_body, no_wrap=False)
    for issue in issues:
        md_body = Markdown(issue.get("body"))
        table.add_row(issue.get("title"), md_body)

    console.print(table)





