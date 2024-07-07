#!/usr/bin/env python3
import sys,glob;[print(*glob.glob(w,recursive=True),sep='\n')for w in sys.argv[1:]]