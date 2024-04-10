import fitz
from pydantic import BaseModel
from typing import Dict, Optional
from copy import copy
from datetime import date


class Model(BaseModel):
    filename: str
    # oneA1: bool
    oneA2: bool
    oneA3: bool
    # oneB1: bool
    oneB2: bool
    oneB3: bool

    twoA1: bool
    twoA2: bool

    threeA1: bool
    threeA11: bool
    threeB1: bool
    threeB11: bool
    three3A2: bool
    three3A21: bool
    three3A22: bool
    three3B2: bool
    three3B21: bool
    three3B22: bool
    three3A31: bool
    three3A32: bool
    three3A33: bool
    three3B31: bool
    three3B32: bool
    three3B33: bool
    three3A4: bool
    three3A42: bool
    fill3A43: bool
    three3B4: bool
    three3B42: bool
    three3B43: bool
    three3A5: bool
    three3B5: bool

    four4A1: bool
    four4B1: bool
    four4A2: bool
    four4B2: bool
    four4A3A: bool
    four4B3A: bool
    four4A3B: bool
    four4B3B: bool
    four4A3C: bool
    four4B3C: bool
    four4A3D: bool
    four4B3D: bool
    four4A3E: bool
    four4B3E: bool
    four4A3F: bool
    four4B3F: bool
    four4A4A: bool
    four4B4A: bool
    four4A4B: bool
    four4B4B: bool
    four4A4C: bool
    four4B4C: bool
    four4A4D: bool
    four4B4D: bool
    four4A5A: bool
    four4B5A: bool
    four4A5B: bool
    four4B5B: bool
    four4A5C: bool
    four4B5C: bool
    four4A5D: bool
    four4B5D: bool
    four4A6A: bool
    four4B6A: bool
    four4A6B: bool
    four4B6B: bool
    four4A6C: bool
    four4B6C: bool
    four4A6D: bool
    four4B6D: bool
    four4A6E: bool
    four4B6E: bool
    four4A7: bool
    four4B7: bool
    four4A8: bool
    four4B8: bool
    four4A9: bool
    four4B9: bool
    four4A10A: bool
    four4B10A: bool
    four4A10B: bool
    four4B10B: bool
    four4A10C: bool
    four4B10C: bool
    four4A10D: bool
    four4B10D: bool
    four4A11: bool
    four4B11: bool


class EnrollmentModel(BaseModel):
    firstName: str  # vv id info
    middleInitial: str
    lastName: str
    permanentAddress1: str
    permanentAddress2: str
    city: str
    state: str
    zip: str
    differentMailingAddress: bool
    mailingAddress1: str
    mailingAddress2: str  # ^^ id info
    oneA: str  # 1A
    oneC: str  # 1C
    oneD: str  # 1D
    oneE: str  # 1E
    oneFi: str  # 1Fi
    oneFii: str  # 1Fii
    oneG: bool  # 1G
    fourPrimaryPhysicianName: str  # vv 4
    fourPrimaryPhysicianPhone: str
    fourSpecialist1Name: str
    fourSpecialist1Phone: str
    fourSpecialist1Diagnosis: str
    fourSpecialist2Name: str
    fourSpecialist2Phone: str
    fourSpecialist2Diagnosis: str  # ^^ 4
    nineD: bool  # 9D
    nineE: bool  # 9E
    nineF: bool  # 9F
    nineG: bool  # 9G
    nineH1: str  # 9H1
    nineH2: str  # 9H2
    nineI: bool  # 9I
    nineJ: bool  # 9J
    nineK: bool  # 9K
    nineL: bool  # 9L
    nineLi: str  # 9Li
    nineLii: str  # 9Lii
    nineOi: str  # 90i
    nineOii: str  # 9Oii
    ninePi: str  # 9Pi
    ninePii: str  # 9Pii
    nineQ: bool  # 9Q


