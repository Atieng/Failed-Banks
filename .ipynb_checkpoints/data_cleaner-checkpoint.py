class DataCleaner:
    def __init__(self, dataframe):
        self.df = dataframe.copy()
    
    def drop_columns(self, columns):
        """Drop specified columns from the DataFrame."""
        self.df = self.df.drop(columns=columns)
    
    def drop_columns_by_null_threshold(self, threshold):
        """Drop columns with a percentage of null values above the threshold."""
        null_percentages = self.df.isnull().mean() * 100
        columns_to_drop = null_percentages[null_percentages > threshold].index.tolist()
        self.df = self.df.drop(columns=columns_to_drop)
        return columns_to_drop
    
    def get_clean_data(self):
        """Return the cleaned DataFrame."""
        return self.df
