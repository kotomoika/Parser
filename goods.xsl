<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
            <body>
                <h2>Furniture</h2>
                <table border="1">
                    <tr>
                        <th>Title</th>
                        <th>Image</th>
                        <th>Text</th>
                    </tr>
                <xsl:for-each select="goods/good">
                    <tr>
                        <td><xsl:value-of select="title"/></td>
                        <td>
                            <img width="100" height="100">
                                <xsl:attribute name="src">
                                    <xsl:value-of select="image"/>
                                </xsl:attribute>
                            </img>
                        </td>
                        <td><xsl:value-of select="text/p"/></td>
                    </tr>
                </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>