def fill_all(body: Model, filename: str):
    doc = fitz.open("Aetna_Alabama_full.pdf")  # Assuming the PDF is already created

    # Convert the received JSON body to a model and call the appropriate fill function for each field
    # fill1A1(doc, body.oneA1)
    fill1A2(doc, body.oneA2)
    fill1A3(doc, body.oneA3)
    # fill1B1(doc, body.oneB1)
    fill1B2(doc, body.oneB2)
    fill1B3(doc, body.oneB3)

    fill2A1(doc, body.twoA1)
    fill2A2(doc, body.twoA2)

    fill3A1(doc, body.threeA1)
    fill3A11(doc, body.threeA11)

    fill3B1(doc, body.threeB1)
    fill3B11(doc, body.threeB11)

    fill3A2(doc, body.three3A2)
    fill3A21(doc, body.three3A21)
    fill3A22(doc, body.three3A22)

    fill3B2(doc, body.three3B2)
    fill3B21(doc, body.three3B21)
    fill3B22(doc, body.three3B22)

    fill3A31(doc, body.three3A31)
    fill3A32(doc, body.three3A32)
    fill3A33(doc, body.three3A33)

    fill3B31(doc, body.three3B31)
    fill3B32(doc, body.three3B32)
    fill3B33(doc, body.three3B33)

    fill3A4(doc, body.three3A4)
    fill3A42(doc, body.three3A42)
    fill3A43(doc, body.fill3A43)

    fill3B4(doc, body.three3B4)
    fill3B42(doc, body.three3B42)
    fill3B43(doc, body.three3B43)

    fill3A5(doc, body.three3A5)
    fill3B5(doc, body.three3B5)

    ###
    fill4A1(doc, body.four4A1)
    fill4B1(doc, body.four4B1)

    fill4A2(doc, body.four4A2)
    fill4B2(doc, body.four4B2)

    fill4A3A(doc, body.four4A3A)
    fill4B3A(doc, body.four4B3A)

    fill4A3B(doc, body.four4A3B)
    fill4B3B(doc, body.four4B3B)

    fill4A3C(doc, body.four4A3C)
    fill4B3C(doc, body.four4B3C)

    fill4A3D(doc, body.four4A3D)
    fill4B3D(doc, body.four4B3D)

    fill4A3E(doc, body.four4A3E)
    fill4B3E(doc, body.four4B3E)

    fill4A3F(doc, body.four4A3F)
    fill4B3F(doc, body.four4B3F)
    ###
    fill4A4A(doc, body.four4A4A)
    fill4B4A(doc, body.four4B4A)

    fill4A4B(doc, body.four4A4B)
    fill4B4B(doc, body.four4B4B)

    fill4A4C(doc, body.four4A4C)
    fill4B4C(doc, body.four4B4C)

    fill4A4D(doc, body.four4A4D)
    fill4B4D(doc, body.four4B4D)
    ###
    fill4A5A(doc, body.four4A5A)
    fill4B5A(doc, body.four4B5A)

    fill4A5B(doc, body.four4A5B)
    fill4B5B(doc, body.four4B5B)

    fill4A5C(doc, body.four4A5C)
    fill4B5C(doc, body.four4B5C)

    fill4A5D(doc, body.four4A5D)
    fill4B5D(doc, body.four4B5D)
    ###
    fill4A6A(doc, body.four4A6A)
    fill4B6A(doc, body.four4B6A)

    fill4A6B(doc, body.four4A6B)
    fill4B6B(doc, body.four4B6B)

    fill4A6C(doc, body.four4A6C)
    fill4B6C(doc, body.four4B6C)

    fill4A6D(doc, body.four4A6D)
    fill4B6D(doc, body.four4B6D)

    fill4A6E(doc, body.four4A6E)
    fill4B6E(doc, body.four4B6E)
    ###
    fill4A7(doc, body.four4A7)
    fill4B7(doc, body.four4B7)

    fill4A8(doc, body.four4A8)
    fill4B8(doc, body.four4B8)

    fill4A9(doc, body.four4A9)
    fill4B9(doc, body.four4B9)

    ###
    fill4A10A(doc, body.four4A10A)
    fill4B10A(doc, body.four4B10A)

    fill4A10B(doc, body.four4A10B)
    fill4B10B(doc, body.four4B10B)

    fill4A10C(doc, body.four4A10C)
    fill4B10C(doc, body.four4B10C)

    fill4A10D(doc, body.four4A10D)
    fill4B10D(doc, body.four4B10D)
    ###
    fill4A11(doc, body.four4A11)
    fill4B11(doc, body.four4B11)

    # fill6A(doc, body.sixA)
    # fill6B(doc, body.sixB)
    # fill6C(doc, body.sixC)
    # fill6D(doc, body.sixD)
    # fill6E(doc, body.sixE)
    # fill6F(doc, body.sixF)
    # fill6G(doc, body.sixG)
    # fill6H(doc, body.sixH)
    # fill7A1(doc, body.sevenA1)
    # fill7A2(doc, body.sevenA2)
    # fill7A3(doc, body.sevenA3)
    # fill7A4(doc, body.sevenA4)
    # fill7A5(doc, body.sevenA5)
    # fill7A6(doc, body.sevenA6)
    # fill7B1(doc, body.sevenB1)
    # fill7B2(doc, body.sevenB2)
    # fill7B3(doc, body.sevenB3)
    # fill7B4(doc, body.sevenB4)
    # fill7B5(doc, body.sevenB5)
    # fill7B6(doc, body.sevenB6)
    # fill7B7(doc, body.sevenB7)
    # fill7B8(doc, body.sevenB8)
    # fill7B9(doc, body.sevenB9)
    # fill7B10(doc, body.sevenB10)
    # fill7B11(doc, body.sevenB11)
    # fill7B12(doc, body.sevenB12)
    # fill7B13(doc, body.sevenB13)
    # fill7B14(doc, body.sevenB14)
    # fill7C(doc, body.sevenC)

    out = copy(body.filename)
    if not out.endswith(".pdf"):
        out += ".pdf"
    doc.save("uhc/" + out)  # Save the modified PDF


