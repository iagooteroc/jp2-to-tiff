
# Convert .jp2 images to .tiff

## If you're using ft2 instead of ft3, load cesga/2020

```
module load cesga/2020
```

## Load Singularity module

```
module load singularity/3.9.7
```

## To process all the files in a folder:

```
singularity exec docker://iagooteroc/image-processing:1.0 ./process_folder.sh FOLDERNAME
```

## They will be generated in a new folder named FOLDERNAME_OUT or you can specify where like:

```
singularity exec docker://iagooteroc/image-processing:1.0 ./process_folder.sh FOLDERNAME OUTDIRNAME 
```

## If you only want to process one file, you can also do it like this:

```
singularity exec docker://iagooteroc/image-processing:1.0 ./jp2_to_tiff.sh FILENAME.jp2 FILENAME.tiff
```

## If something fails, it may be because some script is missing. 
## Make sure all of these are in the same folder:

```
jp2_to_tiff.sh
process_folder.sh
to_tiff.py
```
