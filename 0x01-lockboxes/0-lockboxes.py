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

    for box in range(num_boxes):
        keys = boxes[box]
        for key in keys:
            if key < num_boxes:
                unlocked_boxes[key] = True

    return all(unlocked_boxes)
