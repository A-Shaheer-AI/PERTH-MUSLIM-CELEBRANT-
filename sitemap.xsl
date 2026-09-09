<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" 
                xmlns:html="http://www.w3.org/TR/REC-html40"
                xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"
                xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/">
    <html xmlns="http://www.w3.org/1999/xhtml" lang="en">
      <head>
        <title>XML Sitemap | Sheikh Hisham Gad - Perth Muslim Marriage Celebrant</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <style type="text/css">
          * { box-sizing: border-box; }
          body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            font-size: 14px;
            color: #1e293b;
            background-color: #f8fafc;
            max-width: 960px;
            margin: 0 auto;
            padding: 40px 20px;
            line-height: 1.6;
          }
          .header {
            background: linear-gradient(135deg, #022c22 0%, #044a3a 100%);
            color: white;
            padding: 30px;
            border-radius: 16px;
            margin-bottom: 24px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
          }
          h1 {
            margin: 0 0 8px 0;
            font-size: 24px;
            color: #fde68a;
          }
          .subtitle {
            margin: 0;
            color: #d1fae5;
            font-size: 14px;
          }
          .notice {
            background-color: #ffffff;
            padding: 20px;
            border-left: 4px solid #044a3a;
            margin-bottom: 24px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
          }
          .card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            margin-bottom: 24px;
          }
          h2 {
            font-size: 18px;
            color: #044a3a;
            margin-top: 0;
            margin-bottom: 16px;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 8px;
          }
          table {
            border-collapse: collapse;
            width: 100%;
          }
          th {
            background-color: #f1f5f9;
            color: #475569;
            text-align: left;
            padding: 12px;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.05em;
          }
          td {
            padding: 12px;
            border-bottom: 1px solid #e2e8f0;
          }
          tr:hover {
            background-color: #f8fafc;
          }
          a {
            color: #044a3a;
            font-weight: 600;
            text-decoration: none;
          }
          a:hover {
            text-decoration: underline;
          }
          .badge {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 700;
            background-color: #ecfdf5;
            color: #065f46;
          }
          .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 16px;
            margin-top: 12px;
          }
          .service-item {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 16px;
          }
          .service-title {
            font-weight: 700;
            color: #044a3a;
            margin-bottom: 4px;
          }
          .service-desc {
            font-size: 12px;
            color: #64748b;
          }
        </style>
      </head>
      <body>
        <div class="header">
          <h1>Sheikh Hisham Gad | XML Sitemap</h1>
          <p class="subtitle">Authorized Civil and Islamic Marriage Celebrant in Perth, Western Australia</p>
        </div>

        <div class="notice">
          <p style="margin:0;">
            <strong>Search Engine Crawler Information:</strong><br/>
            This is an XML Sitemap generated in compliance with the standard sitemaps.org protocol for search engines like Google and Bing.
          </p>
        </div>

        <div class="card">
          <h2>Indexable Canonical URL</h2>
          <table>
            <thead>
              <tr>
                <th>Page URL</th>
                <th>Priority</th>
                <th>Change Frequency</th>
                <th>Last Modified</th>
              </tr>
            </thead>
            <tbody>
              <xsl:for-each select="sitemap:urlset/sitemap:url">
                <tr>
                  <td>
                    <a href="{sitemap:loc}"><xsl:value-of select="sitemap:loc"/></a>
                  </td>
                  <td><span class="badge"><xsl:value-of select="sitemap:priority"/></span></td>
                  <td><xsl:value-of select="sitemap:changefreq"/></td>
                  <td><xsl:value-of select="sitemap:lastmod"/></td>
                </tr>
              </xsl:for-each>
            </tbody>
          </table>
        </div>

        <div class="card">
          <h2>Website Services &amp; Navigation Directory</h2>
          <p style="color:#64748b; font-size:13px; margin-bottom:16px;">
            Sheikh Hisham Gad provides comprehensive marriage, visa, legal, and community services across Perth and Western Australia:
          </p>
          <div class="services-grid">
            <div class="service-item">
              <div class="service-title"><a href="https://www.islamicmarriagewa.com.au/#/counselling">Islamic Marriage Counselling &amp; Sulh</a></div>
              <div class="service-desc">Faith-based pre-marital guidance, relationship harmony, and confidential marital dispute mediation.</div>
            </div>
            <div class="service-item">
              <div class="service-title"><a href="https://www.islamicmarriagewa.com.au/#/services">Civil &amp; Islamic Dual Ceremony</a></div>
              <div class="service-desc">Complete ceremony combining Australian civil marriage registration and Islamic Nikah contract.</div>
            </div>
            <div class="service-item">
              <div class="service-title"><a href="https://www.islamicmarriagewa.com.au/#/services">Islamic Nikah Only</a></div>
              <div class="service-desc">Traditional religious marriage ceremony in accordance with Shariah guidelines and Islamic certificates.</div>
            </div>
            <div class="service-item">
              <div class="service-title"><a href="https://www.islamicmarriagewa.com.au/#/services">Civil Registration Only</a></div>
              <div class="service-desc">Legal registration of marriage under Australian Marriage Act 1961 for couples already Nikah-married.</div>
            </div>
            <div class="service-item">
              <div class="service-title"><a href="https://www.islamicmarriagewa.com.au/#/visas">Prospective Spouse Visas (Subclass 300)</a></div>
              <div class="service-desc">Official Notice of Intended Marriage (NOIM) registration and celebrant letters for Home Affairs and visas.</div>
            </div>
            <div class="service-item">
              <div class="service-title"><a href="https://www.islamicmarriagewa.com.au/#/overseas">Overseas &amp; Destination Couples</a></div>
              <div class="service-desc">Remote marriage coordination and legal paperwork assistance for couples visiting Perth from abroad.</div>
            </div>
            <div class="service-item">
              <div class="service-title"><a href="https://www.islamicmarriagewa.com.au/#/wills">Islamic Wills (Wasiyyah)</a></div>
              <div class="service-desc">Preparation of legally binding Shariah-compliant Wills recognized under Australian probate laws.</div>
            </div>
            <div class="service-item">
              <div class="service-title"><a href="https://www.islamicmarriagewa.com.au/#/education">Quran, Tajweed &amp; Counselling</a></div>
              <div class="service-desc">Pre-marital guidance, marital dispute arbitration, and weekly Quran and Tajweed classes in Perth.</div>
            </div>
            <div class="service-item">
              <div class="service-title"><a href="https://www.islamicmarriagewa.com.au/#/contact">Consultation &amp; Inquiries</a></div>
              <div class="service-desc">Direct contact via phone, email, and meeting booking with Sheikh Hisham Gad in Rivervale, WA.</div>
            </div>
          </div>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
