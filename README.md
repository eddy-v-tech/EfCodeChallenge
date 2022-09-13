## EF Ultimate Break Code Challenge

# Requirements

  * Python 3.6 or above
  * A json file named lazy-load.json in the same directory as challenge.py

> This code makes use of the json library

# Test Data Information

The following files are described by how they test the challenge.py solution

lazy-load.json - The original example file given

lazy-load-2.json - The smaller example json given in the instructions

lazy-load-3.json - Getting the ids of the images deeper in original example the file by removing the first banner and two sliders

lazy-load-4.json - Empty example

lazy-load-5.json - Example of deeper nested content and gallery usage

# Sample Execution & Output

Run using the following command and the data.json provided

```
python3 challenge.py
```

the following usage messages will be displayed.

```
Found image containing component: banner
With id: 4eda6cda-0222-4855-a045-f88f529fa8a7
This id will be added to the list of immediately loaded image components

Found image containing component: image
With id: b6c1da2b-d880-4e94-beeb-76cd0f21b8db
This id will be added to the list of immediately loaded image components

Found image containing component: slider
With id: e597d3b8-0837-4210-aa53-fe82f9da2b64
This id will be added to the list of immediately loaded image components

Maximum amount of ids found stopping search

The following ids correspond with image components to be loaded immediately:

banner: 4eda6cda-0222-4855-a045-f88f529fa8a7

image: b6c1da2b-d880-4e94-beeb-76cd0f21b8db

slider: e597d3b8-0837-4210-aa53-fe82f9da2b64
```