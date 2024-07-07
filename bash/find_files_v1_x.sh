#!/bin/bash
shopt -s globstar
for p;do
for f in $p;do
echo "$f"
done
done