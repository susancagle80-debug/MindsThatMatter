#!/usr/bin/env python3
"""
Minds CLI - Command line interface for MindsThatMatter
"""

import click


@click.group()
def cli():
    """Main CLI group"""
    pass


@cli.command()
def setup():
    """Setup command"""
    click.echo("Setting up...")
    # Add setup logic here


@cli.command()
def build_check():
    """Build & syntax verification"""
    click.echo("Running build check...")
    # Add build check logic here


@cli.command()
@click.option('--query', help='Research query')
def research(query):
    """Test Agent Codebase Research"""
    click.echo(f"Researching: {query}")
    # Add research logic here


@cli.command()
def test_oracle():
    """Check Oracle Webhook Status"""
    click.echo("Testing Oracle webhook...")
    # Add Oracle test logic here


if __name__ == '__main__':
    cli()
