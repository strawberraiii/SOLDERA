from inference_sdk import InferenceHTTPClient
from collections import Counter

client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="es97dbNXOpNwQi2SbhxV"
)

response = client.infer(
    "test_image3.jpg",
    model_id="automated-optical-inspection-yolo-vautomated-optical-inspection-yolo-cbab0-1-rfdetr-small-t1-logic"
)


predictions = response["predictions"]


counts = Counter(
    item["class"] 
    for item in predictions
)


good = counts["GoodSoldering"]

defects = (
    counts["BadSoldering"]
    + counts["TooBigSoldering"]
    + counts["NoSoldering"]
)


total = good + defects


if total == 0:
    quality = 0
else:
    quality = (good / total) * 100


print("======================")
print("PCB INSPECTION RESULT")
print("======================")

print("Good Solder:", good)
print("Defective Solder:", defects)
print("Total Solder:", total)

print("Quality Score:", round(quality,2), "%")

if quality >= 90:
    print("STATUS: PASS")
else:
    print("STATUS: FAIL")