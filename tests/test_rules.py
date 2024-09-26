#!/usr/bin/env python

""" Check the rules
"""

import importlib.resources
import json
import re
from seabird import rules


def test_load_available_rules():
    """Try to read all available rules

    https://github.com/castelao/seabird/issues/7
    """
    rules_dir_path = importlib.resources.files(rules)
    rule_files = [entry.name for entry in rules_dir_path.iterdir() if entry.is_file()]
    rule_files = [f for f in rule_files if re.match("^(?!refnames).*json$", f)]
    for rule_file in rule_files:
        print("loading rule: %s", (rule_file))
        with importlib.resources.files(rules).joinpath(rule_file).open('r') as file:
            text = file.read()
        rule = json.loads(text)
        assert type(rule) == dict
        assert len(rule.keys()) > 0
