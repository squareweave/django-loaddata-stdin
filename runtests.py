#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.core.management import execute_from_command_line


def main():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'django_loaddata_stdin.tests.settings'
    if len(sys.argv) == 1:
        from django.test.utils import get_runner
        if django.VERSION >= (1, 7):
            django.setup()
        TestRunner = get_runner(settings)
        test_runner = TestRunner()
        failures = test_runner.run_tests(["django_loaddata_stdin.tests"])
        sys.exit(bool(failures))
    execute_from_command_line(sys.argv[:])

if __name__ == '__main__':
    main()
