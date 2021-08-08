from detecto import core, utils, visualize

# Train model
dataset = core.Dataset('dataset/labels/', 'dataset/images/')
model = core.Model(['grape_Blue', 'grape_Pink', 'grape_White'])

model.fit(dataset)

# Save model
model.save('model_weights.pth')

# Test model
score_max = 0.6
while(True):

    # Specify the path to your image
    path_Image = input("Ingrese nombre de la imagen: ")
    image = utils.read_image(path_Image)
    
    try:
        predictions = model.predict(image)
        
        # predictions format: (labels, boxes, scores)
        labels, boxes, scores = predictions

        for score_value in range(len(scores)):
            if score >= score_max:
                print(labels) 
                print(boxes)
                print(scores)

        # Visualize Result
        #visualize.show_labeled_image(image, boxes, labels)
    except:
        pass