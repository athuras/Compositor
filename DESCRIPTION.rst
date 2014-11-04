Compositor: Morphologically Optimal ASCII-Art
=============================================

Have you ever thought to yourself "Wouldn't it be nice if I had a command line utility to generating ASCII-art?"
I know I have.

Typical ASCII art generators choose a palette of characters of some size K, and reduce the grey-mapped color depth to about K-bits of fidelity, and then simply map each unique color in the image, to an equivalently "dark" character in the palette.

The advantages associated with this are fairly obvious: it's inexpensive, but this convenience comes with a terrible price: the ascii composite 'images' are of significantly reduced fidelity.

Enter Compositor:

At its heart, Compositor overlays true-type font-renderings of each character in your palette on top of each sub-image, and matches based on an arbitrary objective function.
By default, a simple accumulated error function. This enables characters to be based not only on their 'darkness' but also their morphology.

