import torch

torch.cuda.init()

print('Torch version: ' + torch.__version__)
print('CUDA available: ' + str(torch.cuda.is_available()))
print('cuDNN version: ' + str(torch.backends.cudnn.version()))

if torch.cuda.is_initialized():
    for i in range(torch.cuda.device_count()):
        dev_str = f'cuda:{i}'
        print(torch.cuda.get_device_properties(dev_str))
else:
  print('cuda not ready')

