# Robbie: A batch processing work-flow for the detection of radio transients and variables

Robbie automates the process of cataloguing sources, finding variables, and identifying transients.

The workflow is described in Hancock et al. 2018 (in prep):
- Find sources in images
- Compare these catalogues to a reference catalogue
- Use the offsets to model image based distortions
- Make warped/corrected images
- Stack the warped images into a cube and form a mean image
- Source find on the mean image to make a master catalogue
- Priorized fit this catalogue into each of the individual images
- Join the catalogues into a single table and calculate variability stats
- Use the master catalogue to mask known sources from the individual images
- Source find on the masked images to look for transients
- Combine transients tables into a single catalogue, identifying the epoch of each detection

