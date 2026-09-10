# The Field Witness Society

Static website published through GitHub Pages at https://fieldwitnesssociety.com/.

Run `python3 tools/build_site.py` after editing `content/` or the shared templates in `tools/build_site.py`. Commit the generated HTML with its sources. Shared styles are in `assets/site.css`.

The header uses the supplied horizontal logo, unchanged, at `assets/brand/fws-horizontal-lockup.png`.

## Pages

The main navigation has four pages: `/` (Home), `/field-notes/`, `/about/` and `/contacts/`. Published Field Notes retain their existing article URLs. Legacy section links redirect to the corresponding page. `/privacy/` is linked from the footer and contact form, outside the four-section main navigation; it requests no indexing but remains publicly accessible when deployed.

## Proposed privacy update — owner review required before deployment

This branch is a proposal, not a compliance certification. It must not replace the live contact flow until the owner has reviewed these changes.

- The user has confirmed that FWS is a personal project. The proposed notice identifies Tommaso Bruno as controller and uses the existing project email as the contact. This is a specific legal-page exception to the earlier editorial request to show the name only within Field Note 001. No city or residential address has been added.
- The form becomes an email composer. It opens the visitor's email app, and the visitor must send there. This removes the FormSubmit processing and CAPTCHA step for new enquiries, while preserving a form and direct email link. It does not provide automatic in-browser delivery. A webmail fallback is always available, and fields remain intact after opening the mail app. Mail-handler support and maximum URL length vary by device, so the fallback remains necessary.
- The privacy notice proposes handling routine enquiries under legitimate interests. The purpose is responding to communication initiated by the sender; only the message is required in the composer, and a name is optional. Expected use is a direct reply, with no marketing, profiling, or automatic publication. The owner must confirm this assessment and actual practices.
- Retention uses purpose-based criteria rather than claiming an unconfirmed fixed number of months. To adopt the notice, the owner must review closed enquiries and delete messages that no longer serve a documented purpose. No deletion automation has been created or represented as existing.
- Verify the actual terms, roles, any required processing agreements and transfer arrangements for the GitHub and Gmail accounts. General provider notices describe their public practices but do not by themselves establish the controller's compliance.
- If FormSubmit received earlier messages, removing the integration does not erase them. Verify historical processing, account activation and provider retention separately; the documented FormSubmit archive period is 30 days.
- Confirm web embedding and distribution rights for Univers and Submariner fonts. Their licence documentation has not been provided. This proposal does not change brand typography or claim those licences have been verified.
- The owner must secure the mailbox and hosting accounts, handle rights requests, and revise the notice if processing changes. No assertion is made about account MFA settings or controls we cannot inspect.

The legal notice is a draft for approval of actual practices. A qualified privacy adviser should review provider arrangements and remaining legal questions before any claim of full compliance.

## Contact form implementation

`content/contacts.html` uses a `mailto:` action, with `assets/contact-email.js` preparing an encoded subject and body. It makes no HTTP request and stores no form contents. The default HTML form action also targets the email app if JavaScript is disabled. Users can always email `thefieldwitnesssociety@gmail.com` directly.

There are no email credentials or new third-party services. The old `/contact/thank-you/` URL remains available with neutral wording; it no longer claims that a message was sent.
