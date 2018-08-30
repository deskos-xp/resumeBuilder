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

            
        print(doc.keys())
            #from here on, import of each tab's data will be constricted to a per function basis, as in importer_lib

    def json_buttons_connect(self):
        self.actionImport_json.triggered.connect(self.json_getFields)
