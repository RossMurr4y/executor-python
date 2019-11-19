import os
import collections
from unittest import mock
from click.testing import CliRunner
from cot.command.create.reference import reference as create_reference
from tests.unit.command.test_option_generation import run_options_test, run_validatable_option_test

ALL_VALID_OPTIONS = collections.OrderedDict()
ALL_VALID_OPTIONS['!-t,--reference-type'] = 'type'
ALL_VALID_OPTIONS['-o,--reference-output-dir'] = 'output_dir'


@mock.patch('cot.command.create.reference.subprocess')
def test_input_valid(subprocess_mock):
    runner = CliRunner()
    with runner.isolated_filesystem():
        os.mkdir('output_dir')
        run_options_test(runner, create_reference, ALL_VALID_OPTIONS, subprocess_mock)


@mock.patch('cot.command.create.reference.subprocess')
def test_input_validation(subprocess_mock):
    runner = CliRunner()
    with runner.isolated_filesystem():
        os.mkdir('output_dir')
        run_validatable_option_test(
            runner,
            create_reference,
            subprocess_mock,
            {
                '-t': 'type'
            },
            [
                ('-o', 'not_existing_dir', 'output_dir')
            ]
        )