#!/usr/bin/python3

import sys
import pyvips


im = pyvips.Image.new_from_file(sys.argv[1])

# openslide will add an alpha ... drop it
if im.hasalpha():
    im = im[:-1]

image_height = im.height
image_bands = im.bands

# split to separate image planes and stack vertically ready for OME 
# im = pyvips.Image.arrayjoin(im.bandsplit(), across=1)

# set minimal OME metadata
# before we can modify an image (set metadata in this case), we must take a 
# private copy
im = im.copy()
im.set_type(pyvips.GValue.gint_type, "page-height", image_height)
im.set_type(pyvips.GValue.gstr_type, "image-description",
f"""<?xml version="1.0" encoding="UTF-8"?>
<OME xmlns="http://www.openmicroscopy.org/Schemas/OME/2016-06"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.openmicroscopy.org/Schemas/OME/2016-06 http://www.openmicroscopy.org/Schemas/OME/2016-06/ome.xsd">
    <Image ID="Image:0">
        <!-- Fields about image dimensions -->
        <Pixels DimensionOrder="XYCZT"
                BigEndian="true"
                Interleaved="true"
                SignificantBits="8"
                ID="Pixels:0"
                SizeC="{image_bands}"
                SizeT="1"
                SizeX="{im.width}"
                SizeY="{image_height}"
                SizeZ="1"
                Type="uint8">
        </Pixels>
        <Channel ID="Channel:0:0" SamplesPerPixel="3">
        </Channel>
    </Image>
</OME>""")

im.tiffsave(sys.argv[2], compression="jp2k", tile=True,
            tile_width=512, tile_height=512,
            pyramid=True, rgbjpeg=True, subifd=True)
