__source__ = 'https://leetcode.com/problems/design-snake-game/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/design-snake-game.py
# Time:  O(s) per move, s is the current length of the snake.
# Space: O(s)
#
# Description: Leetcode # 353. Design Snake Game
#
# Design a Snake game that is played on a device with screen size = width x height.
# Play the game online if you are not familiar with the game.
#
# The snake is initially positioned at the top left corner (0,0) with length = 1 unit.
#
# You are given a list of food's positions in row-column order.
# When a snake eats the food, its length and the game's score both increase by 1.
#
# Each food appears one by one on the screen.
# For example, the second food will not appear until the first food was eaten by the snake.
#
# When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.
#
# Example:
# Given width = 3, height = 2, and food = [[1,2],[0,1]].
#
# Snake snake = new Snake(width, height, food);
#
# Initially the snake appears at position (0,0) and the food at (1,2).
#
# |S| | |
# | | |F|
#
# snake.move("R"); -> Returns 0
#
# | |S| |
# | | |F|
#
# snake.move("D"); -> Returns 0
#
# | | | |
# | |S|F|
#
# snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )
#
# | |F| |
# | |S|S|
#
# snake.move("U"); -> Returns 1
#
# | |F|S|
# | | |S|
#
# snake.move("L"); -> Returns 2 (Snake eats the second food)
#
# | |S|S|
# | | |S|
#
# snake.move("U"); -> Returns -1 (Game over because snake collides with border)
#
# Companies
# Google
# Related Topics
# Design Queue
#

import unittest
from collections import deque

class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.__width = width
        self.__height = height
        self.__score = 0
        self.__food = deque(food)
        self.__snake = deque([(0, 0)])
        self.__direction =  {"U":(-1, 0), "L":(0, -1), "R":(0, 1), "D":(1, 0)};


    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        def valid(x, y):
            return 0 <= x < self.__height and \
                   0 <= y < self.__width and \
                   (x, y) not in self.__snake

        d = self.__direction[direction]
        x, y = self.__snake[-1][0] + d[0], self.__snake[-1][1] + d[1]
        tail = self.__snake[-1]
        self.__snake.popleft()
        if not valid(x, y):
            return -1
        elif self.__food and (self.__food[0][0], self.__food[0][1]) == (x, y):
            self.__score += 1
            self.__food.popleft()
            self.__snake.appendleft(tail)
        self.__snake.append((x, y))
        return self.__score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 136ms 97.27%
class SnakeGame {
    private int width;
    private int height;
    private int[][] food;
    private int foodIndex;
    private boolean isOver;
    private Deque<Integer> snake;

    /** Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0]. */
    public SnakeGame(int width, int height, int[][] food) {
        this.width = width;
        this.height = height;
        this.food = food;
        snake = new LinkedList<>();
        snake.add(0);
    }

    /** Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body. */
    public int move(String direction) {
        if (isOver) {
            return -1;
        }
        int head = snake.getLast();
        int i = head / width;
        int j = head % width;
        switch (direction) {
            case "U":
                i--;
                break;
            case "L":
                j--;
                break;
            case "R":
                j++;
                break;
            case "D":
                i++;
                break;
            default:
                throw new IllegalArgumentException("Invalid move:" + direction);
        }
        if (i < 0 || i == height || j < 0 || j == width) {
            isOver = true;
            return -1;
        }
        head = i * width + j;
        if (foodIndex < food.length && food[foodIndex][0] == i && food[foodIndex][1] == j) {
            foodIndex++;
        } else {
            snake.poll();
            if (snake.contains(head)) {
                isOver = true;
                return -1;
            }
        }
        snake.add(head);
        return snake.size() - 1;
    }
}

/**
 * Your SnakeGame object will be instantiated and called as such:
 * SnakeGame obj = new SnakeGame(width, height, food);
 * int param_1 = obj.move(direction);
 */

# 208ms 16.79%
class SnakeGame {
    int[][] food;
    int index;
    int row, col;
    // current loc
    int x, y;
    // snack length
    int len;
    LinkedList<int[]> queue;
    /** Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0]. */
    public SnakeGame(int width, int height, int[][] food) {
        this.food = food;
        this.index = 0;
        this.x = 0;
        this.y = 0;
        this.row = height;
        this.col = width;
        this.queue = new LinkedList<int[]>();
        this.queue.offer(new int[]{0, 0});
    }

    /** Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body. */
    public int move(String direction) {
        switch(direction){
            // snake head
            case "U":
                x--;
                break;
            case "L":
                y--;
                break;
            case "R":
                y++;
                break;
            case "D":
                x++;
                break;
        }

        if(!isValid(x,y)){
            return -1;
        }
        return process(x, y);
    }

    public boolean isValid(int x, int y){
        if(x < 0 || x >= row || y < 0 || y >= col)
            return false;

        return true;
    }

    public int process(int x, int y) {
        if (index == food.length) {
            queue.poll();
        }

        // encounter food, length ++, no need to remove snack tail
        else if (food[index][0] == x && food[index][1] == y) {
            // snack lenth + 1
            len ++;
            // ???
            index ++;
        }
        // not hit food, so remove snack tail
        else {
            queue.poll();
        }

        for(int[] p: queue){
            if (p[0] == x && p[1] == y)
                return -1;
        }
        // add snack head's new loc
        queue.offer(new int[]{x,y});

        return len;
    }
}

'''