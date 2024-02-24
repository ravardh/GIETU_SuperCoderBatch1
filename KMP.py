def compute_lps_array(pattern):
    """
    Compute the Longest Prefix Suffix (lps) array for the pattern.
    """
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    """
    Search for occurrences of the pattern within the text using the KMP algorithm.
    """
    n = len(text)
    m = len(pattern)
    lps = compute_lps_array(pattern)
    occurrences = []

    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            occurrences.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return occurrences

# Example usage:
text = "ABABDABACDABABCABAB"
pattern = "ABAB"
print("Occurrences found at indices:", kmp_search(text, pattern))
