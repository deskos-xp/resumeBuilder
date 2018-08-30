#! /usr/bin/env python3

import time,os,sys,lxml.etree

class get_xml:
    def __init__(self):
        self.references=None
        self.suffixes=(
                'jr.',
                'sr.',
                '2nd',
                '3rd',
                'ii',
                'iii',
                'iv',
                'v',
                'vi',
                'esq',
                'cpa',
                'dc',
                'dds',
                'vm',
                'jd',
                'md',
                'phd',
                )

    def getXml(self,doc):
        if os.path.exists(doc) and os.path.isfile(doc):
            xml=lxml.etree.parse(doc)
            root=xml.getroot()
            return xml,root
        else:
            return (None,None)

    def breakName(self,name):
        name=name.split(' ')
        #last name
        if name[-1].lower() not in self.suffixes:
            lname=name[-1]
            dec=-1
        elif name[-1].lower() in self.suffixes:
            lname='{} {}'.format(name[-2],name[-1])
            dec=-2

        name=name[:dec]
        fname=name[0]
        name=name[1:]
        mname=' '.join(name) 
        
        return fname,mname,lname
    def breakLocale(self,locale):
        locale=locale.split(',')
        city=locale[0]
        locale=[ i for i in ''.join(locale[1:]).split(' ') if i != '']
        state=locale[0]
        zipcode=locale[1]
        
        return city,state,zipcode
        
    def referencesContact(self,root):
        data={
            'fname':'',
            'mname':'',
            'lname':'',
            'phone':'',
            'email':'',
            'street':'',
            'city':'',
            'state':'',
            'zip':'',
        }
        for child in root:
            if child.tag == 'contact':
                for subChild in child:
                    if subChild.text != None:
                        if subChild.tag == 'name':
                            data['fname'],data['mname'],data['lname']=self.breakName(subChild.text)
                        if subChild.tag == 'phone':
                            data['phone']=subChild.text
                        if subChild.tag == 'street':
                            data['street']=subChild.text
                        if subChild.tag == 'locale':
                            data['city'],data['state'],data['zip']=self.breakLocale(subChild.text)
                        if subChild.tag == 'email':
                            data['email']=subChild.text
            else:
                break
        return data


if __name__ == '__main__':
    x=get_xml()
    x.references='./templates/xml/references/references.xml'
    refXml=x.getXml(x.references)[1]
    referencesContact=x.referencesContact(refXml)
    print(referencesContact)
