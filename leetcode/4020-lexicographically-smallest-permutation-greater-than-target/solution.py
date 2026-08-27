from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)

        # Remove all characters of target.
        for ch in target:
            cnt[ch] -= 1

        # Try changing target from right to left.
        for i in range(len(target) - 1, -1, -1):

            # Put target[i] back.
            cnt[target[i]] += 1

            # Can we form target[:i] from s?
            if any(x < 0 for x in cnt.values()):
                continue

            # Find the smallest character > target[i].
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c > target[i] and cnt[c] > 0:

                    cnt[c] -= 1

                    # Smallest possible suffix.
                    suffix = ''.join(
                        ch * cnt[ch]
                        for ch in "abcdefghijklmnopqrstuvwxyz"
                    )

                    return target[:i] + c + suffix

        return ""
