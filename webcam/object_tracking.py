import cv2

#tracker = cv2.TrackerKCF.create()
tracker = cv2.TrackerCSRT.create()

#video = cv2.VideoCapture('data/race.mp4')
video = cv2.VideoCapture('data/street.mp4')
ok, frame = video.read()

bbox = cv2.selectROI(frame)

tracker.init(frame, bbox)

while True:
    ok, frame = video.read()
    if not ok:
        break
    ok, bbox = tracker.update(frame)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2, 1)
    else:
        cv2.putText(frame, 'Error', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Tracking', frame)
    key = cv2.waitKey(1)
    if key == 27: #ESC
        break