# Hint: Use a dictionary to build a trie where each character points to the next level of the trie.
# '.' is used as a marker for the end of a word.

class Trie:

    def __init__(self):
        # Initialize the root of the trie as an empty dictionary
        self.root = {}
        
    def insert(self, word: str) -> None:
        # Start at the root of the trie
        current_node = self.root

        # Insert each character in the word into the trie
        for char in word:
            if char not in current_node:
                current_node[char] = {}  # Create a new node if character not found

            current_node = current_node[char]  # Move to the next node

        # Mark the end of the word by adding a special end marker
        current_node['#'] = True

    def search(self, word: str) -> bool:
        # Start at the root of the trie
        current_node = self.root
        
        # Traverse through each character in the word
        for char in word:
            if char not in current_node:
                return False  # Return False if the character is not found in the trie
            current_node = current_node[char]  # Move to the next node

        # Check if the word ends at a valid node marked by '#'
        return '#' in current_node

    def startsWith(self, prefix: str) -> bool:
        # Start at the root of the trie
        current_node = self.root
        
        # Traverse through each character in the prefix
        for char in prefix:
            if char not in current_node:
                return False  # Return False if the prefix is not found
            current_node = current_node[char]  # Move to the next node

        return True  # Return True if the prefix exists in the trie
