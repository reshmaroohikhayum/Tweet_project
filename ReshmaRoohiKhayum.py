import pickle
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt
from collections import defaultdict
import geopandas as gpd

tweets = []
file_destination = '10ktweetsjan2020.jsonl'
with open(file_destination, "rb") as openfile:  
    tweets.append(pickle.load(openfile))  
tweets = tweets[0]  

tweets_text = []

for tweet in tweets:
    tweets_text.append(tweet['full_text'])


#1a start : Analysis type 1
text = ' '.join(tweets_text)
tokens = word_tokenize(text)
tokens = [word.lower() for word in tokens]

words = []

for word in tokens:
    if word.isalpha():
        words.append(word)

stop_words = set(stopwords.words('english'))
words = [word for word in words if word not in stop_words]

word_freq = Counter(words)
common_words = word_freq.most_common(15)

words = []
frequencies = []

for word, freq in common_words:
    words.append(word)
    frequencies.append(freq)

plt.bar(words, frequencies, color='yellow')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 15 Most Frequent Words apart from stopwords')
plt.show()
#1a end

#1b start : Analysis type 2
sources = [tweet['source'] for tweet in tweets]
source_freq = Counter(sources)
common_sources = source_freq.most_common(10)

source_names = []
frequencies = []

for source, freq in common_sources:
    start = source.find('>') + 1
    end = source.find('</a>')
    
    source_name = source[start:end]
    source_names.append(source_name)
    frequencies.append(freq)
    #print(source_name, freq)

plt.bar(source_names, frequencies, color='Pink')
plt.xlabel('Source')
plt.ylabel('Frequency')
plt.title('Most Common Tweet Sources')
plt.show()
#1b end

#2a MID-TERM question : Is there a specific time when users with a high number of followers or friends tend to tweet?
high_followers_threshold = 1000  
tweet_times = []

for tweet in tweets:
    user = tweet['user']
    if user['followers_count'] > high_followers_threshold or user['friends_count'] > high_followers_threshold:
        tweet_time = pd.to_datetime(tweet['created_at'])
        tweet_times.append(tweet_time.hour)

hour_freq = Counter(tweet_times)
hours, frequencies = zip(*hour_freq.items())

plt.bar(hours, frequencies, color='green')
plt.xlabel('Hour of Day')
plt.ylabel('Tweet Frequency')
plt.title('Tweet Frequencies by Hour for Users with High Followers/Friends')
plt.xticks(range(24))  
plt.show()
#2a end

# 2b start : To display the hashtags used by the user who has more than 2500 followers
hashtags = []
for tweet in tweets:
    if 'retweeted_status' not in tweet and tweet['user']['followers_count'] > 2500:
        entities = tweet.get('entities', {})
        hashtags.extend([hashtag['text'] for hashtag in entities.get('hashtags', [])])

hashtag_counter = Counter(hashtags)

top_hashtags = hashtag_counter.most_common()
print("\nThe top hashtags used by user who has more than 2500 followers in the given dataset are:")
for hashtag, count in top_hashtags:
    print(hashtag, " used ", str(count), " times")
#2b end

#3a start
entities_lengths = {}

for tweet in tweets: 
    for k, v in tweet['entities'].items():
        if k not in entities_lengths:
            entities_lengths[k] = [0, 0]  
        entities_lengths[k][0] += len(v)
        entities_lengths[k][1] += 1

average_lengths = {k: v[0]/v[1] for k, v in entities_lengths.items()}

plt.bar(average_lengths.keys(), average_lengths.values(),color='orange')
plt.title('Average lengths of the fields in "entities"')
plt.show()
#3a end

#3b start
user_bools = defaultdict(lambda: [0, 0])

for tweet in tweets: 
    for k, v in tweet['user'].items():
        if isinstance(v, bool):
            user_bools[k][v] += 1

user_bools = {k: v for k, v in user_bools.items() if v[0] > 0 and v[1] > 0}

cols = 2
rows = 2  

for i in range(0, len(user_bools), rows*cols):
    fig, axs = plt.subplots(rows, cols, figsize=(10, 10))
    for ax, (k, v) in zip(axs.flatten(), list(user_bools.items())[i:i+rows*cols]):
        ax.pie(v, labels=[str(False), str(True)], autopct='%1.1f%%')
        ax.set_title(f'Boolean field "{k}" in "user" for all tweets')
    plt.tight_layout()
    plt.show()
#3b end

#3c start
usernames = list({tweet['user']['name'] for tweet in tweets})
first_chars = [name[0].upper() for name in usernames]
char_counts = Counter(first_chars)

x = [chr(i) for i in range(ord('A'), ord('Z')+1)] 
y = [char_counts.get(char, 0) for char in x]

plt.figure(figsize=(10, 5))
plt.plot(x, y, marker='o')
plt.title('Number of Users per Starting Alphabet Letter')
plt.xlabel('Alphabet Letters')
plt.ylabel('Number of Users')
plt.grid(True)
plt.show()
#3c end

#3d start
country_counts = {}
for tweet in tweets:
    if tweet['user']['location']: 
        country = tweet['user']['location']
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

world['user_counts'] = world['name'].map(country_counts)

fig, ax = plt.subplots(1, 1)
world.plot(column='user_counts', ax=ax, legend=True, cmap='Reds')

ax.set_xticks([])
ax.set_yticks([])

ax.set_title("Concentration of Twitter users from different locations")

plt.show()
#3d end