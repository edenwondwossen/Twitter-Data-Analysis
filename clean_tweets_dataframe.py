import csv
import pandas as pd
class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    def __init__(self, df:pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')
        
    def drop_unwanted_column(self, df:pd.DataFrame, column: list)->pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        df.drop(columns=column, inplace=True)
        
        return df
    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows
        """
        
        df = df.drop_duplicates()
        
        return df
    def convert_to_datetime(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert column to datetime
        """
        df['created_at'] = pd.to_datetime(df['created_at'], format='%y%m%d')
        
        df = df[df['created_at'] >= '2020-12-31' ]
        
        return df
    
    def convert_to_numbers(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        df[['polarity','subjectivity', 'retweet_count','favourite_count']] = pd.to_numeric(df['polarity', 'subjectivity', 'retweet_count', 'favorite_count'])
        
        return df
    
    def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove non english tweets from lang
        """
        
        df = df[df["lang"] == "en"]
        
        return df
if __name__ == "__main__":
    columns = ['hashtags', 'user_mentions']
    df = pd.read_csv('processed_tweet_data.csv')
    tweet = Clean_Tweets(df)
    cleaned_data = tweet.drop_unwanted_column(df,columns)
    cleaned_data = tweet.drop_duplicate(df)
    #datetime = tweet.convert_to_datetime(df)
    #numbers = tweet.convert_to_numbers(df)
    cleaned_data = tweet.remove_non_english_tweets(df)
    print(cleaned_data)
    cleaned_data.to_csv('modified_processed_tweet_data.csv')