#!/usr/bin/env python
# Copyright 2013 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from tests.unit import BaseAWSCommandParamsTest
import re


class TestWebsiteCommand(BaseAWSCommandParamsTest):

    prefix = 's3 website '

    def test_index_document(self):
        cmdline = self.prefix + 's3://mybucket --index-document index.html'
        result = {'uri_params': {'Bucket': 'mybucket'},
                  'headers': {},}
        self.assert_params_for_cmd(cmdline, result, ignore_params=['payload'])
        self.assertEqual(
            self.last_kwargs,
            {'website_configuration': {'IndexDocument': {'Suffix': 'index.html'}},
             'bucket': u'mybucket'})

    def test_error_document(self):
        cmdline = self.prefix + 's3://mybucket --error-document mykey'
        result = {'uri_params': {'Bucket': 'mybucket'},
                  'headers': {},}
        self.assert_params_for_cmd(cmdline, result, ignore_params=['payload'])
        self.assertEqual(
            self.last_kwargs,
            {'website_configuration': {'ErrorDocument': {'Key': 'mykey'}},
             'bucket': u'mybucket'})


if __name__ == "__main__":
    unittest.main()
