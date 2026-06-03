# Pairs with Certain Difference

**Difficulty:** Easy
**Accuracy:** 63.41%
**Submissions:** 49K+
**Points:** 2

## Problem Statement

Given an array of integers and a number `k`, the task is the find maximum pair sum with the following conditions on the pairs.

* Pair difference should be less than `k`.
* Pairs should be disjoint. For example if `(x, y)` is a result pair, then neither `x` nor `y` should appear in any other result pair.
* Sum of `p` pairs means sum of `2p` elements in the result.
* If no valid pairs can be formed, return `0`.

---

## Examples

### Example 1

**Input:**

```text
arr[] = [3, 5, 10, 15, 17, 12, 9], K = 4
```

**Output:**

```text
62
```

**Explanation:**

```text
The valid disjoint pairs with difference less than K are:
(3, 5), (10, 12), (15, 17)

The maximum sum obtained from these pairs is:
3 + 5 + 10 + 12 + 15 + 17 = 62

An alternative pairing could be:
(3, 5), (9, 12), (15, 17)

However, this combination results in a smaller total sum, so it is not optimal.
```

---

### Example 2

**Input:**

```text
arr[] = [5, 15, 10, 300], k = 12
```

**Output:**

```text
25
```

**Explanation:**

```text
The valid disjoint pairs with difference less than k are:
(5, 10)

The maximum sum obtained from these pairs is:
5 + 10 = 15

An alternative pairing could be:
(10, 15)

However, this combination results in a larger total sum:
10 + 15 = 25. So this pairing is optimal.
```

---

## Constraints

```text
1 ≤ arr.size() ≤ 10^5
0 ≤ k ≤ 10^5
1 ≤ arr[i] ≤ 10^4
```

---

## Expected Complexities

| Complexity Type | Expected   |
| --------------- | ---------- |
| Time Complexity | O(n log n) |
| Auxiliary Space | O(n)       |

---

## Topic Tags

* Arrays
* Dynamic Programming
* Data Structures
* Algorithms

---

## Related Articles

* Maximum Sum Pairs Specific Difference
