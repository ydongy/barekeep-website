<!-- template: website/design.md v1 -->
# Website design

A private archive in the app's own colors: soft paper, serif display type, monospace for paths and catalogue
labels, and the app's blue as the one accent. `public/style.css` is the single stylesheet; this page describes it.
System fonts only and no external resources, because the Content-Security-Policy allows none
([0004](adr/0004-csp-in-headers-file.md)).

## Palette

Tokens are CSS custom properties on `:root`; dark values apply under `prefers-color-scheme: dark`.

| Token | Light | Dark | Use |
|---|---|---|---|
| `--paper` | `#fbfaf7` | `#0e1220` | page background (also the `theme-color`) |
| `--surface` | `#fff` | `#171c2e` | cards, menus, message boxes |
| `--ink` | `#121626` | `#eef1fa` | text, strong rules, button fill |
| `--ink-2` | `#4a4f63` | `#b4bacd` | secondary text |
| `--ink-3` | `#686d80` | `#8c92a8` | tertiary text, meta lines |
| `--rule` | 14% ink | 15% ink | hairlines and borders |
| `--wash` | 5% ink | 6% ink | code background, hover |
| `--accent` | `#0a6cdb` | `#4da3ff` | links on hover, kickers, catalogue numbers, focus ring |

The lamp colors keep the app's meaning, and the lamp shape carries the state without color: `--lamp-on` green
(`#1f9d4a` / `#34c759`, filled disc), `--lamp-busy` blue (spinning arc), `--lamp-warn` orange (half-filled ring),
`--lamp-error` red (ring with a cross), `--lamp-off` grey (empty ring). The hero glow is three soft gradients
(`--glow-a`, `--glow-b`, `--glow-c`) taken from the app's wallpaper, masked to fade out. With
`prefers-contrast: more` the secondary inks and rules darken (light) or brighten (dark).

## Typography

- Display (`--serif`): Iowan Old Style, Palatino, New York, then the system serif; for Chinese the system song
  typeface. Used for `h1`, `h2`, the brand, card titles and ledger headings. English headings tighten letter
  spacing by 1.5%.
- Body (`--font`): the system UI font (SF Pro, PingFang for Chinese). 17px on a 1.65 line height.
- Mono (`--mono`): SF Mono or Menlo; paths, navigation, kickers, catalogue labels (`No. 01`), the card's rows and
  checksums, usually 11 to 14px with letter spacing.
- Sizes: home `h1` 40 to 72px (Chinese, Japanese and Korean 34 to 54px), home `h2` 30 to 44px, inner-page `h1`
  34 to 48px and `h2` 24px, leads 19 to 21px.

## Components

- **Header**: brand (icon and serif name) on the left; mono navigation (Download, Pricing, FAQ) and the language
  menu on the right. Pricing is hidden below 900px.
- **Language menu**: a `details` disclosure listing the nine languages; the current one is blue and bold. The
  footer repeats the languages as plain links. Choosing one is remembered by `lang.js`.
- **Footer**: brand and tagline, four columns (Product, Support, Legal, Contact), the copyright line and the
  official-downloads notice, then the language links.
- **Button**: a pill filled with ink; on hover it turns accent blue. `secondary` is outlined, `disabled` is dimmed.
- **Catalogue card**: a mirror drawn as a library index card in CSS only: frosted surface (backdrop blur),
  mono header with the synced stamp, serif title, dashed rows of label and value.
- **Ledger**: ruled rows with a serif heading on the left and a description on the right; numbered steps use a
  circled counter; lamp rows put the lamp before the heading.
- **Route and message**: the stop slip for the diverged case: source, this Mac and backup as ruled rows, with the
  held step in orange, and a message box with an orange left rule.
- **Platforms**: a serif line of names separated by blue slashes.
- **Download and pricing**: two columns under the home sections; the download box shows status, the button, the
  SHA-256 and the install hint, filled in by `download.js` from the release feed. Without script it shows a note.
- **FAQ**: plain `details` disclosures with a `+` / minus marker.
- **Legal pages**: title, a "Last updated" lead line, the translation notice (small, non-English only), an
  optional lead paragraph, numbered serif sections each opened by a heavy rule, and a contact line under a
  hairline.
- **Changelog**: one block per release: version, title and date on a line, an optional summary, a list.
- **Motion**: the synced lamp breathes once on the hero and the busy lamp spins four times; both stop under
  `prefers-reduced-motion`.

## Layout

- Content width 1120px (`.wrap`) with 24px side margins; text pages 720px (`.narrow`).
- Home: hero in a 7:5 grid, sections with 112px top padding and a catalogue number counter above each `h2`, the
  ledger as a 4:8 grid, the diverged-case section as 5:7, download and pricing in two equal columns.
- Breakpoint 900px: grids become one column, section padding shrinks to 80px, the footer stacks, the glow moves
  below the heading. Breakpoint 480px: the route rows tighten.
- Headers are 64px high with a hairline; the footer sits 120px (88px on small screens) below the content.
