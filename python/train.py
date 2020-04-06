from textgenrnn import textgenrnn
import datetime
import glob
import time
import sys

inModel = input("\nModel File To Load (Blank To Create New): ")

# --- Set Input Text ---
inText = ""
txts = glob.glob('*.txt')

if len(txts) == 0:
    inText = input("Text File To Train On: ")
else:
    inText = txts[0]
    newText = input("Text File To Train On (Default = " + inText + "): ")

    if newText != "" : inText = newText

if inText == "":
    print("No File Selected!")
    sys.exit()

# --- Set Epochs ---
epochs = 8

try:
    epochs = int(input("Epochs To Run (Default = 8): "))
except:
    print("Invalid Number Of Epochs, Setting To 8")

# --- Set Model ---
textgen = None
if inModel == "":
    textgen = textgenrnn(name="Model-" + str(int(time.time())))
else:
    textgen = textgenrnn(inModel)

# --- Train ---
sTime = int(time.time())
textgen.train_from_file(inText, num_epochs=epochs)

# --- Done ---
print("\nDone Training! Took: " + str(datetime.timedelta(seconds=int(time.time())-sTime))) 
