import sys
import facial_landmarks
import time

file = sys.argv[1]
start = time.time()
x = facial_landmarks.main('shape_predictor_68_face_landmarks.dat', file)
end = time.time()

# 18000 has been arbitrarily selected to hopefully not detect too many beards
# or makeup as a mask, and not detect masks as face
if x < 18000.0:
    print("We believe this person is not wearing a mask,\
the similarity of their forehead and mouth region has been assessed to: %.2f, under 18 000 means not wearing mask" % x)
else:
    print("We believe this person is wearing a mask,\
the similarity of their forehead and mouth region has been assessed to: %.2f, under 18 000 means not wearing mask" % x)

print("This check took: %.2f seconds" % (end-start))
