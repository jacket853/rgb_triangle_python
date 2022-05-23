# rgb_triangle_python
the Exeter rgb triangle using the Zelle graphics library

This program is designed to help students using the Exeter textbook Mathematics 2. The problem in question is #735:

A close look at a color television screen reveals an array of thousands of tiny red, green, and blue dots. This is because 
any color can be obtained as a mixture of these three colors. For example, if neighboring red, green, and blue dots are 
equally bright, the effect is white. If a blue dot is unilluminated and its red and green neighbors are equally bright, 
the effect is yellow. In other words, white corresponds to the red:green:blue ratio ⅓:⅓:⅓ and pure yellow corresponds to 
½:½:0. Notice that the sum of the three terms in each proportion is 1. A triangle RGB provides a simple model for this 
mixing of colors. The vertices represent three neighboring dots. Each point C inside the triangle represents a precise 
color, defined as follows: The intensities of the red dot, green dot, and blue dot are proportional to the areas of the 
triangles CGB, CBR, and CRG, respectively. What color is represented by the centroid of RGB? What color is represented by 
the midpoint of side RG?

Related problems include: #s 736, 737, 747, 748

To use this program:
- Open (double-click) the file named "JackHarveyRGBTriangle.py" in your Finder or File Explorer
	- A graphics window titled "RGB Triangle Visualization" should pop up in your screen.
- Simply click around inside the triangle: the black dot that starts at the centroid of the triangle moves where you 
clicked your mouse
	- This dot represents the point "C" in the above problem. Behind the scenes, this program is calculating the areas 
of these three triangles, and using the RGB triplet sytax (where any color is defined as color(r, g, b), where r, g, and 
b are integers between 0-256, determining the light's intensity.) to convert those proportions into a color
	- This color is determined through "hexadecimals" - these special numbers determine where a color is on the light 
spectrum, as well as its shade - white is (255, 255, 255), and its hexadecimal is #FFFFFF. Black -> (0, 0, 0) -> #000000
- Lastly, clicking the black circle will smoothly close the program - using the red "X" to close the program works, but 
bypasses some code, and therefore throws an error if you decide to run this program through the terminal/cmd.

Opening through Finder (on Mac) or File Explorer (Windows):
- Double-click on the .py file to open
Opening through terminal (on Mac) or command prompt (windows):
- Make sure you have at Python 3.9.6 or later installed
- Install the following packages through these commands - MUST BE INSTALLED IN/MOVED TO THE SAME DIRECTORY:
	- Mac: python3 -m pip install math
	       python3 -m pip install graphics (you need to download this file and save it the same directory you are 
	       using the .py file in: https://drive.google.com/file/d/1Z05lzCFR7J84w3-xjno9S7rP8lmwtPRA/view
	- Windows: py -m pip install math
		   py -m pip install graphics (https://drive.google.com/file/d/1Z05lzCFR7J84w3-xjno9S7rP8lmwtPRA/view)
- Run the file
	- Mac: python3 JackHarveyRGBTriangle.py
	- Windows: python JackHarveyRGBTriangle.py
