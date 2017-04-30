from rest_framework import viewsets
from rest_framework.response import Response
from django.utils.crypto import get_random_string

from ai.models import Picture
from nasa.serializers import PictureSerializer
from nasa import tasks as tk
import tensorflow as tf
from nasa.settings import BASE_DIR


class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    resources = {
                "plastic":
                    {"score": 31, "co2": 5.1, "recyclable": True},
                "carton":
                    {"score": 6, "co2": 0.9, "recyclable": True},
                "can":
                    {"score": 20, "co2": 4.3, "recyclable": True},
                "glass":
                    {"score": 8, "co2": 1.2, "recyclable": True},
                "not recyclable":
                    {"score": 0, "co2": 0, "recyclable": False}
                }

    def get(self, request):
        queryset = self.queryset.order_by('-created_at')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        picture = Picture()
        f = request.data['feature']
        file_name = "{}.jpg".format(get_random_string(length=10))
        picture.feature.save(file_name, f, save=True)

        image_path = picture.feature.path
        print(image_path)

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

        picture.score = self.resources[picture.label]['score']
        picture.co2 = self.resources[picture.label]['co2']
        picture.recyclable = self.resources[picture.label]['recyclable']

        picture.save()
        tk.MoveImages.delay(picture.pk)
        serializer = self.get_serializer(picture, many=False)
        return Response(serializer.data)
