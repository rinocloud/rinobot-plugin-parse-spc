from __future__ import division, absolute_import, unicode_literals, print_function
import rinobot_plugin as bot
import argparse
import os
import sys
from lib.spc import File
import ast
import yaml


def main():
    filepath = bot.filepath()
    f = File(filepath)

    metadata = {
        'xlabel': f.xlabel,
        'ylabel': f.ylabel,
        'zlabel': f.zlabel,
        'exp_type': f.exp_type,
    }

    for bytes_ob in f.log_other:
        s = bytes_ob.decode("utf-8")
        if ':' in s:
            x, y = s.split(':')
            try:
                y = ast.literal_eval(y.strip())
            except:
                y = y.strip()
            metadata[x.strip()] = y

    outname = bot.no_extension() + '-spc-converted.txt'
    outpath = bot.output_filepath(outname)

    f.write_file(outpath, delimiter=',')
    with open(outpath + '.yaml', 'w') as outfile:
        dump_str = yaml.safe_dump(
            metadata,
            outfile,
            encoding='utf-8',
            allow_unicode=True,
            default_flow_style=False
        )

if __name__ == "__main__":
    main()
