### NN TEMPLATE

import numpy as np

class NeuralNetwork:
	def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
		#Set number of nodes in input, hidden and output layers.
		self.input_nodes = input_nodes
		self.hidden_nodes = hidden_nodes
		self.output_nodes = output_nodes
		
		#Initialize weights
		self.weights_input_to_hidden = np.random.normal(0.0, self.hidden_nodes**-0.5,
																			(self.hidden_nodes, self.input_nodes))
		
		self.weights_hidden_to_output = np.random.normal(0.0, self.output_nodes**-0.5,
																			(self.output_nodes, self.hidden_nodes))
																			
		self.learning_rate = learning_rate
		
		####Set this to your implemented sigmoid function ####
		#TODO: Activation function is the sigmoid function
		self.activation_function =
		
	def pre_process_data(self):
		""
	
	def train(self, inputs_list, targets_list):
	
		#Convert inputs list to 2d array
		inputs = np.array(inputs_list, ndmin=2).T
		targets = np.array(targets_list, ndmin=2).T
		
		#### Implement the forward pass here ###
		### Forward pass ###
		# TODO: Hidden layer
		hidden_inputs = #signals into hidden layer
		hidden_outputs = #signals from hidden layer
		
		
		
		
		
		
		
		
		