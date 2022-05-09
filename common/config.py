import argparse

argparser = argparse.ArgumentParser(description='Ego4d Social Benchmark')

argparser.add_argument('--source_path', type=str, default='data/ego/video_imgs', help='Video image directory')
argparser.add_argument('--json_path', type=str, default='data/ego/json_original', help='Face tracklets directory')
argparser.add_argument('--gt_path', type=str, default='data/ego/result_LAM', help='Groundtruth directory')
argparser.add_argument('--train_file', type=str, default='data/split/train1.list', help='Train list')
argparser.add_argument('--val_file', type=str, default='data/split/val1.list', help='Validation list')
argparser.add_argument('--test_file', type=str, default='data/split/test.list', help='Test list')
argparser.add_argument('--train_stride', type=int, default=13, help='Train subsampling rate')
argparser.add_argument('--val_stride', type=int, default=13, help='Validation subsampling rate')
argparser.add_argument('--test_stride', type=int, default=1, help='Test subsampling rate')
argparser.add_argument('--epochs', type=int, default=20, help='Maximum epoch')
argparser.add_argument('--batch_size', type=int, default=128, help='Batch size')
argparser.add_argument('--num_workers', type=int, default=2, help='Num workers')
argparser.add_argument('--lr', type=float, default=5e-4, help='Learning rate')
# argparser.add_argument('--weights', type=list, default=[0.136, 0.864], help='Class weight')
argparser.add_argument('--weights', type=list, default=[0.05, 0.95], help='Class weight')
# argparser.add_argument('--weights', type=list, default=[0.1, 0.9], help='Class weight')
argparser.add_argument('--eval', action='store_true', help='Running type')
argparser.add_argument('--dist', action='store_true', help='Launch distributed training')
argparser.add_argument('--model', type=str, default='BaselineLSTM', help='Model architecture')
argparser.add_argument('--rank', type=int, default=0, help='Rank id')
argparser.add_argument('--start_rank', type=int, default=0, help='Start rank')
argparser.add_argument('--device_id', type=int, default=0, help='Device id')
argparser.add_argument('--world_size', type=int, help='Distributed world size')
argparser.add_argument('--init_method', type=str, help='Distributed init method')
argparser.add_argument('--backend', type=str, default='nccl', help='Distributed backend')
argparser.add_argument('--exp_path', type=str, default='output', help='Path to results')
argparser.add_argument('--checkpoint', type=str, help='Checkpoint to load')
argparser.add_argument('--pretrained', action='store_true', help='Use pretrained weights for ViT')
