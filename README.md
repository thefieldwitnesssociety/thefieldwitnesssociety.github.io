# The Field Witness Society

Static website published through GitHub Pages at https://fieldwitnesssociety.com/.

Run `python3 tools/build_site.py` after editing `content/` or the shared templates in `tools/build_site.py`. Commit the generated HTML with its sources. Shared styles are in `assets/site.css`.

The header uses the supplied horizontal logo, unchanged, at `assets/brand/fws-horizontal-lockup.png`.

## Contact form

The form in `content/about.html` posts to FormSubmit for delivery to `thefieldwitnesssociety@gmail.com`. It uses native browser validation, the provider's default reCAPTCHA, a honeypot and a return page at `/contact/thank-you/`. The visitor's email becomes the Reply-To address. No email credentials are stored in this repository.

First-use activation requires the mailbox owner to submit the published form once and confirm the activation email sent by FormSubmit. This owner verification must be completed before treating inbox delivery as verified. See [FormSubmit setup](https://formsubmit.co/) and [configuration documentation](https://formsubmit.co/documentation).

The direct email link remains available alongside the form.
