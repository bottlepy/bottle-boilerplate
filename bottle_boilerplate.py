#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
from cookiecutter.main import cookiecutter


@click.group()
def cmds():
    pass


@cmds.command()
@click.argument('project_name', type=str)
def startproject(project_name):
    click.echo(u'Bottle Boilerplate start new project...')
    extra_context = {
        'project_name': project_name,
        "repo_name": "{{ cookiecutter.project_name|lower|replace(' ', '-') }}",
        "pkg_name": "{{ cookiecutter.repo_name|replace('-', '') }}"
    }
    cookiecutter(
        'https://github.com/avelino/cookiecutter-bottle.git',
        no_input=True,
        extra_context=extra_context)


@cmds.command()
@click.option('--version', type=str, default="dev",
              help=u'Set version to search!')
def doc(version):
    if version not in ["dev", "0.12", "0.11", "0.10", "0.9"]:
        version = "dev"
    url = 'http://bottlepy.org/docs/{}/'.format(version)
    click.launch(url)
    click.echo(u'Bottle Boilerplate start browser!')


def main():
    cmds()
