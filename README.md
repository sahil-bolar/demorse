---
# Demorse README.md
---

Python script to convert a sequence of dots and dashes (with no spaces) to all possible corresponding strings of letters.

What does .-. translate to from morse code? 
The answer might seem simple, since ".-." just corresponds to "r" in the English alphabet. 
But what if we don't know the spaces between letters?
.-. could just as well be ".- ." (ae), ". -." (en), or ". - ." (ete).
This program takes in an input string of dots and dashes and recursively runs through all possibilities of "words", 
though most of them will just be gibberish.

This idea came to me when my friend showed me his bracelet, which had a morse string on it: "-...--.---...-...---..-.". 
He told me it was a single word, and he wasn't sure if it was read left-to-right or right-to-left. Can you figure it out?
Note: This sequence will result in a LOT of outputs -- it took my laptop nearly 40 seconds to run through all possibilities 
  just for the left-to-right case!
  
<details>
  <summary>Hint!</summary>
  The word has exactly 10 letters. Print only the words that have 10 letters to the console. 
  There will still be many outputs, so I recommend scrolling quickly when the first few letters are obviously gibberish, 
  and slowing down when the starting few letters seem reasonable. 
</details>
