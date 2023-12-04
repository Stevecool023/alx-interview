#!/usr/bin/python3

def canUnlockAll(boxes):
    unlocked_boxes = [False] * len(boxes)
    unlocked_boxes[0] = True
    keys_stack = [0]

    while keys_stack:
        current_box = keys_stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < len(boxes) and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                keys_stack.append(key)

    return all(unlocked_boxes)
