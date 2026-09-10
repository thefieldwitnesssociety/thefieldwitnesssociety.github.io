"""Render the existing static GitHub Pages site. No runtime dependencies."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://fieldwitnesssociety.com'
ARTICLE = '/field-notes/the-iron-ore-railway/'
PDF = '/downloads/The_Field_Witness_Society_Field_Note_001_Mauritania.pdf'
DESCRIPTOR = 'An International Society for Geography, Exploration and Documentary Practice.'
NAVIGATION = [('/', 'Home', 'home'), ('/field-notes/', 'Field Notes', 'notes'), ('/about/', 'About', 'about'), ('/contacts/', 'Contacts', 'contacts')]


def brand(masthead=False):
    if masthead:
        return '<a class="brand-lockup header-brand" href="/" aria-label="The Field Witness Society home"><img class="header-logo" src="/assets/brand/fws-horizontal-lockup.png" width="2048" height="423" alt="The Field Witness Society — Geography · Exploration · Documentary Practice"></a>'
    return '<a class="brand-lockup" href="/" aria-label="The Field Witness Society home"><img class="brand-symbol" src="/assets/brand/crater-section.svg" width="42" height="42" alt=""><span class="brand-name">The Field Witness Society</span></a>'


def header(current=''):
    nav = ''.join(f'<a href="{url}"'+(' aria-current="page"' if key == current else '')+f'>{label}</a>' for url,label,key in NAVIGATION)
    return f'<a class="skip-link" href="#main">Skip to content</a><header class="site-header"><div class="shell masthead">{brand(masthead=True)}<nav class="main-nav" aria-label="Main navigation">{nav}</nav></div></header>'


def footer():
    nav = ''.join(f'<a href="{url}">{label}</a>' for url,label,key in NAVIGATION)
    return f'''<footer class="site-footer"><div class="shell"><div class="footer-top">{brand()}
    <nav class="footer-links" aria-label="Footer navigation">{nav}</nav></div>
    <div class="footer-bottom"><p>Geography · Exploration · Documentary Practice</p><a class="footer-privacy" href="/privacy/">Privacy</a><p>© 2026 The Field Witness Society</p></div></div></footer>'''


def link(url, label):
    return f'<a class="text-link" href="{url}">{label}<span class="arrow" aria-hidden="true">→</span></a>'


def document(title, description, route, body, current='', noindex=False, author=None, scripts=()):
    meta = '<meta name="robots" content="noindex">' if noindex else ''
    if author:
        meta += f'<meta name="author" content="{escape(author)}">'
    page_scripts = ''.join(f'<script src="{escape(src, quote=True)}" defer></script>' for src in scripts)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title><meta name="description" content="{escape(description)}">{meta}
<link rel="canonical" href="{ORIGIN}{route}"><meta name="theme-color" content="#f2ebdd">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" href="/assets/brand/crater-section.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/site.css"><link rel="preload" href="/assets/fonts/eb-garamond.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/univers-67.woff2" as="font" type="font/woff2" crossorigin>
<script src="/assets/legacy-navigation.js" defer></script>{page_scripts}
</head><body>{header(current)}{body}{footer()}</body></html>'''


def home():
    return f'''<main id="main" class="shell home-feature">
      <div class="home-copy">
        <h1>Work that begins in the field.</h1>
        <p>The Field Witness Society is an independent international society for geography, exploration and documentary practice. We publish photographs and writing that bring places into closer view.</p>
        {link('/field-notes/', 'Explore the Field Notes')}
      </div>
      <figure class="home-photo">
        <img src="/assets/field-note-001/figure-06-1600.webp" srcset="/assets/field-note-001/figure-06-960.webp 960w, /assets/field-note-001/figure-06-1600.webp 1600w, /assets/field-note-001/figure-06.jpg 2048w" sizes="(max-width:760px) calc(100vw - 48px), (min-width:1600px) 880px, 58vw" width="2048" height="1365" alt="The Ben Amera monolith rising above sand and sparse vegetation in Mauritania." fetchpriority="high">
        <figcaption><span>Ben Amera, Mauritania</span><a href="{ARTICLE}">From Field Note 001</a></figcaption>
      </figure>
    </main>'''


def field_notes():
    return f'''<main id="main" class="shell">
    <header class="page-heading notes-heading"><h1>Field Notes</h1><p class="standfirst">Photography and writing from the field.</p></header>
    <article class="feature" aria-labelledby="feature-title">
      <div class="feature-copy"><p class="eyebrow">Field Note 001 · Mauritania</p>
      <h2 id="feature-title"><a href="{ARTICLE}">The iron ore railway</a></h2>
      <p class="feature-deck">A westbound passage from Choum to Nouadhibou.</p>
      <p class="feature-meta">9–10 October 2025</p>
      {link(ARTICLE, 'Read the Field Note')}</div>
      <figure class="feature-photo"><a href="{ARTICLE}" aria-label="Read The iron ore railway">
      <img src="/assets/field-note-001/figure-01-1600.webp" srcset="/assets/field-note-001/figure-01-960.webp 960w, /assets/field-note-001/figure-01-1600.webp 1600w, /assets/field-note-001/figure-01.jpg 2048w" sizes="(max-width:760px) calc(100vw - 48px), 58vw" width="2048" height="1365" alt="Iron-ore wagons extending across the desert in northern Mauritania." fetchpriority="high"></a>
      <figcaption><span>Northern Mauritania</span><span>Photography and field notes</span></figcaption></figure>
    </article></main>'''


def build():
    (ROOT/'index.html').write_text(document('The Field Witness Society',DESCRIPTOR,'/',home(),'home'),encoding='utf-8')
    (ROOT/'field-notes').mkdir(exist_ok=True)
    (ROOT/'field-notes/index.html').write_text(document('Field Notes · The Field Witness Society','Photography and writing from the field. Explore the publications of The Field Witness Society.','/field-notes/',field_notes(),'notes'),encoding='utf-8')
    about = (ROOT/'content/about.html').read_text(encoding='utf-8')
    (ROOT/'about').mkdir(exist_ok=True)
    (ROOT/'about/index.html').write_text(document('About · The Field Witness Society','The purpose, field practice and principles of The Field Witness Society.','/about/',about,'about'),encoding='utf-8')
    contacts = (ROOT/'content/contacts.html').read_text(encoding='utf-8')
    (ROOT/'contacts').mkdir(exist_ok=True)
    (ROOT/'contacts/index.html').write_text(document('Contacts · The Field Witness Society','Contact The Field Witness Society for editorial enquiries, fieldwork and contributions.','/contacts/',contacts,'contacts',scripts=('/assets/contact-email.js',)),encoding='utf-8')
    privacy = (ROOT/'content/privacy.html').read_text(encoding='utf-8')
    (ROOT/'privacy').mkdir(exist_ok=True)
    (ROOT/'privacy/index.html').write_text(document('Privacy · The Field Witness Society','How The Field Witness Society handles personal data, email enquiries and website visits.','/privacy/',privacy,noindex=True),encoding='utf-8')
    article = (ROOT/'content/field-note-001.html').read_text(encoding='utf-8')
    (ROOT/'field-notes/the-iron-ore-railway/index.html').write_text(document('The iron ore railway · Field Note 001 · The Field Witness Society','A westbound passage from Choum to Nouadhibou, Mauritania. Photography and field notes by Tommaso Bruno, 9–10 October 2025.',ARTICLE,article,current='notes',author='Tommaso Bruno'),encoding='utf-8')
    error = f'<main id="main" class="shell error-page"><p class="eyebrow">Page not found</p><h1>This page is unavailable.</h1><p>You can return to the Society or read our latest Field Note.</p>{link("/", "Return to the homepage")}</main>'
    (ROOT/'404.html').write_text(document('Page not found · The Field Witness Society','Return to the publications of The Field Witness Society.','/404.html',error,noindex=True),encoding='utf-8')
    thanks = f'<main id="main" class="shell message-page"><p class="eyebrow">Contact</p><h1>Write to the Society.</h1><p>Messages are sent from your email app. This page does not confirm delivery.</p>{link("/contacts/", "Go to Contacts")}</main>'
    (ROOT/'contact/thank-you').mkdir(parents=True,exist_ok=True)
    (ROOT/'contact/thank-you/index.html').write_text(document('Email contact · The Field Witness Society','Contact The Field Witness Society by email.','/contact/thank-you/',thanks,current='contacts',noindex=True),encoding='utf-8')
    (ROOT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nDisallow: /tools/\nDisallow: /content/\nSitemap: {ORIGIN}/sitemap.xml\n',encoding='utf-8')
    entries=''.join(f'<url><loc>{ORIGIN}{p}</loc></url>' for p in ['/', '/field-notes/', '/about/', '/contacts/', ARTICLE])
    (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+entries+'</urlset>',encoding='utf-8')


if __name__ == '__main__':
    build()
