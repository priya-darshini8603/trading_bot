from config import API_KEY, API_SECRET
from core.client import BinanceClient
from core.order_manager import OrderManager
from core.strategies import TWAPStrategy
from cli import parse_args

def main():
    args = parse_args()

    client = BinanceClient(API_KEY, API_SECRET)
    om = OrderManager(client)

    if args.type == "market":
        res = om.market(args.symbol, args.side, args.qty)

    elif args.type == "limit":
        res = om.limit(args.symbol, args.side, args.qty, args.price)

    elif args.type == "stop":
        res = om.stop_limit(args.symbol, args.side, args.qty, args.stop, args.price)

    elif args.type == "twap":
        TWAPStrategy(om).execute(
            args.symbol, args.side, args.qty, args.intervals
        )
        res = {"status": "TWAP EXECUTED"}

    print("\nORDER RESULT:")
    print(res)

if __name__ == "__main__":
    main()
