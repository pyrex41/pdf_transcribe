import fitz
from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime
from datetime import timedelta


class SectionChoices(str, Enum):
    Section_A = "Section A"
    Section_B = "Section B"


class SectionOneEnrollmentModel(BaseModel):
    filename: str
    section: SectionChoices
    applicant_name: str
    phone_number: str
    residential_address: str
    residential_suite_number: str
    residential_city: str
    residential_state: str
    residential_zip: str
    mailing_address: str
    mailing_suite_number: str
    mailing_city: str
    mailing_state: str
    mailing_zip: str
    email: str
    social_security_number: str
    birth_date: Optional[datetime] = None
    age: str
    height: str
    weight: str
    medicare_card_number: str
    effective_date: Optional[datetime] = None
    medicare_part: str


class SectionTwoAEnrollmentModel(BaseModel):
    filename: str
    householder_name: str
    policy_number: str


class SectionTwoBEnrollmentModel(BaseModel):
    filename: str
    section: SectionChoices
    applicant_a_plan_selected: str
    medicare_supplement_date: Optional[datetime] = datetime.now().date()
    modal_premium: str
    modal_premium_with_discount: str
    policy_fee: str
    total_initial_premium_collected: str
    subsequent_draft_date: Optional[datetime] = datetime.now().date()
    billing_file_identifier: str


class SectionthreeEnrollmentModel(BaseModel):
    filename: str
    applicant_a_effective_date: Optional[datetime] = None
    applicant_b_effective_date: Optional[datetime] = None
    applicant_a_startdate: Optional[datetime] = None
    applicant_a_enddate: Optional[datetime] = None
    applicant_b_startdate: Optional[datetime] = None
    applicant_b_enddate: Optional[datetime] = None
    applicant_a_4_company: str
    applicant_a_4_plan: str
    applicant_b_4_company: str
    applicant_b_4_plan: str
    applicant_a_policy_number: str
    applicant_b_policy_number: str
    applicant_a_5_company: str
    applicant_a_5_plan: str
    applicant_a_5_startdate: Optional[datetime] = None
    applicant_a_5_enddate: Optional[datetime] = None
    applicant_b_5_company: str
    applicant_b_5_plan: str
    applicant_b_5_startdate: Optional[datetime] = None
    applicant_b_5_enddate: Optional[datetime] = None


class SectionfiveEnrollmentModel(BaseModel):
    filename: str
    applicant_a_question1: str
    applicant_a_question2: str
    applicant_a_question3: str
    applicant_b_question1: str
    applicant_b_question2: str
    applicant_b_question3: str


class SectionsixEnrollmentModel(BaseModel):
    filename: str
    applicant_a_primary_physician: str
    applicant_a_phone: str
    applicant_a_physician_office_name: str
    applicant_a_city: str
    applicant_a_state: str
    applicant_a_speciallist_seen: str
    applicant_a_speciality: str
    applicant_a_reason_for_seeing: str
    applicant_a_speciallist2_seen: str
    applicant_a_speciality2: str
    applicant_a_reason_for_seeing2: str
    applicant_a_speciallist3_seen: str
    applicant_a_speciality3: str
    applicant_a_reason_for_seeing3: str
    applicant_b_primary_physician: str
    applicant_b_phone: str
    applicant_b_physician_office_name: str
    applicant_b_city: str
    applicant_b_state: str
    applicant_b_speciallist_seen: str
    applicant_b_speciality: str
    applicant_b_reason_for_seeing: str
    applicant_b_speciallist2_seen: str
    applicant_b_speciality2: str
    applicant_b_reason_for_seeing2: str
    applicant_b_speciallist3_seen: str
    applicant_b_speciality3: str
    applicant_b_reason_for_seeing3: str


