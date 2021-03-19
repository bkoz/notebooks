import torch

try:
    torch.cuda.init()

    print('Torch version: ' + torch.__version__)
    print('CUDA available: ' + str(torch.cuda.is_available()))
    print('cuDNN version: ' + str(torch.backends.cudnn.version()))

    try:
        torch.cuda.is_initialized()
        for i in range(torch.cuda.device_count()):
            dev_str = f'cuda:{i}'
            print(torch.cuda.get_device_properties(dev_str))
    except:
        print('Can not init CUDA!')
        assert AssertionError
except:
    print('CUDA is not available')