import os, logging
import time
import torch
import torch.optim
import torch.utils.data
from common.utils import AverageMeter
from common.distributed import is_master
import torch.nn.functional as F
import cv2
import torchvision

logger = logging.getLogger(__name__)


def train(train_loader, model, criterion, optimizer, epoch):
    logger.info('training')
    batch_time = AverageMeter()
    data_time = AverageMeter()
    avg_loss = AverageMeter()

    model.train()

    end = time.time()
    # print('start')

    for i,  (source_frame, target) in enumerate(train_loader):
        
        # print('i',i)
        # print(source_frame.size())
        # print(target)
        
        # torchvision.utils.save_image(source_frame[:,3,:,:], 'source.png')
        
        
        # video=cv2.VideoWriter('loaded.avi',-1,1,(224,224))

        # for j in range(source_frame.size()[1]):
        #     video.write(source_frame[0,j,:,:,:].permute(1, 2, 0).numpy()*255)
 
        # video.release()
        
        # exit()
        
        # b = source_frame.shape[0]
        # rp1 = torch.randperm(b)
        # sf1 = 

        # measure data loading time
        data_time.update(time.time() - end)
        source_frame = source_frame.cuda()
        target = target.cuda()

        # compute output
        output = model(source_frame)
 
        # from common.render import visualize_gaze
        # for i in range(32):
        #     visualize_gaze(source_frame, output[0], index=i, title=str(i))

        # print(target.shape)
        # weight = target.sum()/target.shape[0]
        weight = target[:,1].sum()/target.sum()
        weight = weight.item()
        # print(weight)
        if weight==0:
            weight=0.05
        
        criterion1 = torch.nn.CrossEntropyLoss(weight=torch.FloatTensor([weight, 1-weight]).cuda())
        target = target.squeeze(1)
        loss = criterion1(output, target)
        # output = F.softmax(output, dim=-1)
        # for idx, scores in enumerate(output):
        #     print(scores[1].item())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        avg_loss.update(loss.item())

        # measure elapsed time
        batch_time.update(time.time() - end)
        end = time.time()
        
        # if i==0:
        #     break
        if i % 2 == 0:
            logger.info('Epoch: [{0}][{1}/{2}]\t'
                        'Time {batch_time.val:.3f} ({batch_time.avg:.3f})\t'
                        'Data {data_time.val:.3f} ({data_time.avg:.3f})\t'
                        'Loss {loss.val:.4f} ({loss.avg:.4f})\t'.format(
                        epoch, i, len(train_loader), batch_time=batch_time,
                        data_time=data_time, loss=avg_loss))


def validate(val_loader, model, postprocess):
    logger.info('evaluating')
    batch_time = AverageMeter()
    model.eval()
    end = time.time()

    for i, (source_frame, target) in enumerate(val_loader):

        source_frame = source_frame.cuda()

        with torch.no_grad():
            output = model(source_frame)
            postprocess.update(output.detach().cpu(), target)

            batch_time.update(time.time() - end)
            end = time.time()

        if i % 2 == 0:
            logger.info('Processed: [{0}/{1}]\t'
                        'Time {batch_time.val:.3f} ({batch_time.avg:.3f})\t'.format(
                        i, len(val_loader), batch_time=batch_time))
            # break
    postprocess.save()

    mAP = None
    if is_master():
        mAP = postprocess.get_mAP()
    
    return mAP
