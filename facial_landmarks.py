# import the necessary packages
from imutils import face_utils
import dlib
import cv2


def color_diff(a, b):
	# redmean approximation of how different two colors are
	# acknowledging that cv2 images are BGR and not RGB
	r = (a[2] + b[2])/2
	c = (2 + r/256) * pow((a[2] - b[2]), 2) + 4 * pow((a[1] - b[1]), 2) + (2 + (255 - r)/256) * pow((a[0] - b[0]), 2)
	return c


def image_resize(image, width):
	# initialize the dimensions of the image to be resized and
	# grab the image size
	dim = None
	(h, w) = image.shape[:2]

	# calculate the ratio of the width and construct the
	# dimensions
	r = width / float(w)
	dim = (width, int(h * r))

	# resize the image
	resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

	# return the resized image
	return resized

# Function will return the similarity between the colors of the forehead and of the mouth region.
# if no face is detected(hopefully due to the mask obstructing it) then we return a high value.
def main(shape_predictor, image_name):
	# initialize dlib's face detector (HOG-based) and then create
	# the facial landmark predictor
	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor(shape_predictor)

	# load the input image, resize it, and convert it to grayscale
	image = cv2.imread(image_name)
	image = image_resize(image, width=500)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# detect faces in the grayscale image
	rects = detector(gray, 1)

	similarity = 100000.0

	# loop over the face detections
	for (i, rect) in enumerate(rects):
		# determine the facial landmarks for the face region, then
		# convert the facial landmark (x, y)-coordinates to a NumPy
		# array
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)

		# pick out areas around the forehead and around the mouth and get their mean colour
		forehead = image[(shape[0][1] - 2*(shape[0][1] - shape[19][1])): shape[0][1], shape[17][0]: shape[26][0]]
		forehead_color = cv2.mean(forehead)
		mouth = image[shape[31][1]:shape[11][1], shape[5][0]:shape[11][0]]
		mouth_color = cv2.mean(mouth)

		# calculate how similar the colors of the forehead and mouth are(mask and forehead should be different
		# coloured most likely. However this also has problems with some masks and some people with beards
		similarity = color_diff(forehead_color, mouth_color)

		# cv2.imshow("face", image)
		# cv2.imshow("forehead", forehead)
		# cv2.imshow("mouth", mouth)
		# cv2.waitKey(0)

	return similarity
