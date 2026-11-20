"""Gemeinsame Teile der Ratgeber-Artikel."""
from gemeinsam import ORG, BASE
AUTOR_ZEILE = ('<br><br><span style="font-weight: 700;">Von <a href="https://arbeitgebermagazin.de/provision-infra-gruender-im-interview-zutrittskontrolle-ist-keine-hausmeisterarbeit" '
               'target="_blank" rel="noopener" style="color: #FBC91B;">Jannes Heino Baumann</a>, Gründer und Geschäftsführer von ProVision Infra. Stand: November 2026</span>')
AUTOR = {"@type": "Person", "@id": BASE + "/#gruender", "name": "Jannes Heino Baumann", "jobTitle": "Gründer und Geschäftsführer",
         "worksFor": {"@id": BASE + "/#organization"},
         "sameAs": ["https://arbeitgebermagazin.de/provision-infra-gruender-im-interview-zutrittskontrolle-ist-keine-hausmeisterarbeit"]}
REMOVE = ['a3564b7', '7dfd9f6', 'aed8a2d', 'f9348eb', 'a3437e1']
from gemeinsam import ORDER, GRUENDER, PRESSE, video_kasten, cta, stell_dir_vor
def artikel_schema(url, headline, beschreibung, datum='2026-11-20'):
    return {"@context": "https://schema.org", "@graph": [ORG, AUTOR, {
        "@type": "Article", "@id": url + "#artikel", "headline": headline, "description": beschreibung,
        "mainEntityOfPage": url, "datePublished": datum, "dateModified": datum, "inLanguage": "de-DE",
        "author": {"@id": BASE + "/#gruender"}, "publisher": {"@id": BASE + "/#organization"},
        "image": BASE + "/wp-content/uploads/2026/11/header-foto-1305-q92.webp"}]}
def p(t): return '<p>' + t + '</p>'
def kurz(t): return '<p>Kurz gesagt: ' + t + '</p>'
