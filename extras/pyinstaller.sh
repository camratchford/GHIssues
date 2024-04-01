#!/bin/bash

if ! [ $(which pyinstaller) ]; then
  echo "pyinstaller not found in PATH"
  exit 1
fi

function BuildPyinstallerExe() {
  EXE_NAME="$1"
  INCLUDE_PATHS="$2"
  SUB_MODULES="$3"
  PYTHON_SCRIPT="$4"
  CWD="$5"
  cd "$CWD"
  pyinstaller -y --clean --onefile \
        --name="$EXE_NAME" \
        --paths="$INCLUDE_PATHS" \
        --collect-submodules="$SUB_MODULES" \
        "../$PYTHON_SCRIPT"
}

SCRIPT_DIR="$(dirname $(realpath $0))"
cd "$SCRIPT_DIR"

INCLUDE_PATH="$(realpath $SCRIPT_DIR/../gh_issues)"
SUB_MODULES="gh_issues"
BuildPyinstallerExe \
  ghissues-get \
  "$INCLUDE_PATH" \
  "$SUB_MODULES" \
  "get_issues.py" \
  "$SCIRPT_DIR"


BuildPyinstallerExe \
  ghissues-new \
  "$INCLUDE_PATH" \
  "$SUB_MODULES" \
  "new_issue.py" \
  "$SCRIPT_DIR"
