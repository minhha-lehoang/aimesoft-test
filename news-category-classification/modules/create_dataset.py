import pandas as pd
from sklearn.model_selection import train_test_split
import os


# Load the data
data_dir = './news+aggregator/newsCorpora.csv' # Path to the dataset
news = pd.read_csv(data_dir, sep='\t', header=None)
news.columns = ['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP']

# Map the category to the actual category name
category = {
    'b': 'Business',
    't': 'Science and Technology',
    'e': 'Entertainment',
    'm': 'Health'
}
news['CATEGORY'] = news['CATEGORY'].map(category)

# Filter the news from chosen publishers
publishers = ['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail']
news = news[news['PUBLISHER'].isin(publishers)]

# Shuffle the data
news = news.sample(frac=1).reset_index(drop=True)

# Train, validation, test split
train, val = train_test_split(news[['ID', 'TITLE', 'CATEGORY']], test_size=0.2, random_state=42, stratify=news['CATEGORY'])
val, test = train_test_split(val, test_size=0.5, random_state=42, stratify=val['CATEGORY'])


# Save the data
if not os.path.exists('../news_extracted'):
    os.makedirs('../news_extracted')
train.to_csv('../news_extracted/train.txt', index=False, sep='\t')
test.to_csv('../news_extracted/test.txt', index=False, sep='\t')
val.to_csv('../news_extracted/val.txt', index=False, sep='\t')


if __name__ == '__main__':
    print('Dataset created successfully!')