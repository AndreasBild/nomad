<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="2.0" xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/1999/xhtml">
    <xsl:output omit-xml-declaration="no" method="xml" version="1.0" encoding="UTF-8" indent="yes"
                doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN"
                doctype-system="https://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"/>
    <xsl:template match="/">
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <title>XML Sitemap for Domain www.moderatorin-katrin-neumann.de</title>
                <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
                <style>
                    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; padding: 2rem; color: #333; max-width: 960px; margin: 0 auto; }
                    h1 { font-size: 1.75rem; color: #170c0c; }
                    table { width: 100%; border-collapse: collapse; margin-top: 1.5rem; }
                    th, td { text-align: left; padding: 0.75rem; border-bottom: 1px solid #eee; font-size: 0.95rem; }
                    th { background-color: #f8f9fa; font-weight: 600; }
                    tr.odd { background-color: #fcfcfc; }
                    a { color: #0d6efd; text-decoration: none; }
                    a:hover { text-decoration: underline; }
                    .footer { margin-top: 2rem; font-size: 0.85rem; color: #888; }
                </style>
            </head>
            <body>
                <h1>XML Sitemap für www.moderatorin-katrin-neumann.de</h1>
                <div>
                    <p>Diese Sitemap enthält <xsl:value-of select="count(sitemap:urlset/sitemap:url)"/> URLs.</p>
                </div>
                <div>
                    <table>
                        <thead>
                            <tr>
                                <th>URL</th>
                                <th>Priorität</th>
                                <th>Änderungsintervall</th>
                                <th>Zuletzt geändert</th>
                            </tr>
                        </thead>
                        <tbody>
                            <xsl:for-each select="sitemap:urlset/sitemap:url">
                                <tr>
                                    <xsl:if test="position() mod 2 != 0">
                                        <xsl:attribute name="class">odd</xsl:attribute>
                                    </xsl:if>
                                    <td>
                                        <xsl:variable name="itemURL">
                                            <xsl:value-of select="sitemap:loc"/>
                                        </xsl:variable>
                                        <a href="{$itemURL}" target="_blank">
                                            <xsl:value-of select="sitemap:loc"/>
                                        </a>
                                    </td>
                                    <td>
                                        <xsl:value-of select="concat(sitemap:priority*100,'%')"/>
                                    </td>
                                    <td>
                                        <xsl:value-of select="sitemap:changefreq"/>
                                    </td>
                                    <td>
                                        <xsl:value-of select="sitemap:lastmod"/>
                                    </td>
                                </tr>
                            </xsl:for-each>
                        </tbody>
                    </table>
                </div>
                <div class="footer">© Katrin Neumann</div>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