def page_i_male_points(doc, i):
    page = doc[i]
    return page.search_for("Male", quads=True)


def page_i_female_points(doc, i):
    page = doc[i]
    return page.search_for("Female", quads=True)


def page_i_applicant_points(doc, i):
    page = doc[i]
    return page.search_for("Applicant(s)", quads=True)


def page_i_agent_points(doc, i):
    page = doc[i]
    return page.search_for("Agent", quads=True)


def page_i_yes_points(doc, i):
    page = doc[i]
    return page.search_for("Yes", quads=True)


def page_i_no_points(doc, i):
    page = doc[i]
    return page.search_for("No", quads=True)


q_page_1 = 1
q_page_2 = 2
q_page_3 = 3
q_page_4 = 4
q_page_5 = 5
q_page_6 = 6
q_page_7 = 7

page1_male_points = lambda doc: page_i_male_points(doc, q_page_1)
page1_female_points = lambda doc: page_i_female_points(doc, q_page_1)
page2_applicant_points = lambda doc: page_i_applicant_points(doc, q_page_2)
page2_agent_points = lambda doc: page_i_agent_points(doc, q_page_2)
page1_yes_points = lambda doc: page_i_yes_points(doc, q_page_1)
page1_no_points = lambda doc: page_i_no_points(doc, q_page_1)
page2_yes_points = lambda doc: page_i_yes_points(doc, q_page_2)
page2_no_points = lambda doc: page_i_no_points(doc, q_page_2)
page3_yes_points = lambda doc: page_i_yes_points(doc, q_page_3)
page3_no_points = lambda doc: page_i_no_points(doc, q_page_3)

page4_yes_points = lambda doc: page_i_yes_points(doc, q_page_4)
page4_no_points = lambda doc: page_i_no_points(doc, q_page_4)

page5_yes_points = lambda doc: page_i_yes_points(doc, q_page_5)
page5_no_points = lambda doc: page_i_no_points(doc, q_page_5)

