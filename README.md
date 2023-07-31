# EuroMillionVisualizer

This project aims to give different visualization options for all results of the Euromillion since 2004 (beginning). 

## Requirements

- python
- requests (pip3 install requests)

## Usage

Call the API defined in `.env => API=` and write data to a local file.
Load data from file to process data.

### Functionalities

- call API to load data from a json body
- write data to a file
- load data from file


### To-do

- Add functions to extract data to use in graphs 
>*(i.e.: number of appearance of a number, rate of appearance of a number, rate of a appearance of a number per year, etc...)*;
- Add graph generation;
- Represent most frequent winning number combinations;
- Add option to generate grids according to certain criteria;
>*(i.e.: most likely numbers to appear this year, numbers that haven't appeared much this year/this decade/ever/this month)*
