"""Exercise 4 - Forward algorithm vs Viterbi algorithm
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import numpy as np

states, obs = ['Rainy', 'Sunny'], [0, 1, 2]
pi = np.array([0.6, 0.4])
A = np.array([[0.7, 0.3], [0.4, 0.6]])               # Transitions
B = np.array([[0.1, 0.4, 0.5], [0.6, 0.3, 0.1]])     # Emissions
N, T = len(states), len(obs)

# Forward algorithm
alpha = np.zeros((N, T))
alpha[:, 0] = pi * B[:, obs[0]]
for t in range(1, T):
    alpha[:, t] = (alpha[:, t-1] @ A) * B[:, obs[t]]
fwd_prob = np.sum(alpha[:, -1])

# Viterbi algorithm
viterbi, backptr = np.zeros((N, T)), np.zeros((N, T), dtype=int)
viterbi[:, 0] = pi * B[:, obs[0]]
for t in range(1, T):
    for j in range(N):
        probs = viterbi[:, t-1] * A[:, j]
        backptr[j, t], viterbi[j, t] = np.argmax(probs), np.max(probs) * B[j, obs[t]]
vtr_prob = np.max(viterbi[:, -1])
path = [np.argmax(viterbi[:, -1])]
for t in range(T - 1, 0, -1):
    path.insert(0, backptr[path[0], t])

print(f"Forward Prob (All Paths) : {fwd_prob:.6f}")
print(f"Viterbi Prob (Best Path) : {vtr_prob:.6f}")
print(f"Best Path: {' -> '.join([states[s] for s in path])}")
