#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module to build home page for TOIs"""
import glob
import os
import sys

NOTEBOOK_LOCATION = f"notebooks/{version}/*.ipynb"


def main():
    version = sys.argv[1].strip()
    notebook_files = glob.glob(NOTEBOOK_LOCATION.format(version=version))
    lines = []
    for filename in sorted(notebook_files):
        toi = int(os.path.splitext(os.path.split(filename)[1])[0].split("-")[1])
        lines.append('<li><a href="toi-{0}.html">TOI {0}</a></li>'.format(toi))

    with open("../docs/notebooks/index.html.tpl", "r") as f:
        txt = f.read()

    txt = txt.replace("{{{VERSION}}}", version)
    txt = txt.replace("{{{TOILIST}}}", "\n".join(lines))
    with open("../docs/notebooks/{0}/index.html".format(version), "w") as f:
        f.write(txt)


if __name__ == "__main__":
    main()
