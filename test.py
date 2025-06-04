class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        
        # If numFriends is 1, return the entire word
        if numFriends == 1:
            return word
        
        # Find the maximum length a single part can have
        # We need at least numFriends-1 characters for other parts
        max_length = n - (numFriends - 1)
        
        max_string = ""
        print(f"Initial variables: n={n}, max_length={max_length}, numFriends={numFriends}")
        # For each starting position
        for i in range(n):
            print(f"Checking starting position {i} with character '{word[i]}'")
            # Early termination optimization
            print(f"Current max_string: '{max_string}', comparing with '{word[i]}'")
            if max_string and word[i] < max_string[0]:
                print(f"Skipping position {i} as '{word[i]}' is less than current max_string '{max_string}'")

                continue
            
            # Try lengths from 1 to max_length, but prioritize longer lengths
            # since they're more likely to be lexicographically larger
            for length in range(max_length, 0, -1):
                print(f"Trying length {length} starting at position {i}")
                # Calculate the end index of the substring
                j = i + length
                
                # Check if this substring can be part of a valid split
                chars_before = i
                chars_after = n - j
                remaining_parts = numFriends - 1
                
                if chars_before + chars_after >= remaining_parts:
                    substring = word[i:j]
                    if substring > max_string:
                        max_string = substring
                        # Early termination: if we found a better string starting at i,
                        # no need to check shorter lengths from the same starting position
                        break
        
        return max_string

# Test with the provided examples
def test_solution():
    sol = Solution()
    
    # Example 1
    result1 = sol.answerString("dbca", 2)
    print(f"Example 1: word='dbca', numFriends=2")
    print(f"Result: '{result1}'")
    print(f"Expected: 'dbc'")
    print(f"Correct: {result1 == 'dbc'}")
    print()


# Run the tests
test_solution()