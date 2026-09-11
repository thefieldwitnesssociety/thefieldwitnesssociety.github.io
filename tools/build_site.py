"""Render the existing static GitHub Pages site. No runtime dependencies."""
from pathlib import Path
from html import escape
from hashlib import sha256

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://fieldwitnesssociety.com'
ARTICLE = '/field-notes/the-iron-ore-railway/'
PDF = '/downloads/The_Field_Witness_Society_Field_Note_001_Mauritania.pdf'
DESCRIPTOR = 'An International Society for Geography, Exploration and Documentary Practice.'
NAVIGATION = [('/', 'Home', 'home'), ('/field-notes/', 'Field Notes', 'notes'), ('/about/', 'About', 'about'), ('/contacts/', 'Contacts', 'contacts')]


def asset_url(path):
    fingerprint = sha256((ROOT / path.lstrip('/')).read_bytes()).hexdigest()[:12]
    return f'{path}?v={fingerprint}'


def brand(masthead=False):
    if masthead:
        return '<a class="brand-lockup header-brand" href="/" aria-label="The Field Witness Society home"><img class="header-logo" src="/assets/brand/fws-horizontal-lockup.png" width="2048" height="423" alt="The Field Witness Society — Geography · Exploration · Documentary Practice"></a>'
    return '<a class="brand-lockup footer-brand" href="/" aria-label="The Field Witness Society home"><img src="/assets/brand/fws-horizontal-lockup.png" width="2048" height="423" alt="The Field Witness Society — Geography · Exploration · Documentary Practice"></a>'


def header(current=''):
    nav = ''.join(f'<a href="{url}"'+(' aria-current="page"' if key == current else '')+f'>{label}</a>' for url,label,key in NAVIGATION)
    return f'<a class="skip-link" href="#main">Skip to content</a><header class="site-header"><div class="shell masthead">{brand(masthead=True)}<button class="menu-toggle" aria-label="Open navigation" aria-controls="main-navigation" aria-expanded="false" hidden><span aria-hidden="true"></span><span aria-hidden="true"></span></button><nav id="main-navigation" class="main-nav" aria-label="Main navigation">{nav}</nav></div></header>'


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
    page_scripts = ''.join(f'<script src="{escape(asset_url(src), quote=True)}" defer></script>' for src in scripts)
    page_class = 'article' if route == ARTICLE else current or ('privacy' if route == '/privacy/' else 'utility')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self'; font-src 'self'; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action mailto:; upgrade-insecure-requests">
<title>{escape(title)}</title><meta name="description" content="{escape(description)}">{meta}
<link rel="canonical" href="{ORIGIN}{route}"><meta name="theme-color" content="#f2ebdd">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" href="/assets/brand/crater-section.svg" type="image/svg+xml">
<link rel="stylesheet" href="{asset_url('/assets/site.css')}"><link rel="preload" href="/assets/fonts/eb-garamond.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/univers-67.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/submariner-r24.woff2" as="font" type="font/woff2" crossorigin>
<script src="{asset_url('/assets/legacy-navigation.js')}" defer></script><script src="{asset_url('/assets/site-navigation.js')}" defer></script>{page_scripts}
</head><body class="page-{page_class}">{header(current)}{body}{footer()}</body></html>'''


def home():
    return f'''<main id="main" class="home-feature">
      <section class="home-hero" aria-labelledby="home-title">
        <picture class="hero-image">
          <source media="(max-width: 640px)" srcset="/assets/photography/snow-detail-640.webp 640w, /assets/photography/snow-detail-960.webp 960w" sizes="100vw" width="1365" height="2048">
          <img src="/assets/photography/snow-ridge-1600.webp" srcset="/assets/photography/snow-ridge-960.webp 960w, /assets/photography/snow-ridge-1600.webp 1600w, /assets/photography/snow-ridge-2048.webp 2048w" sizes="100vw" width="2048" height="1365" alt="Wind-shaped snow and exposed rock in a high mountain landscape." fetchpriority="high">
        </picture>
        <div class="shell hero-type"><h1 id="home-title">Work that<br> begins in<br> the <em>field.</em></h1></div>
      </section>
      <div class="shell home-copy">
        <div class="home-intro">
        <p>The Field Witness Society is an independent international society for geography, exploration and documentary practice. We publish photographs and writing that bring places into closer view.</p>
        {link('/field-notes/', 'Explore the Field Notes')}
        </div>
      <figure class="home-photo">
        <img src="/assets/field-note-001/figure-06-1600.webp" srcset="/assets/field-note-001/figure-06-960.webp 960w, /assets/field-note-001/figure-06-1600.webp 1600w, /assets/field-note-001/figure-06.jpg 2048w" sizes="(max-width:640px) calc(100vw - 40px), (min-width:1700px) 1540px, 92vw" width="2048" height="1365" alt="The Ben Amera monolith rising above sand and sparse vegetation in Mauritania." fetchpriority="high">
        <figcaption><span>Ben Amera, Mauritania</span><a href="{ARTICLE}">From Field Note 001</a></figcaption>
      </figure>
      </div>
      <div class="shell landscape-sequence" aria-label="Photographs from the field">
        <figure class="sequence-wide"><img src="/assets/photography/geothermal-landscape-1600.webp" srcset="/assets/photography/geothermal-landscape-960.webp 960w, /assets/photography/geothermal-landscape-1600.webp 1600w" sizes="(max-width: 640px) calc(100vw - 40px), 58vw" width="2048" height="1365" alt="Steam rising from a rocky geothermal landscape." loading="lazy" decoding="async"></figure>
        <figure class="sequence-tall"><img src="/assets/photography/volcanic-lava-960.webp" srcset="/assets/photography/volcanic-lava-640.webp 640w, /assets/photography/volcanic-lava-960.webp 960w" sizes="(max-width: 640px) 65vw, 28vw" width="1365" height="2048" alt="Bright orange lava thrown above dark volcanic rock." loading="lazy" decoding="async"></figure>
      </div>
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
    </article>
    <div class="archive-images" aria-label="Photographs from The iron ore railway">
      <figure><a href="{ARTICLE}" aria-label="Read the Field Note with the SNIM locomotive photograph"><img src="/assets/field-note-001/figure-04-1600.webp" srcset="/assets/field-note-001/figure-04-960.webp 960w, /assets/field-note-001/figure-04-1600.webp 1600w" sizes="(max-width: 640px) calc(100vw - 40px), 57vw" width="2048" height="1365" alt="The blue and cream SNIM locomotive BB 205 beside ore wagons." loading="lazy" decoding="async"></a></figure>
      <figure><a href="{ARTICLE}" aria-label="Read the Field Note from an open ore wagon"><img src="/assets/field-note-001/figure-10-960.webp" srcset="/assets/field-note-001/figure-10-960.webp 960w, /assets/field-note-001/figure-10-1365.webp 1365w" sizes="(max-width: 640px) 64vw, 28vw" width="1365" height="2048" alt="A view along loaded iron-ore wagons during the railway journey." loading="lazy" decoding="async"></a></figure>
    </div></main>'''


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
