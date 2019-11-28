import pandas as pd
import numpy as np

t = 0
graph = {}
freq = {}

def updateFreq(event):
	if event not in freq:
		freq[event] = 0
	freq[event] += 1


def updateGraph(prevState, event):
	if event not in graph:
		graph[event] = {}

	if event not in graph[prevState]:
		graph[prevState][event] = 0
	graph[prevState][event] += 1



events = pd.read_csv("eventVector.csv", header=None)
events = np.array(events)

#for first event vector
event = np.array2string(events[0], separator=',')
graph[event] = {}
freq[event] = 1

for i in events[1:]:
	prevState = event
	event = np.array2string(i, separator=',')
	updateGraph(prevState, event)
	updateFreq(event)
	t += 1
	#probability = freq/t
print(graph['[0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0]'])
