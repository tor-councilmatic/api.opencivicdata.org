from datetime import date

import boundaries

def ocd_id_func(feature):
    return 'ocd-division/country:us/state:il/sldl:{0}'.format(feature.get('District_1'))

def district_namer(feature):
    return 'il-house-district-{0}'.format(str(feature.get('District_1')).zfill(3))

boundaries.register('illinois-lower-2011',  
    file='',
    last_updated=date(2011, 5, 26),
    name='Illinois House of Representatives Districts',
    singular='Illinois House of Representatives District',
    domain='Illinois',
    authority='State of Illinois',
    source_url='http://ilhousedems.com/redistricting/2011-maps/Legislative_Districts_Public_Act/House%20and%20Senate%20shape%20files.zip',
    licence_url='',
    start_date=date(2011,5,1),
    end_date=None,
    notes='',
    name_func=district_namer,
    id_func=ocd_id_func,
    is_valid_func=lambda feature: True,
    label_point_func=lambda feature: None,
)

