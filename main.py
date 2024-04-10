from ssl import HAS_TLSv1_1
from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.cors import CORSMiddleware
import os
import csv
import json
import fitz
from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from typing import Dict
import base64
from urllib.parse import unquote  # Import the unquote function
from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, ApiException, RecipientViewRequest
from app.jwt_helpers import get_jwt_token, get_private_key
from app.eSignature.envelope import EmailController
from app.jwt_config import DS_JWT

import logging

logging.basicConfig(filename='app.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

from uhc_transcribe import fill_all, add_uhc_signature
from uhc_transcribe import Model as UHCModel
from uhc_enroll import fill_enrollment_section_1a, SectionOneEnrollmentModel, \
    SectionTwoAEnrollmentModel, fill_enrollment_section_1b, fill_enrollment_section_2a, SectionTwoBEnrollmentModel, \
    fill_enrollment_section_2ba, fill_enrollment_section_2bb, SectionthreeEnrollmentModel, fill_enrollment_section_3, \
    SectionChoices, SectionfiveEnrollmentModel, fill_enrollment_section_5, SectionsixEnrollmentModel, \
    fill_enrollment_section_6

app = FastAPI()


# Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "*"
#     ],  # You can specify the allowed origins or use ["*"] to allow all origins
#     allow_credentials=True,
#     allow_methods=[
#         "GET", "POST"
#     ],  # You can specify the allowed HTTP methods or use ["*"] to allow all methods
#     allow_headers=[
#         "*"
#     ],  # You can specify the allowed headers or use ["*"] to allow all headers
# )

# app.add_middleware(HTTPSRedirectMiddleware)


@app.get("/hello/{world}")
async def hello_world(world: str = None):
    return {"message": f"Hello, {'world' if world is None else world}!"}


@app.get("/download/{dir}/{filename}")
async def download_file(dir: str, filename: str):
    file_path = os.path.join(os.getcwd(), dir, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path=file_path,
                        filename=filename,
                        media_type='application/pdf')


@app.post("/transcribe/uhc/medical")
async def transcribe_uhc(body: UHCModel):
    logging.info(f"body: {body}")
    fill_all(body, f"uhc/{body.filename}.pdf")
    return {'file_id': body.filename}


@app.post("/transcribe/uhc/enroll/section_1")
async def transcribe_uhc_enroll(
        filename: str = Form(...),
        section: SectionChoices = Form(...),
        applicant_name: str = Form(...),
        phone_number: str = Form(...),
        residential_address: str = Form(...),
        residential_suite_number: str = Form(...),
        residential_city: str = Form(...),
        residential_state: str = Form(...),
        residential_zip: str = Form(...),
        mailing_address: str = Form(...),
        mailing_suite_number: str = Form(...),
        mailing_city: str = Form(...),
        mailing_state: str = Form(...),
        mailing_zip: str = Form(...),
        email: str = Form(...),
        social_security_number: str = Form(...),
        birth_date: Optional[datetime] = Form(datetime.now().date()),
        age: str = Form(...),
        height: str = Form(...),
        weight: str = Form(...),
        medicare_card_number: str = Form(...),
        effective_date: Optional[datetime] = Form(datetime.now().date()),
        medicare_part: str = Form(...),
):
    body = SectionOneEnrollmentModel(
        filename=filename,
        section=section,
        applicant_name=applicant_name,
        phone_number=phone_number,
        residential_address=residential_address,
        residential_suite_number=residential_suite_number,
        residential_city=residential_city,
        residential_state=residential_state,
        residential_zip=residential_zip,
        mailing_address=mailing_address,
        mailing_suite_number=mailing_suite_number,
        mailing_city=mailing_city,
        mailing_state=mailing_state,
        mailing_zip=mailing_zip,
        email=email,
        social_security_number=social_security_number,
        birth_date=birth_date,
        age=age,
        height=height,
        weight=weight,
        medicare_card_number=medicare_card_number,
        effective_date=effective_date,
        medicare_part=medicare_part,
    )
    if 'Section A' in body.section:
        fill_enrollment_section_1a(body, f"uhc/{body.filename}.pdf")
    else:
        fill_enrollment_section_1b(body, f"uhc/{body.filename}.pdf")

    return {"echo": "success"}


@app.post("/transcribe/uhc/enroll/section_2a")
async def transcribe_uhc_enroll(body: SectionTwoAEnrollmentModel):
    # Decode percent-encoded strings for all string fields in the body
    for field, value in body.dict().items():
        if isinstance(value, str):
            setattr(body, field, unquote(value))
    logging.info(f"body: {body}")
    fill_enrollment_section_2a(body, f"uhc/{body.filename}.pdf")
    return {"echo": "success"}


@app.post("/transcribe/uhc/enroll/section_2b")
async def transcribe_uhc_enroll(
        filename: str = Form(...),
        section: SectionChoices = Form(...),
        applicant_a_plan_selected: str = Form(...),
        medicare_supplement_date: Optional[datetime] = Form(datetime.now().date()),
        modal_premium: str = Form(...),
        modal_premium_with_discount: str = Form(...),
        policy_fee: str = Form(...),
        total_initial_premium_collected: str = Form(...),
        subsequent_draft_date: Optional[datetime] = Form(datetime.now().date()),
        billing_file_identifier: str = Form(...),
):
    body = SectionTwoBEnrollmentModel(
        filename=filename,
        section=section,
        applicant_a_plan_selected=applicant_a_plan_selected,
        medicare_supplement_date=medicare_supplement_date,
        modal_premium=modal_premium,
        modal_premium_with_discount=modal_premium_with_discount,
        policy_fee=policy_fee,
        total_initial_premium_collected=total_initial_premium_collected,
        subsequent_draft_date=subsequent_draft_date,
        billing_file_identifier=billing_file_identifier,
    )

    # Here you can proceed with your processing
    if 'Section A' in body.section:
        fill_enrollment_section_2ba(body, f"uhc/{body.filename}.pdf")
    else:
        fill_enrollment_section_2bb(body, f"uhc/{body.filename}.pdf")

    return {"echo": "success"}


@app.post("/transcribe/uhc/enroll/section_3")
async def transcribe_uhc_enroll(body: SectionthreeEnrollmentModel):
    # Decode percent-encoded strings for all string fields in the body
    for field, value in body.dict().items():
        if isinstance(value, str):
            setattr(body, field, unquote(value))
    logging.info(f"body: {body}")
    fill_enrollment_section_3(body, f"uhc/{body.filename}.pdf")
    return {"echo": "success"}


@app.post("/transcribe/uhc/enroll/section_5")
async def transcribe_uhc_enroll(body: SectionfiveEnrollmentModel):
    # Decode percent-encoded strings for all string fields in the body
    for field, value in body.dict().items():
        if isinstance(value, str):
            setattr(body, field, unquote(value))
    logging.info(f"body: {body}")
    fill_enrollment_section_5(body, f"uhc/{body.filename}.pdf")
    return {"echo": "success"}


@app.post("/transcribe/uhc/enroll/section_6")
async def transcribe_uhc_enroll(body: SectionsixEnrollmentModel):
    # Decode percent-encoded strings for all string fields in the body
    for field, value in body.dict().items():
        if isinstance(value, str):
            setattr(body, field, unquote(value))
    logging.info(f"body: {body}")
    fill_enrollment_section_6(body, f"uhc/{body.filename}.pdf")
    return {"echo": "success"}


class SignatureModel(BaseModel):
    filename: str
    signature: str


# update to accept also the filename timestamp to know what file to update
@app.post("/upload_signature/uhc")
async def upload_signature(signature_data: SignatureModel):
    logging.info(f"signature_data: {signature_data}")
    try:
        # URL-decode the signature before decoding it from base64
        decoded_signature = unquote(signature_data.signature)
        logging.info(f"Received decoded signature: {decoded_signature}")

        # It's also important to ensure that only the base64 part of the data URI is decoded
        # Typically, a data URI looks like "data:[<mediatype>][;base64],<data>"
        # So, we should split by ',' and take the second part for decoding
        if ";base64," in decoded_signature:
            base64_signature = decoded_signature.split(";base64,")[1]
        else:
            raise ValueError("String is not in valid Base64 encoded format")

        signature_bytes = base64.b64decode(base64_signature)
        with open(f"uhc/{signature_data.filename}_sig.png", "wb") as sig_file:
            sig_file.write(signature_bytes)

        add_uhc_signature(signature_data.filename)
        return {
            "message": "Signature uploaded successfully.",
            "url": f"/download/uhc/{signature_data.filename}_signed.pdf",
        }
    except Exception as e:
        logging.error(f"Error processing signature: {e}")
        raise HTTPException(status_code=500,
                            detail=f"Error processing signature: {e}")


@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url='/docs')


