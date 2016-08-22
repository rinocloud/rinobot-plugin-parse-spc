#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command line utility to convert .SPC files to .TXT

author: Rohan Isaac
"""
from __future__ import division, absolute_import, unicode_literals, print_function
import argparse
import os
import sys
from lib.spc import File
import ast
import yaml


def main(filepath):
    filename_without_ext = os.path.splitext(filepath)[0]
    delim = '\t'
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

    f.write_file(filename_without_ext + '.txt', delimiter=delim)
    with open(filename_without_ext + '.yaml', 'w') as outfile:
        dump_str = yaml.safe_dump(
            metadata,
            outfile,
            encoding='utf-8',
            allow_unicode=True,
            default_flow_style=False
        )

if __name__ == "__main__":
    main(sys.argv[1])
