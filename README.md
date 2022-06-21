# Amazon Coding Challenge
*Bright Network Internship in association with Amazon, June 2022*

## Task
Create an algorithm which calculates a valid path avoiding the obstacles and reaching the delivery point.

The solution should print the path in the format of
```python
[(x1, y1), (x2, y2), ...]
```
and also the number of steps.

## Phase 1 
Implement a 10x10 grid that contains a starting point on (0,0), the delivery point on (9,9) and the following obstacles on locations (9,7) (8,7) (6,7) (6,8).

## Phase 2
Add an additional 20 randomly placed obstacles and print their location in the format `[(x1, y1), (x2, y2), ...]`.

The obstacles should not overlap existing ones and should not be places at the start and delivery points.

## Bonus
In the event that the vehicle is unable to reach its destination, the algorithm should print "Unable to reach delivery point" and identify which obstacles to be removed in order for the vehicle to reach its destination.

The algorithm should suggest the least amount of obstacles using the format `[(x1, y1), (x2, y2), ...]` in order for the vehicle to reach its destination.