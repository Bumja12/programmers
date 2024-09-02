from collections import defaultdict

def solution(k, tangerine):
    # Step 1: Create a frequency dictionary
    freq = defaultdict(int)
    for t in tangerine:
        freq[t] += 1

    # Step 2: Create a list to store frequencies, assuming the size range is known
    max_freq = max(freq.values())
    count_buckets = [0] * (max_freq + 1)
    
    for f in freq.values():
        count_buckets[f] += 1

    # Step 3: Iterate over the buckets from high to low frequency
    s = 0
    types = 0
    
    for f in range(max_freq, 0, -1):
        if count_buckets[f] > 0:
            num_tangerines = f * count_buckets[f]
            if s + num_tangerines >= k:
                # Calculate how many types are needed
                needed = (k - s + f - 1) // f  # ceiling division
                return types + needed
            s += num_tangerines
            types += count_buckets[f]

    return types + 2
