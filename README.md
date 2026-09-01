# Sliding Window Technique - LeetCode Solutions

## Sliding Window Templates

### Fixed-Size Window Template
```python
def fixed_window(nums, k):
    window_sum = 0
    left = 0
    
    for right in range(len(nums)):
        # 1. Add element at right to window
        window_sum += nums[right]
        
        # 2. When window reaches size k
        if right - left + 1 == k:
            # Process: record result (max, min, count, etc.)
            process(window_sum)
            
            # 3. Remove leftmost element before sliding
            window_sum -= nums[left]
            left += 1
    
    return result
```

**When does left move?** When `right - left + 1 == k` (window full).

---

### Variable-Size Window Template
```python
def variable_window(nums, condition):
    left = 0
    result = 0
    
    for right in range(len(nums)):
        # 1. Add element at right to window
        add_to_window(nums[right])
        
        # 2. Shrink window while condition violated
        while window_invalid():
            # Remove leftmost element
            remove_from_window(nums[left])
            left += 1
        
        # 3. Update result with current valid window
        result = max(result, right - left + 1)
    
    return result
```

**When does left move?** When the window becomes invalid (condition violated).

---

## Solutions

| # | Problem | Difficulty | Type |
|---|---------|------------|------|
| 1 | [Maximum Average Subarray I](Maximum_Average_Subarray_I.py) | Easy | Fixed |
| 2 | [Substrings of Size Three with Distinct Characters](Substrings_of_Size_Three_with_Distinct_Characters.py) | Easy | Fixed |
| 3 | [Maximum Number of Vowels in a Substring of Given Length](Maximum_Number_of_Vowels_in_a_Substring_of_Given_Length.py) | Medium | Fixed |
| 4 | [Contains Duplicate II](Contains_Duplicate_II.py) | Easy | Variable |
| 5 | [Longest Substring Without Repeating Characters](Longest_Substring_Without_Repeating_Characters.py) | Medium | Variable |
| 6 | [Longest Repeating Character Replacement](Longest_Repeating_Character_Replacement.py) | Medium | Variable |
| 7 | [Permutation in String](Permutation_in_String.py) | Medium | Variable |
| 8 | [Check If a String Contains All Binary Codes of Size K](Check_If_a_String_Contains_All_Binary_Codes_of_Size_K.py) | Medium | Fixed |
| 9 | [Subarrays with Product Less Than K](Subarrays_product_with_Sum_Less_Than_K.py) | Medium | Variable |
| 10 | [Sliding Window Maximum](Sliding_Window_Maximum.py) | Hard | Fixed (Deque) |
| 11 | [Minimum Window Substring](Minimum_Window_Substring.py) | Hard | Variable |

---

## Key Concepts

### Fixed Window
- Window size is constant `k`
- Left moves after window is full
- Use for: subarray sum, substring count, window stats

### Variable Window
- Window size changes based on condition
- Left moves when condition is violated
- Use for: longest/shortest substring, valid windows

### When Left Moves
| Scenario | Left Action |
|----------|-------------|
| Fixed window full (`right - left + 1 == k`) | Move left to slide window |
| Variable window invalid | Move left until valid again |
| Duplicate in window | Move left past duplicate |
| Window too large | Move left to shrink |

---

## Complexity

| Problem | Time | Space |
|---------|------|-------|
| Maximum Average Subarray I | O(n) | O(1) |
| Size Three Distinct | O(n) | O(1) |
| Max Vowels | O(n) | O(1) |
| Contains Duplicate II | O(n) | O(k) |
| Longest Substring No Repeat | O(n) | O(min(n,m)) |
| Longest Repeating Replace | O(n) | O(1) |
| Permutation in String | O(n) | O(1) |
| Binary Codes Size K | O(n·k) | O(2^k) |
| Product Less Than K | O(n) | O(1) |
| Sliding Window Max | O(n) | O(k) |
| Minimum Window Substring | O(n) | O(k) |
