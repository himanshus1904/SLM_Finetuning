import pandas as pd

class Utils:
    def __init__(self):
        pass

    def df_to_csv(self, df, output_file):
        """Converts a df to csv"""
        df.to_csv(path_or_buf=output_file, index=False)
        return "CSV created and stored"

    def read_jsonfile(self, json_file_path):
        """Takes the file name and creates the dataframe"""
        df = pd.read_json(json_file_path, lines=True)
        return df

    def __call__(self, json_file_path, output_file):
        """The call method to handle calls to the Utils class"""

        df_json = self.read_jsonfile(json_file_path=json_file_path)
        result = self.df_to_csv(df=df_json, output_file=output_file)

        return result

if __name__ == "__main__":
    util_obj = Utils()
    json_file_path = '/Users/himanshusharma/Personal_Code/FineTune/data/News_Category_Dataset_v3.json'
    output_file = "/Users/himanshusharma/Personal_Code/FineTune/data/News_Category.csv"
    print(util_obj(json_file_path, output_file=output_file))