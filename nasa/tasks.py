# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from nasa.celery import app
import tensorflow as tf
from celery.task import Task
from nasa.settings import BASE_DIR
from celery.signals import celeryd_after_setup

from ai import models


class MoveImages(Task):
    def run(self, pk):
        picture = models.Picture.objects.get(pk=pk)

        image_path = picture.feature.path
        recyclable = picture.recyclable

        ind = image_path.rfind('/')
        name = image_path[ind+1:]
        # name = os.path.basename(image_path.picture.name)
        # Copy image to label'path
        if recyclable:
            os.system("cp " + image_path + " " + BASE_DIR + "/media/tf_files/recyclable/" + picture.label +"/" + name)

class ReTrain(Task):
    def run(self):
        # Necessary, execute docker run --name what-i-want -it
        name = "nasatf"
        comm = "python/tensorflow/tensorflow/examples/image_retraining/retrain.py\
        --bottleneck_dir=/tf_files/bottlenecks\
        --how_many_training_steps 500 \
        --model_dir=/tf_files/inception\
        --output_graph=/tf_files/retrained_graph.pb\
        --output_labels=/tf_files/retrained_labels.txt\
        --image_dir/tf_files/recyclable"
        os.system("docker exec -it " + name + " " + comm)


app.tasks.register(MoveImages)
app.tasks.register(ReTrain)
