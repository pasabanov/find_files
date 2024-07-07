#!/usr/bin/env python3
import sys,glob;[print(f)for w in sys.argv[1:]for f in glob.glob(w,recursive=True)]