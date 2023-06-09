
# NST Challenge

#### This repository will demonstrate the steps taken to solve the NST challenge that is mentioned below.
---
Company send you to a conference!

You head off to the airport and when it’s time to board your flight, you discover a problem; you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the other passengers.

Not to worry, you write a quick program to use your phone's camera to scan all of the nearby boarding passes (your input); perhaps you can find your seat through the process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like **FBFBBFFRLR**, where F means "front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

For example, consider just the first **seven** characters of **FBFBBFFRLR**:

Start by considering the whole range, rows 0 through 127.\
F means to take the lower half, keeping rows 0 through 63.\
B means to take the upper half, keeping rows 32 through 63.\
F means to take the lower half, keeping rows 32 through 47.\
B means to take the upper half, keeping rows 40 through 47.\
B keeps rows 44 through 47.\
F keeps rows 44 through 45.\
The final F keeps the lower of the two, **row 44**.\

The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last **three** characters of **FBFBBFFRLR**:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, **column 5**.
So, decoding **FBFBBFFRLR** reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = **357**.

Here are some other boarding passes:

**BFFFBBFRRR**: row 70, column 7, seat ID 567.
**FFFBBBFRRR**: row 14, column 7, seat ID 119.
**BBFFBBFRLL**: row 102, column 4, seat ID 820.

As a sanity check, look through your list of boarding passes. **What is the highest seat ID on a boarding pass?**

As it’s time to board... **you’ll also need to find your seat ID!**

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though the seats with IDs +1 and -1 from yours will be in your list.

**What is the ID of your seat?**
## Thought Process

#### Let's first see what the challenge's requests are.
* What is the highest seat ID on a boarding pass?
* What is the ID of your seat?

#### Now let's see what main piece of information is available.
* The input file has 859 instances binary encoded using letters F, B, L, and R.
* 7 characters were used to show rows from 0 to 127.
* 3 characters were used to show seat columns from 0 to 7.
* Seat ID = multiply the row by 8, then add the column.
* It's a completely full flight.
* Some of the seats at the very front and back of the plane don't exist on this aircraft.
* Your seat wasn't at the very front or back.
* The seats with IDs +1 and -1 from yours will be in your list.

#### What are my initial thought?
* 7 characters, 128 rows, only two different characters. It is a 7 bit binary that F and B represent 0 and 1. **FBFBBFF** is row 44. 44 in binary is '0101100'. F = 0 and B=1.
* 3 characters, 8 seat columns, only two different characters. It is a 3 bit binary that R and L represent 0 and 1. **RLR** is seat column 5. 5 in binary is '101'. L = 0 and R=1.
* multiplying by 8 basically means shifting the binary 3 bits to the left to make space for the seat column.
* Replace F and L with 0, and B and R with one to get the seat ID.
* Examining the hypothesis:
    * **FBFBBFFRLR** => 357 = 0101100101 &check;
    * **BFFFBBFRRR** => 567 = 1000110111 &check;
    * **FFFBBBFRRR** => 119 = 0001110111 &check;
    * **BBFFBBFRLL** => 820 = 1100110100 &check;
* Considering the range for rows and columns, we can have a maximum of 1024 seats encoded using the binary replacement method.

* Not all the seats are present. The instances given are not at the very front or back. It means that the available seats are in the middle. So we have a minimum seat ID and a maximum seat ID that are not 0 and 1023.

* My seat has neither the minimum nor the maximum ID. As minimum ID -1 and maximum ID + 1 are not available.

* There are 859 lines in the input.txt. I wasn't told that the data is clean. So I need to be aware of any duplicate instances.
* It is a completely full flight. So maximum ID - minimum Id + 1 = the number of available seats.

* 
