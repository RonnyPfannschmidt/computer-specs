#! .hacks/python

import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('playbook', default='playbook/all.yml', nargs="?")


def main(args):
    subprocess.call([
        'ansible-playbook',
        '-i', "inventory/local.ini",
        args.playbook,
    ])


if __name__ == "__main__":
    main(parser.parse_args())
