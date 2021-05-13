def print_inferences(infered_classes, scores):
    return (
        '\n'.join('  {:12s}: {:.3f}'.format(infered_classes[i], scores[i])
                    for i in range(len(scores)))
    )