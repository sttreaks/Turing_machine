# Turing_machine

## Turing machine implemintation 
Turing machine is using unary (only 0 and 1 symbols) alphabet. There are some examples how it works:
At the start and at the end of tape there must be a ```“0”``` drawn
A132 (University example):
Input tape: ```0011111110```
Machine finds all ```"0"``` before ```"1"``` and deletes shift 1s so that only 1 ```"0"``` stay before 1s.
Summing 2 intrgers:
Integer, in unary system, presented as n+1 ```"1"```, so if we present 0 as tape it seems like ```"010"``` 4 seems like ```"0111110"``` etc.
So tape for suming 5 and 5 seems like ```"011111101111110"```. For correct summing we need to shift second substring (delete ```"0"``` between integers), then we need to and delete 1 ```"1"``` becouse it is responsible for 0.
Correct machine will return such a string: ```"0111111111110"```.

Multipling to integers:
Firstly, we need to check multipling by 0 and delete all extra ```"1"```. Secondly, if both integers ```>0``` we need to create algorithm for multipling.

Here is explaining of my realisation:
Multiplication is same as summing num to itself n times Firstly we want to delete "1" on second integer. It will help us to copy num n times correctly.
```"011101110" -> "01110110"```
Now we need to start replicating.
We are changing last ```"1"``` on ```"0"```, it is needed for understanding that we are already replicated second num 1 time.
How do we replicate second num? We successively replace ```"1"``` on ```"0"``` and then add extra ```"1"``` at the end of tape we will return ```"1"``` that we replaced back (if we dont we will lose our second num and multipling will be broken). Then we need to repeat that operation with all next ```"1"``` of second num.
Here you can see how it works:
```
"01110110"
"011000101"
"011001101"
"0110010011"
"0110011011"
```
When replicating of second num will be done, we will return to the first num and delete second ```"1"``` to copy second num one more time. When from first will remain only ```"1"``` (as we know it means 0) we will understand that copying n times done and all that we need is to shift result to this ```"1"``` at the start of tape (before shifting we will delete second num because it is useless now).
Here you can see full machine working cycle for better understanding.
```
011101110
01110110
01100110
01100010
0110001010
0110011010
0110010010
01100100110
01100110110
01000110110
01000010110
010000101110
010001101110
010001001110
0100010011110
0100011011110
0100001011110
0100000011110
0100000001110
0110000001110
0110000000110
0111000000110
0111000000010
0111100000010
0111100000000
0111110
```
This is somewhat beautiful process, isn’t it?
Using the program you can turn on logging and watch it multiplying bigger data. Enjoy.


