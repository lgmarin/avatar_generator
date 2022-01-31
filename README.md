# Python Avatar Generator

## _Yet another Snake game in Python_
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)

Avatar Generator built in Python.

- Can generate random images, a SHA1 hash is created for each image
- Can generate a list of all possible combinations

## Objectives

Develop a basic avatar generator, that can randomize the final avatar based on different assets.

* Python development and good config practices
* Using PIL library to work with png images
* Passing arguments to a Python code
* Working with file operations

## Dependencies

* pil - Python Image Library

## Usage

    python app.py PARAM
        --help  ->  Display help
        all     ->  Generate all possible combinations
        random  ->  Generate random avatar

    Assets need to be in an specific name style, inside the designated folder

        BG0x.png    -   Background
        SK0x.png    -   Skin
        EY0x.png    -   Eyes
        MO0x.png    -   Mouth