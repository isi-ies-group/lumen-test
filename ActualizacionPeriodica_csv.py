import pandas as pd
import schedule
import time

def job():
     df = pd.DataFrame({'irr_sup': [10,20,30,40],
                     'irr_fro': [11,21,31,41],
                     'irr_tra': [12,22,32,42],
                     'irr_der': [13,23,33,43],
                     'irr_izq': [14,24,34,44]})
     df.to_csv('ficheros/tracker_TiempoReal.csv', mode='a', index=False, header=False)
     print("Imprimiendo en csv")

    
schedule.every(1).minutes.do(job)

while True: 
    schedule.run_pending()
    time.sleep(1)
    

    
    
