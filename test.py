from PySeoHtml import PySeoHtml

# Initialize the PySeoHtml with your HTML text and keywords
html_text = """
<p>This is an example HTML text containing keywords like Python and SEO.</p>
<p>
    PySeoHtml is a versatile Python library created to empower SEO (Search Engine Optimization) strategies by strategically embedding hyperlinks into HTML text content. Its primary objective is to intelligently link designated keywords, thereby optimizing content for search engines while preserving readability and mitigating the risk of over-optimization. With a focus on enhancing online visibility, PySeoHtml allows users to define keywords and their respective target URLs, facilitating the process of integrating contextual links seamlessly.
    By carefully analyzing the input HTML text, PySeoHtml identifies instances of specified keywords and intelligently transforms them into hyperlinks. To ensure a balanced and natural appearance, the library considers both the left and right context of keywords. It extracts adjacent words, taking care to respect sentence boundaries and avoid disruptions to the text's coherence.
    PySeoHtml offers flexibility by allowing users to customize the link density, ensuring that the generated hyperlinks align with specific SEO objectives. This means you can control how often keywords are linked, preventing the text from becoming overly saturated with links, which can negatively impact user experience and SEO performance.
</p>
"""
keywords = {"python": "https://python.org", "seo": "https://seo-example.com"}
linker = PySeoHtml(html_text, keywords, density=500, random_links=False)

# Process the HTML text to add links to keywords
processed_html = linker.process_text()

# Use the processed_html in your web content
print(processed_html)
