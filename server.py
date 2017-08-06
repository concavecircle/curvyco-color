import numpy as np
import cv2
from flask import Flask
from boto import S3Connection
from color_detection import detect


app = Flask(__name__)
s3_bucket = ''


def get_image(name):
	

@app.route('/<s3_path>'):
def get_color(s3_path):
    np_image = get_image(s3_path)
	return detect(np_image)


if __name__ == "__main__":
    app.run()
