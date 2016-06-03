"""
Test command.
"""

from mock import patch

from django.test import TestCase
from django.utils.six import BytesIO
from django.core.management import execute_from_command_line

from django_loaddata_stdin.tests.testapp.models import CharModel

YAML_FIXTURE = b"""
- fields: {field: a}
  model: testapp.charmodel
  pk: 1
"""


@patch('django_loaddata_stdin.management.commands.loaddata.sys.stdin',
       BytesIO(YAML_FIXTURE))
class LoadDataTest(TestCase):
    """Test command."""

    def test_command(self):
        """Test loading data from stdin"""
        argv = ['', 'loaddata', '--format=yaml', '-']
        execute_from_command_line(argv)
        self.assertTrue(CharModel.objects.exists())
