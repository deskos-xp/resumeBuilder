#! /usr/bin/env python3

import json,os,sys
import importer_lib
import import_xml

class get_json:
    allJson=None
    def __init__(self):
        pass

    def getJson(self,jsonfile):
        data=None
        with open(jsonfile,'rb') as ifile:
            data=json.load(ifile)
        return data

    def json_getFields(self):
        doc=None
        status=None
        self.allJson=self.import_getFname('json','References and Resume')
        if self.allJson == None:
            status=('file state',self.allJson)
            print(status)
            return status
        else:
            if os.path.exists(self.allJson) and os.path.isfile(self.allJson):
                doc=self.getJson(self.allJson)
            else:
                if os.path.exists(self.allJson) and not os.path.isfile(self.allJson):
                    status=('not a file',self.allJson)
                else:
                    status=('does not exist',self.allJson)
                print(status)
                return status
            self.resumeClearWidgets()
            self.referencesClearWidgets()
            self.setContactTabFields(doc['contact'])
            self.json_getEmployer(doc)
            self.json_getSchool(doc)
            self.json_getCert(doc)
            self.json_getSkill(doc)
            self.json_getLink(doc)
            self.json_getAi(doc)
            self.json_getRef(doc)

    def json_getEmployer(self,doc):
        x=import_xml.get_xml()
        d={'work_xp':doc['employment']}
        print(d['work_xp'].keys())
        for i in d['work_xp'].keys():
            d['work_xp'][i]['employer']=d['work_xp'][i]['name']
            d['work_xp'][i].pop('name')

            date=x.breakDate(d['work_xp'][i]['date'])
            d['work_xp'][i]['startDate']=date[0]
            d['work_xp'][i]['endDate']=date[1]
            d['work_xp'][i].pop('date') 
        self.resumeGetEmployer(d)
            
    def json_getSchool(self,doc):
        x=import_xml.get_xml()
        d={'schools':doc['education']}
        for i in d['schools'].keys():
            date=x.breakDate(d['schools'][i]['date'])
            d['schools'][i]['startDate']=date[0]
            d['schools'][i]['endDate']=date[1]
            d['schools'][i]['school']=d['schools'][i]['name']
            for si in ['date','name']:
                print(d['schools'][i].pop(si))
        self.resumeGetSchool(d)

    def json_getCert(self,doc):
        x=import_xml.get_xml()
        d={'certs':doc['certifications']}
        for i in d['certs'].keys():
            date=x.breakDate(d['certs'][i]['date'])
            d['certs'][i]['startDate']=date[0]
            d['certs'][i]['endDate']=date[1]
            for si in ['date']:
                d['certs'][i].pop(si)
        self.resumeGetCert(d)

    def json_getSkill(self,doc):
        x=import_xml.get_xml()
        d={'skills':doc['skills']}
        for i in d['skills'].keys():
            skillString='{} ({})'.format(d['skills'][i]['name'],d['skills'][i]['date'])
            skill=x.breakSkill(skillString)
            d['skills'][i]['grade']=skill[3]
            d['skills'][i]['months']=skill[1]
            d['skills'][i]['years']=skill[2]
            d['skills'][i]['skill']=skill[0]
            d['skills'][i].pop('name')
        self.resumeGetSkill(d)

    def json_getLink(self,doc):
        self.resumeGetLink(doc)

    def json_getAi(self,doc):
        self.resumeGetAi(doc)
            #from here on, import of each tab's data will be constricted to a per function basis, as in importer_lib
    def json_getRef(self,doc):
        self.getReferences(doc['references'])

    def json_buttons_connect(self):
        self.actionImport_json.triggered.connect(self.json_getFields)
