class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        num_char = len(chars)
        write_index = 0  # Index to write compressed character data
        read_index = 0  # Index to read through original data
        
        if num_char<2:
            return num_char

        while read_index < num_char:
            current_char = chars[read_index]
            count = 0

            # Count occurrences of the current character
            while read_index < num_char and chars[read_index] == current_char:
                read_index += 1
                count += 1

            # Write the character
            chars[write_index] = current_char
            write_index += 1

            # Write the count (if > 1) as individual digits
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1

        # Return the length of the compressed array
        return write_index

