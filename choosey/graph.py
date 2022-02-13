import textwrap
import random
import string
from inspect import signature

try:
    from . import actions
except ImportError:
    import actions


def graphlabel(val, width):
    return '\n'.join(textwrap.wrap(val, width=width))


def nodename(val):
    return '_'.join(val.lower().split())


def get_action_params():

    params = set()
    for name in dir(actions):
        if not name.startswith('_'):
            try:
                p = signature(getattr(actions, name)).parameters
            except TypeError:
                continue

            if 'game_data' in p:
                params |= set(p.keys())

    return params


def graph(game, label_width=12):

    action_params = get_action_params()

    lines = ['digraph G {']
    lines.append('edge [color=grey fontcolor=grey];')
    for step, d in game.items():
        fromname = nodename(step)
        nodelabel = graphlabel(step, width=label_width)
        if '_action' in d:
            nodelabel += '\n[{}]'.format(d['_action'])

        lines.append(f'{fromname} [ label="{nodelabel}" ];')

        for key, val in d.items():
            if key.startswith('_'):
                continue

            edgelabel = graphlabel(key, width=label_width)
            if val == '???':
                # if one of the options is '???', create a unique dummy node
                dummy = ''.join(random.choices(string.ascii_letters, k=6))
                lines.append(f'{dummy} [ label="???" ];')
                lines.append(f'"{fromname}" -> "{dummy}" [ label="{edgelabel}" ];')
            elif val in game or key not in action_params:
                toname = nodename(val)
                lines.append(f'"{fromname}" -> "{toname}" [ label="{edgelabel}" ];')

    lines.append('}\n')
    return '\n'.join(lines)
