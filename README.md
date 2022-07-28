# Journal Feed Generator
## Motivation
The number of journal articles increases immensely in any given year, particularly when accounting for papers in pre-print servers such as arXiv. Perhaps as a result, many look to social media (med-Twitter, etc.) to filter articles for relevance and importance. While any type of curation introduces bias, a reasonable alternative to social media, particularly for those not involved with the medium, would be journal-based article curation. PubMed is a poor alternative to this, as articles therein are restricted to medical or medically-adjacent articles, which poses a challenge for research who increasingly operate at the intersection of multiple fields.

RSS feeds are, unfortunately, becoming obsolete, with at least one journal (https://www.ajronline.org) abandoning them. Due to dynamically-generated HTML (Brain journal, for example), it is difficult to use pre-existing RSS-feed-generators, which rely on static HTML.

Therefore, the proposal is to:
- utilize headless browser automation to scrape articles from our favorite journals
- return the articles titles in a simple, well-curated format

Future directions:
- Allow users to create accounts
- Allow people with accounts to create their own download-able scripts so that they can be run locally (no need to host)
- Build up native library of journals supported by the app
