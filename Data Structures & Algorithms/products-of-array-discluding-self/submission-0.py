class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Example:
        # nums = [1,2,4,6]

        # Length of array
        n = len(nums)

        # Create left array
        # [1] repeated 4 times
        # left = [1,1,1,1]
        left = [1] * n

        # Create right array
        # right = [1,1,1,1]
        right = [1] * n

        # Create answer array
        # answer = [1,1,1,1]
        answer = [1] * n

        # -------------------------
        # FILL LEFT ARRAY
        # -------------------------

        # range(1,4)
        # i = 1,2,3

        for i in range(1, n):

            # ---------- i = 1 ----------
            # left[1] = left[0] * nums[0]
            #         = 1 * 1
            #         = 1
            #
            # left = [1,1,1,1]

            # ---------- i = 2 ----------
            # left[2] = left[1] * nums[1]
            #         = 1 * 2
            #         = 2
            #
            # left = [1,1,2,1]

            # ---------- i = 3 ----------
            # left[3] = left[2] * nums[2]
            #         = 2 * 4
            #         = 8
            #
            # left = [1,1,2,8]

            left[i] = left[i-1] * nums[i-1]

        # Final left array:
        # left = [1,1,2,8]

        # -------------------------
        # FILL RIGHT ARRAY
        # -------------------------

        # range(2,-1,-1)
        # i = 2,1,0

        for i in range(n-2, -1, -1):

            # ---------- i = 2 ----------
            # right[2] = right[3] * nums[3]
            #          = 1 * 6
            #          = 6
            #
            # right = [1,1,6,1]

            # ---------- i = 1 ----------
            # right[1] = right[2] * nums[2]
            #          = 6 * 4
            #          = 24
            #
            # right = [1,24,6,1]

            # ---------- i = 0 ----------
            # right[0] = right[1] * nums[1]
            #          = 24 * 2
            #          = 48
            #
            # right = [48,24,6,1]

            right[i] = right[i+1] * nums[i+1]

        # Final right array:
        # right = [48,24,6,1]

        # -------------------------
        # MULTIPLY LEFT AND RIGHT
        # -------------------------

        # range(4)
        # i = 0,1,2,3

        for i in range(n):

            # ---------- i = 0 ----------
            # answer[0] = left[0] * right[0]
            #           = 1 * 48
            #           = 48

            # ---------- i = 1 ----------
            # answer[1] = left[1] * right[1]
            #           = 1 * 24
            #           = 24

            # ---------- i = 2 ----------
            # answer[2] = left[2] * right[2]
            #           = 2 * 6
            #           = 12

            # ---------- i = 3 ----------
            # answer[3] = left[3] * right[3]
            #           = 8 * 1
            #           = 8

            answer[i] = left[i] * right[i]

        # Final answer:
        # [48,24,12,8]

        return answer