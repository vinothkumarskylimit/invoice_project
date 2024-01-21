import pdf2jpg
from pdf2jpg import pdf2jpg
import os
import sys
import keras_ocr
import matplotlib.pyplot as plt
import tensorflow as tf
Source = "sample.pdf"
Destination = "output/"
Final = pdf2jpg.convert_pdf2jpg(  Source , Destination )
#print(Final)
image1=Final[0]['output_jpgfiles'][0]
#print(Final['output_jpgfiles'])


pipeline = keras_ocr.pipeline.Pipeline()
# Read images from folder path to image object
#images = [keras_ocr.tools.read(img) for img in [image1,'/content/text.jpeg']]
images = keras_ocr.tools.read(image1)

# generate text predictions from the images
prediction_groups = pipeline.recognize([images])
predicted_image = prediction_groups[0]

for text, box in predicted_image:
    print(text)
