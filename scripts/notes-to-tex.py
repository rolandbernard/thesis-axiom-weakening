# The notes are exported from Notion and cleand up using this script.

import re
import sys
from pathlib import Path


def generateLabel(name: str):
    label = re.sub('[^a-zA-Z0-9_]+', '-', name.lower())
    return f'\\label{{{label}}}'


def indentText(text: str, level: int, skip_first=False):
    indent = '    ' * level
    lines = []
    for i, line in enumerate(text.split('\n')):
        if (not skip_first or i != 0) and line:
            lines.append(indent + line)
        else:
            lines.append(line)
    return '\n'.join(lines)


def convertListItems(items: list[str]):
    result = []
    for i, item in enumerate(items):
        lines = item.split('\n')
        itm = [convertInline(lines[0])]
        tmp = []
        for line in lines[1:]:
            if line[:4] == '    ':
                tmp.append(line[4:])
            else:
                itm.append(convertInline(line))
                itm.append(convertMd('\n'.join(tmp)))
                tmp = []
        if tmp:
            itm.append(convertMd('\n'.join(tmp)))
        if len(itm) > 1 and i != len(items) - 1:
            itm.append('')
        result.append('\n'.join(itm))
    return result


def convertInline(text: str):
    active = {}
    output = []
    idx = 0
    while idx < len(text):
        match text[idx]:
            case '~' if text[idx + 1] == '~':
                idx += 2
                if 'sout' in active:
                    output.append('}')
                    del active['sout']
                else:
                    active['sout'] = True
                    output.append('\\sout{')
            case '*' | '_':
                if idx + 1 < len(text) and text[idx + 1] == text[idx]:
                    idx += 2
                    if 'bf' in active:
                        output.append('}')
                        del active['bf']
                    else:
                        active['bf'] = True
                        output.append('\\textbf{')
                else:
                    idx += 1
                    if 'it' in active:
                        output.append('}')
                        del active['it']
                    else:
                        active['it'] = True
                        output.append('\\emph{')
            case '$':
                output.append(text[idx])
                idx += 1
                while idx + 1 < len(text) and text[idx] != '$':
                    output.append(text[idx])
                    idx += 1
                output.append(text[idx])
                idx += 1
            case '[':
                name = []
                idx += 1
                while idx < len(text) and text[idx] != ']':
                    name.append(text[idx])
                    idx += 1
                idx += 1
                link = []
                if idx < len(text) and text[idx] == '(':
                    idx += 1
                    while idx < len(text) and text[idx] != ')':
                        link.append(text[idx])
                        idx += 1
                    idx += 1
                output.append(f'\\href{{{"".join(link)}}}{{{"".join(name)}}}')
            case '\\':
                output.append(text[idx + 1])
                idx += 2
            case '`':
                output.append('\\lstinline{')
                idx += 1
                while idx + 1 < len(text) and text[idx] != '`':
                    output.append(text[idx])
                    idx += 1
                output.append('}')
                idx += 1
            case c:
                output.append(c)
                idx += 1
    for _ in active:
        output.append('}')
    return ''.join(output)


def convertMd(md: str):
    blocks = [block for block in re.split('\n{2,}', md.strip())]
    tex = []
    for block in blocks:
        if block[:4] == '### ':
            name = block[4:].strip()
            tex.append(f'\\subsubsection{{{name}}} {generateLabel(name)}')
        elif block[:3] == '## ':
            name = block[3:].strip()
            tex.append(f'\\subsection{{{name}}} {generateLabel(name)}')
        elif block[:2] == '# ':
            name = block[2:].strip()
            tex.append(f'\\section{{{name}}} {generateLabel(name)}')
        elif block[:2] == '- ':
            items = convertListItems(block[2:].split('\n- '))
            tex.append('\n'.join([
                f'\\begin{{itemize}}',
                *(f'    \\item {indentText(item, 2, True)}' for item in items),
                f'\\end{{itemize}}',
            ]))
        elif re.match('^[0-9]+. ', block):
            trimed = re.sub('^[0-9]+. ', '', block)
            items = convertListItems(re.split('\n[0-9]+. ', trimed))
            tex.append('\n'.join([
                f'\\begin{{enumerate}}',
                *(f'    \\item {indentText(item, 2, True)}' for item in items),
                f'\\end{{enumerate}}',
            ]))
        elif block[:3] == '```':
            lines = block.split('\n')
            assert lines[-1] == '```'
            lang = lines[0][3:].strip().capitalize()
            tex.append('\n'.join([
                f'\\begin{{lstlisting}}[language={lang}]',
                *lines[1:-1],
                f'\\end{{lstlisting}}',
            ]))
        elif block[:2] == '$$':
            lines = ''.join(block[2:].split('\n')[1:-1]).split('\\\\')
            tex.append('\n'.join([
                f'\\begin{{align*}}',
                *(indentText(line.strip().rstrip('\\') + ' \\\\', 1)
                  for line in lines),
                f'\\end{{align*}}',
            ]))
        elif block[:1] == '|':
            rows = [
                [cell.strip()
                 for cell in row.strip().rstrip('\\').strip('|').split('|')]
                for row in block.split('\n')
            ]
            tex.append('\n'.join([
                f'\\begin{{tabular}}{{{"|".join("l" * len(rows[0]))}}}',
                *(indentText(
                    ' & '.join(map(convertInline, row)) + ' \\\\'
                    if row[0] != '---' else '\\hline', 1
                ) for row in rows),
                f'\\end{{tabular}}',
            ]))
        else:
            tex.append('\\\n'.join(convertInline(line)
                       for line in block.split('\n')))
    return '\n\n'.join(tex)


def convertContent(src: Path, dst: Path):
    dst.write_text(convertMd(src.read_text()))


def recursiveConversion(src: Path, dst: Path):
    if src.is_dir():
        if not dst.exists():
            dst.mkdir()
        for child in src.iterdir():
            recursiveConversion(child, dst.joinpath(child.name))
    elif src.suffix == '.md':
        convertContent(src, dst.parent.joinpath(dst.stem + '.tex'))


recursiveConversion(Path(sys.argv[1]), Path(sys.argv[2]))
