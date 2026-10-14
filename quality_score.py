def calculate_quality(predictions):
    score = 100

    for item in predictions:
        defect = item["class"]

        if defect == "BadSoldering":
            score -= 20

        elif defect == "TooBigSoldering":
            score -= 15

    if score < 0:
        score = 0

    return score


# test
sample_predictions = [
    {"class": "BadSoldering"},
    {"class": "TooBigSoldering"}
]

quality = calculate_quality(sample_predictions)

print("PCB Quality Score:", quality, "%")