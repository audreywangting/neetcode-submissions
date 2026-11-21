class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        result = 0

        # 1. Sliding Window
        left = 0
        customer_val = 0
        start_index = 0

        # First window
        for i in range(minutes):
            if grumpy[i] == 1:
                customer_val += customers[i]

        max_customer = customer_val

        # Second window and onwards
        for right in range(minutes, len(customers)):

            # Add new customers
            if grumpy[right] == 1:
                customer_val += customers[right]

            # Remove old customers
            if grumpy[left] == 1:
                customer_val -= customers[left]

            left += 1

            # Update maximum and best window position
            if customer_val > max_customer:
                max_customer = customer_val
                start_index = left

        # 2. Calculate total satisfied customers
        for i in range(len(customers)):

            # Inside the selected window
            if start_index <= i < start_index + minutes:
                result += customers[i]

            # Outside the window
            elif grumpy[i] == 0:
                result += customers[i]

        return result