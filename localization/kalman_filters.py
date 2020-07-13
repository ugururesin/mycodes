### PROBABILITY AFTER SENSE
'''
SCENARIO: There is 5 cells area in which
the color of a cell is either red or green.
'''
# Example Data
p = [0.2, 0.2, 0.2, 0.2, 0.2] #prior
world = ['green','red','red','green','green']
pHit = 0.6 
pMiss = 0.2

Z = 'red' #single measurement
measurements = ['red', 'green'] #multiple measurements

def sense(p,Z):
	q-=[]
	for i in range(len(p)):
		hit = (Z == world[i])
		q.append(p[i] * (hit*pHit+(1-hit)*pMiss))
	s = sum(q)
	for i in range(len(q)):
		q[i] = q[i] / s
	return q

def sense_multiple(p,measurements):
	for k in range(len(measurements)):
		p = sense(p, measurements[k])
	return p

def move(p,U):
	q = []
	for i in range(len(p)):
		q.append(p[(i-U) % len(p)])
	return q
###


### ONE-DIMENSIONAL KALMAN FILTER

## MOTION UPDATE
def update(mean1, var1, mean2, var2):
	new_mean = (var2*mean1 + var1*mean2) / (var1+var2)
	new_var = 1 / (1/var1 + 1/var2)
	return [new_mean, new_var]

## MOTION PREDICTION
def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

# Example Data
measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 1000. #very-large uncertainty!

for n in range(len(measurements)):
	[mu, sig] = update(mu, sig, measurements[n], measurement_sig)
	print('update: ')
	print([mu,sig])
	[mu,sig] = predict(mu, sig, motion[n], motion_sig)
	print('predict: ')
	print([mu,sig])



### MULTI-DIMENSIONAL KALMAN FILTER






