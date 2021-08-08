from detecto import core, utils, visualize

#cars.jpg
#fruits.jpeg
#person.jpg
image = utils.read_image('ejemplo_0/person.jpg')
model = core.Model()

labels, boxes, scores = model.predict_top(image)

print(labels)
print(scores)

visualize.show_labeled_image(image, boxes, labels)

# Upgrade -> Filtering by score
aux_label = []
aux_scores = []

max_score = 0.7
index = 0

for value in scores:
    if value > max_score:
        aux_label.append(labels[index])
        aux_scores.append(value)
    index += 1

print(aux_scores)
print(aux_label)