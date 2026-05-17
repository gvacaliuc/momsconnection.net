# momsconnection.net

This is the source for the website https://momsconnection.net.

## building

This website is built w/ hugo.

The code requires Hugo `0.153.1`.

```shell
# runs live-reloading server at :1313
hugo serve
```

## image optimization

We store raw design assets in `design/v2`. Before adding new images to the site,
optimize them using ImageMagick.

```shell
brew install imagemagick
```

Run the optimizer:

```shell
bash scripts/optimize-images.sh
```

This writes optimized copies to `design/v2/optimized` without modifying originals.
