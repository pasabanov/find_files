#!/bin/bash
shopt -s globstar nullglob;for p;{ for f in $p;{ echo "$f";};}