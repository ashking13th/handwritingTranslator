import predictionTranslation
# import d
import argparse
import bha

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True, help="Image path")
args = vars(ap.parse_args())

readText = bha.returnstr(args['path'])
predictionTranslation.translate(readText)