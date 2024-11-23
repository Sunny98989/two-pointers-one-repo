class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows = len(box)
        cols = len(box[0])
        
        for r in range(rows):
            empty_pos = cols - 1
            for c in range(cols - 1, -1, -1):
                if box[r][c] == '#': 
                    box[r][c], box[r][empty_pos] = box[r][empty_pos], box[r][c]
                    empty_pos -= 1
                elif box[r][c] == '*': 
                    empty_pos = c - 1
        
        rotated_box = []
        for c in range(cols):
            new_row = []
            for r in range(rows - 1, -1, -1):
                new_row.append(box[r][c])
            rotated_box.append(new_row)
        
        return rotated_box
