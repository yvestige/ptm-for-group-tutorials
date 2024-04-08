#!/bin/bash

link="https://github.com/Yves242/ptm-for-group-tutorials"
output_image="qrcode.png"

# Generate QR code
qrencode -s 50 -o "$output_image" "$link"

echo "QR code generated for: $link"
echo "Image saved as: $output_image"
