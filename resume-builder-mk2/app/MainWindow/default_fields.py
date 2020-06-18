import json,os,sys
from PyQt5.QtWidgets import QHeaderView
def prep_table(table):
    table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


def phoneTypes():
    return ["Cell","Home","Work"]

def education():
    school=dict(
        school="",
        start_date="",
        present=False,
        end_date="",
        degree="",
        city="",
        state="",
        ZIP="",
        school_type=""
        )
    return school

def schoolTypes():
    return ['School Types','High School','2 Year College','4 Year College','Trade School','Other']

def employment():
    return dict(
        employer="",
        job_title="",
        start_date="",
        present=False,
        end_date="",
        duties="",
        city="",
        state="",
        ZIP="")

def you():
    return dict(
        first_name="",
        middle_name="",
        last_name="",
        phone_number="",
        phone_type="",
        street_number="",
        street_name="",
        city="",
        state="",
        ZIP=""
        )

def states():
    with open("app/MainWindow/states.json","r") as fd:
        return json.load(fd)