class EnvelopeRequest(BaseModel):
    target_id: str


@app.post("/create_envelope/uhc")
async def create_envelope(request: EnvelopeRequest):
    target_id = request.target_id
    api_client = ApiClient()
    api_client.set_base_path(DS_JWT["authorization_server"])
    api_client.set_oauth_host_name(DS_JWT["authorization_server"])

    private_key = get_private_key(
        DS_JWT["private_key_file"]).encode("ascii").decode("utf-8")

    jwt_values = get_token(private_key, api_client)

    envelope_args = {
        "signer_email": "reub.brooks@gmail.com",
        "signer_name": "Reuben Brooks",
        "cc_email": "reub.brooks@gmail.com",
        "cc_name": "Reuben Brooks",
        "status": "sent",
        "client_user_id": "1"
    }
    args = {
        "account_id": jwt_values["api_account_id"],
        "base_path": jwt_values["base_path"],
        "access_token": jwt_values["access_token"],
        "envelope_args": envelope_args,
    }
    add_uhc_signature(target_id)
    pdf_file = f"uhc/{target_id}_sigs.pdf"

    return EmailController.worker(args, pdf_file)


def get_token(private_key, api_client):
    # Call request_jwt_user_token method
    token_response = get_jwt_token(private_key, ["signature", "impersonation"],
                                   DS_JWT["authorization_server"],
                                   DS_JWT["ds_client_id"],
                                   DS_JWT["ds_impersonated_user_id"])
    access_token = token_response.access_token

    # Save API account ID
    user_info = api_client.get_user_info(access_token)
    accounts = user_info.get_accounts()
    api_account_id = accounts[0].account_id
    base_path = f"{accounts[0].base_uri}/restapi"

    return {
        "access_token": access_token,
        "api_account_id": api_account_id,
        "base_path": base_path
    }


@app.get("/get_token")
async def get_token_endpoint():
    api_client = ApiClient()
    api_client.set_base_path(DS_JWT["authorization_server"])
    api_client.set_oauth_host_name(DS_JWT["authorization_server"])

    private_key = get_private_key(
        DS_JWT["private_key_file"]).encode("ascii").decode("utf-8")

    return get_token(private_key, api_client)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
