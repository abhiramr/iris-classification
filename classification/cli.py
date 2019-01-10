"""
Hallmark Command Line 
------------------

"""
import os
import sys
from texttable import Texttable
import click

from . import classify 

@click.group()
def main():
    """ 
    Commandline for Iris Specifications 
    """
    pass


@main.group("schema")
def schema():
    """
    Discovery and operation specification formats
    """
    pass 


@schema.command("list")
def _schema_list():
    """
    List available schemas 
    """

    parser = spec.parser() 
    summary = parser.schema_list()
    table = Texttable()
    table.add_rows(summary)
    print(table.draw())