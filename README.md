# The Field Witness Society

Static website published through GitHub Pages at https://fieldwitnesssociety.com/.

Run `python3 tools/build_site.py` after editing `content/` or the shared templates in `tools/build_site.py`. Commit the generated HTML with its sources. Shared styles are in `assets/site.css`.

The header uses the supplied horizontal logo, unchanged, at `assets/brand/fws-horizontal-lockup.png`.

## Pages

The main navigation has four pages: `/` (Home), `/field-notes/`, `/about/` and `/contacts/`. Published Field Notes retain their existing article URLs. Legacy section links redirect to the corresponding page. `/privacy/` is linked from the footer and contact form, outside the four-section main navigation; it requests no indexing but remains publicly accessible when deployed.

## Privacy update authorised on 11 September 2026

The owner confirmed that FWS is a personal project and authorised publication of the privacy notice and email-app contact flow. This implementation is not a certification of compliance with every applicable law.

- The notice identifies Tommaso Bruno as controller and uses the existing project email as the contact. This is the approved legal-page exception to the earlier editorial request to show the name only within Field Note 001. No city or residential address has been added.
- The form becomes an email composer. It opens the visitor's email app, and the visitor must send there. This removes the FormSubmit processing and CAPTCHA step for new enquiries, while preserving a form and direct email link. It does not provide automatic in-browser delivery. A webmail fallback is always available, and fields remain intact after opening the mail app. Mail-handler support and maximum URL length vary by device, so the fallback remains necessary.
- Routine enquiries are handled under legitimate interests. The purpose is responding to communication initiated by the sender; only the message is required in the composer, and a name is optional. Expected use is a direct reply, with no marketing, profiling, or automatic publication. This limited use is reasonably expected by a sender, and the notice identifies the right to object. Reassess this basis if the purpose or data changes.
- Retention uses the approved purpose-based criteria. The owner must review closed enquiries and delete messages that no longer serve a documented purpose, including copies under the owner's control. No deletion automation has been created or represented as existing. Longer retention for a collaboration, legal obligation or claim must have a specific recorded reason.
- Verify the actual terms, roles, any required processing agreements and transfer arrangements for the GitHub and Gmail accounts. General provider notices describe their public practices but do not by themselves establish the controller's compliance.
- If FormSubmit received earlier messages, removing the integration does not erase them. Verify historical processing, account activation and provider retention separately; the documented FormSubmit archive period is 30 days.
- At the owner's subsequent explicit request, the original Univers 67 Condensed Bold and Submariner R24 WOFF2 files have been restored for the visual refresh. EB Garamond remains self-hosted with its OFL licence. The exact supplied logo image is used in both header and footer. Restoring the requested fonts does not verify their licences; licence evidence remains an owner responsibility. Raw proprietary TTF/OTF masters have not been republished.
- The owner must secure the mailbox and hosting accounts, handle rights requests, and revise the notice if processing changes. No assertion is made about account MFA settings or controls we cannot inspect.

Account-specific arrangements for Google/GitHub and any earlier FormSubmit processing cannot be verified from public website code. No new contract has been signed on the owner's behalf. A qualified privacy adviser should resolve those questions before any claim of full compliance.

The published pages include a restrictive meta Content Security Policy and a no-referrer policy. There are no third-party form endpoints, analytics or external embedded resources. These controls do not replace account security or a full accessibility/security audit.

## Contact form implementation

`content/contacts.html` uses a `mailto:` action, with `assets/contact-email.js` preparing an encoded subject and body. It makes no HTTP request and stores no form contents. The default HTML form action also targets the email app if JavaScript is disabled. Users can always email `thefieldwitnesssociety@gmail.com` directly.

There are no email credentials or new third-party services. The old `/contact/thank-you/` URL remains available with neutral wording; it no longer claims that a message was sent.

## Visual refresh

The visual system uses Univers for institutional display headings, EB Garamond for editorial titles and prose, and Submariner for navigation and field metadata. The home page combines an ink background, large type and a full-width photograph. The Field Notes index uses a blue editorial spread; the remaining pages share the revised reading grid and responsive typography.

All public text is preserved, except the paragraph explicitly removed from About beginning “The Society is developing its first programme of Field Notes.” No photographic asset, logo or downloadable PDF has been altered. Images keep their intrinsic proportions. No additional runtime scripts, tracking services or data storage have been added. Reduced-motion preferences are respected.
