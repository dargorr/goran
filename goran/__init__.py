# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>
def getting_data():
    import untangle
    xml_file = "nyct_ene.xml"

    # <codecell>

    doc=untangle.parse(xml_file)
    doc.get_elements()

    # <codecell>

    outages = doc.NYCOutages.outage

    # <codecell>

    repair=0
    for outage in outages:
        if(outage.reason.cdata=='REPAIR'): repair=repair+1

    # <codecell>

    fraction=(float(repair))/len(outages)
    output='fraction = %0.2f%%' %fraction		
    print output
