from pygrabber.dshow_graph import FilterGraph
from Service.Controller.ConfigController.AppConfig import config

class CameraIdentification:

    def camera_init(self):
        self.graph = FilterGraph()
        self.listCamera = self.graph.get_input_devices()
        return self.listCamera

    def set_camera(self, name):
        try:
            index = self.graph.get_input_devices().index(name)
        except ValueError as e:
            index = 0

        config.set_param('CAMERA_INDEX', index)

camera = CameraIdentification()
