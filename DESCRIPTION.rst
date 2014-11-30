Compositor: Morphologically Optimal ASCII-Art
=============================================

Have you ever thought to yourself "Wouldn't it be nice if I had a command line utility to generating ASCII-art?"
I know I have.

Typical ASCII art generators choose a palette of characters of some size K, and reduce the grey-mapped color depth to about K-bits of fidelity, and then simply map each unique color in the image, to an equivalently "dark" character in the palette.

The advantages associated with this are fairly obvious: it's inexpensive, but this convenience comes with a terrible price: the ascii composite 'images' are of significantly reduced fidelity. This can be improved by simply increasing the effective resolution of the ascii-art image; however wouldn't it be nice if we could exploit the gamut of geometry that monospace-typographers have already built into our fonts?

Enter Compositor:

At its heart, Compositor overlays true-type font-renderings of each character from a "palette" on top of each sub-image, and matches based on an arbitrary objective function.
By default, we use a simple (but highly effective) sum-of-error function; this enables characters to be chosen not only on their 'darkness' but also their morphology (i.e. straight lines vs curves and loops).
Additionally, Compositor exposes a simplified image preprocessing interface, which is useful for 'noisy', or poorly equalised, or otherwise images whose native ASCII representations would be (to put it mildly) ugly as sin.

This software is more of an experiment than anything else, so expect terrible, terrible system retribution (and possibly really serendipitously interesting results) for using 'crazy' parameters, and avoid rendering fonts at sizes below say 12-18pt.
