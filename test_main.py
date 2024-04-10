import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_transcribe_uhc_enroll_section_1():
    # Define the test data
    data = {
        "filename": "test_file",
        "section": "Section A",
        "applicant_name": "John Doe",
        "phone_number": "1234567890",
        "residential_address": "123 Main St",
        "residential_suite_number": "Suite 1",
        "residential_city": "City",
        "residential_state": "State",
        "residential_zip": "12345",
        "mailing_address": "456 Elm St",
        "mailing_suite_number": "Suite 2",
        "mailing_city": "Mailing City",
        "mailing_state": "Mailing State",
        "mailing_zip": "54321",
        "email": "johndoe@example.com",
        "social_security_number": "123-45-6789",
        "birth_date": "1990-01-01",
        "age": "30",
        "height": "5'10",
        "weight": "180",
        "medicare_card_number": "1234567890",
        "effective_date": "2023-01-01",
        "medicare_part": "Part A"
    }


def test_transcribe_uhc_enroll_section_2a():
    data = {
        "filename": "test_file",
        "section": "Section A",
        "secondary_contact": "Jane Doe",
        "secondary_contact_phone": "9876543210",
        "secondary_contact_email": "janedoe@example.com",
        "hpaa_secondary_contact": "Yes",
        "authorized_representative": "John Smith",
        "authorized_representative_phone": "5555555555",
        "authorized_representative_email": "johnsmith@example.com",
        "hpaa_authorized_representative": "Yes"
    }

    response = client.post("/transcribe/uhc/enroll/section_2a", json=data)

    assert response.status_code == 200
    assert response.json() == {"echo": "success"}

def test_transcribe_uhc_enroll_section_2b():
    data = {
        "filename": "test_file",
        "section": "Section A",
        "applicant_a_plan_selected": "Plan A",
        "medicare_supplement_date": "2023-01-01",
        "modal_premium": "100.00",
        "modal_premium_with_discount": "90.00",
        "policy_fee": "10.00",
        "total_initial_premium_collected": "100.00",
        "subsequent_draft_date": "2023-02-01",
        "billing_file_identifier": "1234"
    }

    response = client.post("/transcribe/uhc/enroll/section_2b", data=data)

    assert response.status_code == 200
    assert response.json() == {"echo": "success"}

def test_transcribe_uhc_enroll_section_3():
    data = {
        "filename": "test_file",
        "section": "Section A",
        "turn_65": "Yes",
        "enrolled_part_b_or_a": "Yes",
        "medicare_medicade_eligibility": "No",
        "medicaid_benefits": "No",
        "plan_other_than_medicare": "No",
        "replace_medicare_supplement": "No",
        "medical_assistance_program": "No",
        "medicaid_nursing_home": "No"
    }

    response = client.post("/transcribe/uhc/enroll/section_3", json=data)

    assert response.status_code == 200
    assert response.json() == {"echo": "success"}

def test_transcribe_uhc_enroll_section_5():
    data = {
        "filename": "test_file",
        "section": "Section A",
        "payment_method": "Bank Draft (EFT)",
        "account_type": "Checking",
        "account_holder_name": "John Doe",
        "bank_name": "Example Bank",
        "routing_number": "123456789",
        "account_number": "987654321"
    }

    response = client.post("/transcribe/uhc/enroll/section_5", json=data)

    assert response.status_code == 200
    assert response.json() == {"echo": "success"}

def test_transcribe_uhc_enroll_section_6():
    data = {
        "filename": "test_file",
        "section": "Section A",
        "request_effective_date": "2023-01-01"
    }

    response = client.post("/transcribe/uhc/enroll/section_6", json=data)

    assert response.status_code == 200
    assert response.json() == {"echo": "success"}

    # Send a POST request to the endpoint
    response = client.post("/transcribe/uhc/enroll/section_1", data=data)

    # Assert the response status code
    assert response.status_code == 200

    # Assert the response content
    assert response.json() == {"echo": "success"}
