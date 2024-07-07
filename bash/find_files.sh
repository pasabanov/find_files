shopt -s globstar
for p;do
for f in $p;do
realpath "$f"
done
done