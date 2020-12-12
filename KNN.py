from math import sqrt


# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1) - 1):
		distance += (row1[i] - row2[i]) ** 2
	return sqrt(distance)


# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	## Sort the data based on distance value decending order
	distances.sort(key=lambda tup: tup[1])
	## return the neighbour based on K value
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors


# Make a classification prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
	## get the neighbour first
	neighbors = get_neighbors(train, test_row, num_neighbors)
	## get the last value for each row to check classfication field
	output_values = [row[-1] for row in neighbors]
	print(output_values)
	## now use max function . use set and value count to check th countand get the maximum count for each class
	prediction = max(set(output_values), key=output_values.count)
	return prediction


# Test distance function
dataset = [[2.7810836, 2.550537003, 0],
		   [1.465489372, 2.362125076, 0],
		   [3.396561688, 4.400293529, 0],
		   [1.38807019, 1.850220317, 0],
		   [3.06407232, 3.005305973, 0],
		   [7.627531214, 2.759262235, 1],
		   [5.332441248, 2.088626775, 1],
		   [6.922596716, 1.77106367, 1],
		   [8.675418651, -0.242068655, 1],
		   [7.673756466, 3.508563011, 1]]
prediction = predict_classification(dataset, dataset[0], 7)
print('Expected %d, Got %d.' % (dataset[5][-1], prediction))

