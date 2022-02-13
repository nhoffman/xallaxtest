import textwrap
import random
import string


def graphlabel(val, width):
    return '\n'.join(textwrap.wrap(val, width=width))


def nodename(val):
    return '_'.join(val.lower().split())


def graph(game, label_width=12):
    lines = ['digraph {']
    for step, d in game.items():
        fromname = nodename(step)
        nodelabel = graphlabel(step, width=label_width)
        if '_action' in d:
            nodelabel += '\n[{}]'.format(d['_action'])

        lines.append(f'{fromname} [ label="{nodelabel}" ];')
        # if one of the options is '???', create a dummy node to connect to
        if '???' in d.values():
            dummy = ''.join(random.choices(string.ascii_letters, k=6))
            lines.append(f'{dummy} [ label="???" ];')

        for key, val in d.items():
            edgelabel = graphlabel(key, width=label_width)
            if val in game:
                toname = nodename(val)
                lines.append(f'"{fromname}" -> "{toname}" [ label="{edgelabel}" '
                             'color=grey fontcolor=grey];')
            elif val == '???':
                lines.append(f'"{fromname}" -> "{dummy}" [ label="{edgelabel}" '
                             'color=grey fontcolor=grey];')

    lines.append('}\n')
    return '\n'.join(lines)
