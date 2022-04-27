Tom needs help

Tom is a computer science student studying a mysterious websocket address he found in an internet forum that challenged  all readers, and if he succeeded, 
he would discover the identity of none other than Satoshi Nakamoto.

The operation of this websocket stream is very simple: it consists of connecting and receiving every 100 ms, 100 different JSON with the same structure: 


Analyzing, Tom realized something, a pattern, if we organize the data In a certain way, very valuable information could be obtained that would help us to complete the
challenge. Tom thinks that the parameter “a” represents an index and the “b” is a number taken from a strange and unknown numerical sequence, which he does not know the formula yet. That's why, he created a system of 100 blocks of information with the same structure that contained a summary of one minute, with the behavior of the values ​​obtained from "b". 

The structure used is the following:


The first data represents what was the highest number obtained from "b" in that period of time.
The second, the smaller number.
The third, the first number obtained.
The fourth, the last number.
The fifth is a counter that tells us how many of those numbers were prime numbers.
The sixth, another counter but it tell us how many were even numbers.
The seventh, a counter that tells us how many numbers were odd.

Tom needs to collect all that information in the different blocks and print them every
minute that goes by and then restart them, to continue processing new data to come,
this will help him analyze their behavior over time. But he has a problem
Tom, despite being a computer science student, does not know how to program!
then he asks for our help, are you willing to help Tom? 

Resources you may need for the test:

You need to figure out which port that you are going to be able to connect!

1. ws://209.126.82.146 (Mysterious websocket address provided by a mysterious user in the strange forum that returns the previously explained data)/
2. https://github.com/kython28/websockh (A simple websocket client library for C) 
3. https://janv.people.uic.edu/mcs572/mcs572notes/lec10.html (Introduction to Pthreads)
4. https://www.geeksforgeeks.org/linked-list-set-1-introduction/ (Linked list introduction) 
5. https://www.geeksforgeeks.org/fifo-first-in-first-out-approach-in-programming/ (FIFO (First-In-First-Out) approach in Programming)


To Run The Project:
 First activate your venv
 -source venv/bin/activate
 -pip install websockets
ws://209.126.82.146 (This websocket was working i created my own on localhost and port 8000)

before running server.py file please free the localhost port 8000
 First you need to run the server file 
-python server.py

Second you need to run the client file
-python client.py

result will be printed on terminal