# CSE-40437-Final-Project



### File Contents

* `crawler.py`
  * Usage: `crawler.py keyword1 [keyword2] ... [keywordn]`
  * Function: Starts a streaming filter on all of the n keywords provided. Writes the tweets gathered to `data/keyword.json` where keyword is a keyword specified as an argument to the program. 
* `reducer.py`
  * Usage: `reducer.py path/to/tweet/file1.json path/to/tweet/file2.json path/to/output/file.json`
  * Function: Creates or appends to a file (`path/to/output/file.json`) that contains all of the tweets that are common to `path/to/tweet/file1.json` and `path/to/tweet/file2.json`.
* `data/`
  * Directory to hold the tweets datasets gathered from `crawler.py` and produced by `reducer.py`.
