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
# TODO: Figure out grouping from https://docs.python.org/3/howto/regex.html#grouping
#
test_in = r'''
DEBUG Instr: ADD x4, x4, x5, cid=0, wid=0, tmask=1111, PC=0x80000138 (#17)
DEBUG Src0 Reg: x4={0x8000728c, 0x8000728c, 0x8000728c, 0x8000728c}
DEBUG Src1 Reg: x5={0x0, 0x1c, 0x38, 0x54}
DEBUG Dest Reg: x4={0x8000728c, 0x800072a8, 0x800072c4, 0x800072e0}
DEBUG Instr: ADD x4, x4, x5, cid=0, wid=3, tmask=1111, PC=0x80000138 (#12884901901)
DEBUG Src0 Reg: x4={0x8000728c, 0x8000728c, 0x8000728c, 0x8000728c}
DEBUG Src1 Reg: x5={0x150, 0x16c, 0x188, 0x1a4}
DEBUG Dest Reg: x4={0x800073dc, 0x800073f8, 0x80007414, 0x80007430}
DEBUG Instr: JALR x0, x1, 0x0, cid=0, wid=0, tmask=1111, PC=0x8000013c (#18)
DEBUG Src0 Reg: x1={0x8000001c, 0x8000001c, 0x8000001c, 0x8000001c}
DEBUG Instr: JALR x0, x1, 0x0, cid=0, wid=1, tmask=1111, PC=0x8000013c (#4294967310)
DEBUG Src0 Reg: x1={0x8000014c, 0x8000014c, 0x8000014c, 0x8000014c}
DEBUG Instr: ADDI x5, x0, 0x1, cid=0, wid=0, tmask=1111, PC=0x8000001c (#19)
DEBUG Src0 Reg: x0={0x0, 0x0, 0x0, 0x0}
DEBUG Dest Reg: x5={0x1, 0x1, 0x1, 0x1}
'''

op_delim = "DEBUG Instr: "
aaa = """
DEBUG Instr: ADD x4, x4, x5, cid=0, wid=0, tmask=1111, PC=0x80000138 (#17)
DEBUG Src0 Reg: x4={0x8000728c, 0x8000728c, 0x8000728c, 0x8000728c}
DEBUG Src1 Reg: x5={0x0, 0x1c, 0x38, 0x54}
DEBUG Dest Reg: x4={0x8000728c, 0x800072a8, 0x800072c4, 0x800072e0}
"""
def parse(template, regex, text):
    print(text)
    print(type(text))
    m = re.search(regex, text)
    print(type(m))
    print(m.groupdict())
    return m.groupdict()

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
    op_pattern = re.compile(r'''
DEBUG Instr: (?P<instr>\w+) .* cid=(?P<cid>\d), wid=(?P<wid>\d), tmask=(?P<tmask>\d+), .*
(DEBUG Src0 Reg: x\d=(?P<src_0>\{.*\}))?
(DEBUG Src1 Reg: x\d=(?P<src_1>\{.*\}))?
(DEBUG Dest Reg: x\d=(?P<dest>\{.*\}))?
''')
    with open("run.log", 'r') as log:
        log_content = log.read()

        # parse(out, op_pattern, test_in)
        op_block = [(op_delim + x) for x in test_in.split(op_delim)][1]
        parse(out, op_pattern, op_block)
        # instructions = [
        #     parse(out, op_pattern, instr)
        #     for instr in [
        #         op_delim+x for x in test_in.split(op_delim)
        #     ][1]
        # ]
        print(*instructions, sep="\n")

