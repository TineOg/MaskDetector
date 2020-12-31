# MaskDetector

This is a small little program I wrote for a bit of fun and to learn some stuff.

It takes as an argument a path to an image of a person,
and then it decides if there is a person in this image not wearing a mask.

It tries to first detect a face, if none is detected it assumes there isn't any idiots not wearing masks in there.
If a face is detected it then runs another check to try and figure out if the person in the image
may actually be wearing a mask. It does this by using dlibs frontal face detector to outline the basic facial features.
Then it uses those detected facial features to take out an image of the forehead and of the mouth region, then it
gets the mean color of those regions and compares it using redmean approximation. Then it checks that approximation
against a value I hardcoded in arbitrarily to minimise the false positives and the false negatives and if its bigger
than that value it says the person is wearing a mask.