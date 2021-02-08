import time
import argparse
import pandas

from mwprojekt.traffic import traffic_computation


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-fl", "--folder", type=str, default='data/', help="Folder with Data")
    ap.add_argument("-sf", "--save", type=bool, default=False, help="save to file")
    ap.add_argument("-dt", "--date", type=str, default='03.02.2021', help="date to save")
    ap.add_argument("-nr", "--number", type=int, default=4, help="date to save")

    args = vars(ap.parse_args())    
    traffic = traffic_computation(args['folder'], args['date'], args['number'])
    print("collected data:")
    print([df.head() for df in traffic])
    if args['save'] == True:
        [traffic[i].to_csv('analytics{0}.csv'.format(i),index=False) for i in range(len(traffic))]