
# Sliding windows brute force

nums1 = [2, 1, 5, 1, 3, 2]
k = 3
maximum = 0

for i in range(0, len(nums1) - k + 1):
    prefix_sum = 0
    
    for j in range(i, k + i):
        prefix_sum += nums1[j]

    if prefix_sum > maximum:
        maximum = prefix_sum
        print(maximum)

# Sliding window optimized solution

maximum = sum(nums1[0:k])

for i in range(k, len(nums)):
    window_sum = maximum - nums1[i - k] + nums1[i]
 
    if window_sum > maximum:
        maximum = window_sum
        print(maximum)
    
        

        
    
