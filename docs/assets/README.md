# Hero assets

The landing page in `docs/index.md` is a three-layer parallax scene built
from the SVGs in this folder:

| File | Layer | Parallax speed | Role |
|---|---|---|---|
| `hero-stars.svg` | back   | 0.15× | Deep-space backdrop with nebula gradients and starfield |
| `hero-alien.svg` | middle | 0.45× | Silhouette of an alien wearing headphones, viewed from behind |
| `hero-ui.svg`    | front  | 0.75× | Stylised AetherSDR panadapter+waterfall the alien is "looking at" |

The current SVGs are **placeholders** — clean and on-brand, but flat illustrations.
Replace any of them with a higher-fidelity rendered image to lift the page.

## Replacing the alien

The intended scene is: **an alien wearing studio headphones, seen from behind,
looking at a glowing AetherSDR panadapter.** To generate a polished version with
Midjourney, DALL·E 3, or Stable Diffusion, use this prompt as a starting point:

> Cinematic back-view portrait of a slender grey alien sitting at a desk,
> wearing oversized cyan-glowing studio headphones, illuminated only by the
> blue-violet glow of a curved monitor showing a software-defined radio
> waterfall display, dark room, subtle volumetric light, ultra-detailed,
> moody color grading in deep purple and cyan, 4k, painterly digital art,
> centred composition with negative space above the head for typography,
> the alien fills the lower-third silhouette.

### Guidelines for the swap

- **Format:** SVG is preferred for sharpness at any size, but a transparent
  PNG (≥ 1600px wide) works fine — the CSS uses `background-size: contain`.
- **Background:** transparent. The hero gradient lives on the parent
  `.aether-hero` element; bake-in backgrounds will fight it.
- **Composition:** the alien should fill the lower 80% of the image and
  be horizontally centred. Leave the top 20% empty for the title/subtitle
  to breathe over.
- **Filename:** keep `hero-alien.svg` (or change the extension and update
  `docs/stylesheets/extra.css` to point at the new file).

## Replacing the UI panel

The middle UI layer is meant to suggest the AetherSDR spectrum/waterfall the
alien is looking at. A real screenshot works well too:

1. Take a screenshot of AetherSDR running with a clean panadapter view.
2. Crop tightly around the spectrum + waterfall area.
3. Save as `hero-ui.png` (transparent background or matched-dark background).
4. Update the `background-image` URL in `docs/stylesheets/extra.css` if you
   change the extension.

## Replacing the starfield

Less critical — the SVG starfield is procedurally clean. Replace if you want
a real astrophotography background. Same dimensions and transparent-ish
treatment recommended.
