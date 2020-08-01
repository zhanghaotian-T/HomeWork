import pandas as pd
import os
import re


class TestAnalays(object):
    def __init__(self):
        self.source_dataframe = pd.DataFrame()

    def open_resource(self):
        file_path = 'EXCEL'
        for file_path, dirname, file_names in os.walk(file_path):
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
        sequence_id_dict = dict()
        filter_dataframe = dict()
        sequence_list = source_dataframe['SEQUENCE_COMMENTS'].unique()
        for sub_sequence_id in sequence_list:
            sequence_id = sub_sequence_id[:sub_sequence_id.rfind('ANT')]    # 根据分离出来的senary建立sequence的分类的空list和dataframe
            sequence_id_dict[sequence_id] = list()
            filter_dataframe[sequence_id] = pd.DataFrame
        for sub_sequence_id in sequence_list:
            sequence_id = sub_sequence_id[:sub_sequence_id.rfind('ANT')]    # 将sequence进行分类放入到不同的senarylist中
            sequence_id_dict[sequence_id].append(sub_sequence_id)
        data_groups = source_dataframe.groupby(source_dataframe['SEQUENCE_COMMENTS'])
        for sequence_filter in filter_dataframe.keys():
            for sequence in sequence_id_dict[sequence_filter]:
                if filter_dataframe[sequence_filter].empty:
                    filter_dataframe[sequence_filter] = data_groups.get_group(sequence)
                else:
                    filter_dataframe[sequence_filter].append(data_groups.get_group(sequence))
        return source_dataframe

    def outputpower_analysi(self, source_dict):

        pass

if __name__ == '__main__':
    analysis_tool = TestAnalays()
    dataframe = analysis_tool.open_resource()
    analysis_tool.test_result_classify(dataframe)

