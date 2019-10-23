from handtracking import detect_single_threaded
from keras.models import load_model

gen = detect_single_threaded.detectNcrop()


model = load_model('signeye_M1.h5')

for i in gen:
    model.predict(i)