page6_yes_points = lambda doc: page_i_yes_points(doc, q_page_6)
page6_no_points = lambda doc: page_i_no_points(doc, q_page_6)

page7_yes_points = lambda doc: page_i_yes_points(doc, q_page_7)
page7_no_points = lambda doc: page_i_no_points(doc, q_page_7)


def fill_page_1_male_female(doc, ii: int, answer: bool):
    page = doc[q_page_1]
    location = page1_male_points(doc)[ii] if answer else page1_female_points(doc)[ii]
    x0, y0, x1, y1 = location.rect
    if answer:
        box = fitz.Rect(x0 - 10, y0 + 3, x0 - 1, y1 - 1)
    else:
        box = fitz.Rect(x0 - 11, y0 + 3, x0 - 1, y1 - 1)

    page.draw_rect(box, color=(0, 0, 0), fill=(0, 0, 0), overlay=True)
    return page


def fill_page_1(doc, ii: int, answer: bool):
    page = doc[q_page_1]
    location = page1_yes_points(doc)[ii] if answer else page1_no_points(doc)[ii]
    x0, y0, x1, y1 = location.rect
    if answer:
        box = fitz.Rect(x0 - 10, y0 + 3, x0 - 1, y1 - 1)
    else:
        box = fitz.Rect(x0 - 11, y0 + 3, x0 - 1, y1 - 1)

    page.draw_rect(box, color=(0, 0, 0), fill=(0, 0, 0), overlay=True)
    return page


def fill_page_2_applicant_agent(doc, ii: int, answer: bool):
    page = doc[q_page_2]
    location = page2_applicant_points(doc)[ii] if answer else page2_agent_points(doc)[ii]
    x0, y0, x1, y1 = location.rect
    if answer:
        box = fitz.Rect(x0 - 10, y0 + 3, x0 - 1, y1 - 1)
    else:
        box = fitz.Rect(x0 - 11, y0 + 3, x0 - 1, y1 - 1)

    page.draw_rect(box, color=(0, 0, 0), fill=(0, 0, 0), overlay=True)
    return page


def fill_page_2(doc, ii: int, answer: bool):
    page = doc[q_page_2]
    location = page2_yes_points(doc)[ii] if answer else page2_no_points(doc)[ii]
    x0, y0, x1, y1 = location.rect
    if answer:
        box = fitz.Rect(x0 - 10, y0 + 3, x0 - 1, y1 - 1)
    else:
        box = fitz.Rect(x0 - 11, y0 + 3, x0 - 1, y1 - 1)

    page.draw_rect(box, color=(0, 0, 0), fill=(0, 0, 0), overlay=True)
    return page


def fill_page_3(doc, ii: int, answer: bool):
    page = doc[q_page_3]
    location = page3_yes_points(doc)[ii] if answer else page3_no_points(doc)[ii]
    x0, y0, x1, y1 = location.rect
    if answer:
        box = fitz.Rect(x0 - 10, y0 + 3, x0 - 1, y1 - 1)
    else:
        box = fitz.Rect(x0 - 11, y0 + 3, x0 - 1, y1 - 1)

    page.draw_rect(box, color=(0, 0, 0), fill=(0, 0, 0), overlay=True)
    return page


def fill_page_4(doc, ii: int, answer: bool):
    page = doc[q_page_4]
    location = page4_yes_points(doc)[ii] if answer else page4_yes_points(doc)[ii]
    x0, y0, x1, y1 = location.rect
    if answer:
        box = fitz.Rect(x0 - 10, y0 + 3, x0 - 1, y1 - 1)
    else:
        box = fitz.Rect(x0 - 11, y0 + 3, x0 - 1, y1 - 1)

    page.draw_rect(box, color=(0, 0, 0), fill=(0, 0, 0), overlay=True)
    return page


