# Gallery — Generated Manhwa Panels

Drop finished panel images into `gallery/panels/arc-01/` using the panel ID as the filename:

```
gallery/panels/arc-01/
  1.1.png
  1.2.png
  10.10.png
```

After adding images, rebuild the Arc 1 reader:

```bash
python scripts/build_arc01_reader.py
```

The reader auto-links any matching `.png`, `.jpg`, or `.webp` when chapter pages are regenerated.
