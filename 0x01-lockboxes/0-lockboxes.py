#!/usr/bin/python3
"""This module define a function checks if boxes can be unlocked
"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened
    Args:
        boxes: a list of lists
    Return:
        True if all boxes can be opened, else return False
    """
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True
    position = 0

    for box in boxes:
        for key in box:
            if key < num_boxes and key != position:
                unlocked_boxes[key] = True
        position += 1
    return all(unlocked_boxes)
