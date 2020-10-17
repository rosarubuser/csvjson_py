# CSV and JSON converter

The tool helps to convert between CSV and JSON format files.

## Installation
Require Python 3+

## Usage
In the Terminal, run csv_json.py inputFileName outputFileName convertMethod.

For example:
```bash
python csv_json.py testing result csv2js
```
You must input three arguments.

The first is the input file name. You should not include the suffix.

The second is the output file name. Also, you should not include the suffix.

The last argument is to choose the converting method. You should input either csv2js (represents csv to json format) or js2csv (represents json to csv format).

The resulting file will be produced in the folder **test**.


Here is an example of showing the result from changing csv file to json file
(The example code is contained in the package):
```
album, year, US_peak_chart_post
The White Stripes, 1999, -
De Stijl, 2000, -
White Blood Cells, 2001, 61
Elephant, 2003, 6
Get Behind Me Satan, 2005, 3
Icky Thump, 2007, 2
Under Great White Northern Lights, 2010, 11
Live in Mississippi, 2011, -
Live at the Gold Dollar, 2012, -
Nine Miles from the White City, 2013, -
```
After running the command line above, it'll give a json output file in the folder **test**.
```
{
    "album": "The White Stripes",
    "year": "1999",
    "US_peak_chart_post": "-"
}
{
    "album": "De Stijl",
    "year": "2000",
    "US_peak_chart_post": "-"
}
{
    "album": "White Blood Cells",
    "year": "2001",
    "US_peak_chart_post": "61"
}
{
    "album": "Elephant",
    "year": "2003",
    "US_peak_chart_post": "6"
}
{
    "album": "Get Behind Me Satan",
    "year": "2005",
    "US_peak_chart_post": "3"
}
{
    "album": "Icky Thump",
    "year": "2007",
    "US_peak_chart_post": "2"
}
{
    "album": "Under Great White Northern Lights",
    "year": "2010",
    "US_peak_chart_post": "11"
}
{
    "album": "Live in Mississippi",
    "year": "2011",
    "US_peak_chart_post": "-"
}
{
    "album": "Live at the Gold Dollar",
    "year": "2012",
    "US_peak_chart_post": "-"
}
{
    "album": "Nine Miles from the White City",
    "year": "2013",
    "US_peak_chart_post": "-"
}
```