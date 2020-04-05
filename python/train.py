from textgenrnn import textgenrnn
import datetime
import time

inFile = input("\nModel File To Load (Leave Blank To Create New): ")

# --- Set Epochs ---
epochs = 8

try:
    epochs = int(input("Epochs To Run (Default = 8): "))
except:
    print("Invalid Number Of Epochs, Setting To 8")

# --- Set Model ---
textgen = None
if inFile == "":
    textgen = textgenrnn(name="Arab-" + str(int(time.time())))
else:
    textgen = textgenrnn(inFile)

# --- Train ---
sTime = int(time.time())
textgen.train_from_file('titles.txt', num_epochs=epochs)

# --- Done ---
print("\nDone Training! Took: " + str(datetime.timedelta(seconds=int(time.time())-sTime))) 
