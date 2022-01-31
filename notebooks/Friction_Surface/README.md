## Using these notebooks

These notebooks describe a process to create a custom friction surface for custom data inputs using the best methods known to ESAPV.

The notebooks are meant to be used in order. The notebooks are largely self explanatory by title, with the output of each feeding into the next. Note that Step 1's code may require heavy adaptation to your road data inputs.

This process presupposes the following data inputs:
* OpenStreetMap and / or custom roads vector data
* A raster landcover model
* A raster Digital Elevation Model
* A rivers vector layer
* Optionally, a bridges vector (point) layer

The concepts behind this friction surface modeling are documented in https://www.sciencedirect.com/science/article/abs/pii/S0966692321001101. Note that we have since adopted improved walking speed and altitude adjustment functions.
