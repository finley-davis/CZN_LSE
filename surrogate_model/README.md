
To run: python3 -m surrogate_model.train; This takes forever...

I call it like this because I am using relative import, so I run it as a module from the repo root, rather than as a file. 

Prediction:
I've added lse and time data to the fields csvs. Now I need to train the model on this, so that 
salinity can be predicted based on this. 

I'm going to do this in multiple ways.
    1 - get max value from salt front (salinity and x-value)
    2 - get total salinity from sim.
    3 - mean salinity from sim.