def fill_enrollment_section_1a(data: SectionOneEnrollmentModel, filename: str):
    doc = fitz.open(filename)

    # Page 1
    page1 = doc[1]
    page1_width, page1_height = page1.rect.width, page1.rect.height

    # todo -- wire AARP number in from elm / db
    # set_text(page1, "12302400022291", page1_width * .62, page1_height * .415, fontsize=12)

    set_text(page1, data.applicant_name, page1_width * 0.067,
             page1_height * 0.20)
    set_text(page1, data.phone_number, page1_width * 0.649,
             page1_height * 0.197)
    set_text(page1, data.residential_address, page1_width * 0.059,
             page1_height * 0.238)
    set_text(page1, data.residential_suite_number, page1_width * 0.649,
             page1_height * 0.238)
    set_text(page1, data.residential_city, page1_width * 0.059,
             page1_height * 0.271)
    set_text(page1, data.residential_state, page1_width * 0.442,
             page1_height * 0.271)
    set_text(page1, data.residential_zip, page1_width * 0.649,
             page1_height * 0.271)
    set_text(page1, data.mailing_address, page1_width * 0.059,
             page1_height * 0.304)
    set_text(page1, data.mailing_suite_number, page1_width * 0.649,
             page1_height * 0.304)
    set_text(page1, data.mailing_city, page1_width * 0.059,
             page1_height * 0.340)
    set_text(page1, data.mailing_state, page1_width * 0.442,
             page1_height * 0.340)
    set_text(page1, data.mailing_zip, page1_width * 0.649,
             page1_height * 0.340)
    set_text(page1, data.email, page1_width * 0.059,
             page1_height * 0.372)

    set_text(page1, data.social_security_number, page1_width * 0.649,
             page1_height * 0.372)
    set_text(page1, data.birth_date.strftime("%m    %d    %Y"), page1_width * 0.059,
             page1_height * 0.418)
    set_text(page1, data.age, page1_width * 0.316,
             page1_height * 0.418)
    set_text(page1, data.height, page1_width * 0.570,
             page1_height * 0.413)

    set_text(page1, data.weight, page1_width * 0.768,
             page1_height * 0.413)
    set_text(page1, data.medicare_card_number, page1_width * 0.059,
             page1_height * 0.495)
    set_text(page1, data.effective_date.strftime("%m    %d    %Y"), page1_width * 0.452,
             page1_height * 0.495)
    set_text(page1, data.medicare_part, page1_width * 0.780,
             page1_height * 0.495)

    modified_filename = filename.rsplit('.pdf', 1)[0] + "_section_1a.pdf"
    doc.save(modified_filename)


def fill_enrollment_section_1b(data: SectionOneEnrollmentModel, filename: str):
    doc = fitz.open(filename)
    # Page 1
    page1 = doc[1]
    page1_width, page1_height = page1.rect.width, page1.rect.height
    # todo -- wire AARP number in from elm / db
    # set_text(page1, "12302400022291", page1_width * .62, page1_height * .415, fontsize=12)
    set_text(page1, data.applicant_name, page1_width * 0.059,
             page1_height * 0.640)
    set_text(page1, data.phone_number, page1_width * 0.650,
             page1_height * 0.640)
    set_text(page1, data.residential_address, page1_width * 0.059,
             page1_height * 0.678)
    set_text(page1, data.residential_suite_number, page1_width * 0.650,
             page1_height * 0.678)
    set_text(page1, data.residential_city, page1_width * 0.059,
             page1_height * 0.707)
    set_text(page1, data.residential_state, page1_width * 0.442,
             page1_height * 0.707)
    set_text(page1, data.residential_zip, page1_width * 0.656,
             page1_height * 0.707)
    set_text(page1, data.mailing_address, page1_width * 0.059,
             page1_height * 0.742)
    set_text(page1, data.mailing_suite_number, page1_width * 0.650,
             page1_height * 0.742)
    set_text(page1, data.mailing_city, page1_width * 0.059,
             page1_height * 0.779)
    set_text(page1, data.mailing_state, page1_width * 0.442,
             page1_height * 0.779)
    set_text(page1, data.mailing_zip, page1_width * 0.649,
             page1_height * 0.779)
    set_text(page1, data.email, page1_width * 0.059,
             page1_height * 0.813)
    set_text(page1, data.social_security_number, page1_width * 0.649,
             page1_height * 0.813)
    set_text(page1, data.birth_date.strftime("%m    %d    %Y"), page1_width * 0.059,
             page1_height * 0.854)
    set_text(page1, data.age, page1_width * 0.316,
             page1_height * 0.854)
    set_text(page1, data.height, page1_width * 0.570,
             page1_height * 0.850)
    set_text(page1, data.weight, page1_width * 0.768,
             page1_height * 0.850)
    set_text(page1, data.medicare_card_number, page1_width * 0.059,
             page1_height * 0.936)
    set_text(page1, data.effective_date.strftime("%m    %d    %Y"), page1_width * 0.452,
             page1_height * 0.936)
    set_text(page1, data.medicare_part, page1_width * 0.780,
             page1_height * 0.936)
    modified_filename = filename.rsplit('.pdf', 1)[0] + "_1b.pdf"
    doc.save(modified_filename)


