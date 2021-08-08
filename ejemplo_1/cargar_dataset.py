from detecto import core

# All images and XML files in the same folder
#dataset = core.Dataset('images_and_labels/')

# Images and XML files in separate folders
dataset = core.Dataset('dataset/labels/', 'dataset/images/')

image, target = dataset[0]
print(image, target)