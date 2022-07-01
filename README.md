# Amazon Coding Challenge
*Bright Network Internship in association with Amazon, June 2022*

## Preface
I would highly recommend trying this challenge out yourself, mainly for the purpose of learning how to design clean and properly organised code. The required program is short and simple and can therefore be structured as a small application. The challenge brief is in the [following link](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:c05e7ec0-25f5-4ce1-a7eb-45993cf4cbaa).

---
## Execution
With the folder installed, run 
```shell
python3 -m pathfinder
```
to start the interactive program.

---
## Main Task
Create an algorithm which calculates a valid path avoiding the obstacles and reaching the delivery point.
The starting point is (0,0) and the delivery point is (9,9). 10x10 Grid.

The solution should print the path in the format of
```python
[(x1, y1), (x2, y2), ...]
```
and also the number of steps.

---
## Actions
### Phase 1 
Obstacles: (9,7) (8,7) (6,7) (6,8)  

### Phase 2 
Obstacles include all of Phase 1's obstacles, and 20 additional randomly placed obstacles which do not overlap existing ones nor find themselves at the start and delivery points.

### Bonus
If the vehicle is unable to reach its destination, the algorithm prints "Unable to reach delivery point" and identifies the least amount of obstacles which need to be removed in order for the vehicle to reach its destination.

\- Morgane Ohlig, June 2022
