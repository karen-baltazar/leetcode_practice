# Problems

| Problem Number | Problem Name                                         | Explanation                                      | Code                                          |
|----------------|------------------------------------------------------|--------------------------------------------------|-----------------------------------------------|
| 981            | [Time Based Key-Value Store](#981-time-based-key-value-store) | [Explanation](#981-time-based-key-value-store)   | [Python Code](./981_time_based_key_value_store.py) |

## 981. Time Based Key-Value Store

**Description**:
Design a time-based key-value store that supports setting and retrieving values based on keys and timestamps. Implement two functions:
1. `set(key, value, timestamp)`: Stores the key-value pair with the given timestamp.
2. `get(key, timestamp)`: Retrieves the value corresponding to the key such that the timestamp is less than or equal to the given timestamp.

**Example**:
```plaintext
Input: 
TimeMap kv = new TimeMap();
kv.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
kv.get("foo", 1);         // output "bar"
kv.get("foo", 3);         // output "bar", since "bar" is the latest value before timestamp 3.
kv.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
kv.get("foo", 4);         // output "bar2"
kv.get("foo", 5);         // output "bar2"
```

**Solution**:
The key idea is to store the values along with their timestamps in a dictionary where each key maps to a list of `[value, timestamp]` pairs. To efficiently retrieve the correct value for a given timestamp, binary search is employed. The `get` method performs a binary search to find the latest timestamp that is less than or equal to the given timestamp and returns the corresponding value.

[Link to code](./981_time_based_key_value_store.py)

**Notes**:
- Time complexity:
  - `set`: O(1) for inserting the key-value pair.
  - `get`: O(log n), where `n` is the number of timestamps for the key. Binary search efficiently finds the correct value.
- Space complexity: O(n), where `n` is the number of `set` operations since each one stores a new key-value pair with its timestamp.