import itertools


class ImCaculator(object):

    def imodaration_caculate(self, dataframe):
        freqency_sections = [[925, 928], [793, 787]]

    def imoduratation_count(self, frequency_list):
        im_result = list()
        frequency_combine = itertools.combinations(frequency_list, 2)
        for combine in frequency_combine:
            im_frequency = 2 * combine[0][0] + 1 * combine[1][0]
            im_bw = 2 * combine[0][1] + 1 * combine[1][1]
            frequency_section = [im_frequency - im_bw / 2, im_frequency + im_bw / 2]
            im_result.append(frequency_section)
        print(im_result)
        return im_result

    def section_combine(self, frequency_sections):
        frequency_sections.sort(key=lambda x: x[0])
        merge_list = []
        for frequency_section in frequency_sections:
            if len(merge_list) == 0 or frequency_section[0] > merge_list[-1][-1]:
                merge_list.append(frequency_section)
            else:
                merge_list[-1][-1] = max(merge_list[-1][-1], frequency_section[-1])
        print(merge_list)
        return merge_list


a = ImCaculator()
frequency_list_A = [[925, 1.4], [818, 3], [793.5, 5], [758, 3]]
b = a.imoduratation_count(frequency_list_A)
c = a.section_combine(b)
