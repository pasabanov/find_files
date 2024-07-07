#!/usr/bin/env python3
import sys,glob
for w in sys.argv[1:]:print(*glob.glob(w,recursive=True),sep='\n')