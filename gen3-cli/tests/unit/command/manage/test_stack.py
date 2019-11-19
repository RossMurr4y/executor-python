import collections
from unittest import mock
from click.testing import CliRunner
from cot.command.manage.stack import stack as manage_stack
from tests.unit.command.test_option_generation import run_options_test, run_validatable_option_test


ALL_VALID_OPTIONS = collections.OrderedDict()
ALL_VALID_OPTIONS['!-u,--deployment-unit'] = 'unit'
ALL_VALID_OPTIONS['!-l,--level'] = [
    'account',
    'product',
    'segment',
    'solution',
    'application',
    'multiple'
]
ALL_VALID_OPTIONS['-d,--delete'] = [True, False]
ALL_VALID_OPTIONS['-i,--stack-initiate'] = [True, False]
ALL_VALID_OPTIONS['-m,--stack-monitor'] = [True, False]
ALL_VALID_OPTIONS['-n,--stack-name'] = 'name'
ALL_VALID_OPTIONS['-r,--region'] = 'region'
ALL_VALID_OPTIONS['-w,--stack-wait'] = 10
ALL_VALID_OPTIONS['-z,--deployment-unit-subset'] = 'subset'
ALL_VALID_OPTIONS['-y,--dryrun'] = [True, False]


@mock.patch('cot.command.manage.stack.subprocess')
def test_input_valid(subprocess_mock):
    run_options_test(CliRunner(), manage_stack, ALL_VALID_OPTIONS, subprocess_mock)


@mock.patch('cot.command.manage.stack.subprocess')
def test_input_validation(subprocess_mock):
    runner = CliRunner()
    run_validatable_option_test(
        runner,
        manage_stack,
        subprocess_mock,
        {
            '-u': 'unit',
            '-l': 'segment'
        },
        [
            ('-l', 'badlevelvalue', 'segment'),
            ('-w', 'not_an_int', 10)
        ]
    )