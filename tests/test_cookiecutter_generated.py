#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `cookiecutter_generated` package."""


import unittest
from click.testing import CliRunner

from cookiecutter_generated import cookiecutter_generated
from cookiecutter_generated import cli


class TestCookiecutter_generated(unittest.TestCase):
    """Tests for `cookiecutter_generated` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'cookiecutter_generated.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
