from learner import get_learner

if __name__ == "__main__":
    learner = get_learner()
    learner.fine_tune(5)

    learner.save("weights")
