#! /usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pandas",
#     "numpy", 
# ]
# ///
import pandas as pd
import numpy as np
import re

op_pattern = re.compile(r'''
^DEBUG\sInstr:\s+(?P<instr>\S+)
.*?
cid=(?P<cid>\d),\s*
wid=(?P<wid>\d),\s*
tmask=(?P<tmask>\d+),.*?$
(?:
    \n^DEBUG\s+Src0\s+Reg:\s+x\d+=(?P<src_0>\{.*?\})
)?
(?:
    \n^DEBUG\s+Src1\s+Reg:\s+x\d+=(?P<src_1>\{.*?\})
)?
(?:
    \n^DEBUG\s+Dest\s+Reg:\s+x\d+=(?P<dest>\{.*?\})
)?
''', re.MULTILINE | re.VERBOSE)



# TODO: Figure out grouping from https://docs.python.org/3/howto/regex.html#grouping
#
if __name__ == "__main__":
    out = pd.DataFrame(
        columns = [
            "Instruction",
            "cid",
            "wid",
            "tmask",
            "src 0",
            "src 1",
            "dest"
        ]
    )
    with open("run.log", 'r') as log:
        log_content = log.read()
        print(
              *[
                  m.groupdict()
                  for m in op_pattern.finditer(log_content)
              ],
              sep="\n\n"
          )
