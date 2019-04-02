#! .hacks/python

import subprocess
import click


@click.command()
@click.argument('playbooks', type=click.Path(exists=True, dir_okay=False), nargs=-1)
def main(playbooks):
    subprocess.call([
        'ansible-playbook',
        '-i', "inventory/local.ini",
    ] + list(playbooks or ["playbook/all.yml"]))


if __name__ == "__main__":
    main()
