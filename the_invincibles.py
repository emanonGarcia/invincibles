import argparse
import psycopg2
from player import Player

conn = psycopg2.connect("dbname=invincibles0304 user=Emanon805")
cur = conn.cursor()

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--create', help='Create a new record', action='store_true')
parser.add_argument('-r', '--read', help='Read the table', action='store_true')

args = parser.parse_args()


def create_player():
    try:
        name = input("What is the player's name? ")
        kit_num = int(input("What was {}'s kit number? ".format(name)))
        pos = input("What position did {} play? GK, DF, MF, or FW: ".format(name))
        dob = input("Do you know {} was born? MM/DD/YY ".format(name))
        nat = input("What is {} nation of origin? ".format(name))
        apps = input("How many appearences did he make in the Premier league? apps(subs): ")
        goals = int(input("How many goals did {} score? ".format(name)))
        assists = int(input("How many assists did he have? "))
        mins = int(input("Finally, how many minutes did he play? "))

        user_input = input("Want to see your new record Y/n? ")
        if len(user_input) > 0:
            if user_input.lower() == 'y' or user_input[0].lower() == 'y':
                read_players()
            elif user_input.lower() == 'n' or user_input[0].lower() == 'n':
                print('Okay')

        cur.execute("INSERT INTO squad (kit_num, name, pos, dob, nat, apps, goals, assists, mins) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (kit_num, name, pos, dob, nat, apps, goals, assists, mins))

        conn.commit()

    except ValueError as verr:
        print("ValueError {}".format(verr))


def read_players():
    cur.execute("SELECT kit_num, name ,pos FROM squad ORDER BY kit_num;")
    for num, name, pos in cur:
        print("{}: {}, {}".format(num, name, pos))

    while True:
        user_input = input("Search by kit number or position (Q/q to quit): ")
        if len(user_input) > 0:
            if user_input.isdigit():
                cur.execute("SELECT * FROM squad WHERE kit_num = %s ORDER BY kit_num;", (user_input,))
                for record in cur:
                    player = Player(*record)
                    print(player, '\n')

            elif user_input.upper() in ['GK', 'DF', 'MF', 'FW']:
                cur.execute("SELECT * FROM squad WHERE pos = %s ORDER BY mins DESC;", (user_input.upper(),))
                for record in cur:
                    player = Player(*record)
                    print(player, '\n')

            elif user_input.lower() == 'q' or user_input[0].lower() == 'q':
                exit()
        else:
            continue

def main():

    if args.create:
        create_player()

    elif args.read:
        read_players()

    elif args.update:
        update_player()
    else:
        print("Try passing the -h/--help flag for instructions")

    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
