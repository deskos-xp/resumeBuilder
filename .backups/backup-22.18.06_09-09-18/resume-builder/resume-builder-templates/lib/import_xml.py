#! /usr/bin/env python3
import lxml.etree
import os, sys, time,string
import json
#NoGuiLinux
############################################################
#Import Xml data from resume and references xml documents
#for use with resumebuilder's createpdf_$Template_scripts.py
############################################################

class get_xml:
    resumeXml=''
    referencesXml=''
    resumePdf=''
    referencesPdf=''
    phoneDefaultsConfig='cfg/phone.json'
    
    resumeData={
        'contact':{},
        'objective':{},
        'employment':{},
        'education':{},
        'certifications':{},
        'skills':{},
        'links':{},
        'additional_info':{},
        'additional_info_awards':{},
        'additional_info_activities':{},
        'additional_info_hobbies':{},
            }
    
    referencesData={
            'contact':{},
            'references':{},
            }

    suffixes=(
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
    
    international='1'
    region='804'
    local='1234567'

    def __init__(self):
        self.setPhoneDefaults()

    def setPhoneDefaults(self):
        pconfig=None
        if os.path.exists(self.phoneDefaultsConfig):
            with open(self.phoneDefaultsConfig,'rb') as ifile:
                pconfig=json.load(ifile)
            self.internation=pconfig['international']
            self.region=pconfig['region']
            self.local=pconfig['local']
        else:
            print('"{}" : config file for phone defaults status 404... using hard coded defaults.'.format(self.phoneDefaultsConfig))

    def returnXml(self,doc):
        xml=None
        if os.path.exists(doc) and os.path.isfile(doc):
            with open(doc,'rb') as ifile:         
                xml=lxml.etree.parse(ifile)
            return xml.getroot()
        else:
            if os.path.exists(doc):
                print('"{}" : not a file'.format(doc))
            else:
                print('"{}" : does not exist'.format(doc))
            return None

    def resumeGetAi(self,root):
        data={
                        'additional_info':{},
                        'additional_info_awards':{},
                        'additional_info_hobbies':{},
                        'additional_info_activities':{},
                        'objective':{},
                            }
        objectives=0
        for child in root:
            if child.tag == 'additional_info':
                for num,line in enumerate(child):
                    if line.attrib['type'] == 'Disabled':
                        data['additional_info'][str(num)]=line.text
                    if line.attrib['type'] not in ['Awards','Activities','Hobbies','Objective','Disabled']:
                        if 'additional_info_{}'.format(line.attrib['type']) not in data.keys():
                            data['additional_info_{}'.format(line.attrib['type'])]={}
                            data['additional_info_{}'.format(line.attrib['type'])][str(num)]=line.text
                        else:
                            data['additional_info_{}'.format(line.attrib['type'])][str(num)]=line.text
                    if line.attrib['type'] == 'Awards':
                        data['additional_info_awards'][str(num)]=line.text
                    if line.attrib['type'] == 'Hobbies':
                        data['additional_info_hobbies'][str(num)]=line.text
                    if line.attrib['type'] == 'Activities':
                        data['additional_info_activities'][str(num)]=line.text
                    if line.attrib['type'] == 'Objective':
                        objectives+=1
                        if objectives > 1:
                            print('there are more than one objective. the last objective will be used.')
                        data['objective'][str(num)]=line.text
        return data
    
    def phoneStripper(self,number):
        num=''
        for char in number:
            if char in string.digits:
                num+=char
        if len(num) not in [7,10,11]:
            print('number may be invalid')
            return False,number
        else:
            return True,num

    def breakPhone(self,number):
        if number[0] == False:
            return None,None,number[1]
        else:
            number=number[1]
        international=self.international
        region=self.region
        local=self.local
        nl=len(number)
        if nl in [7,10,11]:
            if nl == 7:
                local=number
            if nl == 10:
                region=number[:3]
                local=number[3:]
            if nl == 11:
                internation=number[:1]
                region=number[1:4]
                local=number[4:]
            return international,region,local
        else:
            return None,None,number

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
 
    def resumeGetContact(self,root):
        contact={
                'fname':'',
                'mname':'',
                'lname':'',
                'phone_local':'',
                'phone_region':'',
                'phone_international':'',
                'email':'',
                'street':'',
                'city':'',
                'state':'',
                'zip':'',
                'phoneType':''
                }
        for child in root:
            if child.tag == 'contact':
                for info in child:
                    if info.tag == 'name':
                        name=self.breakName(info.text)
                        contact['fname']=name[0]
                        contact['mname']=name[1]
                        contact['lname']=name[2]
                    if info.tag == 'phone':
                        contact['phoneType']=info.attrib['type']
                        num=self.phoneStripper(info.text)
                        phone=self.breakPhone(num)
                        contact['phone_local']=phone[2]
                        contact['phone_region']=phone[1]
                        contact['phone_international']=phone[0]
                    if info.tag == 'email':
                        contact['email']=info.text
                    if info.tag == 'street':
                        contact['street']=info.text
                    if info.tag == 'locale':
                        locale=self.breakLocale(info.text)
                        contact['city']=locale[0]
                        contact['state']=locale[1]
                        contact['zip']=locale[2]
        return contact
        #print(self.data['contact'])
   
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


    def resumeGetEmployment(self,root):
        data={}
        for child in root:
            if child.tag == 'work_xp':
                for num,employer in enumerate(child):
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
                    for sub in employer:
                        if sub.tag == 'title':
                            data[str(num)]['title']=sub.text
                        if sub.tag == 'employer_region':
                            res=self.breakEmp(sub.text)                            
                            data[str(num)]['employer']=res[0]
                            data[str(num)]['city']=res[1]
                            data[str(num)]['state']=res[2]
                            data[str(num)]['zip']=res[3]
                        if sub.tag == 'start2end':
                            date=self.breakDate(sub.text)
                            data[str(num)]['startDate']=date[0]
                            data[str(num)]['endDate']=date[1]
                        if sub.tag == 'duties':
                            data[str(num)]['duties']=sub.text
        return data
        #print(self.data['employment'])

    def resumeGetEducation(self,root):
        data={}
        for child in root:
            if child.tag == 'education':
                for num,sub in enumerate(child):
                    data[str(num)]={
                                'degree':'',
                                'school':'',
                                'city':'',
                                'state':'',
                                'zip':'',
                                'startDate':'',
                                'endDate':'',
                                'type':'',
                                }
                    data[str(num)]['type']=sub.attrib['type']
                    for school in sub:    
                        if school.tag == 'degree':
                            data[str(num)]['degree']=school.text
                        if school.tag == 'school_region':
                            res=self.breakEmp(school.text)
                            data[str(num)]['school']=res[0]
                            data[str(num)]['city']=res[1]
                            data[str(num)]['state']=res[2]
                            data[str(num)]['zip']=res[3]
                        if school.tag == 'start2end':
                            date=self.breakDate(school.text)
                            data[str(num)]['startDate']=date[0]
                            data[str(num)]['endDate']=date[1]
        return data
        #print(self.data['education'])

    def breakSkill(self,skill):
        skill=skill.split(' (')
        SKILL=skill[0]
        skill=''.join(skill[1:])
        GRADE=''
        if skill[0] in ['-','+']:
            GRADE=skill[0]
            skill=skill[1:-1*len('experience)')]
        else:
            skill=skill[:-1*len('experience)')]

        skill=skill.split(' ')
        MONTHS=''
        YEARS=''
        for num,i in enumerate(skill):
            if i in ['Months','Month']:
                MONTHS=skill[num-1]
            if i in ['Years','Year']:
                YEARS=skill[num-1]

        return SKILL,MONTHS,YEARS,GRADE


    def resumeGetSkills(self,root):
        data={}
        for child in root:
            if child.tag == 'skills':
                for num,skill in enumerate(child):
                    data[str(num)]={
                            'skill':'',
                            'years':'',
                            'months':'',
                            'grade':'',
                            }
                    sk=self.breakSkill(skill.text)
                    data[str(num)]['skill']=sk[0]
                    data[str(num)]['years']=sk[2]
                    data[str(num)]['months']=sk[1]
                    data[str(num)]['grade']=sk[3]

        return data
        #print(self.data['skills'])

    def resumeGetCerts(self,root):
        data={}
        for child in root:
            if child.tag == 'certs':
                for num,cert in enumerate(child):
                    data[str(num)]={
                            'name':'',
                            'startDate':'',
                            'endDate':'',
                            }
                    for sub in cert:
                        if sub.tag == 'name':
                            data[str(num)]['name']=sub.text
                        if sub.tag == 'start2end':
                            date=self.breakDate(sub.text)
                            data[str(num)]['startDate']=date[0]
                            data[str(num)]['endDate']=date[1]
        return data
        #print(self.data['certifications'])

    def resumeGetLinks(self,root):
        data={}
        for child in root:
            if child.tag == 'links':
                for num,link in enumerate(child):
                    data[str(num)]={
                            'link':'',
                            }
                    data[str(num)]['link']=link.text
        return data
        #print(self.data['links'])

    def resumeGetAllFields(self,root):
        self.resumeData['contact']=self.resumeGetContact(root)
        self.resumeData['employment']=self.resumeGetEmployment(root)
        self.resumeData['education']=self.resumeGetEducation(root)
        self.resumeData['skills']=self.resumeGetSkills(root)
        self.resumeData['certifications']=self.resumeGetCerts(root)
        self.resumeData['links']=self.resumeGetLinks(root)
        data=self.resumeGetAi(root)
        for key in data.keys():
            self.resumeData[key]=data[key]
        return self.resumeData

    def referencesGetReferences(self,root):
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
                'phone_local':'',
                'phone_region':'',
                'phone_international':'',
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
                        phone=self.breakPhone(self.phoneStripper(subChild.text))
                        data[key]['phone_international']=phone[0]
                        data[key]['phone_region']=phone[1]
                        data[key]['phone_local']=phone[2]

                        data[key]['email']=subChild.attrib['email']
                        name=self.breakName(subChild.attrib['owner'])
                        data[key]['fname']=name[0]
                        data[key]['mname']=name[1]
                        data[key]['lname']=name[2]
                        data[key]['title']=subChild.attrib['title']
                        data[key]['type']=subChild.attrib['type']
                counter+=1
        return data

    def referencesGetAllFields(self,root):
        self.referencesData['contact']=self.resumeGetContact(root)
        self.referencesData['references']=self.referencesGetReferences(root)
        return self.referencesData


if __name__ == "__main__":
    x=get_xml()

    x.resumeXml='./default-resume.xml'
    xml=x.returnXml(x.resumeXml)
    if xml != None:
        x.resumeGetAllFields(xml)
        print(x.resumeData)

    x.referencesXml='./default-references.xml'
    xml=x.returnXml(x.referencesXml)
    if xml != None:
        x.referencesGetAllFields(xml)
        print(x.referencesData)


