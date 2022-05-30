#!/bin/bash
#-----------------------------------------------------------------
# process_folder.sh    v1.0
# 2022.05.25
#
# Parameters:
# $1: path to the folder with .jp2 images
# $2: [optional] path to the output folder (default is $1_out)
#-----------------------------------------------------------------

folder=$1
# Check if the folder exists
if [ ! -d "$folder" ]; then
    printf "Error: '%s' folder not found.\n" "$folder" >&2
    exit 1
fi

# Check if the folder has .jp2 files
files=(`find "$folder" -maxdepth 1 -name "*.jp2"`)
if [ ${#files[@]} -eq 0 ]; then
    printf "Error: '%s' folder doesn't have .jp2 files.\n" "$folder" >&2
    exit 1
fi

# If no second argument provided, set default value for outdir
if [ -z "$2" ]; then
    outdir=${folder}_out
    printf "Info: No second argument provided, setting output dir as '%s'\n" "$outdir"
else
    outdir=$2
fi

mkdir -p ${outdir}
for file in ${files[@]}; do
    filename=${file#"$folder"}
    printf "Processing '%s'... " "$file"
    ./jp2_to_tiff.sh ${file} ${outdir%%/}/${filename%%.jp2}.tiff
    printf "done.\n"
done
