#!/usr/bin/env python3
# DESCRIPTION: Verilator: Verilog Test driver/expect definition
#
# Copyright 2024 by Wilson Snyder. This program is free software; you
# can redistribute it and/or modify it under the terms of either the GNU
# Lesser General Public License Version 3 or the Perl Artistic License
# Version 2.0.
# SPDX-License-Identifier: LGPL-3.0-only OR Artistic-2.0

import vltest_bootstrap

test.scenarios('dist')

root = ".."

if 'VERILATOR_TEST_NO_LINT_PY' in os.environ:
    test.skip("Skipping due to VERILATOR_TEST_NO_LINT_PY")
if not os.path.exists(root + "/.git"):
    test.skip("Not in a git repository")

test.run(cmd=["cd " + root + " && make lint-py"])

test.passes()