def fill_enrollment_section_2a(data: SectionTwoAEnrollmentModel, filename: str):
    doc = fitz.open(filename)
    # Page 1
    page1 = doc[2]
    page1_width, page1_height = page1.rect.width, page1.rect.height
    # todo -- wire AARP number in from elm / db
    # set_text(page1, "12302400022291", page1_width * .62, page1_height * .415, fontsize=12)
    set_text(page1, data.householder_name, page1_width * 0.086,
             page1_height * 0.480)
    set_text(page1, data.policy_number, page1_width * 0.613,
             page1_height * 0.480)

    modified_filename = filename.rsplit('.pdf', 1)[0] + "_2a.pdf"
    doc.save(modified_filename)


def fill_enrollment_section_2ba(data: SectionTwoBEnrollmentModel, filename: str):
    doc = fitz.open(filename)
    # Page 1
    page1 = doc[3]
    page1_width, page1_height = page1.rect.width, page1.rect.height
    # todo -- wire AARP number in from elm / db

    set_text(page1, data.applicant_a_plan_selected, page1_width * 0.060,
             page1_height * 0.114)
    set_text(page1, data.medicare_supplement_date.strftime("%m    %d    %Y"), page1_width * 0.449,
             page1_height * 0.114)

    set_text(page1, data.modal_premium, page1_width * 0.060,
             page1_height * 0.154)
    set_text(page1, data.modal_premium_with_discount, page1_width * 0.242,
             page1_height * 0.154)
    set_text(page1, data.policy_fee, page1_width * 0.536,
             page1_height * 0.154)
    set_text(page1, data.total_initial_premium_collected, page1_width * 0.686,
             page1_height * 0.154)
    set_text(page1, data.subsequent_draft_date.strftime("%m    %d    %Y"), page1_width * 0.060,
             page1_height * 0.235)
    set_text(page1, data.billing_file_identifier, page1_width * 0.447,
             page1_height * 0.275)
    modified_filename = filename.rsplit('.pdf', 1)[0] + "_2ba.pdf"
    doc.save(modified_filename)


def fill_enrollment_section_2bb(data: SectionTwoBEnrollmentModel, filename: str):
    doc = fitz.open(filename)
    # Page 1
    page1 = doc[3]
    page1_width, page1_height = page1.rect.width, page1.rect.height
    # todo -- wire AARP number in from elm / db
    set_text(page1, data.applicant_a_plan_selected, page1_width * 0.060,
             page1_height * 0.481)
    set_text(page1, data.medicare_supplement_date.strftime("%m    %d    %Y"), page1_width * 0.449,
             page1_height * 0.481)
    set_text(page1, data.modal_premium, page1_width * 0.060,
             page1_height * 0.519)
    set_text(page1, data.modal_premium_with_discount, page1_width * 0.242,
             page1_height * 0.519)
    set_text(page1, data.policy_fee, page1_width * 0.536,
             page1_height * 0.519)
    set_text(page1, data.total_initial_premium_collected, page1_width * 0.686,
             page1_height * 0.519)
    set_text(page1, data.subsequent_draft_date.strftime("%m    %d    %Y"), page1_width * 0.060,
             page1_height * 0.602)
    set_text(page1, data.billing_file_identifier, page1_width * 0.447,
             page1_height * 0.642)
    modified_filename = filename.rsplit('.pdf', 1)[0] + "_2bb.pdf"
    doc.save(modified_filename)


