# CSE-40437-Final-Project


### Requirements
The following python packages might be required to run some of the scripts.

* tweepy
* vader
* lxml
* pyquery
* nltk
* matplotlib
* wordcloud

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
  * `get_old_tweets.py`
    * Usage: `get_old_tweets.py keyword since_date until_date outfile.json`
    * Function: Gets 10000 tweets with the given keyword which were created at the two given times. Writes the resulting tweet id, created_at time, and tweet text to the file outfile.json.
  * `create_word_cloud_file.py`
    * Usage: `create_word_cloud_file.py ratings.csv`
    * Function: Creates a file named temp.txt which has each of the adjectives in the ratings printed a proportional number of times.
  * `wordcloud.sh`
    * Usage: `wordcloud.sh ratings.csv outimage.png`
    * Function: Creates a wordcloud image named outimage.png based on the adjectives found in ratings.csv.
  * `wordcloud_cli.py`
    * Usage: `wordcloud_cli.py --help`
    * Function: Creates wordcloud images. Taken from https://github.com/amueller/word_cloud.
  * `find_bad_lines.py`
    * Usage: `find_bad_lines.py tweets.json`
    * Function: Prints out all of the lines that are not valid JSON, with the intention of deleting those lines.
* `data/`
  * Directory to hold the tweets datasets gathered from `crawler.py` and produced by `reducer.py`.
* `results/`
  * Directory to hold the csv files generated from `analyzer.py`.
* `sentiment_analysis/`
  * Directory that holds downloaded sentiment analysis tools to use in `analyze.py`.
* `images/`
  * Folder that holds word cloud images.
* `website/`
  * Contains website files and scripts.
