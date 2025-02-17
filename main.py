import torch
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
from models.lenet5 import LeNet5
from utils.data_loader import CMUFacesDataset
from utils.train import train_model
from utils.evaluate import evaluate_model

transform = transforms.Compose([transforms.Resize((32, 32)), transforms.ToTensor()])
dataset = CMUFacesDataset(root_dir='data/cmu_faces', transform=transform)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

model = LeNet5(num_classes=6)
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

model = train_model(model, dataloader, criterion, optimizer, epochs=10)
evaluate_model(model, dataloader)