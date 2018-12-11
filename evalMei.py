# compare two mei files

from evalStaff import evalStaff

class evalMei(object):

    def __init__(self, **kwargs):
        self.mei = '{http://www.music-encoding.org/ns/mei}'
        self.xml = '{http://www.w3.org/XML/1998/namespace}'

    def evaluate(self, GT, OG):

        # extract useful info
        GT_surface = self.getSurface(GT)
        GT_staffDef = self.getStaffDef(GT)
        GT_staves = self.getStaves(GT)

        OG_surface = self.getSurface(OG)
        OG_staffDef = self.getStaffDef(OG)
        OG_staves = self.getStaves(OG)

        staves_results = self.evalStaves(GT_staves, OG_staves, GT_surface, OG_surface)

        return 0

    def evalStaves(self, staves1, staves2, surface1, surface2):
        staff_evaluator = evalStaff()
        staff_results = []

        i_facs1 = self.interpFacs(surface1)
        i_facs2 = self.interpFacs(surface2)
        i_staves1 = self.interpStaves(staves1, i_facs1)
        i_staves2 = self.interpStaves(staves2, i_facs2)

        # metrics
        order_error = 0
        staff_position_error = 0
        extra_staves = len(i_staves2) - len(i_staves1)

        i = 0
        for staff1 in i_staves1:
            staff2 = i_staves2[i]

            print staff1, '\n', staff2
            print '\n'
            staff_results.append(staff_evaluator.evaluate(staff1, staff2))
            i += 1

        print staff_results
        return staff_results

    #####################
    # compare Functions
    #####################

    def compareStaffPosition(self, s1, s2):
        if  s1['ulx'] == s2['ulx'] and s1['uly'] == s2['uly'] or \
            s1['lrx'] == s2['lrx'] and s1['lry'] == s2['lry']:
            return True

        else:
            return False

    #######################
    # Interpret Functions
    #######################

    def interpFacs(self, surface):
        facs = surface.findall('./{0}zone'.format(self.mei))

        return [{
            'id': z.get('{0}id'.format(self.xml)),
            'ulx': z.get('ulx'),
            'uly': z.get('uly'),
            'lrx': z.get('lrx'),
            'lry': z.get('lry')
            } for z in facs]

    def interpStaves(self, staves, i_facs):
        i_staves = []
        for s in staves:
            facs = [f for f in i_facs if f['id'] == s.get('facs')][0]
            i_staves.append({
                'id': s.get('{0}id'.format(self.xml)),
                'ulx': facs['ulx'],
                'uly': facs['uly'],
                'lrx': facs['lrx'],
                'lry': facs['lry'],
                'n': s.get('n'),
                'lines': s.get('lines')
            })

        return i_staves

    ################
    # mei parsers
    ################

    def getSurface(self, root):
        return root.find('./{0}music/{0}facsimile/{0}surface'.format(self.mei))

    def getStaffDef(self, root):
        return root.find('./{0}music/{0}body/{0}mdiv/{0}score/{0}scoreDef/{0}staffGrp/{0}staffDef'.format(self.mei))

    def getStaves(self, root):
        return root.findall('./{0}music/{0}body/{0}mdiv/{0}score/{0}section/{0}staff'.format(self.mei))

    # methods of evaluation

    # All staves in right order
    # All pitches in order
    # All neume groupings in order
