def candidate_elimination(data):
    # Initialize G to the set of maximally general hypotheses
    G = [["?" for _ in range(len(data[0]) - 1)]]
    # Initialize S to the set of maximally specific hypotheses
    S = [data[0][:-1]]

    for instance in data:
        if instance[-1] == "Yes":
            G = [g for g in G if all(g[i] == "?" or g[i] == instance[i] for i in range(len(g)))]
            for i in range(len(S[0])):
                if S[0][i] != instance[i]:
                    S[0][i] = "?"
        else:
            S = [s for s in S if any(s[i] != instance[i] for i in range(len(s)))]
            G_new = []
            for g in G:
                for i in range(len(g)):
                    if g[i] == "?" and instance[i] != S[0][i]:
                        g_new = g.copy()
                        g_new[i] = S[0][i]
                        G_new.append(g_new)
            G += G_new
            G = [g for g in G if any(g[i] != s[i] for s in S for i in range(len(s)))]

    return G, S

# Example usage:
data = [
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"]
]
G, S = candidate_elimination(data)
print("G:", G)
print("S:", S)