def fill_page_5(doc, ii: int, answer: bool):
    page = doc[q_page_5]
    location = page5_yes_points(doc)[ii] if answer else page5_yes_points(doc)[ii]
    x0, y0, x1, y1 = location.rect
    if answer:
        box = fitz.Rect(x0 - 10, y0 + 3, x0 - 1, y1 - 1)
    else:
        box = fitz.Rect(x0 - 11, y0 + 3, x0 - 1, y1 - 1)

    page.draw_rect(box, color=(0, 0, 0), fill=(0, 0, 0), overlay=True)
    return page


def fill_page_6(doc, ii: int, answer: bool):
    page = doc[q_page_6]
    location = page6_yes_points(doc)[ii] if answer else page6_yes_points(doc)[ii]
    x0, y0, x1, y1 = location.rect
    if answer:
        box = fitz.Rect(x0 - 10, y0 + 3, x0 - 1, y1 - 1)
    else:
        box = fitz.Rect(x0 - 11, y0 + 3, x0 - 1, y1 - 1)

    page.draw_rect(box, color=(0, 0, 0), fill=(0, 0, 0), overlay=True)
    return page


def fill_page_7(doc, ii: int, answer: bool):
    page = doc[q_page_7]
    location = page7_yes_points(doc)[ii] if answer else page7_yes_points(doc)[ii]
    x0, y0, x1, y1 = location.rect
    if answer:
        box = fitz.Rect(x0 - 10, y0 + 3, x0 - 1, y1 - 1)
    else:
        box = fitz.Rect(x0 - 11, y0 + 3, x0 - 1, y1 - 1)

    page.draw_rect(box, color=(0, 0, 0), fill=(0, 0, 0), overlay=True)
    return page


def fill1A1(doc, answer: bool):
    return fill_page_1_male_female(doc, 0, answer)


def fill1A2(doc, answer: bool):
    return fill_page_1(doc, 0, answer)


def fill1A3(doc, answer: bool):
    return fill_page_1(doc, 1, answer)


def fill1B1(doc, answer: bool):
    return fill_page_1_male_female(doc, 1, answer)


def fill1B2(doc, answer: bool):
    return fill_page_1(doc, 2, answer)


def fill1B3(doc, answer: bool):
    return fill_page_1(doc, 3, answer)


def fill2A1(doc, answer: bool):
    return fill_page_2(doc, 0, answer)


def fill2A2(doc, answer: bool):
    return fill_page_2_applicant_agent(doc, 1, answer)


#############
def fill3A1(doc, answer: bool):
    return fill_page_3(doc, 0, answer)


def fill3A11(doc, answer: bool):
    return fill_page_3(doc, 2, answer)


def fill3B1(doc, answer: bool):
    return fill_page_3(doc, 1, answer)


def fill3B11(doc, answer: bool):
    return fill_page_3(doc, 3, answer)


def fill3A2(doc, answer: bool):
    return fill_page_4(doc, 0, answer)


def fill3A21(doc, answer: bool):
    return fill_page_4(doc, 3, answer)


def fill3A22(doc, answer: bool):
    return fill_page_4(doc, 5, answer)


def fill3B2(doc, answer: bool):
    return fill_page_4(doc, 1, answer)


def fill3B21(doc, answer: bool):
    return fill_page_4(doc, 4, answer)


def fill3B22(doc, answer: bool):
    return fill_page_4(doc, 6, answer)


def fill3A31(doc, answer: bool):
    return fill_page_4(doc, 7, answer)


def fill3A32(doc, answer: bool):
    return fill_page_4(doc, 9, answer)


def fill3A33(doc, answer: bool):
    return fill_page_4(doc, 11, answer)


def fill3B31(doc, answer: bool):
    return fill_page_4(doc, 8, answer)


def fill3B32(doc, answer: bool):
    return fill_page_4(doc, 10, answer)


def fill3B33(doc, answer: bool):
    return fill_page_4(doc, 12, answer)


def fill3A4(doc, answer: bool):
    return fill_page_4(doc, 13, answer)


def fill3A42(doc, answer: bool):
    return fill_page_4(doc, 15, answer)


def fill3A43(doc, answer: bool):
    return fill_page_4(doc, 17, answer)


