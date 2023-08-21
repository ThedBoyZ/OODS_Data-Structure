def permute_string(s, k):
    if k < 0:
        return ("Invalid value of k. k must be a non-negative integer.")
    if k > len(s):

        return ("Invalid value of k. k must be less than or equal to the length of the string.")
    
    def generate_permutations(prefix, remaining, k):
        if k == 0:
            return [prefix]
        
        permutations = []
        for i in range(len(remaining)):
            permutations.extend(generate_permutations(prefix + remaining[i], remaining[:i] + remaining[i+1:], k - 1))
        
        return permutations
    
    unique_permutations = list(set(generate_permutations('', s, k)))
    sorted_permutations = sorted(unique_permutations)
    return sorted_permutations

inp = input("Enter a string and k: ")
s, k = inp.split("/")
k = int(k)

try:
    result = permute_string(s, k)
    print(result)
except Exception as e:
    print(e)