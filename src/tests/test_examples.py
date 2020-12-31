import os
import glob
import subprocess

import pytest

thisfile = os.path.abspath(__file__)
thisdir = os.path.dirname(thisfile)
topdir = os.path.dirname(os.path.dirname(thisdir))
exdir = os.path.join(topdir, "examples")
examples = []
examples.extend(glob.glob(os.path.join(exdir, "*.py")))
baselinedir = os.path.join(thisdir, "example_baselines")

assert os.path.exists(exdir)
assert thisfile not in examples

tdict = {}
for fname in examples:
    basename = os.path.basename(fname)
    assert basename.endswith(".py")
    assert len(basename) >= 3
    basename = basename[:-3]
    tname = "test_" + basename
    tdict[tname] = fname
assert len(tdict) == len(examples)


@pytest.mark.parametrize(("example_name"), sorted(tdict))
def test_example(example_name):
    filename = tdict[example_name]
    cmd = ["python", filename]
    assert os.path.exists(filename)
    subprocess.check_call(cmd)