def fill3B4(doc, answer: bool):
    return fill_page_4(doc, 14, answer)


def fill3B42(doc, answer: bool):
    return fill_page_4(doc, 16, answer)


def fill3B43(doc, answer: bool):
    return fill_page_4(doc, 18, answer)


def fill3A5(doc, answer: bool):
    return fill_page_5(doc, 0, answer)


def fill3B5(doc, answer: bool):
    return fill_page_5(doc, 1, answer)


def fill4A1(doc, answer: bool):
    return fill_page_6(doc, 1, answer)


def fill4B1(doc, answer: bool):
    return fill_page_6(doc, 2, answer)


def fill4A2(doc, answer: bool):
    return fill_page_6(doc, 3, answer)


def fill4B2(doc, answer: bool):
    return fill_page_6(doc, 4, answer)


def fill4A3A(doc, answer: bool):
    return fill_page_6(doc, 5, answer)


def fill4B3A(doc, answer: bool):
    return fill_page_6(doc, 6, answer)


def fill4A3B(doc, answer: bool):
    return fill_page_6(doc, 7, answer)


def fill4B3B(doc, answer: bool):
    return fill_page_6(doc, 8, answer)


def fill4A3C(doc, answer: bool):
    return fill_page_6(doc, 9, answer)


def fill4B3C(doc, answer: bool):
    return fill_page_6(doc, 10, answer)


def fill4A3D(doc, answer: bool):
    return fill_page_6(doc, 11, answer)


def fill4B3D(doc, answer: bool):
    return fill_page_6(doc, 12, answer)


def fill4A3E(doc, answer: bool):
    return fill_page_6(doc, 13, answer)


def fill4B3E(doc, answer: bool):
    return fill_page_6(doc, 14, answer)


def fill4A3F(doc, answer: bool):
    return fill_page_6(doc, 15, answer)


def fill4B3F(doc, answer: bool):
    return fill_page_6(doc, 16, answer)


def fill4A4A(doc, answer: bool):
    return fill_page_6(doc, 17, answer)


def fill4B4A(doc, answer: bool):
    return fill_page_6(doc, 18, answer)


def fill4A4B(doc, answer: bool):
    return fill_page_6(doc, 19, answer)


def fill4B4B(doc, answer: bool):
    return fill_page_6(doc, 20, answer)


def fill4A4C(doc, answer: bool):
    return fill_page_6(doc, 21, answer)


def fill4B4C(doc, answer: bool):
    return fill_page_6(doc, 22, answer)


def fill4A4D(doc, answer: bool):
    return fill_page_6(doc, 23, answer)


def fill4B4D(doc, answer: bool):
    return fill_page_6(doc, 24, answer)


def fill4A5A(doc, answer: bool):
    return fill_page_6(doc, 25, answer)


def fill4B5A(doc, answer: bool):
    return fill_page_6(doc, 26, answer)


def fill4A5B(doc, answer: bool):
    return fill_page_6(doc, 27, answer)


def fill4B5B(doc, answer: bool):
    return fill_page_6(doc, 28, answer)


def fill4A5C(doc, answer: bool):
    return fill_page_6(doc, 29, answer)


def fill4B5C(doc, answer: bool):
    return fill_page_6(doc, 30, answer)


def fill4A5D(doc, answer: bool):
    return fill_page_6(doc, 31, answer)


def fill4B5D(doc, answer: bool):
    return fill_page_6(doc, 32, answer)


def fill4A6A(doc, answer: bool):
    return fill_page_7(doc, 0, answer)


def fill4B6A(doc, answer: bool):
    return fill_page_7(doc, 1, answer)


def fill4A6B(doc, answer: bool):
    return fill_page_7(doc, 2, answer)


def fill4B6B(doc, answer: bool):
    return fill_page_7(doc, 3, answer)


def fill4A6C(doc, answer: bool):
    return fill_page_7(doc, 4, answer)


def fill4B6C(doc, answer: bool):
    return fill_page_7(doc, 5, answer)


