"""Gemeinsame Bausteine aller neuen Seiten (Kontaktblock, Organisation im Schema, Wortlisten)."""
BASE = 'https://provision-infra.de'
NAP = ('<p><strong>ProVision Infra GmbH</strong><br>Klein Hesebecker Straße 11, 29549 Bad Bevensen<br>'
       'Telefon: <a href="tel:+4958214049040">05821 4049040</a><br>'
       'E-Mail: <a href="mailto:info@provision-infra.de">info@provision-infra.de</a><br>Mo–Do 9–18 Uhr, Fr 9–14 Uhr</p>')
ORTE_NORD = ['Lüneburg', 'Uelzen', 'Bad Bevensen', 'Celle', 'Winsen (Luhe)', 'Dannenberg (Elbe)', 'Hitzacker (Elbe)', 'Bleckede',
             'Lüchow (Wendland)', 'Gifhorn', 'Wittingen', 'Ebstorf', 'Bienenbüttel', 'Wieren', 'Bad Bodenteich', 'Munster', 'Soltau',
             'Hamburg', 'Hannover']
ORG = {
    "@type": "LocalBusiness", "@id": BASE + "/#organization", "name": "ProVision Infra GmbH", "url": BASE + "/",
    "logo": BASE + "/wp-content/uploads/2026/10/kamera-logo-provision-infra-1032.png",
    "image": BASE + "/wp-content/uploads/2026/11/header-foto-1305-q92.webp",
    "telephone": "+49 5821 4049040", "email": "info@provision-infra.de", "priceRange": "$$",
    "address": {"@type": "PostalAddress", "streetAddress": "Klein Hesebecker Straße 11", "postalCode": "29549",
                "addressLocality": "Bad Bevensen", "addressRegion": "Niedersachsen", "addressCountry": "DE"},
    "geo": {"@type": "GeoCoordinates", "latitude": 53.0779485, "longitude": 10.5903962},
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"], "opens": "09:00", "closes": "18:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "09:00", "closes": "14:00"}],
    "areaServed": [{"@type": "City", "name": o} for o in ORTE_NORD] + [{"@type": "State", "name": "Niedersachsen"}],
    "sameAs": ["https://www.instagram.com/provision_infra_gmbh/", "https://www.facebook.com/share/1CWs2rohMt/",
               "https://www.linkedin.com/company/provision-infra-gmbh-i-g/"]}
# Wörter der Uelzen-Vorlage, die auf überregionalen Seiten nicht stehen bleiben dürfen
VERBOTEN = ['Uelzen', 'Uelzener', 'Veerßen', 'Oldenstadt', 'Holdenstedt', 'B4', 'Suderburg', 'Rosche', 'Himbergen', 'Altenmedingen']
