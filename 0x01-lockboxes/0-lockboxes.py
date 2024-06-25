#!/usr/bin/python3
"""
Method to determine if all boxes can be opened
Using prototype: def canUnlockAll(boxes)
"""


def canUnlockAll(boxes):
    """
    Check if boxes can be unlocked
    """
    num_boxes = len(boxes)

    for key in range(1, num_boxes):
        found_key = False
        for idx in range(num_boxes):
            if key in boxes[idx] and key != idx:
                found_key = True
                break
        if not found_key:
            return False
    
    return True
