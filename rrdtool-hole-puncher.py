#!/usr/bin/env python

"""
This file is licensed under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License. You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
"""

from pprint import pprint
import sys
assert sys.argv[1:], "Must specify hole start Unix timestamp in decimal"

iHoleStart = int(sys.argv[1])
iHoleEnd = int(time.time()) 
if sys.argv[2]:
    iHoleEnd = int(sys.argv[2])

for rLine in iter(sys.stdin.readline, ''):
    if "<lastupdate>" in rLine:
        # <lastupdate>1414782122</lastupdate> <!-- 2014-10-31 19:02:02 GMT -->
        _, _, rData = rLine.partition("<lastupdate>")
        rData, _, _ = rData.partition("</lastupdate")
        iLastUpdate = int(rData)
        assert iLastUpdate > iHoleStart, "Last update in RRD older than " \
                                    "the hole start you provided, nothing to do"
        if iLastUpdate < iHoleEnd:
            print "<lastupdate>{0}</lastupdate>".format(iMaxUpdate)
        else:
            print rLine,
    elif "<row>" in rLine:
        #<!-- 2016-12-08 19:50:00 CET / 1481223000 --> <row><v>9.8546654097e+05</v><v>5.3412737180e+04</v></row>
        date, _, _ = rLine.partition("<row>")
        _, _, rData = date.partition("/")
        rData, _, _ = rData.partition("--")
        rData = rData.strip()
        iUpdate = int(rData)
        if iUpdate < iHoleStart or iUpdate > iHoleEnd:
            print rLine,
        else:
            values = ''.join(['<v>NaN</v>'] * rLine.count('<v>'))
            print date + '<row>' + values + '</row>' + '<!-- data removed -->'
            sys.stderr.write("Ignoring line-: " + rLine)
    else:
        print rLine,
