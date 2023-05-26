# Flooded Cave

> This repository is just for education study purpose.



### Description

You are an archeologist exploring a cave and looking for ancient treasure. Eventually, you discover the treasure, but just as you are about to start stuffing your pockets with gold coins you hear a burst of water rushing towards you. Your enemies followed you and have flooded the cave!

You are given a matrix x with m rows and n columns representing the layout of the cave. Each cell has one of 3 values: - 0 represents solid ground - 1 represents a wall - 2 represents water

You are placed in the top-left corner of the map (0, 0) and you need to get to the exit at the bottom-right corner (m - 1, n - 1). At each step, you may move to an adjacent solid ground cell. After you move, every water cell will spread to all adjacent solid ground cells. Cells are considered adjacent if they are north, south, east, or west from each other (water does not spread diagonally). Neither you, nor water can bypass walls.

Before you start heading for the exit, instead of walking, you may decide to spend a turn to add an additional gold coin to your pocket. Once you start moving and leave the top-left corner, the treasure is lost and you will be left only with the coins you collected.

Write a Python algorithm that calculates the maximum number of gold coins you can safely reach the exit with. If it is impossible to reach the exit, return -1. If the water never reaches you and can spend eternity collecting coins before you head for the exit, return 1e9.

### Example 1
Input: 
```
[
 [0,1,0,0,0,0,0],
 [0,0,0,1,1,2,0],
 [0,1,0,0,2,1,0],
 [0,0,1,1,1,0,1],
 [0,0,0,0,0,0,0]
]
```
Output:
```
3
```
In this case, you can spend 3 turns collecting coins before the water reaches you. If you spend an additional turn, the water will block your way and you will not be able to reach the exit.

### Example 2
Input:
```
[
 [0,0,0,0],
 [0,2,1,0],
 [0,1,0,0]
]
```
Output:
```
-1
```
In this case, the water will immediately block all the possible path you can reach the exit.

### Example 3
Input:
```
[
 [0,0,0],
 [1,1,0],
 [2,1,0]
]
```
Output:
```
1e9
```
In this case, the water is surrounded by walls, so it will never be flooded. You can collect the coins as much as you want.

### Constraint

2 <= m <= 300

2 <= n <= 300

