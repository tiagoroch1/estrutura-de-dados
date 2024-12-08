def interpolation_search_notas(sorted_list, target):
    """Realiza a busca por interpolação para encontrar uma nota específica."""
    low, high = 0, len(sorted_list) - 1
    
    while low <= high and sorted_list[low] <= target <= sorted_list[high]:
        if low == high:
            if sorted_list[low] == target:
                return low
            return -1
        
        pos = low + ((high - low) * (target - sorted_list[low]) // (sorted_list[high] - sorted_list[low]))
        
        if sorted_list[pos] == target:
            return pos
        elif sorted_list[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    
    return -1
