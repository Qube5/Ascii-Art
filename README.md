# Ascii-Art
Ascii Art Generator

In main ascii.py file, settings are configurable to tune every image and level of detail.

The program takes a jpg, converts it to grayscale, and rescales it to the desired output dimensions.

Configurable variables:
jpg name
Output size
Output characters and what brightness range will map to each character

Note that python is unable to do extended ascii characters but a conversion is easy using find and replace in a text editor. I have commented out a suggested mapping in the map in the file and repeated here.

Mapping
* 0.1 : "0", #█
* 0.2 : "8", #▇
* 0.3 : "6", #▆
* 0.4 : "4", #▅
* 0.5 : "2", #▄
* 0.6 : "1", #▃
* 0.7 : "a", #▂
* 0.8 : "i", #▁
* 0.9 : ":", #▁
* 1.0 : ".", #  [space]

# Potential Improvements
* Inputting filename input and output in terminal
* Inputting output file size in terminal
