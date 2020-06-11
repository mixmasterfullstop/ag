from flask import Flask, send_from_directory, jsonify, request
from flask_cors import cross_origin
from PIL import Image
from agapi import app
import os
from agapi import db,CORS
from agapi.models import User, Ad


# ads schema
@app.route('/image_list')
@cross_origin()
def image_list():
    import os
    data = []

    def scandir():

        """check if exists"""
        if (os.path.exists(app.config['CLIENT_IMAGES'])):

            """loop through files"""
            for path in os.listdir(app.config['CLIENT_IMAGES']):

                """if dir list else check if file type"""
                if os.path.isdir(path):

                    """call self"""
                    scandir()
                else:
                    exts = ['jpg', 'jpeg', 'png', 'gif']
                    for ext in exts:
                        if path.endswith(ext):
                            data.append(path)

        return data

    scandir()
    results = []
    for i in data:
        i = {'url': 'http://127.0.0.1:5000/image/'+i}
        results.append(i)


    rizo = jsonify(results)
    return rizo



@app.route('/image/<url>')
def image(url):



    image_size= (200, 200)
    i = Image.open(open(app.config['CLIENT_IMAGES']+url ,'rb'))
    i.thumbnail(image_size)
    fn, fext = os.path.splitext(url)
    
    i.save(app.config['CLIENT_IMAGES']+ fn + '.png')
    returnImg = fn+'.png'
    return send_from_directory(app.config['CLIENT_IMAGES'], filename=returnImg)