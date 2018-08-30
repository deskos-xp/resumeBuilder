#! /usr/bin/env python3

import time,os,sys,lxml.etree

class get_xml:
    def __init__(self):
        self.references=None
        self.resume=None
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
        
    def contact(self,root):
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

    def referencesEmployer(self,root):
        data={}
        counter=0
        for child in root: 
            if child.tag == 'employer':
                tm=time.localtime()
                key='{}:{}:{}:Ref_{}'.format(tm.tm_hour,tm.tm_min,tm.tm_sec,counter)
                data[key]={
                'employer':'',
                'title':'',
                'fname':'',
                'mname':'',
                'lname':'',
                'phone':'',
                'email':'',
                'street':'',
                'city':'',
                'state':'',
                'zip':'',
                'type':'',
                }
                data[key]['employer']=child.attrib['name']
                for subChild in child:
                    if subChild.tag == 'street_address':
                        data[key]['street']=subChild.text
                    if subChild.tag == 'city':
                        data[key]['city']=subChild.text
                    if subChild.tag == 'zip':
                        data[key]['zip']=subChild.text
                    if subChild.tag == 'state':
                        data[key]['state']=subChild.text
                    if subChild.tag == 'phone':
                        data[key]['phone']=subChild.text
                        data[key]['email']=subChild.attrib['email']
                        name=self.breakName(subChild.attrib['owner'])
                        data[key]['fname']=name[0]
                        data[key]['mname']=name[1]
                        data[key]['lname']=name[2]
                        data[key]['title']=subChild.attrib['title']
                        data[key]['type']=subChild.attrib['type']
                counter+=1
        return data
    def breakDate(self,date):
        date=date.split(' to ')
        return date

    def breakEmp(self,emp):
        emp=emp.split(' - ')
        empEnd=emp[1]
        empStart=emp[0]
        
        empEnd=empEnd.split(' ')
        zipcode=empEnd[-1]
        state=empEnd[-2]
        empEnd=empEnd[:-2]
        city=' '.join(empEnd)[:-1]

        employer=empStart
        return employer,city,state,zipcode

    def resumeGetWorkXp(self,root):
        data={}
        for child in root:
            if child.tag == 'work_xp':
                for num,emp in enumerate(child):
                    if emp.tag == 'employer':
                        data[str(num)]={
                            'title':'',
                            'employer':'',
                            'city':'',
                            'state':'',
                            'zip':'',
                            'startDate':'',
                            'endDate':'',
                            'duties':'',
                            }
                        for subChild in emp:
                            if subChild.tag == 'title':
                                data[str(num)]['title']=subChild.text
                            if subChild.tag == 'duties':
                                data[str(num)]['duties']=subChild.text
                            if subChild.tag == 'start2end':
                                date=self.breakDate(subChild.text)
                                data[str(num)]['startDate']=date[0]
                                data[str(num)]['endDate']=date[1]
                            if subChild.tag == 'employer_region':
                                res=self.breakEmp(subChild.text)
                                data[str(num)]['employer']=res[0]
                                data[str(num)]['city']=res[1]
                                data[str(num)]['state']=res[2]
                                data[str(num)]['zip']=res[3]    
        return data
    def resumeGetEd(self,root):
        data={}
        for child in root:
            if child.tag == 'education':
                for num,school in enumerate(child):
                    data[str(num)]={
                        'type':'',
                        'school':'',
                        'city':'',
                        'state':'',
                        'zip':'',
                        'startDate':'',
                        'endDate':'',
                        'degree':''
                            }
                    data[str(num)]['type']=school.attrib['type']
                    for f in school:
                        if f.tag == 'degree':
                            data[str(num)]['degree']=f.text
                        if f.tag == 'school_region':
                            res=self.breakEmp(f.text)
                            data[str(num)]['school']=res[0]
                            data[str(num)]['city']=res[1]
                            data[str(num)]['state']=res[2]
                            data[str(num)]['zip']=res[3]
                        if f.tag == 'start2end':
                            date=self.breakDate(f.text)
                            data[str(num)]['startDate']=date[0]
                            data[str(num)]['endDate']=date[1]
        return data

    def resumeGetCert(self,root):
        data={}
        return data

    def resumeGetSkill(self,root):
        data={}
        return data

    def resumeGetLink(self,root):
        data={}
        return data

    def resumeGetAi(self,root):
        data={}
        return data

    def getResumeFields(self,root):
        resume={}

        resume['work_xp']=self.resumeGetWorkXp(root)
        resume['schools']=self.resumeGetEd(root)
        resume['certs']=self.resumeGetCert(root)
        resume['skills']=self.resumeGetSkill(root)
        resume['links']=self.resumeGetLink(root)
        resume['additional_info']=self.resumeGetAi(root)
        print(resume)
        try:
            print('-'*os.get_terminal_size().columns)
        except:
            print('-'*20)
        for key in resume.keys():
            for subKey in resume[key].keys():
                print(key,subKey,resume[key][subKey])

        
    
if __name__ == '__main__':
    x=get_xml()
    x.references='./templates/xml/references/references.xml'
    
    
    x.resume='./templates/xml/resume/resume-genned.xml'
    resXml=x.getXml(x.resume)[1]
    resumeContact=x.contact(resXml)
    resumeFields=x.getResumeFields(resXml)
    
    '''
    refXml=x.getXml(x.references)[1]
    referencesContact=x.contact(refXml)
    referencesEmployers=x.referencesEmployer(refXml)

    print(referencesContact)
    for i in referencesEmployers.keys():
        print(referencesEmployers[i])
    '''