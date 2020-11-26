# -*- coding:utf-8 -*-
#
# Copyright 2015 Hewlett-Packard Development Company, L.P.
#
# SPDX-License-Identifier: Apache-2.0


import bandit
from bandit.core import test_properties as test


@test.test_id('B324')
@test.checks('Call')
def close_file(context):
    if context.call_function_name_qual.endswith('.close'):
        return bandit.Issue(
                    severity=bandit.HIGH,
                    confidence=bandit.MEDIUM,
                    text="close_file",
                    lineno=context.get_lineno_for_call_arg('debug'),
                )
