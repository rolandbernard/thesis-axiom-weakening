# The notes are exported from Notion and cleand up using this script.

import re
import sys
from pathlib import Path


def rename(file: Path):
    filename = file.stem
    match = re.match('(.*) [0-9a-f]{32}', filename)
    if match:
        file.rename(file.parent.joinpath(match.group(1) + file.suffix))


def filterContent(file: Path):
    content = file.read_text()
    content = re.sub('\\(https://www.notion.so/[^\\)]*\\)', '()', content)
    content = re.sub('%20[0-9a-f]{32}', '', content)
    content = content.replace('****', '')
    content = content.replace('’', '\'')
    content = content.replace('\\lang', '\\langle')
    content = content.replace('\\rang', '\\rangle')
    content = content.replace('\\Beta', 'B')
    if content[-1] != '\n':
        content += '\n'
    file.write_text(content)


def recursiveCleanup(file: Path):
    if file.is_dir():
        for child in file.iterdir():
            recursiveCleanup(child)
    else:
        filterContent(file)
    rename(file)


recursiveCleanup(Path(sys.argv[1]))
