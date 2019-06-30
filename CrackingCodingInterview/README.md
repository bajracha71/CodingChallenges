# Cracking Coding Interview Problems

## Arrays

1.1. Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structure?

1.2. Implement a function void reverse(char* str) in C or C++ which reverses a null-terminated string.

1.3. Given two strings, write a method to decide if one is a permutation of the other

1.4. Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end of the string to hold the additional characters, and that you are given the "true" length of the string. (Note: if implementing in java or python please use a charcter array so that you can perform this operation in place.)

1.5. Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string.

1.6 Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate image by 90 ( write a program for both clockwise and anticlockwise rotation). Can you do this in place? (This is difficult)

1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0 (This is tricky)

1.8 Assume you have a method `isSubstring` which checks if one word is a substring of another. Given two strings, `s1` and `s2`, write code to check if `s2` is a roation of `s1` using only one call to `isSubstring` (eg. `waterbottle` is a rotation of `erbottlewat`)

## Linked Lists

2.1 Write code to remove duplicates from an unsorted linked list.

- Follow up: How would you solve this problem if a temporary buffere is not allowed? With no extra space, it will take time O(n^2) and O(1) space.

2.2 Implement an algorithm to find the kth to last element of a singly linked list

2.3 Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.

2.4 Write a code to partition a linked list around a value x, such that all nodes less than x comes before all nodes greater than or equal to x

2.5. You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the Ts digit is at the head of the list. Write a function that adds the two numbers and returns the sum
as a linked list.

2.6 Given a circular linked list, implement an algorith which returns the node at the beginning of the loop.

2.7 Implement a function to check if a linked list is a palindrome
