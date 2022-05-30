#!/bin/bash

input=$1
output=$2

python3 to_tiff.py "$input" "$output"

# Photometric interpretation (RGB):
tiffset -s 262 2 "$output"
# Samples/Pixel (3):
tiffset -s 277 3 "$output"
