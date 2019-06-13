from xml.etree import ElementTree as ET
import random
import string

fh = open('k.txt','w+',encoding="utf-8")

class xml:

    def ParseProcessInfo(self,root, primkey, indikey):
        name = None
        functionalunit = None
        for child in root.findall('{http://lca.jrc.it/ILCD/Process}processInformation'):
            for baby in child.findall('{http://lca.jrc.it/ILCD/Process}dataSetInformation'):
                for enfant in baby:
                    if enfant.tag == '{http://lca.jrc.it/ILCD/Common}UUID':
                        key = enfant.text
                        key = str(key)
                    if enfant.tag == '{http://lca.jrc.it/ILCD/Process}name':
                        for newborn in enfant:
                            if newborn.tag == '{http://lca.jrc.it/ILCD/Process}baseName' and newborn.attrib['{http://www.w3.org/XML/1998/namespace}lang'] == 'en':
                                name = newborn.text 
                            elif newborn.tag == '{http://lca.jrc.it/ILCD/Process}baseName' and newborn.attrib['{http://www.w3.org/XML/1998/namespace}lang'] == 'de' and name == None:
                                name = newborn.text       
                            if newborn.tag == '{http://lca.jrc.it/ILCD/Process}functionalUnitFlowProperties':
                                functionalunit = newborn.text

                            
                            



                    if enfant.tag == '{http://lca.jrc.it/ILCD/Process}classificationInformation':
                        for newborn in enfant:
                            ind = 1
                            for unborn in newborn:
                                if unborn.tag == '{http://lca.jrc.it/ILCD/Common}class':
                                    klass = unborn.text
                                    if (ind == 1 ):
                                        parentclass = klass
                                    elif(ind == 2):
                                        childclass = klass
                                    else:
                                        subclass = klass
                                    ind = ind + 1
            for baby in child.findall('{http://lca.jrc.it/ILCD/Process}time'):
                for enfant in baby.findall('{http://lca.jrc.it/ILCD/Common}referenceYear'):
                    refyear = enfant.text
                for enfant in baby.findall('{http://lca.jrc.it/ILCD/Common}dataSetValidUntil'):
                    validuntil = enfant.text

            for baby in child.findall('{http://lca.jrc.it/ILCD/Process}geography'):
                for enfant in baby.findall('{http://lca.jrc.it/ILCD/Process}locationOfOperationSupplyOrProduction'):
                    pass # print(enfant.attrib['location'])
        
            for baby in child.findall('{http://lca.jrc.it/ILCD/Process}technology'):
                for enfant in baby.findall('{http://lca.jrc.it/ILCD/Process}technologyDescriptionAndIncludedProcesses'):
                    if enfant.attrib['{http://www.w3.org/XML/1998/namespace}lang'] == 'en':
                        print(enfant.text)
                        break
                    else:
                        print('does not exist')
        #print(name.encode("utf-8"))
        fh.writelines('\n'+name+' and the functional unit is '+str(functionalunit))
        return name

    def parseexchange(self, root, key, indikey):
        for child in root:
            for baby in child.findall('{http://lca.jrc.it/ILCD/Process}exchange'):
                for enfant in baby:
                    for newborn in enfant:
                        if newborn.tag == '{http://lca.jrc.it/ILCD/Common}shortDescription' and newborn.attrib['{http://www.w3.org/XML/1998/namespace}lang'] == 'de':
                            exchangename = newborn.text
                            break
                        elif newborn.tag == '{http://lca.jrc.it/ILCD/Common}shortDescription' and newborn.attrib[
                            '{http://www.w3.org/XML/1998/namespace}lang'] == 'en':
                            exchangename = newborn.text
                            break
                for enfant in baby.findall('{http://lca.jrc.it/ILCD/Process}exchangeDirection'):
                    direction = enfant.text
                    direction = str(direction)
                for enfant in baby.findall('{http://lca.jrc.it/ILCD/Common}other'):
                    dict = {}
                    for newborn in enfant:
                        tracker = len(enfant.findall('{http://www.iai.kit.edu/EPD/2013}amount'))
                        if newborn.tag == '{http://www.iai.kit.edu/EPD/2013}amount':
                            Dict = newborn.attrib
                            realattrib = Dict['{http://www.iai.kit.edu/EPD/2013}module']
                            #print(realattrib)
                            value = newborn.text
                            dict[realattrib] = value
                        else:
                            for unborn in newborn:
                                unit = unborn.text
                                unit = str(unit)
                                break
                    # print(list(dict.keys()))

    def parceLCIAresults(self,root, key, indikey):
        for child in root:
            for baby in child.findall('{http://lca.jrc.it/ILCD/Process}LCIAResult'):
                for enfant in baby:
                    for newborn in enfant:
                        if newborn.tag == '{http://lca.jrc.it/ILCD/Common}shortDescription' and newborn.attrib[
                            '{http://www.w3.org/XML/1998/namespace}lang'] == 'de':
                            indicatortext = newborn.text
                            break
                        elif newborn.tag == '{http://lca.jrc.it/ILCD/Common}shortDescription' and newborn.attrib[
                                '{http://www.w3.org/XML/1998/namespace}lang'] == 'en':
                            indicatortext = newborn.text
                            break
                for enfant in baby.findall('{http://lca.jrc.it/ILCD/Common}other'):
                    for newborn in enfant:
                        if newborn.tag == '{http://www.iai.kit.edu/EPD/2013}amount':
                            value = newborn.text
                            if value is None:
                                for enfant in baby.findall('{http://lca.jrc.it/ILCD/Process}meanAmount'):
                                    value = enfant.text
                                    value = float(value)
                                    break
                            else:
                                value = float(value)

                        else:
                            for unborn in newborn:
                                unit = unborn.text
                                break



def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


k = {1:204, 2:236, 3:143, 4:6, 5:18, 6:74, 7:66, 8:257, 9:39, 10:120, 11:66}
for findex in range (1, 12):
    key = k[findex]
    for index in range(1, key):
        index = str(index)
        findex = str(findex)
        foo = 'Folder number is ' +findex +'File is ' +index
        print(foo)
        fh.writelines('\n'+foo)

        hee = ET.parse('Source/MLEPD/'+findex+'/'+findex+' ('+index +').xml')

        root = hee.getroot()

        r = xml()
        primkey = randomString(10)
        indikey = randomString(10)
        if indikey == primkey:
            indikey = randomString(10)
        r.ParseProcessInfo(root, primkey, indikey)
        r.parseexchange(root, primkey, indikey)
        r.parceLCIAresults(root, primkey, indikey)

fh.close()