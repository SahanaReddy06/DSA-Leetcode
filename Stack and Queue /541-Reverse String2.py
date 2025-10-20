class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Step 1️⃣: Convert string to list (strings are immutable)
        s = list(s)

        # Step 2️⃣: Loop through the string in steps of 2k
        for i in range(0, len(s), 2 * k):
            # Step 3️⃣: Reverse the first k characters in every 2k block
            s[i:i + k] = reversed(s[i:i + k])

        # Step 4️⃣: Join the list back into a string
        return ''.join(s)
