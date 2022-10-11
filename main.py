import torch
print(f"pytorch version: {torch.__version__}")
print(f"cuda available: {torch.cuda.is_available()}")

import torchvision
print(f"torchvision version: {torchvision.__version__}")