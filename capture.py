# capture.py
import cv2, os

def capture_person(name, out_dir='dataset', num_images=20):
    path = os.path.join(out_dir, name)
    os.makedirs(path, exist_ok=True)
    cap = cv2.VideoCapture(0)
    count = 0
    print("Press 'c' to capture, 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Capture - press c", frame)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('c'):
            fname = os.path.join(path, f'{name}_{count}.jpg')
            cv2.imwrite(fname, frame)
            print("Saved", fname)
            count += 1
            if count >= num_images:
                break
        elif k == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # replace name below for whoever you want to capture
    capture_person("Vivek", num_images=30)