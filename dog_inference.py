def classes():
    return [
        "dog",
        "bark",
        "whining",
        "howl",
        "yip",
        "bow-wow",
        "growling",
        "whimper (dog)",
    ]

def isDogInfered(infered_classes_scores, threshold = 0.25):
    if "dog" in infered_classes_scores:
        return infered_classes_scores["dog"] > threshold
    return False

def inferDogSound(infered_classes_scores):
    dog_sounds = {}
    for i in classes():
        if i not in infered_classes_scores:
            continue
        dog_sounds[i] = infered_classes_scores[i]
    return dog_sounds