def fill4A6D(doc, answer: bool):
    return fill_page_7(doc, 6, answer)


def fill4B6D(doc, answer: bool):
    return fill_page_7(doc, 7, answer)


def fill4A6E(doc, answer: bool):
    return fill_page_7(doc, 8, answer)


def fill4B6E(doc, answer: bool):
    return fill_page_7(doc, 9, answer)


def fill4A7(doc, answer: bool):
    return fill_page_7(doc, 10, answer)


def fill4B7(doc, answer: bool):
    return fill_page_7(doc, 11, answer)


def fill4A8(doc, answer: bool):
    return fill_page_7(doc, 12, answer)


def fill4B8(doc, answer: bool):
    return fill_page_7(doc, 13, answer)


def fill4A9(doc, answer: bool):
    return fill_page_7(doc, 14, answer)


def fill4B9(doc, answer: bool):
    return fill_page_7(doc, 15, answer)


def fill4A10A(doc, answer: bool):
    return fill_page_7(doc, 16, answer)


def fill4B10A(doc, answer: bool):
    return fill_page_7(doc, 17, answer)


def fill4A10B(doc, answer: bool):
    return fill_page_7(doc, 18, answer)


def fill4B10B(doc, answer: bool):
    return fill_page_7(doc, 19, answer)


def fill4A10C(doc, answer: bool):
    return fill_page_7(doc, 20, answer)


def fill4B10C(doc, answer: bool):
    return fill_page_7(doc, 21, answer)


def fill4A10D(doc, answer: bool):
    return fill_page_7(doc, 22, answer)


def fill4B10D(doc, answer: bool):
    return fill_page_7(doc, 23, answer)


def fill4A11(doc, answer: bool):
    return fill_page_7(doc, 24, answer)


def fill4B11(doc, answer: bool):
    return fill_page_7(doc, 25, answer)


#####################


# def fill6A(doc, answer: bool):
#     ii = 3 if answer else 9
#     return fill_page_1(doc, ii, answer)
#
#
# def fill6B(doc, answer: bool):
#     ii = 4 if answer else 11
#     return fill_page_1(doc, ii, answer)
#
#
# def fill6C(doc, answer: bool):
#     ii = 5 if answer else 14
#     return fill_page_1(doc, ii, answer)
#
#
# def fill6D(doc, answer: bool):
#     ii = 6 if answer else 16
#     return fill_page_1(doc, ii, answer)
#
#
# def fill6E(doc, answer: bool):
#     ii = 0 if answer else 1
#     return fill_page_2(doc, ii, answer)
#
#
# def fill6F(doc, answer: bool):
#     ii = 1 if answer else 6
#     return fill_page_2(doc, ii, answer)
#
#
# def fill6G(doc, answer: bool):
#     ii = 2 if answer else 10
#     return fill_page_2(doc, ii, answer)
#
#
# def fill6H(doc, answer: bool):
#     ii = 3 if answer else 13
#     return fill_page_2(doc, ii, answer)
#
#
# def fill7A1(doc, answer: bool):
#     ii = 6 if answer else 20
#     return fill_page_2(doc, ii, answer)
#
#
# def fill7A2(doc, answer: bool):
#     ii = 7 if answer else 22
#     return fill_page_2(doc, ii, answer)
#
#
# def fill7A3(doc, answer: bool):
#     ii = 8 if answer else 24
#     return fill_page_2(doc, ii, answer)
#
#
# def fill7A4(doc, answer: bool):
#     ii = 9 if answer else 26
#     return fill_page_2(doc, ii, answer)
#
#
# def fill7A5(doc, answer: bool):
#     ii = 10 if answer else 28
#     return fill_page_2(doc, ii, answer)
#
#
# def fill7A6(doc, answer: bool):
#     ii = 11 if answer else 30
#     return fill_page_2(doc, ii, answer)


