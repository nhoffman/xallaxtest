import textwrap
import random
import string
from inspect import signature

try:
    from . import actions
except ImportError:
    import actions


def graphlabel(val, width=12):
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


def graph(game):

    action_params = get_action_params()

    lines = ['digraph G {']
    lines.append('edge [color=grey fontcolor=grey];')
    for step, d in game.items():
        fromname = nodename(step)
        nodelabel = graphlabel(step)
        if '_action' in d:
            nodelabel += '\n[{}]'.format(d['_action'])

        lines.append(f'{fromname} [ label="{nodelabel}" ];')

        for key, val in d.items():
            if val == '???':
                # create a unique dummy node for each ???
                toname = ''.join(random.choices(string.ascii_letters, k=6))
                lines.append(f'{toname} [ label="???" color=red ];')
            elif val in game:
                toname = nodename(val)
            elif not (key in action_params or key.startswith('_')):
                # assume this is a node without a defined step
                toname = nodename(val)
                # add another node definition
                nodelabel = graphlabel(val) + '\n[step not defined]'
                lines.append(f'{toname} [ label="{nodelabel}" color=red ];')
            else:
                continue

            edgelabel = graphlabel(key)
            lines.append(f'"{fromname}" -> "{toname}" [ label="{edgelabel}" ];')

    lines.append('}\n')
    return '\n'.join(lines)
