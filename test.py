import pickle
import warnings

try:
    pipe = pickle.load(open('pipe_suriya.pkl','rb'))
except Exception as e:
    print(e)
