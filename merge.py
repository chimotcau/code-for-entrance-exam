MergeArrays(arr1, arr2):
    merged = [] # Create an empty list to store the merged array
    i = 0
    j = 0
    while i < length(arr1) and j < length(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    # Add remaining elements from arr1, if any
    while i < length(arr1):
        merged.append(arr1[i])
        i += 1
    # Add remaining elements from arr2, if any
    while j < length(arr2):
        merged.append(arr2[j])
        j += 1
    return merged
