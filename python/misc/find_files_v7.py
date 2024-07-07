import sys,glob
for w in sys.argv[1:]:[print(f)for f in glob.glob(w,recursive=True)]