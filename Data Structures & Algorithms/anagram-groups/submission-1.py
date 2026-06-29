from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Dictionary where:
        # Key   -> Sorted version of a word (canonical representation)
        # Value -> List of all words that share the same sorted form
        groups = defaultdict(list)

        for s in strs:

            # Sort the characters to create a unique key.
            # All anagrams become identical after sorting.
            #
            # Example:
            # "eat" -> "aet"
            # "tea" -> "aet"
            # "ate" -> "aet"
            key = "".join(sorted(s))

            # Append the original word to the list corresponding
            # to its sorted key.
            # defaultdict(list) automatically creates an empty list
            # if 'key' is seen for the first time.
            groups[key].append(s)

        # We only need the grouped lists, not the keys.
        return list(groups.values())