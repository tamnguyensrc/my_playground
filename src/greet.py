import argparse


def main():
    parser = argparse.ArgumentParser(prog='greet', description='CLI tes demo package.')

    parser.add_argument('-greet', action='store_const', const=True, default=False, dest='greet', help="Greet Message")
    parser.add_argument('-name', type=str, help='user name')

    args = parser.parse_args()

    if args.greet:
        if args.name:
            print(f"Welcome {args.name}!")
        else:
            print("Welcome, Friend!")
    else:
        print("Bye!")


if __name__ == '__main__':
    main()
