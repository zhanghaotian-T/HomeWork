import itertools


class ImCaculator(object):

    def imodaration_caculate(self, dataframe):
        freqency_sections = [[925, 928], [793, 793]]

    def imoduratation_count(self, frequency_list, degree_list):
        im_result = list()
        frequency_combine = itertools.combinations(frequency_list, 2)
        for degree in degree_list:
            for combine in frequency_combine:
                im_frequency_low_sub = degree[0] * combine[0][0] - degree[1] * combine[1][0]
                im_bw = degree[0] * combine[0][1] + degree[1] * combine[1][1]
                frequency_section_low_sub = [im_frequency_low_sub - im_bw / 2, im_frequency_low_sub + im_bw / 2]
                im_frequency_high_sub = degree[0] * combine[1][0] - degree[1] * combine[0][0]
                frequency_section_high_sub = [im_frequency_high_sub - im_bw / 2, im_frequency_high_sub + im_bw / 2]
                im_frequency_low_add = degree[0] * combine[0][0] + degree[1] * combine[1][0]
                frequency_section_low_add = [im_frequency_low_add - im_bw / 2, im_frequency_low_add + im_bw / 2]
                im_frequency_high_add = degree[0] * combine[1][0] - degree[1] * combine[0][0]
                frequency_section_high_add = [im_frequency_high_add - im_bw / 2, im_frequency_high_add + im_bw / 2]
                im_result.extend([frequency_section_low_sub, frequency_section_high_sub, frequency_section_low_add
                                  , frequency_section_high_add])
        return im_result

    def section_combine(self, frequency_sections):
        frequency_sections.sort(key=lambda x: x[0])
        merge_list_sub = []
        for frequency_section in frequency_sections:
            if len(merge_list_sub) == 0 or frequency_section[0] > merge_list_sub[-1][-1]:
                merge_list_sub.append(frequency_section)
            else:
                merge_list_sub[-1][-1] = max(merge_list_sub[-1][-1], frequency_section[-1])
        merge_list = self.list_round(merge_list_sub)
        print(merge_list)
        return merge_list

    def list_round(self, round_list):
        return [[round(i, 2) for i in sublist] for sublist in round_list]

    def imoduration_3GPP(self, protocol_list, freqency_section_list):
        freqency_section_imodulation = list()
        for protocol in protocol_list:
            for freqency_section in freqency_section_list:
                imdulation_frequency = self.imdulation_frequency_caculate(freqency_section, protocol)
                freqency_section_imodulation.extend(imdulation_frequency)
            freqency_section_imodulation.extend(freqency_section_list)
        return freqency_section_imodulation

    def imdulation_frequency_caculate(self, frequency_list, protocol):
        frequency_list_fianal = list()
        if protocol == 'EUTRA':
            imdulation_list = [2.5, 7.5, 12.5]
            for imdulation in imdulation_list:
                low = [frequency_list[0] - (frequency_list[1] / 2) - imdulation, 5]
                high = [frequency_list[0] + (frequency_list[1] / 2) + imdulation, 5]
                frequency_list_fianal.append(low)
                frequency_list_fianal.append(high)
        if protocol == 'MSR':
            imdulation_list = [0.8, 2, 3.2, 6.2]
            for imdulation in imdulation_list:
                low = [frequency_list[0] - (frequency_list[1] / 2) - imdulation, 0]
                high = [frequency_list[0] + (frequency_list[1] / 2) + imdulation, 0]
                frequency_list_fianal.append(low)
                frequency_list_fianal.append(high)
        return frequency_list_fianal


a = ImCaculator()
frequency_list_A = [[925, 1.4], [818, 3], [793.5, 5], [758, 0]]
protoclo = ['MSR', 'EUTRA']
b = a.imoduration_3GPP(protoclo, frequency_list_A)
c = a.imoduratation_count(b, [[2, 1], [3, 2]])
d = a.section_combine(c)
# b = a.imoduratation_count(frequency_list_A)
# c = a.section_combine(b)
