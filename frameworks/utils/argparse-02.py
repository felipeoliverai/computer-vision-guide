import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Testing")
    parser.add_argument('--weights', type=str, default='model.h5',
                        help='weights of trained neural network file')
    parser.add_argument('--epochs', type=int, default=100,
                        help='epochs for running training model')
    parser.add_argument('--batch', type=int, default=16,
                        help='batching size of samples for each epoch')

    # store_true = boolean value
    parser.add_argument('--pretrained', action='store_true',
                        help='Setup way to train pre-trained architecture')
    args = parser.parse_args()

    # visualize results
    print("Weights: ", args.weights)
    print("Epochs: ", args.epochs)
    print("Batch size: ", args.batch)
    print('Pre-trained: ', args.pretrained)
