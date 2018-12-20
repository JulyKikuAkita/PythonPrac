__source__ = 'https://leetcode.com/problems/lru-cache/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/lru-cache.py
# Time:  O(1)
# Space: O(n)
#
# Description: Leetcode # 146. LRU Cache
#
# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and set.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
#
# set(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
#
#
# Companies
# Google Uber Facebook Twitter Zenefits Amazon Microsoft Snapchat Yahoo Bloomberg Palantir
# Related Topics
# Design
# Similar Questions
# LFU Cache Design In-Memory File System Design Compressed String Iterator
#

import unittest
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.list = DL()
        self.cache = {}
        self.capacity = capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            val = self.cache[key].val
            self.list.delete(self.cache[key])
            self.update(key, val)
            return val
        return -1

    def update(self, key, val):
        node = Node(key, val)
        self.list.insert(node)
        self.cache[key] = node

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache:
            self.list.delete(self.cache[key])
        elif len(self.cache) == self.capacity:
            del self.cache[self.list.tail.key] #always remove tail
            self.list.delete(self.list.tail)
        self.update(key, value)

class DL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        #add to First
        if not self.head:
            self.head = node
            self.tail = node
            node.pev = node.next = None
            return
        else:
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node

    def delete(self, node):
        if self.head == self.tail:
            self.head = self.tail = None
            return
        if node == self.head:
            node.next.prev = None
            self.head = node.next
            return
        if node == self.tail:
            node.prev.next = None
            self.tail = node.prev
            return
        node.prev.next = node.next
        node.next.prev = node.prev

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


# (2) fastest
import collections
class LRUCache2:
    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        val = self.cache[key]
        del self.cache[key]
        self.cahce[key] = val
        return val

    def set(self, key, value):
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) == self.capacity:
            # OrderedDict.popitem() returns the first or last key-value,
            # after deleting it. Setting last to False signals you wanted to remove the first.
            self.cache.popitem(last = False)
        self.cache[key] = value

# (3)
#http://www.cnblogs.com/zuoyuan/p/3701572.html
class Node2:
    def __init__(self, k ,x):
        self.key = k
        self.val = x
        self.prev = None
        self.next = None

class DoubleLinkedList2:
    def __init__(self):
        self.tail = None
        self.head = None

    def isEmpty(self):
        return not self.tail

    def removeLast(self):
        self.remove(self.tail)

    def remove(self, node):
        if self.head == self.tail:
            self.head, self.tail = None, None
            return
        if node == self.head:
            node.next.prev = None
            self.head = node.next
            return
        if node == self.tail:
            node.prev.next = None
            self.tail = node.prev
            return
        node.prev.next = node.next
        node.next.prev = node.prev

    def addFirst(self, node):
        if not self.head:
            self.head = self.tail = node
            node.prev = node.next = None
            return
        node.next = self.head
        self.head.prev = node
        self.head = node
        node.prev = None


class LRUCacheOther:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.P = dict()
        self.cache = DoubleLinkedList2()

    # @return an integer
    def get(self, key):
        if (key in self.P) and self.P[key]:
            self.cache.remove(self.P[key])
            self.cache.addFirst(self.P[key])
            return self.P[key].val
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.P:
            self.cache.remove(self.P[key])
            self.cache.addFirst(self.P[key])
            self.P[key].val = value
        else:
            node = Node2(key, value)
            self.P[key] = node
            self.cache.addFirst(node)
            self.size += 1
            if self.size > self.capacity:
                self.size -= 1
                del self.P[self.cache.tail.key]
                self.cache.removeLast()

# Test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        test = LRUCacheOther(1)
        print test.get(0)
        test.set(2,1)
        print test.get(2)
        self.assertEqual(1, 1)
        cache = LRUCache(3)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        print cache.get(1)
        cache.set(4, 4)
        print cache.get(2)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: 
# https://discuss.leetcode.com/topic/6613/java-hashtable-double-linked-list-with-a-touch-of-pseudo-nodes
# HashMap + doubly-linked list implementation:
# Without dummyhead tail

