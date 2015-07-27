#!/usr/bin/env python

import i3
outputs = i3.get_outputs()

# set current workspace to output 0
i3.workspace(outputs[0]['current_workspace'])

# ..and move it to the other output.
# outputs wrap, so the right of the right is left ;)
i3.move__workspace__to__output__left()
