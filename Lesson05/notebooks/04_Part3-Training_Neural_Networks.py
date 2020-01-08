import torch
from torch import nn
import torch.nn.functional as F
from torchvision import datasets, transforms
from collections import OrderedDict

# Build a feed-forward network
input_size = 784
hidden_sizes = [128, 64]
output_size = 10

model = nn.Sequential(OrderedDict([
                      ('fc1', nn.Linear(input_size, hidden_sizes[0])),
                      ('relu1', nn.ReLU()),
                      ('fc2', nn.Linear(hidden_sizes[0], hidden_sizes[1])),
                      ('relu2', nn.ReLU()),
                      ('output', nn.Linear(hidden_sizes[1], output_size)),
                      ('logSoftmax', nn.LogSoftmax(dim=1))]))

print(model)