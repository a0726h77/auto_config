#! /usr/bin/env python
from common.dir_operator import get_home_dir, make_link
import os.path


source = 'awesome/rc.lua'
target = os.path.join(get_home_dir(), '.config', source)
print make_link(source, target)


source = 'awesome/init_awesome.py'
target = os.path.join(get_home_dir(), '.config', source)
print make_link(source, target)

print make_link(source, target)
print 'Please install konsole or change terminal value in rc.lua.'
print 'Please install dmenu.'

