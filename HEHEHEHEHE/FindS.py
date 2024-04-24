def find_s(concepts, target):
    # Initialize the hypothesis to the most specific hypothesis
    hypothesis = ['0'] * len(concepts[0])
    for i, concept in enumerate(concepts):
        if target[i] == "yes":
            for j in range(len(concept)):
                if hypothesis[j] == '0' or hypothesis[j] == concept[j]:
                    hypothesis[j] = concept[j]
                else:
                    hypothesis[j] = '?'
    return hypothesis

# Example usage:
concepts = [
    ['sunny', 'warm', 'normal', 'strong', 'warm', 'same'],
    ['sunny', 'warm', 'high', 'strong', 'warm', 'same'],
    ['rainy', 'cold', 'high', 'strong', 'warm', 'change'],
    ['sunny', 'warm', 'high', 'strong', 'cool', 'change']
]
target = ['yes', 'yes', 'no', 'yes']

hypothesis = find_s(concepts, target)
print(hypothesis)