# def fill7B1(doc, answer: bool):
#     ii = 1 if answer else 3
#     return fill_page_3(doc, ii, answer)
#
#
# def fill7B2(doc, answer: bool):
#     ii = 2 if answer else 5
#     return fill_page_3(doc, ii, answer)
#
#
# def fill7B3(doc, answer: bool):
#     ii = 3 if answer else 7
#     return fill_page_3(doc, ii, answer)
#
#
# def fill7B4(doc, answer: bool):
#     ii = 4 if answer else 9
#     return fill_page_3(doc, ii, answer)
#
#
# def fill7B5(doc, answer: bool):
#     ii = 5 if answer else 11
#     return fill_page_3(doc, ii, answer)
#
#
# def fill7B6(doc, answer: bool):
#     ii = 6 if answer else 13
#     return fill_page_3(doc, ii, answer)
#
#
# def fill7B7(doc, answer: bool):
#     ii = 7 if answer else 15
#     return fill_page_3(doc, ii, answer)
#
#
# def fill7B8(doc, answer: bool):
#     ii = 8 if answer else 17
#     return fill_page_3(doc, ii, answer)
#
#
# def fill7B9(doc, answer: bool):
#     ii = 9 if answer else 19
#     return fill_page_3(doc, ii, answer)
#
#
# def fill7B10(doc, answer: bool):
#     ii = 10 if answer else 21
#     return fill_page_3(doc, ii, answer)
#
#
# def fill7B11(doc, answer: bool):
#     ii = 11 if answer else 23
#     return fill_page_3(doc, ii, answer)
#
#
# def fill7B12(doc, answer: bool):
#     ii = 12 if answer else 25
#     return fill_page_3(doc, ii, answer)
#
#
# def fill7B13(doc, answer: bool):
#     ii = 13 if answer else 27
#     return fill_page_3(doc, ii, answer)
#
#
# def fill7B14(doc, answer: bool):
#     ii = 14 if answer else 29
#     return fill_page_3(doc, ii, answer)
#
#
# def fill7C(doc, answer: bool):
#     # Assuming the logic for `fill7C` is similar to others but with specific indices.
#     # Adjust indices as per actual requirements.
#     ii = 15 if answer else 32
#     return fill_page_3(doc, ii, answer)


def add_uhc_signature_demo(target_id: str):
    # Open the PDF document
    doc = fitz.open(target_id + ".pdf")
    page = doc[2]
    w = 150
    h = 150
    x0 = page.rect[2] / 2 - w / 2
    x1 = x0 + w
    y1 = page.rect[3] * .92
    y0 = y1 - h
    rect = fitz.Rect(x0, y0, x1, y1)
    page.insert_image(rect, filename=target_id + "_sig.png", overlay=True)
    doc.save(target_id + "_signed.pdf")


def add_uhc_signature(target_id: str):
    # Open the PDF document
    doc = fitz.open("uhc/" + target_id + "_enroll.pdf")

    # Define the signature and date insertion logic
    def insert_sig_and_date(page_num, y_percent, sig_number, sig_left=True):
        page = doc[page_num]
        today = date.today()
        formatted_date = today.strftime("%m    %d     %Y")
        rect_width, rect_height = 130, 30
        x0 = page.rect[0] + 30 if sig_left else page.rect[2] - rect_width
        y0 = page.rect[3] * y_percent
        y1 = y0 + rect_height
        x1 = x0 + rect_width if sig_left else page.rect[2]
        rect = fitz.Rect(x0, y0, x1, y1)
        page.insert_text((x0 + 442, y1 - 9),
                         formatted_date,
                         fontsize=11,
                         color=(0, 0, 0))

    # Insert signature placeholders on specified pages and positions
    insert_sig_and_date(7, 0.278, 1)  # Page 8, about 25% down
    insert_sig_and_date(8, 0.385, 2)  # Page 9, about 40% down
    insert_sig_and_date(8, 0.83, 3)  # Page 9, about 90% down
    insert_sig_and_date(9, 0.44,
                        4)  # Page 10, about 48% down, signature on right

    # Save the modified document
    doc.save("uhc/" + target_id + "_sigs.pdf")
