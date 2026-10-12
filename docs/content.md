# Content

## Pages

| Page | File | Copy source |
|---|---|---|
| Home | `i18n/<code>.json` `home`; layout in `scripts/build.py` | Written here; names of menus and buttons are the app's own |
| FAQ | `i18n/<code>.json` `faq` | Written here; answers that restate product behaviour match the app's legal facts |
| Changelog | `changelog.json`, labels in `i18n/<code>.json` `changelog` | The app's `CHANGELOG.md`, entered by the app's release flow |
| Privacy Policy | `i18n/<code>.json` `privacy` | Written here only; checked against the app's legal facts |
| Terms of Service | `i18n/<code>.json` `terms` | The text of the app repository's `LICENSE`, translated section by section |
| Refund Policy | `i18n/<code>.json` `refund` | Written here only; derives from the refund paragraph of the app's legal facts |
| Not found | built by sitekit | `scripts/sitekit/core.py` |

The shared strings (navigation, footer, contact line, download button wording) are `nav`, `meta` and `download_js`
in the same files.

## Copy sources

- English is the reference for every page; the maintainer decides the wording, and AI collaborators translate
  from English.
- The Terms of Service have the same 14 sections, in the same order, as the app's `LICENSE`: License · Free plan
  and Pro · License key · Activation and verification · Your data and credentials · Restrictions · Updates ·
  Third-party components · Purchases and refunds · Intellectual property · Termination · Disclaimer · Limitation
  of liability · Changes. The English text matches the license text; the contact line is `nav.contact`, rendered
  under every legal page, so the terms have no Contact section. When the license text changes, the English terms
  change in the same change set and the other eight languages are re-translated from them.
- The Privacy Policy opens with `lead` and has these sections: What we collect · What we don't collect ·
  Third-party services · Data storage · Your rights and control · Changes. The Refund Policy has five: 14-day
  refund · How to ask · What happens to your license · Cancellation · Your legal rights.
- "Last updated" is a month and year and changes whenever the text of that page changes.
- The home page does not state a price until the payment provider's product exists; then the Pricing section gets
  the Free/Pro table with a visible price row and the buy button.

## Facts

Every number that appears in legal text, the FAQ or the home page is a fact with one source: the product's own legal facts list (maintained with the
product, not published), which names the code that implements it. This table is the website's copy of those facts: the value, and every place in `i18n/en.json` that
states it. `scripts/check_facts.py` reads this table and fails when a listed place states other numbers than the
table says, when a language differs from English at that place, or when a table number turns up at a place that is
not listed.

When a product fact changes, the product's legal facts and this table change together, in the same change set as the
copy; the check then points at every place still to translate.

| Fact | Value | Where stated |
|---|---|---|
| Minimum macOS version | 26.0 | `home.meta`, `home.status_default`, `faq.groups[0].items[1].a` |
| Mirrors in the free plan | 3 | `home.pricing_lead`, `faq.groups[0].items[2].a`, `faq.groups[0].items[5].a`, `terms.sections[1].body`, `refund.sections[2].body` |
| Macs one key can be active on | 2 | `faq.groups[0].items[3].a`, `terms.sections[2].body` |
| Refund window in days | 14 | `meta.refund_desc`, `faq.groups[0].items[4].a`, `refund.sections[0].h`, `refund.sections[0].body` |
| Offline grace for a Pro license, in days | 30 | `terms.sections[3].body` |
| Reply time for a data request, in days | 30 | `privacy.sections[4].body` |
| Business days a bank takes to show a refund | 3 to 5 | `refund.sections[1].body` |
| Version that needs no purchase | 1.0 | `home.meta` |

The check also verifies, without a table, that the terms, privacy and refund pages each have one name per language
(footer label, title and meta title), that every language except English carries the translation notice, that the
footer of every page links `/privacy`, `/terms`, `/refund` and `support@barekeep.com`, and that no `_redirects`
file or `eula` page exists.

## Languages and translation

English is the reference;
the terms, privacy, refund and FAQ pages carry a translation notice in every other language, Chinese included.
`check_i18n.py` requires every language file to have English's structure, tags, links and placeholders and no em or
en dashes. All nine files are formatted identically (2-space JSON, UTF-8, trailing newline).
