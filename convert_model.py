"""File for accessing YOLOv5 via PyTorch Hub https://pytorch.org/hub/

Usage:
    import torch
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, channels=3, classes=80)
"""

from models.yolo import Model
import torch
import os
dependencies = ['torch', 'yaml']




def create(name, pretrained, channels, classes):
    """Creates a specified YOLOv5 model

    Arguments:
        name (str): name of model, i.e. 'yolov5s'
        pretrained (bool): load pretrained weights into the model
        channels (int): number of input channels
        classes (int): number of model classes

    Returns:
        pytorch model
    """
    config = os.path.join(os.path.dirname(__file__),
                          'models', f'{name}.yaml')  # model.yaml path
    fname = f'{name}.pt'  # checkpoint filename
    ckpt = torch.load(fname, map_location=torch.device('cpu'))  # load
    ckpt['names'] = ckpt['model'].names
    ckpt['model'] = ckpt['model'].float().state_dict()  # to FP32
    
    torch.save(ckpt, 'test_save.pt')




if __name__ == '__main__':
    model = create(name='yolov5l', pretrained=True,
                   channels=3, classes=80)  # example
