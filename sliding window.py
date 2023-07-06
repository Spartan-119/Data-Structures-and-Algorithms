from typing import List

class SlidingWindow:
    def fixed_sliding_window(self, arr: List[int], k: int) -> List[int]:
        # summing up the first sub array and adding it to the result
        curr_subarray = sum(arr[: k])
        result = [curr_subarray]

        # to get each subsequent subarray, and the next value in
        # the list and remove the first value

        for i in range(1, len(arr) - k + 1):
            curr_subarray = curr_subarray - arr[i - 1]
            curr_subarray = curr_subarray + arr[i + k - 1]
            result.append(curr_subarray)
        
        return result

    def dynamic_sliding_window(self, arr: List[int], x: int) -> int:
        # we want to track our min value
        min_length = float('inf')

        # the current range and sum of our sliding window
        start = 0
        end = 0
        current_sum = 0

        # extend the sliding window until our criteria is met
        while end < len(arr):
            current_sum += arr[end]
            end += 1

            # the contract the sliding window until it 
            # no longer meets our condition
            while start < end and current_sum >= x:
                current_sum -= arr[start]
                start += 1

                # update the min_length if this is shorter 
                # than the current min
                min_length = min (min_length, end - start + 1)
        
        return min_length
    
#################
# the main driver function
if __name__ == '__main__':
    sw = SlidingWindow()
    print(sw.fixed_sliding_window([1, 2, 3, 4 ,5, 6], 2))
    print()
    print(sw.dynamic_sliding_window([1, 2, 3, 4 ,5, 6], 2))