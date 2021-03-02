import torch

torch.cuda.init()

if torch.cuda.is_initialized():
    for i in range(torch.cuda.device_count()):
        dev_str = f'cuda:{i}'
        print(torch.cuda.get_device_properties(dev_str))
else:
  print('cuda not ready')

