# CSE-40437-Final-Project



### File Contents
* `scripts/`
  * `analyzer.py`
    * Usage: `analyzer.py path/to/tweet/file.json path/to/output/file.csv`
    * Function: generates popularity scores for products for each day in the dataset provided. Writes out the dates and scores in a comma separated format to the filename provided to the script.
  * `crawler.py`
    * Usage: `crawler.py keyword1 [keyword2] ... [keywordn]`
    * Function: Starts a streaming filter on all of the n keywords provided. Writes the text, id, and created_at field of tweets gathered to `data/keyword.json` where keyword is a keyword specified as an argument to the program. 
  * `reducer.py`
    * Usage: `reducer.py path/to/tweet/file1.json path/to/tweet/file2.json path/to/output/file.json`
    * Function: Creates or appends to a file (`path/to/output/file.json`) that contains all of the tweets that are common to `path/to/tweet/file1.json` and `path/to/tweet/file2.json`.
  * `simplify_colon.py`
    * Usage: `simplify_colon.py path/to/tweet/file.txt path/to/output/file.json`
    * Function: Changes tweet from antiquated format separated by colons to a json format. Ingnores tweets that are not created in 2017 or have "2017\n" in tweet text.
  * `simplify_json.py`
    * Usage: `simplify_json.py path/to/tweet/file.json path/to/output/file.json next_field`
    * Function: Changes tweet from full json (found in `path/to/tweet/file.json`) to reduced json, where only the text, id, and created_at field exist. Write a newfile named `path/to/output/file.json`. `next_field` argument is the dictionary entry of the entry that follows the text field.
  * `frequent_words.py`
    * Usage: `frequent_words.py path/to/tweet/file.json`
    * Function: Prints out the ten most frequent adjectives in the input file.
  * `smoother.py`
    * Usage: `smoother.py ratings.csv k output.csv`
    * Function: Takes the rating information from ratings.csv and outputs a similar file with new ratings computed by the k day moving average smoothing function in output.csv.
* `data/`
  * Directory to hold the tweets datasets gathered from `crawler.py` and produced by `reducer.py`.
* `results/`
  * Directory to hold the csv files generated from `analyzer.py`.
* `sentiment_analysis/`
  * Directory that holds downloaded sentiment analysis tools to use in `analyze.py`.
