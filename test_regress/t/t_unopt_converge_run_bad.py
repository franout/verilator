#!/usr/bin/env python3
# DESCRIPTION: Verilator: Verilog Test driver/expect definition
#
# Copyright 2024 by Wilson Snyder. This program is free software; you
# can redistribute it and/or modify it under the terms of either the GNU
# Lesser General Public License Version 3 or the Perl Artistic License
# Version 2.0.
# SPDX-License-Identifier: LGPL-3.0-only OR Artistic-2.0

import vltest_bootstrap

test.scenarios('simulator')
test.top_filename = "t/t_unopt_converge.v"

test.compile(v_flags2=['+define+ALLOW_UNOPT --output-split 0'])

if test.vlt_all:
    test.execute(fails=True, expect_filename=test.golden_filename)

test.passes()
