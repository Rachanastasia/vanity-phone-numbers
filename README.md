# Vanity Phone Number Generator

## Prompt

Vanity phone numbers are often displayed with letters instead of numbers, such as 1800flowers (18003569377). Write a program that, when provided with a potential phone number (3569377) and word (flower), returns all combinations containing the search word ("flowerp", "flowerq", "flowerr", "flowers"). For reference the numbers of a phone kepad map to letters as shown in the hash below. Note 0 and 1 do not have corresponding letters. 

Digit to Letter hash: 

0: [""]

1: [""]

2: ["a","b","c"]

3: ["d","e","f"]

4: ["g","h","i"]

5: ["j","k","l"]

6: ["m","n","o"]

7: ["p","q","r","s"]

8: ["t","u","v"]

9: ["w","x","y","z"]

Example:
1. Given "228" and "cat", matching strings would be "cat".

2. Given "2283" and "cat", matching strings would be "catd", "cate", "catf". 

3. Given "52283" and "cat", matching strings would be "jcatd", "jcate", "jcatf", "kcatd", "kcate", "kcatf", "lcatd", "lcate", "lcatf".

Bonus:
Vanity phone numbers often include numbers, as in 1-866-4ZIPCAR (1-866-4947227) where the number 4 is a homonym for 'for'. Expand the above algorithm to include the ability to match numbers in the search string.

Example:
Given "242287" and "4cats", matching strings would be "a4cats", "b4cats", "c4cats", "24cats".