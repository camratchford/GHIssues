# GHIssues

> Scripts to view and create Github issues from the CLI


## Commands

### `ghissues-new`

```
usage: ghissues-new [-h] [--user USER] [--token TOKEN] [--repo REPO] [-t TITLE] [-m MESSAGE] [--pwd]

options:
  -h, --help                     show this help message and exit
  --user USER                    owner of the git repo (environment variable = GITHUB_USERNAME)
  --token TOKEN                  Github token used to authenticate with the Github REST API (environment variable = GITHUB_TOKEN)
  --repo REPO                    repo name (environment variable = GITHUB_DEFAULT_REPO)
  -t TITLE, --title TITLE        issue title
  -m MESSAGE, --message MESSAGE  issue message (if not provided, the script will open EDITOR for message entry)
  --pwd                          flag when if set will cause the script to derrive 'USER' and 'REPO' from the current working directory .git/config file
```

> The `--pwd` flag will attempt to override both the environment variables and the passed arguments for the `USER` and `USER` options


### `ghissues-get`

```
usage: ghissues-get [-h] [--user USER] [--token TOKEN] [--repo REPO] [--pwd]

options:
  -h, --help                     show this help message and exit
  --user USER                    owner of the git repo (environment variable = GITHUB_USERNAME)
  --token TOKEN                  Github token used to authenticate with the Github REST API (environment variable = GITHUB_TOKEN)
  --repo REPO                    repo name (environment variable = GITHUB_DEFAULT_REPO)
  --pwd                          flag when if set will cause the script to derrive 'USER' and 'REPO' from the current working
```

> The `--pwd` flag will attempt to override both the environment variables and the passed arguments for the `USER` and `REPO` options
