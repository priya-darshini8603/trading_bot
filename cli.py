import argparse

def parse_args():
    parser = argparse.ArgumentParser("Advanced Trading Bot")

    parser.add_argument("--symbol", default="BTCUSDT")
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True,
                        choices=["market", "limit", "stop", "twap"])
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop", type=float)
    parser.add_argument("--intervals", type=int)

    return parser.parse_args()
