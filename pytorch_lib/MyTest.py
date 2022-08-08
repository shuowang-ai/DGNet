import os
import sys
PROJ_DIR = os.path.dirname(os.path.abspath(__file__))

import os
import torch
import argparse
import numpy as np
from scipy import misc
import imageio

from datetime import datetime

import torch.nn.functional as F
import torch.backends.cudnn as cudnn

from utils.dataset import test_dataset as EvalDataset
from lib.DGNet import DGNet as Network


def evaluator(model, val_root, map_save_path, trainsize=352):
    val_loader = EvalDataset(image_root=val_root + 'Imgs/',
                             gt_root=val_root + 'GT/',
                             testsize=trainsize)

    model.eval()
    with torch.no_grad():
        for i in range(val_loader.size):
            image, gt, name, _ = val_loader.load_data()
            gt = np.asarray(gt, np.float32)

            image = image.cuda()

            output = model(image)
            output = F.upsample(output[0], size=gt.shape, mode='bilinear', align_corners=False)
            output = output.sigmoid().data.cpu().numpy().squeeze()
            output = (output - output.min()) / (output.max() - output.min() + 1e-8)

            output = np.uint8(output * 255)

            imageio.imwrite(map_save_path + name, output)
            print('>>> prediction save at: {}'.format(map_save_path + name))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, default='DGNet', choices=['DGNet', 'DGNet-S'])
    parser.add_argument('--snap_path', type=str, default=os.path.join(PROJ_DIR, 'snapshots/DGNet/Net_epoch_best.pth'),
                        help='train use gpu')
    parser.add_argument('--gpu_id', type=str, default='0',
                        help='train use gpu')
    opt = parser.parse_args()

    now = datetime.now()
    txt_save_path = '/cluster/work/cvl/shuowang/results/cv/dgnet/{}/{}'.format(str(now)[:19], opt.snap_path.split('/')[-2])
    os.makedirs(txt_save_path, exist_ok=True)

    print('>>> configs:', opt)

    # set the device for training
    if opt.gpu_id == '0':
        os.environ["CUDA_VISIBLE_DEVICES"] = "0"
        print('USE GPU 0')
    elif opt.gpu_id == '1':
        os.environ["CUDA_VISIBLE_DEVICES"] = "1"
        print('USE GPU 1')
    elif opt.gpu_id == '2':
        os.environ["CUDA_VISIBLE_DEVICES"] = "2"
        print('USE GPU 2')
    elif opt.gpu_id == '3':
        os.environ["CUDA_VISIBLE_DEVICES"] = "3"
        print('USE GPU 3')

    cudnn.benchmark = True

    if opt.model == 'DGNet':
        model = Network(channel=64, arc='B4', M=[8, 8, 8], N=[4, 8, 16])
    elif opt.model == 'DGNet-S':
        model = Network(channel=32, arc='B1', M=[8, 8, 8], N=[8, 16, 32])
    else:
        raise Exception("Invalid Model Symbol: {}".format(opt.model))

    model.load_state_dict(torch.load(opt.snap_path))
    model.eval()
    model.cuda()

    for data_name in ['CAMO', 'COD10K', 'NC4K']:
        map_save_path = txt_save_path + "/{}/".format(data_name)
        os.makedirs(map_save_path, exist_ok=True)
        evaluator(
            model=model,
            val_root='/cluster/work/cvl/shuowang/data/cv/dgnet/dataset/TestDataset/' + data_name + '/',
            map_save_path=map_save_path,
            trainsize=352)
