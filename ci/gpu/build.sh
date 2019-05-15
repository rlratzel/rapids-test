#!/bin/bash
#!/bin/bash

# CI build (and test) script. Executed from a clean gpuCI
# environment. Install all required packages here then add commands to
# execute build and optionally test.
#
# Unlike cpu/build.sh, this is executed on a machine with GPUs (no
# guarantee they are appropriate, check for that upfront!). The
# intention is that test that need GPUs shoul dbe run using this
# script.

