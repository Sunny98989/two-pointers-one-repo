# Max Product Subset

**Difficulty:** Medium
**Accuracy:** 17.21%
**Submissions:** 110K+
**Points:** 4

## Problem Statement

Given an array `arr[]`, find and return the maximum product possible with the subset of elements present in the array.

### Note

* The maximum product can be of a single element also.
* Since the product can be large, return it modulo `10^9 + 7`.

---

## Examples

### Example 1

**Input:**

```text
arr[] = [-1, 0, -2, 4, 3]
```

**Output:**

```text
24
```

**Explanation:**

```text
Maximum product will be ( -1 * -2 * 4 * 3 ) = 24
```

---

### Example 2

**Input:**

```text
arr[] = [-1, 0]
```

**Output:**

```text
0
```

**Explanation:**

```text
Maximum product will be ( -1 * 0 ) = 0
```

---

### Example 3

**Input:**

```text
arr[] = [5]
```

**Output:**

```text
5
```

**Explanation:**

```text
Maximum product will be 5.
```

---

## Constraints

```text
1 ≤ arr.size() ≤ 2 * 10^4
-10 ≤ arr[i] ≤ 10
```

---

## Expected Complexities

| Complexity Type | Expected |
| --------------- | -------- |
| Time Complexity | O(n)     |
| Auxiliary Space | O(1)     |

---

## Topic Tags

* Arrays
* Data Structures

---

## Related Articles

* Maximum Product Subset Array