# 98ms 47.75%
    private int capacityLeft;
    private Map<Integer, DoublyLinkedNode<KeyValuePair>> keyElementMap;
    private DoublyLinkedNode<KeyValuePair> first;
    private DoublyLinkedNode<KeyValuePair> last;

    public LRUCache(int capacity) {
        capacityLeft = capacity;
        keyElementMap = new HashMap<>();
    }

    public int get(int key) {
        DoublyLinkedNode<KeyValuePair> node = keyElementMap.get(key);
        if (node == null) {
            return -1;
        } else {
            removeNode(node);
            addToFirst(node);
            return node.element.value;
        }
    }

    public void put(int key, int value) {
        DoublyLinkedNode<KeyValuePair> node = keyElementMap.get(key);
        if (node == null) {
            DoublyLinkedNode<KeyValuePair> newNode = new DoublyLinkedNode<>(new KeyValuePair(key, value));
            if (capacityLeft == 0) {
                keyElementMap.remove(last.element.key);
                removeNode(last);
            } else {
                capacityLeft--;
            }
            addToFirst(newNode);
            keyElementMap.put(key, newNode);
        } else {
            node.element.value = value;
            removeNode(node);
            addToFirst(node);
            keyElementMap.put(key, node);
        }
    }

    private void removeNode(DoublyLinkedNode node) {
        if (node == null) {
            return;
        }
        if (node == first) {
            first = first.next;
        } else {
            node.prev.next = node.next;
        }
        if (node == last) {
            last = last.prev;
        } else {
            node.next.prev = node.prev;
        }
        node.prev = null;
        node.next = null;
    }

    private void addToFirst(DoublyLinkedNode node) {
        if (node == null) {
            return;
        }
        if (first == null) {
            first = node;
            last = node;
        } else {
            first.prev = node;
            node.next = first;
            first = node;
        }
    }
}

class DoublyLinkedNode<E> {
    DoublyLinkedNode prev;
    DoublyLinkedNode next;
    E element;

    public DoublyLinkedNode(E element) {
        this.element = element;
    }
}

class KeyValuePair {
    int key;
    int value;

    public KeyValuePair(int key, int value) {
        this.key = key;
        this.value = value;
    }
}

#https://discuss.leetcode.com/topic/43961/laziest-implementation-java-s-linkedhashmap-takes-care-of-everything
This is the laziest implementation using Java's LinkedHashMap. In the real interview,
however, it is definitely not what interviewer expected.
# LinkedHashMap
# 84ms 77.58%
import java.util.LinkedHashMap;
public class LRUCache {
    private LinkedHashMap<Integer, Integer> map;
    private final int CAPACITY;

    public LRUCache(int capacity) {
        CAPACITY = capacity;
        //In the constructor, the third boolean parameter specifies the ordering mode.
        //If we set it to true, it will be in ascending order.
        //(https://docs.oracle.com/javase/8/docs/api/java/util/LinkedHashMap.html#LinkedHashMap-int-float-boolean-)
        //By overriding removeEldestEntry in this way, we do not need to take care of it ourselves.
        //It will automatically remove the least recent one when the size of map exceeds the specified capacity.
        //(https://docs.oracle.com/javase/8/docs/api/java/util/LinkedHashMap.html#removeEldestEntry-java.util.Map.Entry-)
        map = new LinkedHashMap<Integer, Integer>(capacity, 0.75f, true){
                protected boolean removeEldestEntry(Map.Entry eldest) {
                    return size() > CAPACITY;
                }
            };
    }

    public int get(int key) {
        return map.getOrDefault(key, -1);
    }

    public void put(int key, int value) {
        map.put(key, value);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */

# 126ms 24.69%
class LRUCache {
    Node head = null;
    Node tail = null;
    Map<Integer, Node> map;
    int cap = 0;
    public LRUCache(int capacity) {
        head = new Node(-1,-1);
        tail = new Node(-1, -1);
        head.next = tail;
        cap = capacity;
        map = new HashMap<>();
    }

    public int get(int key) {
        if(!map.containsKey(key)) return -1;
        Node node = map.get(key);
        moveToHead(node);
        return node.val;
    }

    public void put(int key, int value) {
        if(map.containsKey(key)) {
            Node n = map.get(key);
            n.val = value;
            moveToHead(n);
        } else {
            Node newNode = new Node(key, value);
            if(map.size() == cap) {
                Node last = tail.prev;
                int toRemoveKey = last.key;
                map.remove(toRemoveKey);
                last.prev.next = tail;
                tail.prev = last.prev;
                newNode.prev = head;
                newNode.next = head.next;
                head.next = newNode;
                newNode.next.prev = newNode;
            } else {
                newNode.next = head.next;
                newNode.prev = head;
                head.next = newNode;
                newNode.next.prev = newNode;
            }
            map.put(key, newNode);
        }
    }

    private void moveToHead(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
        node.prev = head;
        node.next = head.next;
        head.next = node;
        node.next.prev = node;
    }

    public class Node {
        int val;
        int key;
        Node next;
        Node prev;
        public Node(int k, int v) {
            key = k;
            val = v;
        }
    }
}

'''
