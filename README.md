<h1 align="center">
  combinatory-gradient-generator
</h1>

<p align="center">
  <b>Small program to generate gradient images combinating a set of given hex colours</b><br><br>
  <img src="https://img.shields.io/badge/Project-WIP-orange"> <img src="https://img.shields.io/badge/Documentation-Up%20to%20date-success"><!--<img src="https://img.shields.io/badge/Documentation-Outdated-orange">--> 
</p>

## Setup

- Download and unzip repository.
- Open cmd inside the folder.
- Activate python environment
  - `./venv/Scripts/Activate`
- With the environment activated, execute the program as explained in [Usage](#Usage):
  - `python cgg.py...`

## Features 

<details>
    <summary>TO-DO</summary>
  
- [ ] Option to introduce color list as text file.

</details>

- [x] Generates a gradient image from two colors
- [x] Generates gradient images from multiple colors by:
  - [x] Making every combination possible of 2 colors.
  - [x] Making pairs as long as the color amount is even.

## Usage

Execute cgg.py through the command prompt: <!-- using **Python 3.10 or higher**. -->

<p align="center">
  <code>python cgg.py [-h] [-d DIRECTORY] [-W WIDTH] [-H HEIGHT] [-m [{combinatory,pairs}]] [-v VERBOSE] colors [colors ...]</code>
</p>
<br>

- `directory` must be enclosed in quotes.

- `width` in pixels (default is 100).

- `height` in pixels (default is 200).

- `mode` Choose between combinatory or pairs mode. 

    - `-c COMBINATORY` Generates a gradient for every combination of the colors introduced.
    
    - `-p PAIRS` Generates gradients by selecting the colors introduced in pairs of two.

- `verbose` enables console output.

- `colors` list of hexadecimal color values separated by whitespaces.

Example:

    python cgg.py -v -W 10 -H 10 -m pairs ff0000 00ff00 0000ff ffffff

---
<p align="center">
 Contact me on <a href="https://twitter.com/ChgvCode">Twitter</a>
</p>
