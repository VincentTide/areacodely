from app import app, db
from app.models import *
from utility import parse_no_default
import us


db.drop_all()
db.create_all()

# Add in the data from text files to the database
def parse_ratecentername():
    input = open("data/RateCenterName_tabbed.csv")
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
        msa_name = fcc_msa_name.replace("Metropolitan Statistical Area", "").strip()

        if rate_center_10char in full_name:
            full_name[rate_center_10char][state] = {
                'fullname': rate_center_fullname.title(),
                'msa_name': msa_name}
        else:
            full_name[rate_center_10char] = {state: {
                'fullname': rate_center_fullname.title(),
                'msa_name': msa_name}
                                             }

    full_name['XXXXX'] = {
        'NY': {'fullname': None, 'msa_name': None}
    }

    return full_name


def parse_areacode(full_name):
    input = open("data/AllBlocks_tabbed.csv")
    firstline = input.readline()

    ac = {}

    for line in input:
        string = line.split('\t')

        region = string[0]
        state = string[1]
        state_name = us.states.lookup(state).name
        area_code = string[2]
        central_office_code = string[3]
        rate_center = string[9]
        date_effective = parse_no_default(string[10])
        assigned_to = string[12]
        try:
            date_assigned = parse_no_default(string[14])
        except:
            date_assigned = None

        name = full_name[rate_center][state]

        print area_code, central_office_code, rate_center, name['fullname'], name['msa_name']

        phone = Telephone.query.filter_by(area_code=area_code, central_office_code=central_office_code).first()

        # If the area code and prefix already exist, don't overwrite it
        # if it doesn't exist, create a new entry
        if phone is None:
            telephone = Telephone(region=region,
                                  state=state_name,
                                  area_code=area_code,
                                  central_office_code=central_office_code,
                                  rate_center=rate_center,
                                  full_name=name['fullname'],
                                  metro=name['msa_name'],
                                  assigned_to=assigned_to,
                                  date_assigned=date_assigned,
                                  date_effective=date_effective)
            db.session.add(telephone)
            db.session.commit()

    print "Finished loading into database."


if __name__ == '__main__':
    full_name = parse_ratecentername()
    parse_areacode(full_name)
