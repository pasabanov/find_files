import sys,glob
for w in sys.argv[1:]:print(*glob.glob(w),sep='\n')