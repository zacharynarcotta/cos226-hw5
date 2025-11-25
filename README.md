# cos226-hw5
HW5: "Hash Something Out"
Zachary Narcotta
UMAINE 2025 FALL

# Method Reflection
## General
Generally, these functions were effective. I expected a lot of collisions because almost all of the data was entirely different and not simple (as in, integers). Also, I expected Linked List handling to perform better than Linear Probing, which was absolutely the case.

## Statistics
Each method I tried ended up being just a little faster, used just a little less space, and had just a few less collisions than the previous method. ASCII Addition (Probing) was, by far, the worst method in terms of construction time and collisions. 
When researching, I expected Polynomial Rolling Hash to be the fastest by a large margin, as it is the string hashing method that sees the broadest use in real-world data storage and hashing.
What I did not anticipate, though, was its time complexity; when roll-hashing by movie quotes, the size of the data become apparent, especially when both Probing and List handling took over a minute for the quotes (likely, the entire Bee Movie script is the culprit, but I digress).

## Effectiveness
Despite its time complexity issues with extremely large data, Polynomial Rolling Hash had the fewest collisions, and was also generally among faster methods. It makes efficient use of space while not being computationally intensive in its actual hash calculations. The "elephant in the room" with this method, though, is how significantly the effectiveness drops when the input data becomes extremely large. I would select this method over any others if I knew that my dataset is not thousands upon thousands of characters long.