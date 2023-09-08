

# PySeoHtml Documentation

## Description

PySeoHtml is a Python library designed to intelligently link specific keywords within HTML text content. It enhances SEO (Search Engine Optimization) strategies by optimizing content with linked keywords, maintaining readability, and preventing over-optimization.

## Table of Contents

1. [Installation](#installation)
2. [How It Works](#how-it-works)
    - [Initialization](#initialization)
    - [Text Processing](#text-processing)
    - [Randomization (Optional)](#randomization-optional)
    - [Benefits for SEO](#benefits-for-seo)
3. [Usage](#usage)
    - [Example](#example)
    - [Parameters](#parameters)
    - [Result](#result)


## Installation

To install PySeoHtml, you can use pip:

```bash
pip install py-seo-html
```

### Text Processing

The library processes the HTML text and replaces keywords with links. This process includes tokenization, keyword matching, link insertion, HTML escaping, punctuation handling, and link limitation.

### Randomization (Optional)

You can choose to place links randomly (if `random_links` is set to True), which can help avoid over-optimization penalties from search engines.

### Initialization

To get started, create an instance of the PySeoHtml class by providing the following parameters:

| Parameter      | Description                                                                                         | Default Value   |
|----------------|-----------------------------------------------------------------------------------------------------|-----------------|
| `html_text`    | The HTML text content you want to process.                                                         | - (required)    |
| `keywords`     | A list of keyword-link pairs where each item is a list with the keyword and its associated link. | - (required)    |
| `density`      | The maximum allowed length (in characters) for linked text snippets.                                 | 500             |
| `random_links` | If set to True, the library will randomly choose keywords to link each time. If False, it will consistently link the same keywords. | False  |
| `stemming`     | If set to True, keywords are stemmed before processing.                                            | True            |
| `language`     | The language to use for stemming. Supported languages include "arabic," "danish," "dutch," "english," "finnish," "french," "german," "hungarian," "italian," "norwegian," "porter," "portuguese," "romanian," "russian," "spanish," and "swedish." | "english"  |
| `valid_tags`   | A list of HTML tags that are considered valid for keyword linking.                                   | ["p", "h1", "h2", "h3", "h4", "h5", "h6"] |


### Randomization (Optional)
You can choose to place links randomly (if random_links is set to True), which can help avoid over-optimization penalties from search engines.

### Benefits for SEO
PySeoHtml offers several benefits for SEO:

* **Keyword Linking:** It automatically identifies and links keywords to relevant URLs within your HTML content, improving search engine understanding and rankings.
* **Content Optimization:** By strategically linking keywords, you can enhance the SEO value of your content and increase its visibility in search results.
* **Prevents Over-Optimization:** The library limits the number of linked keywords to maintain a natural keyword density, helping you avoid SEO penalties.
* **Maintains Readability:** Linked keywords are embedded within readable text snippets, improving the user experience and preventing content from appearing spammy.

## Usage
### Here's an example of how to use the PySeoHtml library:

```python
from PySeoHtml import PySeoHtml

html_text = """
<h1>Enhance Your SEO with PySeoHtml</h1>
<p>PySeoHtml is a powerful Python library that can help boost your website's SEO performance. By intelligently linking specific keywords within your content, you can improve search engine rankings and increase organic traffic.</p>
<p>Here are some examples of keywords you can link:</p>
<ul>
    <li>Search Engine Optimization</li>
    <li>Keyword Research</li>
    <li>On-Page SEO</li>
    <li>Link Building</li>
</ul>
"""

keywords = [
    [["Search Engine"], "https://example.com/seo"],
    [["Research"], "https://example.com/keyword-research"],
    [["SEO"], "https://example.com/on-page-seo"],
    [["Building"], "https://example.com/link-building"],
    # Add more keyword-link pairs as needed
]

# Initialize PySeoHtml
seo_html = PySeoHtml(
    html_text=html_text,
    keywords=keywords,
    density=100,
    random_links=False,
    stemming=True,
    language="english",
    valid_tags=["li", "p", "h1", "h2", "h3", "h4", "h5", "h6"],
)

# Generate the processed HTML content
processed_html = seo_html.make()

print(processed_html)
```

## Result
The processed_html variable will contain the HTML content with keywords replaced by links. This processed content can be used to enhance SEO strategies.

```html
<h1>
 Enhance Your SEO with PySeoHtml
</h1>
<p>
 PySeoHtml is a powerful Python library that can help boost your website's SEO performance. By intelligently linking specific keywords within your content, you can improve
 <a href="https://example.com/seo">
  search engine rankings and increase organic traffic
 </a>
 .
</p>
<p>
 <a href="https://example.com/seo">
  Here are some examples
 </a>
 of keywords you can link:
</p>
<ul>
 <li>
  Search Engine Optimization
 </li>
 <li>
  Keyword Research
 </li>
 <li>
  <a href="https://example.com/on-page-seo">
   On-Page SEO
  </a>
 </li>
 <li>
  <a href="https://example.com/link-building">
   Link Building
  </a>
 </li>
</ul>
```

## Thank you!
Please feel free to reach out if you have any further questions or need additional assistance!
