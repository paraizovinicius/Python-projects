from rpc import RPCClient
import argparse
import sys
from typing import List


def parse_value(s: str):
	"""Try to convert a string CLI arg to int or float, otherwise return as str."""
	# Try int
	try:
		return int(s)
	except ValueError:
		pass
	# Try float
	try:
		return float(s)
	except ValueError:
		return s


def main(argv: List[str] = None):
	argv = argv if argv is not None else sys.argv[1:]

	parser = argparse.ArgumentParser(description="Simple RPC client CLI")

	# We accept a single method name as a flag (e.g. --add) followed by its positional args
	# To keep parsing simple, we treat the first non-option as the method name.
	parser.add_argument("method", nargs="?", help="RPC method name to call (add, sub, multiply, divide)")
	parser.add_argument("args", nargs=argparse.REMAINDER, help="Positional arguments for the method")

	ns = parser.parse_args(argv)

	if not ns.method:
		parser.print_help()
		return 1

	# Extract positional args (ignore leading '--' that argparse may keep)
	raw_args = ns.args or []
	# Remove leading '--' if present (argparse.REMAINDER keeps it when used)
	if raw_args and raw_args[0] == "--":
		raw_args = raw_args[1:]

	parsed_args = [parse_value(a) for a in raw_args]
    
	# Connect to server
	client = RPCClient()

	try:
		client.connect()
	except Exception as e:
		print(f"Failed to connect to RPC server: {e}")
		return 2

	print(getattr(client,parsed_args[0])(parsed_args[1], parsed_args[2]))

	client.disconnect()
	return 0


if __name__ == "__main__":
	raise SystemExit(main())