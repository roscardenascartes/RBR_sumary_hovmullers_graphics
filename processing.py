def processing_rbr(datafile,dirout,dir):

    from pyrsktools import RSK
    import matplotlib.pyplot as plt
    import numpy as np
    import os
    from pathlib import Path


    os.makedirs(Path(dirout+"_"+dir),exist_ok="true")
    print(datafile)


    rsk = RSK(Path(datafile))
    rsk.open()
    rsk.readdata()
    rsk.deriveseapressure()
    rsk.derivesalinity()
    rsk.derivesigma()
    # haciendo una copia para no alterar los datos originales
    raw = rsk.copy()
    raw.readdata()
   # raw.printchannels() # datos con los que viene
    raw.deriveseapressure()
    # correcion A2D zero-holder
    raw.correcthold(action = "interp")
    # Filtro pasa bajo
    raw.smooth(channels = ["temperature","conductivity","pressure","dissolved_o2_saturation","chlorophyll","turbidity","sea_pressure"], windowLength = 7)
    # Alineacion temperatura y conductividad
    # Required shift of C relative to T for each profile
    lag = raw.calculateCTlag(seapressureRange = (3,round(max(raw.data["sea_pressure"]),0)), direction = dir) 
    # Advance temperature
    lag = -np.array(lag)
    #print('THE LAG IS: '+str(lag))
    # Select best lag for consistency among profiles
    lag = np.median(lag)
    if isinstance(lag,int):
        raw.alignchannel(channel = "temperature", lag = lag, direction = dir) # revisarque no falte un paso "eliminacion bucles" luego de este
        print('THE LAG IS: '+str(lag))
    else:
        lag=round(lag)
        raw.alignchannel(channel = "temperature", lag = lag, direction = dir) # revisarque no falte un paso "eliminacion bucles" luego de este
        print('THE LAG IS: '+str(lag))
    # correccion de oxigeno y conductividad termica
    raw.correcttau(channel="dissolved_o2_saturation", tauResponse=3, direction=dir, profiles=[])  #rinko 3. 
    raw.correctTM(alpha=0.04, beta=0.1)
    # derivacion de profundidad y velocidad
    raw.derivedepth()
    raw.derivevelocity()
    # Removiendo loops
    raw.removeloops(threshold = 0.25) 
    # derivacion de salinidad y sigma
    raw.derivesalinity()
    raw.derivesigma()
    raw.deriveSA()
    # Alineando bins
    raw.binaverage(
        binBy = "depth",
        binSize = 1.5, #[0.5,5],
        boundary = [1, 90],#[0.5, 40], 
        direction = dir #si se ha hecho todo lo demas con el downcast, entonces se debe seguir con el downcast.
    )
   # raw.printchannels() # datos luego del procesamiento
    #guardando los datos en csv
    raw.RSK2CSV(channels = [], profiles= [],outputDir= Path(dirout+"_"+dir),comment= "processed data")
    #guardando los datos en rsk
    raw.RSK2RSK(outputDir= Path(dirout+"_"+dir,suffix="processed"))
    #print(raw.logs)
    rsk.close()
    raw.close()
    print("done")
