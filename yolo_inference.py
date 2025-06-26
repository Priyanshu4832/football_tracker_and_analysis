from ultralytics import YOLO

#used this model for first predict not detecting ball or goalkeeper just the person
#model = YOLO('yolov8x')


#predict 2 predicts ball,goalkeeper
model= YOLO('models/best.pt')

results = model.predict('input_videos/08fd33_4.mp4',save=True)

print(results[0])

print('==================================================')

for box in results[0].boxes:
    print(box)