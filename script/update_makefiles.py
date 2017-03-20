#
# Copyright (C) 2017 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Updates .bp, .mk, .xml files under test/vts-testcase/fuzz.

Among files affected are:
Build rules:
1. test/vts-testcase/fuzz/func_fuzzerAndroid.bp
2. files matching: test/vts-testcase/fuzz/func_fuzzer/Android.bp
3. files matching: test/vts-testcase/fuzz/func_fuzzer/<hal_name>/<hal_version>/Android.bp

Config Files:
1. files matching: test/vts-testcase/fuzz/<hal_name>/<hal_version>/func_fuzzer/Android.mk
2. files matching: test/vts-testcase/fuzz/<hal_name>/<hal_version>/func_fuzzer/AndroidTest.xml

Usage:
    python test/vts-testcase/fuzz/update_makefiles.py
"""

import argparse
import os
import sys

from build.func_fuzzer_build_rule_gen import FuncFuzzerBuildRuleGen
from config.config_gen import ConfigGen

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--build',
        dest='build',
        action='store_true',
        required=False,
        help='Whether to create update build rules.')

    parser.add_argument(
        '--config',
        dest='config',
        action='store_true',
        required=False,
        help='Whether to create update config files.')
    args = parser.parse_args()

    if not args.build and not args.config:
        print 'Updating build rules and config files.'
        args.build = True
        args.config = True

    if args.build:
        print 'Updating build rules.'
        warning_header = (
            '// This file was auto-generated by test/vts-testcase/fuzz/script/update_makefiles.py.\n'
            '// Do not edit manually.\n')
        build_rule_gen = FuncFuzzerBuildRuleGen(warning_header)
        build_rule_gen.UpdateBuildRule()

    if args.config:
        print 'Updating config files.'
        config_gen = ConfigGen()
        config_gen.UpdateFuncFuzzerConfigs()