def fill_enrollment_section_3(data: SectionthreeEnrollmentModel, filename: str):
    doc = fitz.open(filename)

    page3 = doc[3]
    page3_width, page3_height = page3.rect.width, page3.rect.height

    page4 = doc[4]
    page4_width, page4_height = page4.rect.width, page4.rect.height

    page5 = doc[5]
    page5_width, page5_height = page5.rect.width, page5.rect.height

    # todo -- wire AARP number in from elm / db
    # set_text(page1, "12302400022291", page1_width * .62, page1_height * .415, fontsize=12)
    set_text(page3, data.applicant_a_effective_date.strftime("%m    %d    %Y"), page3_width * 0.095,
             page3_height * 0.874)
    set_text(page3, data.applicant_b_effective_date.strftime("%m    %d    %Y"), page3_width * 0.445,
             page3_height * 0.874)
    set_text(page4, data.applicant_a_startdate.strftime("%m    %d    %Y"), page4_width * 0.09,
             page4_height * 0.385)
    set_text(page4, data.applicant_a_enddate.strftime("%m    %d    %Y"), page4_width * 0.10,
             page4_height * 0.452)
    set_text(page4, data.applicant_b_startdate.strftime("%m    %d    %Y"), page4_width * 0.450,
             page4_height * 0.385)
    set_text(page4, data.applicant_b_enddate.strftime("%m    %d    %Y"), page4_width * 0.454,
             page4_height * 0.452)
    set_text(page4, data.applicant_a_4_company, page4_width * 0.111,
             page4_height * 0.692)
    set_text(page4, data.applicant_a_4_plan, page4_width * 0.573,
             page4_height * 0.692)
    set_text(page4, data.applicant_b_4_company, page4_width * 0.111,
             page4_height * 0.783)
    set_text(page4, data.applicant_b_4_plan, page4_width * 0.578,
             page4_height * 0.783)
    set_text(page4, data.applicant_a_policy_number, page4_width * 0.111,
             page4_height * 0.925)
    set_text(page4, data.applicant_b_policy_number, page4_width * 0.447,
             page4_height * 0.925)
    set_text(page5, data.applicant_a_5_company, page5_width * 0.098,
             page5_height * 0.316)
    set_text(page5, data.applicant_a_5_plan, page5_width * 0.573,
             page5_height * 0.316)
    set_text(page5, data.applicant_a_5_startdate.strftime("%m    %d    %Y"), page5_width * 0.098,
             page5_height * 0.420)

    set_text(page5, data.applicant_a_5_enddate.strftime("%m    %d    %Y"), page5_width * 0.444,
             page5_height * 0.420)
    set_text(page5, data.applicant_b_5_company, page5_width * 0.098,
             page5_height * 0.517)
    set_text(page5, data.applicant_b_5_plan, page5_width * 0.573,
             page5_height * 0.517)
    set_text(page5, data.applicant_b_5_startdate.strftime("%m    %d    %Y"), page5_width * 0.098,
             page5_height * 0.621)

    set_text(page5, data.applicant_b_5_enddate.strftime("%m    %d    %Y"), page5_width * 0.444,
             page5_height * 0.621)

    modified_filename = filename.rsplit('.pdf', 1)[0] + "_3.pdf"
    doc.save(modified_filename)


def fill_enrollment_section_5(data: SectionfiveEnrollmentModel, filename: str):
    doc = fitz.open(filename)
    # Page 1
    page8 = doc[8]
    page8_width, page8_height = page8.rect.width, page8.rect.height
    # todo -- wire AARP number in from elm / db
    # set_text(page1, "12302400022291", page1_width * .62, page1_height * .415, fontsize=12)
    set_text(page8, data.applicant_a_question1, page8_width * 0.059,
             page8_height * 0.221)
    set_text(page8, data.applicant_a_question2, page8_width * 0.059,
             page8_height * 0.329)
    set_text(page8, data.applicant_a_question3, page8_width * 0.059,
             page8_height * 0.423)
    set_text(page8, data.applicant_b_question1, page8_width * 0.059,
             page8_height * 0.665)
    set_text(page8, data.applicant_b_question2, page8_width * 0.059,
             page8_height * 0.769)
    set_text(page8, data.applicant_b_question3, page8_width * 0.059,
             page8_height * 0.844)
    modified_filename = filename.rsplit('.pdf', 1)[0] + "_5.pdf"
    doc.save(modified_filename)


