#!/bin/bash

link=" https://bit.ly/Cluster5Eval-2S23-24"
output_image="qrcode.png"

# Generate QR code
qrencode -s 50 -o "$output_image" "$link"

echo "QR code generated for: $link"
echo "Image saved as: $output_image"
