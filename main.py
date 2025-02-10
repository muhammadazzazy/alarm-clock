import datetime
import time
import playsound
from sys import exit


def main() -> None:
    print('Welcome to The ⏰ Clock!')
    file_path = input('Enter the path of the audio file for the alarm clock: ')
    while True:
        try:
            user_input = input(
                'Enter some duration (in minutes or seconds) or local time in 24-hour format: ')

            if user_input == 'exit':
                print('Thanks for trying my program!')
                exit()

            if (len(user_input.split()) == 2) and (('minutes' in user_input) or ('seconds' in user_input)):
                value_unit = user_input.split()

                x = int(value_unit[0])

                if value_unit[1] == 'seconds':
                    time.sleep(x)
                else:
                    time.sleep(x*60)

                playsound.playsound(file_path)

            elif (len(user_input.split(':')) == 2) and (user_input[2] == ':'):
                hours_minutes = user_input.split(':')
                while True:
                    string = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    date_time = string.split()
                    hours_minutes_seconds = date_time[1].split(':')
                    if hours_minutes_seconds[0] == hours_minutes[0] and hours_minutes_seconds[1] == hours_minutes[1]:
                        break

                playsound.playsound(file_path)
            else:
                print('Invalid input...')

        except playsound.PlaysoundException:
            print('Invalid file path...')
            continue

        except ValueError:
            print('Invalid time...')
            continue

        except KeyboardInterrupt:
            print('Exiting...')
            exit()


if __name__ == '__main__':
    main()