def fill_enrollment_section_6(data: SectionsixEnrollmentModel, filename: str):
    doc = fitz.open(filename)
    # Page 1
    page9 = doc[9]
    page9_width, page9_height = page9.rect.width, page9.rect.height
    # todo -- wire AARP number in from elm / db
    # set_text(page1, "12302400022291", page1_width * .62, page1_height * .415, fontsize=12)
    set_text(page9, data.applicant_a_primary_physician, page9_width * 0.059,
             page9_height * 0.172)
    set_text(page9, data.applicant_a_phone, page9_width * 0.647,
             page9_height * 0.172)
    set_text(page9, data.applicant_a_physician_office_name, page9_width * 0.059,
             page9_height * 0.209)
    set_text(page9, data.applicant_a_city, page9_width * 0.059,
             page9_height * 0.240)
    set_text(page9, data.applicant_a_state, page9_width * 0.647,
             page9_height * 0.240)
    set_text(page9, data.applicant_a_speciallist_seen, page9_width * 0.059,
             page9_height * 0.276)
    set_text(page9, data.applicant_a_speciality, page9_width * 0.647,
             page9_height * 0.276)
    set_text(page9, data.applicant_a_reason_for_seeing, page9_width * 0.059,
             page9_height * 0.313)
    set_text(page9, data.applicant_a_speciallist2_seen, page9_width * 0.059,
             page9_height * 0.346)
    set_text(page9, data.applicant_a_speciality2, page9_width * 0.647,
             page9_height * 0.346)
    set_text(page9, data.applicant_a_reason_for_seeing2, page9_width * 0.059,
             page9_height * 0.378)
    set_text(page9, data.applicant_a_speciallist3_seen, page9_width * 0.059,
             page9_height * 0.414)
    set_text(page9, data.applicant_a_speciality3, page9_width * 0.647,
             page9_height * 0.414)
    set_text(page9, data.applicant_a_reason_for_seeing2, page9_width * 0.059,
             page9_height * 0.453)
    set_text(page9, data.applicant_b_primary_physician, page9_width * 0.059,
             page9_height * 0.595)
    set_text(page9, data.applicant_b_phone, page9_width * 0.647,
             page9_height * 0.595)
    set_text(page9, data.applicant_b_physician_office_name, page9_width * 0.059,
             page9_height * 0.631)
    set_text(page9, data.applicant_b_city, page9_width * 0.059,
             page9_height * 0.662)
    set_text(page9, data.applicant_b_state, page9_width * 0.647,
             page9_height * 0.662)
    set_text(page9, data.applicant_b_speciallist_seen, page9_width * 0.059,
             page9_height * 0.699)
    set_text(page9, data.applicant_b_speciality, page9_width * 0.647,
             page9_height * 0.699)
    set_text(page9, data.applicant_b_reason_for_seeing, page9_width * 0.059,
             page9_height * 0.736)
    set_text(page9, data.applicant_b_speciallist2_seen, page9_width * 0.059,
             page9_height * 0.768)
    set_text(page9, data.applicant_b_speciality2, page9_width * 0.647,
             page9_height * 0.768)
    set_text(page9, data.applicant_b_reason_for_seeing2, page9_width * 0.059,
             page9_height * 0.802)
    set_text(page9, data.applicant_b_speciallist3_seen, page9_width * 0.059,
             page9_height * 0.839)
    set_text(page9, data.applicant_b_speciality3, page9_width * 0.647,
             page9_height * 0.839)
    set_text(page9, data.applicant_b_reason_for_seeing2, page9_width * 0.059,
             page9_height * 0.879)
    modified_filename = filename.rsplit('.pdf', 1)[0] + "_6.pdf"
    doc.save(modified_filename)


def set_text(page, text, x, y, fontsize=10):
    page.insert_text((x, y), text, fontsize=fontsize)


def set_checkbox(page, value, x_yes, y_yes, x_no, y_no):
    if value is not None:
        if value:
            page.draw_rect((x_yes, y_yes, x_yes + 10, y_yes + 10), fill=(0, 0, 0))
        else:
            page.draw_rect((x_no, y_no, x_no + 10, y_no + 10), fill=(0, 0, 0))


def format_phone_number(phone_number: str) -> str:
    """Formats a 10 digit phone number by adding two spaces between the groups.

      Args:
          phone_number (str): The 10 digit phone number to format.

      Returns:
          str: The formatted phone number.
      """
    if len(phone_number) != 10 or not phone_number.isdigit():
        raise ValueError("Invalid phone number. Must be 10 digits.")
    return f'{phone_number[:3]}      {phone_number[3:6]}      {phone_number[6:]}'
