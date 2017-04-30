# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from nasa.celery import app
import tensorflow as tf
from celery.task import Task
from nasa.settings import BASE_DIR
from celery.signals import celeryd_after_setup

from ai import models


class PredictTask(Task):
    def run(self, pk):
        picture = models.Picture.objects.get(pk=pk)
        print(picture.feature.path)
        image_path = picture.feature.path

        # Read in the image_data
        image_data = tf.gfile.FastGFile(image_path, 'rb').read()
        # Loads label file, strips off carriage return

        txt = BASE_DIR + "/media/tf_files/retrained_labels.txt"
        label_lines = [line.rstrip() for line in tf.gfile.GFile(txt)]
        # Unpersists graph from file
        pb = BASE_DIR + "/media/tf_files/retrained_graph.pb"
        with tf.gfile.FastGFile(pb, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name='')

        max_score = 0
        max_human_string = ""
        with tf.Session() as sess:
            # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
            predictions = sess.run(softmax_tensor, \
                    {'DecodeJpeg/contents:0': image_data})
            # Sort to show labels of first prediction in order of confidence
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
            for node_id in top_k:
                human_string = label_lines[node_id]
                score = predictions[0][node_id]
                print('%s (score = %.5f)' % (human_string, score))
                if(score > max_score):
                    max_score = score
                    max_human_string = human_string

        picture.label = max_human_string
        picture.save()


class MoveImages(Task):
    def run(self, pk):
        picture = models.Picture.objects.get(pk=pk)

        image_path = picture.feature.path
        recyclable = picture.recyclable
        # print("IMAGE_PATH" + image_path)
        ind = image_path.rfind('/')
        name = image_path[ind+1:]
        # name = os.path.basename(image_path.picture.name)
        # print("NAME:: " + name)
        print(image_path)
        # Copy image to label'path
        if recyclable:
            os.system("cp " + image_path + " " + BASE_DIR + "/media/tf_files/recyclable/" + picture.label +"/" + name)



app.tasks.register(PredictTask)
app.tasks.register(MoveImages)


