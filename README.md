Uses the same idea as described at https://www.mercurial-scm.org/wiki/DiffMerge
applied to SmartSynchronize on Windows.

Usage
=====

1. Copy smartsync.bat and smartsync.py to any directory, for example,
C:\Program Files\TortoiseHg

2. Add the following lines to mercurial.ini:

[merge-tools]
smartsync.executable = C:\Program Files\TortoiseHg\smartsync.bat
smartsync.args = $local $base $other
diffmerge.binary = False
diffmerge.symlinks = False
diffmerge.gui = True

After that a new 'smartsync' option will appear in the list of available 
3-way merge tools in TortoiseHg.

To assign it as the default option, use

[ui]
merge = smartsync
