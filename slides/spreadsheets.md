---
layout: presentation
title: Spreadsheets
permalink: /slides/spreadsheets/
---

class: center, middle

# Spreadsheets

Database Design

---

# Agenda

1. [Overview](#overview)
1. [Typical Example](#example)
1. [Imposing Criteria](#criteria)
1. [Further Exploration](#further-exploration)
1. [Conclusions](#conclusions)

---

name: overview

# Overview

---

template: overview

## Example files

The examples outlined on these slides is implemented in the following additional documents:

- [New York Times' COVID-19 data](https://github.com/nytimes/covid-19-data/) by US county by day since the start of the pandemic - raw data in CSV format.
- A subset of that data for only 19 September, 2022 - [available in Google Sheets](https://docs.google.com/spreadsheets/d/15ZMOzKe1bLB9bB6k87HVCpXX66Qnzy9vRx3f0osRvwI/edit#gid=0)
- A breakdown of that data for only New York's Hudson Valley region - [available in Google Sheets](https://docs.google.com/spreadsheets/d/1Q4J2NgwArqa-f-t-deEEEobmfQwKaEcFwseue8vAkUw/edit#gid=0)
- A breakdown of that data by state - [available in Google Sheets](https://docs.google.com/spreadsheets/d/1PS15N7Ixyt9Se5sM47YNMe_VBPJ5MZvQk1LUX91xenU/edit#gid=0)
- A time series breakdown of that data for New York's Hudson Valley - [available in Microsoft Excel's .xlsx format](https://docs.google.com/spreadsheets/d/1WjUeIkvWSsfJ-Yf8ibszzwp1gjNHYy4q/edit?usp=sharing&ouid=103688061522095437051&rtpof=true&sd=true)

---

template: overview

## Intro

Microsoft Excel, Apple Numbers, Google Sheets, and their spreadsheet software ilk organize data sets into _rows_ and _columns_.

![Spreadsheet with rows and columns](../files/data_formats/spreadsheet_structure.png)

--

- Each row and column has a _unique identifier_ - rows numbers and column letters.
  These indices are attached to the spreadsheet, not the data.

--

- At the intersection of each row and column is a _data cell_, where data of a variety of types can either be _manually input_ or _formulaically calculated_.

---

template: overview

## Programming environment

Behind the scenes in any spreadsheet software is a sophisticated _programming environment_ which can be accessed most simply by calling _built-in functions_ from the text within a data cell.

--

![Spreadsheet formula](../files/data_formats/spreadsheet_formula.png)

---

template: overview

## Programming environment

Users who are familiar with high-level computer programming concepts can write _custom functions_ using a spreadsheet software's _Integrated Development Environment_ (IDE).

![Spreadsheet integrated development environment](../files/data_formats/spreadsheet_ide.png)

---

template: overview

## Programming environment

The following spreadsheet softwares have integrated IDEs:

--

- **Microsoft Excel** has the Visual Basic for Applications Editor (VBA editor) .
  - Access from the `Developer` menu.
  - Programs are written in the Visual Basic programming language.

--

- **Google Sheets** has the Script Editor.
  - Access from the `Tools`->`Script Editor` menu.
  - Programs are written in Javascript.

--

- **Apple Numbers** integrates with Apple's automation language, AppleScript.
  - Access via Apple's Script Editor app.
  - Programs are written in AppleScript.

--

- **LibreOffice Calc** provides several scripting options.
  - Access in the `Tools`->`Customize` menu.
  - Program can written in Javascript, Python, LibreOffice Basic, and BeanShell.

---

template: overview

## Spreadsheets as databases

Spreadsheet software can be considered a type of database and, in fact, have much in common with more sophisticated _relational databases_.

--

- each sheet holds data about a single _entity_ - a kind of thing

--

- sheets hold _records_ - data about one instance of the entity (i.e. one of the things)

--

- each record has the same fixed set of _fields_ (i.e. there is a fixed schema)

--

- each _field_ represents one attribute of the record

--

- sheets are shown as _tables_, records are stored in _rows_, fields are in _columns_

--

- automated _functions_ allow you to filter the data and perform analysis

---

template: overview

## Data munging

Using a spreadsheet does not absolve one of doing data munging.

--

Some data munging tasks common to spreadsheets:

--

- Excessive **empty rows and columns** should be removed

--

- Make sure there are **easy-to-understand headings** to each column

--

- **Break up any fields that contain more than one piece of data** into multiple fields so each can be analyzed independently

--

- **Indicate data types** appropriate for each column to harness the programming power of spreadsheets

---

name: example

# Typical Example

--

## Raw data

We will look into data on the number of COVID-19 cases _aggregated_, updated daily, and _published_ by the New York Times in Comma-Separated Values (CSV) format.

--

![Raw CSV data](../files/data_formats/csv_raw_data.png)

--

- Access the raw data in CSV form [here](https://github.com/nytimes/covid-19-data/).

--

- In case you were wondering, the `fips` column holds unique identifiers for each county, according to the [FIPS system](https://en.wikipedia.org/wiki/FIPS_county_code).

---

template: example

## Import into spreadsheet

This particular data set contains a few _million records_ (thousands of new records are added each day). Upon importing the raw data file into a spreadsheet, we immediately hit a problem with spreadsheet software...

--

- With large data sets, spreadsheets often work slowly and sometimes don't work at all.

--

- Web-based (i.e. 'cloud'-based) spreadsheet programs, such as Google Sheets, have the hardest time processing large data sets and may crash.

--

- Native desktop applications, such as Microsoft Excel and Apple Numbers work significantly better with large data sets.

--

- If you must use a web-based spreadsheet for a large data set, use a plain text editor to first chop up the CSV file into a bunch of smaller CSV files and then import each smaller file into its own sheet (_not recommended_).

---

template: example

## A sheet for an entity

Once imported into a spreadsheet, the data appears in a typical nicely-aligned _row/column structure_.

![Spreadsheet with rows and columns](../files/data_formats/spreadsheet_structure.png)

--

- Each _row_ is a _record_ with _fields_ in the _columns_ describing various attributes of _one particular instance of the entity_.

--

- In this example, each row represents _COVID-19 stats for one day in one US county_ during the pandemic.

---

template: example

## Sorting rows

If we simply wanted to sort the rows by the number of cases or the number of deaths, we can do that with the click of a button.

--

- Highlight the entire data set (not including the headings), and the sort menu item (the exact position of this button varies by spreadsheet program).

![Sorting data in a spreadsheet](../files/data_formats/spreadsheet_sort.png)

---

template: example

## Simple statistics

Spreadsheets are great for simple statistical analysis, such as finding the _sum_, _average_, _minimum_, _maximum_, _standard deviation_, of a series of values.

--

- To do this, we will run formulas using the spreadsheet's _built-in functions_.

--

- To enter a formula into a cell, click into the cell and type the equals sign `=` followed by the formula.

--

- To calculate total deaths, enter `=SUM( F1 : F852846 )` into column `F` of a new row at the very end of the spreadsheet, where `F1` is the first cell in the deaths column, and `F852846` is the last value in that column - your last row number will differ. Hit the `enter/return` key when done.

![Sum of spreadsheet column](../files/data_formats/spreadsheet_sum_formula.png)

---

template: example

## Passing the smell test

Always use your common sense to think about whether the raw data and your analysis of that data make sense... the so-called _smell test_.

--

- Summing the values in the deaths column leads to a result of about _256 million deaths from COVID-19 in the US_ at the time of this writing.

--

- [Authoritative reports](https://coronavirus.jhu.edu/map.html) put that number at about _1,053,840 deaths_ at the time of this writing.

--

- Something does not smell good!

--

- Either the raw data is flawed, or we are wrong in our analysis.

--

- What went wrong?!

---

template: example

## The meaning of the data

Upon further inspection, it seem that each row in the data set represents the _cumulative data for that county_.

--

- So we have misunderstood the meaning of the data

--

- _a very very common problem_!

--

- Since each record includes a cumulative count of the deaths, in order to calculate total US deaths, we simply have to _sum the death counts for all counties on the most recent day available in the data set_: `= SUM( F849589 : F852846 )` (your row row numbers may differ if viewing more recent data)

--

- This results in a _total US death count of 1,050,282_ (as of September 19th 2022)... a better-smelling number.

--

- PS: this data set has already been munged well for us by The New York Times.... not all data sets will be so good!

---

template: example
name: assumptions

## Assumptions

In doing such a simple calculation, we have made a series of assumptions that we should be aware of, in case they prove to be false.

--

- We have assumed that the raw data is reliable and trustworthy

--

- We have assumed that no deaths are counted simultaneously in two or more different US counties

--

- We have assumed that the data set includes one record for every US county on each day

--

- How can we check these assumptions?

---

name: criteria

# Imposing Criteria

--

## Analyzing a subset of records

What if we wanted to count only _total COVID-19 cases in New York's Hudson Valley region_, which is composed of 11 of New York State's 62 counties..

--

- Basic statistical functions, such as `SUM()`, `AVERAGE()`, `MIN()`, `MAX()`, `STDEV()` work as we have seen when calculating total deaths. But they cannot filter the records for us.

--

- Remember, the counts are cumulative. So let's copy just the records for the most recent date and _put them into their own sheet_. This will speed up the program massively and is now small enough to be shared in a web-based spreadsheet - see [here](https://docs.google.com/spreadsheets/d/15ZMOzKe1bLB9bB6k87HVCpXX66Qnzy9vRx3f0osRvwI/edit#gid=0).

--

- We could manually go through and add up the case counts for the 11 counties of interest, but that would be very time consuming.

--

- Rather, we should use the _spreadsheet's filtering abilities_ to extract data from the rows representing the counties of interest to us, and then run our statistics functions on just those filtered results.

---

template: criteria

## Filtering records

To calculate _total COVID-19 case counts in New York's Hudson Valley region_, we will go step-by-step, rather than try to do everything at once.

--

- First create two new columns: one for county names and the other for case counts.

![Extraction column](../files/data_formats/spreadsheet_extraction_column.png)

---

template: criteria

## Filtering records (continued)

Now add a formula into the `Case count` field corresponding to the first county: `=SUMIF( B:B, H2, E:E )`. Note the use of `SUMIF` to add criteria.

--

- `SUMIF` will sum together case counts (column `E`) for any records where the county (column `B`) matches the county name of interest (cell `H2`).

--

- Copy this formula into the `Case counts` field for each county. Be sure to update `H2` to be the correct cell identifier for each county.

--

- You can use the spreadsheet's _autofill_ feature to do this copying for you.

--

![Extraction complete](../files/data_formats/spreadsheet_extraction_column_complete.png)

---

template: criteria

## Filtering records (continued again)

We now have total case counts for each county of interest. If we add them all up, we will have _total case counts for the entire Hudson Valley_.

--

- In our custom `Case counts` column, in a row below the last county of interest, enter a function to calculate the `SUM` of all case counts. A bit more than `835,749` as of 19 September 2022.

![Extraction summation](../files/data_formats/spreadsheet_extraction_column_total.png)

---

template: criteria

## Mashing up data sets

We know how many COVID-19 cases there have been in the Hudson Valley... but what percent of the population does this represent?

--

- Finding a reputable population estimate for each county is not difficult... ([for example](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html#par_textimage_739801612)). `Cases as % of population` is only a simple formula away.

![Data mashup](../files/data_formats/spreadsheet_mashup.png)

---

template: criteria

## Results

The completed spreadsheet is available [here](https://docs.google.com/spreadsheets/d/1Q4J2NgwArqa-f-t-deEEEobmfQwKaEcFwseue8vAkUw/edit#gid=0).

Our data and initial analysis suggest that _about 29% of the population in New York's Hudson Valley have had COVID-19_... that's almost 1 in every 3 people.

--

- Does this smell good?

  - Look over the numbers and do a sanity check.
  - Compare your results to other reputable sources of information and analysis.

--

- Where might we have gone wrong?

--

- What other assumptions might this result depend upon that we did not [originally consider](#assumptions).

---

template: criteria

## Results

We have made a mistake

--

of course.

--

- Our data contains COVID-19 cases for counties in all US states.

--

- Our use of the `SUMIF` functions add case counts for only those counties with particular names.

--

- We didn't consider that perhaps there might be counties with the same names in different states.
  There are.

--

- We need to apply two criteria - add only those rows where the county names AND the state names match.

--

- Whereas the `SUMIF` function can only apply one criterion, the `SUMIFS` function can apply multiple criteria.
  Look up documentation and try it out.

---

name: further-exploration

# Further Exploration

--

template: further-exploration

## Time series

It might be interesting to see how COVID-19 case counts vary over time.

--

- The original New York Times data set has cumulative case numbers for all dates since the pandemic began.

--

- Similarly to how we counted cases within the Hudson Valley, we could calculate cases for each date using `SUMIF` or `SUMIFS`, where we filter by only those rows that match a specific date.

--

- If we wanted to show case counts over time for only counties in the Hudson Valley, we would use `SUMIFS` to apply three criteria:

--

    - matching a specified **date**
    - matching a specified **county name**
    - matching the **state** of New York

---

template: further-exploration

## Time series

In order to easily do a time series analysis, it helps to line up our fixed values nicely.

![Set up for time series](../files/spreadsheets/covid-19-time-series-setup.png)

--

- Then fill in the empty data cells with formulae in the following pattern:

```excel
=SUMIFS($E:$E, $C:$C, "New York", $A:$A, J$3,  $B:$B, $I4)
```

--

- Where `E` is the case count column, `C` is the state column, and `A` is the date column, `$J3` is the cell with our desired date, `B` is the county name column, and `$I4` is the cell with our desired county name.

---

template: further-exploration

## Time series

At the end, we can easily click the spreadsheet's line chart button to produce:

![Hudson Valley COVID-19 cumulative cases per month](../files/spreadsheets/covid-19-time-series-chart.png)

---

template: further-exploration

## Time series

We have produced an easy-to-understand chart of cumulative case counts in the Hudson Valley since the start of the pandemic.

--

- Rather than cumulative counts, how would we calculate the change in case counts over time?

--

- Hint, you will simply have to subtract the previous month's cumulative case count from each month.

--

- [Download an example Excel file](https://docs.google.com/spreadsheets/d/1WjUeIkvWSsfJ-Yf8ibszzwp1gjNHYy4q/edit?usp=sharing&ouid=103688061522095437051&rtpof=true&sd=true) to see these explorations for yourself.

---

template: further-exploration

## Visualizations

Visualizations can help people infer insights that may not be obvious by staring at numbers.

--

Spreadsheets are remarkably good at generating simple visualizations, such as:

--

- Line charts

--

- Area charts

--

- Column & bar charts

--

- Pie charts

--

- Scatter plots

--

- ... and more

---

template: further-exploration

## Pivot tables

Pivot tables are a very powerful feature of spreadsheets that allow us to group together records based on one or more shared field values, and then automatically perform aggregate statistics on each group.

--

For example, using a pivot table, we might easily group all counties in our data set by state, and then perform statistics on each state, potentially showing us:

--

- total case counts per state

--

- total deaths per state

--

- the miinimum and maximum case counts per state

--

See [an example of this data with a pivot table and a map chart](https://docs.google.com/spreadsheets/d/1PS15N7Ixyt9Se5sM47YNMe_VBPJ5MZvQk1LUX91xenU/edit#gid=0).

---

name: conclusions

# Conclusions

--

Thank you. Bye.
