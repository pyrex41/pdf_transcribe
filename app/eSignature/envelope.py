import base64
from os import path, getenv

from docusign_esign import EnvelopesApi, EnvelopeDefinition, Document, Signer, CarbonCopy, SignHere, Tabs, Recipients, RecipientViewRequest
from docusign_esign.models import recipient_view_request

from ..jwt_helpers import create_api_client


class EmailController:

  @classmethod
  def worker(cls, args, pdf_filename):
    """
        1. Create the envelope request object
        2. Send the envelope
        """
    envelope_args = args["envelope_args"]
    recipient_view_request = RecipientViewRequest(
        authentication_method="password",
        client_user_id=envelope_args["client_user_id"],
        recipient_id="1",
        return_url="http://localhost:1234/uhc-signature-land",
        user_name=envelope_args["signer_name"],
        email=envelope_args["signer_email"],
        frame_ancestors=[
            "http://localhost:1234", "https://apps-d.docusign.com",
            "https://msblitz.netlify.app"
        ],
        message_origins=["https://apps-d.docusign.com"])
    envelope_definition = cls.make_envelope_uhc(envelope_args, pdf_filename)
    api_client = create_api_client(base_path=args["base_path"],
                                   access_token=args["access_token"])
    envelopes_api = EnvelopesApi(api_client)
    results = envelopes_api.create_envelope(
        account_id=args["account_id"], envelope_definition=envelope_definition)

    envelope_id = results.envelope_id
    recip_result = envelopes_api.create_recipient_view(
        account_id=args["account_id"],
        envelope_id=envelope_id,
        recipient_view_request=recipient_view_request)

    print(results)
    return {"envelope_id": envelope_id, "redirect_url": recip_result.url}

  @classmethod
  def make_envelope_uhc(cls, args, pdf_filename):
    """
        Creates envelope with a single PDF document.
        """

    with open(pdf_filename, "rb") as file:
      doc_pdf_bytes = file.read()
    doc_b64 = base64.b64encode(doc_pdf_bytes).decode("ascii")

    document = Document(
        document_base64=doc_b64,
        name="Document",  # can be different from actual file name
        file_extension="pdf",  # only PDF is accepted in this simplified version
        document_id="1")

    signer = Signer(email=args["signer_email"],
                    name=args["signer_name"],
                    recipient_id="1",
                    routing_order="1",
                    client_user_id=args["client_user_id"])

    sign_here_1 = SignHere(
        anchor_string="Your Signature (required)",
        anchor_units="pixels",
        anchor_x_offset="10",
        anchor_y_offset="-20",
    )

    signer.tabs = Tabs(sign_here_tabs=[sign_here_1])

    cc = CarbonCopy(email=args["cc_email"],
                    name=args["cc_name"],
                    recipient_id="2",
                    routing_order="2")

    env = EnvelopeDefinition(
        email_subject=
        "Please sign your UHC Medical Supplemental Insurance Application",
        documents=[document],
        recipients=Recipients(signers=[signer], carbon_copies=[cc]),
        status=args["status"])

    return env
