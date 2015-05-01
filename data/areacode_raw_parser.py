import sys






def parser_ratecentername():
    input = open("RateCenterName_tabbed.csv")
    firstline = input.readline()

    # 10char name, state, full name
    full_name = {}

    for line in input:
        string = line.split('\t')
        state = string[0]
        area_code = string[1]
        rate_center_10char = string[2]
        rate_center_fullname = string[3]
        fcc_msa_name = string[6]

        if rate_center_10char in full_name:
            full_name[rate_center_10char][state] = {
                'fullname': rate_center_fullname,
                'msa_name': fcc_msa_name }
        else:
            full_name[rate_center_10char] = {state:
                {
                'fullname': rate_center_fullname,
                'msa_name': fcc_msa_name }
                                             }


    # print full_name["SPRINGVL"]

    return full_name




def parse_areacode(full_name):
    input = open("AllBlocks_tabbed.csv")
    firstline = input.readline()

    ac = {}

    for line in input:
        string = line.split('\t')

        region = string[0]
        state = string[1]
        area_code = string[2]
        central_office_code = string[3]
        rate_center = string[9]
        date_effective = string[10]
        assigned_to = string[12]
        try:
            date_assigned = string[14]
        except:
            date_assigned = None

        name = full_name[rate_center][state]

        print area_code, central_office_code, rate_center, name['fullname'], name['msa_name']




















if __name__ == '__main__':
    full_name = parser_ratecentername()
    parse_areacode(full_name)















