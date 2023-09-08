PySeoHtml Documentation
=======================

Description
-----------

PySeoHtml is a Python library designed to intelligently link specific
keywords within HTML text content. It enhances SEO (Search Engine
Optimization) strategies by optimizing content with linked keywords,
maintaining readability, and preventing over-optimization.

Table of Contents
-----------------

1. `Installation <#installation>`__
2. `How It Works <#how-it-works>`__

   -  `Initialization <#initialization>`__
   -  `Text Processing <#text-processing>`__
   -  `Randomization (Optional) <#randomization-optional>`__
   -  `Benefits for SEO <#benefits-for-seo>`__

3. `Usage <#usage>`__

   -  `Example <#example>`__
   -  `Parameters <#parameters>`__
   -  `Result <#result>`__

Installation
------------

To install PySeoHtml, you can use pip:

.. code:: bash

   pip install py-seo-html

Text Processing
~~~~~~~~~~~~~~~

The library processes the HTML text and replaces keywords with links.
This process includes tokenization, keyword matching, link insertion,
HTML escaping, punctuation handling, and link limitation.

Randomization (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~

You can choose to place links randomly (if ``random_links`` is set to
True), which can help avoid over-optimization penalties from search
engines.

Initialization
~~~~~~~~~~~~~~

To get started, create an instance of the PySeoHtml class by providing
the following parameters:

+-------+-----------------------------------------------------+--------+
| Para  | Description                                         | D      |
| meter |                                                     | efault |
|       |                                                     | Value  |
+=======+=====================================================+========+
| ``h   | The HTML text content you want to process.          | -      |
| tml_t |                                                     | (req   |
| ext`` |                                                     | uired) |
+-------+-----------------------------------------------------+--------+
| ``    | A list of keyword-link pairs where each item is a   | -      |
| keywo | list with the keyword and its associated link.      | (req   |
| rds`` |                                                     | uired) |
+-------+-----------------------------------------------------+--------+
| `     | The maximum allowed length (in characters) for      | 500    |
| `dens | linked text snippets.                               |        |
| ity`` |                                                     |        |
+-------+-----------------------------------------------------+--------+
| `     | If set to True, the library will randomly choose    | False  |
| `rand | keywords to link each time. If False, it will       |        |
| om_li | consistently link the same keywords.                |        |
| nks`` |                                                     |        |
+-------+-----------------------------------------------------+--------+
| ``    | If set to True, keywords are stemmed before         | True   |
| stemm | processing.                                         |        |
| ing`` |                                                     |        |
+-------+-----------------------------------------------------+--------+
| ``    | The language to use for stemming. Supported         | “en    |
| langu | languages include “arabic,” “danish,” “dutch,”      | glish” |
| age`` | “english,” “finnish,” “french,” “german,”           |        |
|       | “hungarian,” “italian,” “norwegian,” “porter,”      |        |
|       | “portuguese,” “romanian,” “russian,” “spanish,” and |        |
|       | “swedish.”                                          |        |
+-------+-----------------------------------------------------+--------+
| ``va  | A list of HTML tags that are considered valid for   | [“p”,  |
| lid_t | keyword linking.                                    | “h1”,  |
| ags`` |                                                     | “h2”,  |
|       |                                                     | “h3”,  |
|       |                                                     | “h4”,  |
|       |                                                     | “h5”,  |
|       |                                                     | “h6”]  |
+-------+-----------------------------------------------------+--------+

.. _randomization-optional-1:

Randomization (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~

You can choose to place links randomly (if random_links is set to True),
which can help avoid over-optimization penalties from search engines.

Benefits for SEO
~~~~~~~~~~~~~~~~

PySeoHtml offers several benefits for SEO:

-  **Keyword Linking:** It automatically identifies and links keywords
   to relevant URLs within your HTML content, improving search engine
   understanding and rankings.
-  **Content Optimization:** By strategically linking keywords, you can
   enhance the SEO value of your content and increase its visibility in
   search results.
-  **Prevents Over-Optimization:** The library limits the number of
   linked keywords to maintain a natural keyword density, helping you
   avoid SEO penalties.
-  **Maintains Readability:** Linked keywords are embedded within
   readable text snippets, improving the user experience and preventing
   content from appearing spammy.

Usage
-----

Here’s an example of how to use the PySeoHtml library:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

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
       ["Search Engine", "https://example.com/seo"],
       ["Research", "https://example.com/keyword-research"],
       ["SEO", "https://example.com/on-page-seo"],
       ["Building", "https://example.com/link-building"],
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

Result
------

The processed_html variable will contain the HTML content with keywords
replaced by links. This processed content can be used to enhance SEO
strategies.

.. code:: html

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

Thank you!
----------

Please feel free to reach out if you have any further questions or need
additional assistance!
