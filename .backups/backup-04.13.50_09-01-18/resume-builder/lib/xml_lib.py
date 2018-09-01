#! /usr/bin/python3

import lxml.etree
import os,sys,time

class data:
    master=None
    failedStates=[{},None]
    def header(self):
        if self.master not in self.failedStates:
            if self.master['contact'] not in self.failedStates:
                contact=lxml.etree.Element('contact')
                data=self.master['contact']
            
                xmlPre={
                        'name':'',
                        'street':'',
                        'locale':'',
                        'phone':'',
                        'type':'',
                        'email':'',
                        }
                xmlPre['name']='{} {} {}'.format(
                        data['fname'],
                        data['mname'],
                        data['lname']
                        )
                xmlPre['street']=data['street']
                xmlPre['locale']='{}, {} {}'.format(
                        data['city'],
                        data['state'],
                        data['zip'],
                        )
                xmlPre['email']=data['email']
                xmlPre['phone']=data['phone']
                xmlPre['type']=data['type']

                for key in xmlPre.keys():
                    if key != 'type':
                        if key == 'phone':
                            sub=lxml.etree.SubElement(contact,key,type=xmlPre['type'])
                            sub.text=xmlPre[key]
                        else:
                            sub=lxml.etree.SubElement(contact,key)
                            sub.text=xmlPre[key]

                print(lxml.etree.tostring(contact))
                return contact

    def employment(self):
        if self.master not in self.failedStates:
            if self.master['employment'] not in self.failedStates:
                data=self.master['employment']
                workXp=lxml.etree.Element('work_xp',tag='Work Experience')
                for num,key in enumerate(data.keys()):
                    e=data[key]
                    employer=lxml.etree.SubElement(workXp,'employer',name=e['name'],num=str(num))
                    emp={
                            'title':'',
                            'employer_region':'',
                            'start2end':'',
                            'duties':'',
                            }
                    emp['title']=e['title']
                    emp['start2end']=e['date']
                    emp['employer_region']='{} - {}, {} {}'.format(
                            e['name'],
                            e['city'],
                            e['state'],
                            e['zip'],
                            )
                    emp['duties']=e['duties']
                    
                    for key_1 in emp.keys():
                        sub=lxml.etree.SubElement(employer,key_1)
                        sub.text=emp[key_1]
                print(lxml.etree.tostring(workXp))
                return workXp

    def education(self):
        if self.master not in self.failedStates:
            if self.master['education'] not in self.failedStates:
                data=self.master['education']
                edu=lxml.etree.Element('education')
                for num,key in enumerate(data.keys()):
                    school=data[key]
                    ed=lxml.etree.SubElement(edu,'school',type=school['type'],num=str(num))
                    schoolInfo={
                            'degree':'',
                            'school_region':'',
                            'start2end':'',
                            }
                    schoolInfo['degree']=school['degree']
                    schoolInfo['school_region']='{} - {}, {} {}'.format(school['name'],school['city'],school['state'],school['zip'])
                    schoolInfo['start2end']=school['date']
                    for key in schoolInfo.keys():
                        sub=lxml.etree.SubElement(ed,key)
                        sub.text=schoolInfo[key]
                print(lxml.etree.tostring(edu))
                return edu
                    ###pause
    def links(self):
        if self.master not in self.failedStates:
            if self.master['links'] not in self.failedStates:
                data=self.master['links']
                linkXml=lxml.etree.Element('links',tag='Links')
                for num,key in enumerate(data.keys()):
                    link=lxml.etree.SubElement(linkXml,'link',num=str(num))
                    link.text=data[key]['link']
                print(lxml.etree.tostring(linkXml))
                return linkXml

    def skills(self):
        if self.master not in self.failedStates:
            if self.master['skills'] not in self.failedStates:
                data=self.master['skills']
                skillXml=lxml.etree.Element('skills',tag='Skills')
                for num,key in enumerate(data.keys()):
                    skill=lxml.etree.SubElement(skillXml,'skill',num=str(num))
                    skill.text='{} ({})'.format(data[key]['name'],data[key]['date'])

                print(lxml.etree.tostring(skillXml))
                return skillXml

    def additional_info(self):
        if self.master not in self.failedStates:
            if self.master['additional_info'] not in self.failedStates:
                data=self.master['additional_info']
                aiXml=lxml.etree.Element('additional_info',tag='Additional Information')
                lines=[]
                for key in data.keys():
                    lines.append(data[key]['line'])
                aiXml.text='\n'.join(lines)
                print(lxml.etree.tostring(aiXml))
                return aiXml


    def certs(self):
        if self.master not in self.failedStates:
            if self.master['certifications'] not in self.failedStates:
                data=self.master['certifications']
                certsXml=lxml.etree.Element('certs',tag='Certifications/Licenses')
                for num,key in enumerate(data.keys()):
                    cert=lxml.etree.SubElement(certsXml,'cert',num=str(num))
                    certInfo={
                            'name':'',
                            'start2end':'',
                            }
                    certInfo['name']=data[key]['name']
                    certInfo['start2end']=data[key]['date']
                    for key in certInfo.keys():
                        sub=lxml.etree.SubElement(cert,key)
                        sub.text=certInfo[key]
                print(lxml.etree.tostring(certsXml))
                return certsXml
    def mkReferences(self):
        if self.master not in self.failedStates:
            if self.master['references'] not in self.failedStates:
                data=self.master['references']
                refXml=lxml.etree.Element('references')

                contact=self.header()
                if contact not in self.failedStates:
                    refXml.append(self.header())

                for num,key in enumerate(data.keys()):
                    ref=data[key]
                    reference=lxml.etree.SubElement(refXml,'employer',name=ref['employer'])
                    refInfo={
                            'street_address':'',
                            'city':'',
                            'state':'',
                            'zip':'',
                            }
                    refInfo['street_address']=ref['street']
                    refInfo['city']=ref['city']
                    refInfo['state']=ref['state']
                    refInfo['zip']=ref['zip']
                    for key_1 in refInfo.keys():
                        print(key_1)
                        sub=lxml.etree.SubElement(reference,key_1)
                        sub.text=refInfo[key_1]

                    sub=lxml.etree.SubElement(reference,'phone',email=data[key]['email'],owner='{} {} {}'.format(data[key]['fname'],data[key]['mname'],data[key]['lname']),title=data[key]['title'],type=ref['type'])
                    sub.text=ref['phone']
                print('#pre-ref#',lxml.etree.tostring(refXml))
                return refXml

    def mkDocs(self):
        resume=self.mkResume()
        references=self.mkReferences()
        return resume,references

    def mkResume(self):
        r={
                'contact':self.header(),
                'work_xp':self.employment(),
                'education':self.education(),
                'skills':self.skills(),
                'links':self.links(),
                'certs':self.certs(),
                'additional_info':self.additional_info(),
        }
        resume=lxml.etree.Element('resume',date=time.ctime())
        for key in r.keys():
            if r[key] not in self.failedStates:
                resume.append(r[key])

        print(lxml.etree.tostring(resume))
        return resume
