import json,os,sys
from PyQt5.QtWidgets import QHeaderView
def prep_table(table):
    table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


def reference():
    return dict(
        employer="",
        title="",
        first_name="",
        middle_name="",
        last_name="",
        phone_number="",
        phone_type="",
        email="",
        street_name="",
        street_number="",
        city="",
        state="",
        ZIP=""
    )


def phoneTypes():
    return ["Cell","Home","Work"]


def certification():
    return dict(
        certification_name="",
        date_acquired="",
        date_expires=""
        )
def AdditionalInfoTypes():
    return [
        'activities',
        'awards',
        'hobbies',
        'object',
        'other'
        ]

def additionalInfo():
    return dict(
        additional_info="",
        type=""
    )

def links():
    return dict(link="")

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

def contact():
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
