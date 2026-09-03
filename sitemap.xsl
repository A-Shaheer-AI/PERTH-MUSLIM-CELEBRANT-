<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" 
                xmlns:html="http://www.w3.org/TR/REC-html40"
                xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"
                xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/">
    <html xmlns="http://www.w3.org/1999/xhtml">
      <head>
        <title>XML Sitemap - Sheikh Hisham Gad</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <style type="text/css">
          body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            font-size: 14px;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
          }
          h1 {
            color: #044a3a;
            font-size: 24px;
            margin-bottom: 10px;
          }
          p.description {
            background-color: #f0fdf4;
            padding: 15px;
            border-left: 4px solid #065f46;
            margin-bottom: 30px;
            border-radius: 4px;
            line-height: 1.5;
          }
          table {
            border: none;
            border-collapse: collapse;
            width: 100%;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
          }
          th {
            background-color: #044a3a;
            color: white;
            text-align: left;
            padding: 12px 15px;
            font-size: 13px;
          }
          td {
            padding: 12px 15px;
            border-bottom: 1px solid #eee;
          }
          tr:nth-child(even) {
            background-color: #fafafa;
          }
          tr:hover {
            background-color: #f5f5f5;
          }
          a {
            color: #065f46;
            text-decoration: none;
          }
          a:hover {
            text-decoration: underline;
          }
        </style>
      </head>
      <body>
        <h1>XML Sitemap for IslamicMarriageWA.com.au</h1>
        <p class="description">
          <strong>This is an XML Sitemap, meant for consumption by search engines like Google and Bing.</strong><br/>
          It provides a map of all the important pages and sections on Sheikh Hisham Gad's website to ensure search engines crawl and index all of your services perfectly.
        </p>
        <table>
          <thead>
            <tr>
              <th>Page URL</th>
              <th>Priority</th>
              <th>Update Frequency</th>
              <th>Last Modified</th>
            </tr>
          </thead>
          <tbody>
            <xsl:for-each select="sitemap:urlset/sitemap:url">
              <tr>
                <td>
                  <a href="{sitemap:loc}"><xsl:value-of select="sitemap:loc"/></a>
                </td>
                <td><xsl:value-of select="sitemap:priority"/></td>
                <td><xsl:value-of select="sitemap:changefreq"/></td>
                <td><xsl:value-of select="sitemap:lastmod"/></td>
              </tr>
            </xsl:for-each>
          </tbody>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
