"""
Extension for loaddata
"""
from future.builtins import super

import sys

from django.core.management.commands import loaddata
from django.core.management.base import CommandError


class Command(loaddata.Command):
    """
    Extension for loaddata to allow reading from stdin
    """

    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument('--format', action='store',
                            dest='format', default=None,
                            help="Format when reading stdin")

    def handle(self, *args, **options):
        self.format = options.get('format')

        return super().handle(*args, **options)

    def parse_name(self, fixture_name):
        self.compression_formats['stdin'] = (lambda x, y: sys.stdin, None)

        if fixture_name == '-':
            if not self.format:
                raise CommandError(
                    "Must specify format when reading from stdin")

            return '-', self.format, 'stdin'
        else:
            return super().parse_name(fixture_name)

    def find_fixtures(self, fixture_label):
        if fixture_label == '-':
            return [('-', None, '-')]

        return super().find_fixtures(fixture_label)
