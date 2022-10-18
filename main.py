# python script

import os

config = {'obj.data': 'obj.data', 
       'cfg':'yolov4-obj.cfg',
       'weights': 'yolov4-obj_best.weights', 
       'thresh': 0.7}

class ObDetModel:
  
  def __init__(self, config):
    self.obj_data = config['obj.data']
    self.cfg = config['cfg']
    self.weights = config['weights']
    self.thresh = config['thresh']

  def predict(self, path):
    cmd = './darknet detector test {} {} {} {} -thresh {}'.format(self.obj_data, 
                                                                  self.cfg, 
                                                                  self.weights, 
                                                                  path,
                                                                  self.thresh)
    so = os.popen(cmd).read()

    return 'Result was saved to predictions.jpg'

model = ObDetModel(config)
model.predict('1657.jpg')
