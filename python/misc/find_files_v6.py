import sys,glob
for w in sys.argv[1:]:print('\n'.join(glob.glob(w,recursive=True)))