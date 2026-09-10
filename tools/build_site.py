"""Render the existing static GitHub Pages site. No runtime dependencies."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://fieldwitnesssociety.com'
ARTICLE = '/field-notes/the-iron-ore-railway/'
PDF = '/downloads/The_Field_Witness_Society_Field_Note_001_Mauritania.pdf'
DESCRIPTOR = 'An International Society for Geography, Exploration and Documentary Practice.'


def brand():
    return '<a class="brand-lockup" href="/" aria-label="The Field Witness Society home"><img class="brand-symbol" src="/assets/brand/crater-section.svg" width="42" height="42" alt=""><span class="brand-name">The Field Witness Society</span></a>'


def header(current=''):
    links = [('/#field-notes', 'Field Notes', 'notes'), ('/about/', 'About', 'about'), ('/about/#contact', 'Contact', 'contact')]
    nav = ''.join(f'<a href="{url}"'+(' aria-current="page"' if key == current else '')+f'>{label}</a>' for url,label,key in links)
    return f'<a class="skip-link" href="#main">Skip to content</a><header class="site-header"><div class="shell masthead">{brand()}<nav class="main-nav" aria-label="Main navigation">{nav}</nav></div></header>'


def footer():
    return f'''<footer class="site-footer"><div class="shell"><div class="footer-top">{brand()}
    <nav class="footer-links" aria-label="Footer navigation"><a href="/#field-notes">Field Notes</a><a href="/about/">About</a><a href="/about/#contact">Contact</a></nav></div>
    <div class="footer-bottom"><p>Geography · Exploration · Documentary Practice</p><p>Turin, Italy · © 2026 The Field Witness Society</p></div></div></footer>'''


def link(url, label):
    return f'<a class="text-link" href="{url}">{label}<span class="arrow" aria-hidden="true">→</span></a>'


def document(title, description, route, body, current='', noindex=False, author=None):
    meta = '<meta name="robots" content="noindex">' if noindex else ''
    if author:
        meta += f'<meta name="author" content="{escape(author)}">'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title><meta name="description" content="{escape(description)}">{meta}
<link rel="canonical" href="{ORIGIN}{route}"><meta name="theme-color" content="#f2ebdd">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" href="/assets/brand/crater-section.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/site.css"><link rel="preload" href="/assets/fonts/eb-garamond.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/univers-67.woff2" as="font" type="font/woff2" crossorigin>
</head><body>{header(current)}{body}{footer()}</body></html>'''


def home():
    return f'''<main id="main" class="shell">
    <p class="site-descriptor">{DESCRIPTOR}</p>
    <section id="field-notes" class="feature" aria-labelledby="feature-title">
      <div class="feature-copy"><p class="eyebrow">Field Note 001 · Mauritania</p>
      <h1 id="feature-title">The iron ore railway</h1>
      <p class="feature-deck">A westbound passage from Choum to Nouadhibou.</p>
      <p class="feature-meta"><span>Tommaso Bruno</span><span>9–10 October 2025</span></p>
      {link(ARTICLE, 'Read the Field Note')}</div>
      <figure class="feature-photo"><a href="{ARTICLE}" aria-label="Read The iron ore railway">
      <img src="/assets/field-note-001/figure-01-1600.webp" srcset="/assets/field-note-001/figure-01-960.webp 960w, /assets/field-note-001/figure-01-1600.webp 1600w, /assets/field-note-001/figure-01.jpg 2048w" sizes="(max-width:760px) calc(100vw - 48px), 58vw" width="2048" height="1365" alt="Iron-ore wagons extending across the desert in northern Mauritania." fetchpriority="high"></a>
      <figcaption><span>Northern Mauritania</span><span>Photography and field notes</span></figcaption></figure>
    </section>
    <section id="about" class="home-about" aria-labelledby="society-title">
      <p class="eyebrow">The Society</p><div><h2 id="society-title">Geography, exploration and documentary practice.</h2>
      <p class="body">The Field Witness Society publishes photography and writing from the field. Each record brings together direct observation, geographical context and the perspective of its author.</p>
      <span id="principles"></span><span id="practice"></span>{link('/about/', 'About the Society')}</div>
    </section></main>'''


def build():
    (ROOT/'index.html').write_text(document('The Field Witness Society',DESCRIPTOR,'/',home(),'notes'),encoding='utf-8')
    about = (ROOT/'content/about.html').read_text(encoding='utf-8')
    (ROOT/'about').mkdir(exist_ok=True)
    (ROOT/'about/index.html').write_text(document('About · The Field Witness Society','The purpose, field practice and principles of The Field Witness Society. Founded in Turin in 2026.','/about/',about,'about'),encoding='utf-8')
    article = (ROOT/'content/field-note-001.html').read_text(encoding='utf-8')
    (ROOT/'field-notes/the-iron-ore-railway/index.html').write_text(document('The iron ore railway · Field Note 001 · The Field Witness Society','A westbound passage from Choum to Nouadhibou, Mauritania. Photography and field notes by Tommaso Bruno, 9–10 October 2025.',ARTICLE,article,author='Tommaso Bruno'),encoding='utf-8')
    error = f'<main id="main" class="shell error-page"><p class="eyebrow">Page not found</p><h1>This page is unavailable.</h1><p>You can return to the Society or read our latest Field Note.</p>{link("/", "Return to the homepage")}</main>'
    (ROOT/'404.html').write_text(document('Page not found · The Field Witness Society','Return to the publications of The Field Witness Society.','/404.html',error,noindex=True),encoding='utf-8')
    (ROOT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nDisallow: /tools/\nDisallow: /content/\nSitemap: {ORIGIN}/sitemap.xml\n',encoding='utf-8')
    entries=''.join(f'<url><loc>{ORIGIN}{p}</loc></url>' for p in ['/', '/about/', ARTICLE])
    (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+entries+'</urlset>',encoding='utf-8')


if __name__ == '__main__':
    build()
