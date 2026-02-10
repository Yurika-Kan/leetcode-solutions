// Last updated: 2/10/2026, 6:53:07 AM
1class Solution {
2    public boolean isRobotBounded(String instructions) {
3        // circle = end dir equals start dir
4        int UP = 0;
5        int LEFT = 1;
6        int DOWN = 2;
7        int RIGHT = 3;
8        int ORIGIN_DIR = UP;
9
10        int curDir = ORIGIN_DIR;
11        int row = 0, col = 0;
12
13        for (char curChar: instructions.toCharArray()) {
14            // go - move forward with current direction
15            if (curChar == 'G') {
16                if (curDir == UP) {
17                    row--;
18                } else if (curDir == DOWN) {
19                    row++;
20                } else if (curDir == LEFT) {
21                    col--;
22                } else if (curDir == RIGHT) {
23                    col++;
24                }
25            }
26            else if (curChar == 'L') {
27                curDir++;
28                if (curDir > RIGHT) {
29                    curDir = ORIGIN_DIR;
30                }
31            } else if (curChar == 'R') {
32                curDir--;
33                if (curDir < UP) {
34                    curDir = RIGHT;
35                }
36            }
37        }
38
39        boolean posChanged = row != 0 | col != 0;
40        if (!posChanged) return true;
41        if (curDir != ORIGIN_DIR) return true;
42        return false;
43    }
44}
45
46// Time: O(n)
47// Space: O(1)