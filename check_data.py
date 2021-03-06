'''
syntax:

from a command prompt:
python check_data.py raw rop con inl

from a Python interpreter:
import sys
sys.argv = [raw, rop, con, inl]
execfile("check_data.py")
'''

import argparse
import time

# gocomp imports
import data
    
def main():

    parser = argparse.ArgumentParser(description='Check data files for a problem instance')
    
    parser.add_argument('raw_in', help='raw_in')
    parser.add_argument('rop_in', help='rop_in')
    parser.add_argument('con_in', help='con_in')
    parser.add_argument('inl_in', help='inl_in')
    
    args = parser.parse_args()

    start_time = time.time()
    p = data.Data()
    p.read(args.raw_in, args.rop_in, args.inl_in, args.con_in)
    time_elapsed = time.time() - start_time
    print("read data time: %f" % time_elapsed)
    
    # show data stats
    print("buses: %u" % len(p.raw.buses))
    print("loads: %u" % len(p.raw.loads))
    print("fixed_shunts: %u" % len(p.raw.fixed_shunts))
    print("generators: %u" % len(p.raw.generators))
    print("nontransformer_branches: %u" % len(p.raw.nontransformer_branches))
    print("transformers: %u" % len(p.raw.transformers))
    print("areas: %u" % len(p.raw.areas))
    print("switched_shunts: %u" % len(p.raw.switched_shunts))
    print("generator inl records: %u" % len(p.inl.generator_inl_records))
    print("generator dispatch records: %u" % len(p.rop.generator_dispatch_records))
    print("active power dispatch records: %u" % len(p.rop.active_power_dispatch_records))
    print("piecewise linear cost functions: %u" % len(p.rop.piecewise_linear_cost_functions))
    print('contingencies: %u' % len(p.con.contingencies))

    start_time = time.time()
    p.check()
    time_elapsed = time.time() - start_time
    print("check data time: %f" % time_elapsed)

if __name__ == '__main__':
    main()
