import pandas as pd
import os
import re


class TestAnalays(object):
    def __init__(self):
        self.source_dataframe = pd.DataFrame()

    def open_resource(self):
        file_path = 'EXCEL'
        for file_path, dirname, file_names in os.walk(file_path):
            print(file_path, dirname, file_names)
            for file_name in file_names:
                file_type = re.findall(r'.csv|.xlx', file_name)[0]
                file_soure = os.path.join(file_path, file_name)
                if file_type == '.csv':
                    sub_source_dataframe = pd.read_csv(file_soure)
                elif file_type == '.xlx':
                    sub_source_dataframe = pd.read_excel(file_soure)
                else:
                    raise Exception('No File in EXCEL FILE PATH')
                if self.source_dataframe.empty:
                    self.source_dataframe = sub_source_dataframe
                else:
                    self.source_dataframe = pd.concat(self.source_dataframe, sub_source_dataframe)
        return self.source_dataframe

    def test_result_classify(self, source_dataframe):
        data_groups = source_dataframe.groupby([''])
        pass


if __name__ == '__main__':
    analysis_tool = TestAnalays()
    dataframe = analysis_tool.open_resource()
    analysis_tool.test_result_classify(dataframe)

