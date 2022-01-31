## Using these notebooks

Step 1 uses the friction surface(s) and destinations previously generated to batch create access surfaces, one for each destination for each travel scenario (season).

Step 2 joins the resulting access data to points from WorldPop / HRSL and aggregate the data by administrative unit, weighting for population.

Step 3 aggregates the resulting point access data in long and wide formats per admin unit. You can skip the wide aggregation if you already did it in Step 2.

Steps 2 and 3 require a working Dask installation and a computer with sufficient cores + memory to process the data. We recommend 8 cores + 32 GB RAM as a minimum with 16 cores + 64GB the ideal.
