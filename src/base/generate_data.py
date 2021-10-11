import pandas as pd
from pandas.core.groupby.generic import generate_property
from sklearn.model_selection import train_test_split
import argparse


def generate_data():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--location", help="url of file to be processed", required=True)
    parser.add_argument('-t', '--test_size', type=float,
                        default=0.2, help='split size for the test data')
    args = parser.parse_args()

    print(args)
    data = pd.read_csv(args.location)
    print(data.head())


if __name__ == "__main__":
    generate_data()
