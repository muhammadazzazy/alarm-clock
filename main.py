import datetime
import time
import playsound
from sys import exit


def main() -> None:
    print('Welcome to The ⏰ Clock!')
    file_path: str = input(
        'Enter the path of the audio file for the alarm clock: ')
    exit_message: str = 'Exiting program...'
    while True:
        try:
            user_input: str = input(
                'Enter some duration (in minutes or seconds) or local time in 24-hour format: ')

            if user_input == 'exit':
                print(exit_message)
                exit()

            if (len(user_input.split()) == 2) and (('minutes' in user_input) or ('seconds' in user_input)):
                value_unit: list[str] = user_input.split()

                x: int = int(value_unit[0])

                if value_unit[1] == 'seconds':
                    time.sleep(x)
                else:
                    time.sleep(x*60)

                playsound.playsound(file_path)

            elif (len(user_input.split(':')) == 2) and (user_input[2] == ':'):
                hours_minutes: list[str] = user_input.split(':')
                while True:
                    string: str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    date_time: list[str] = string.split()
                    hours_minutes_seconds: list[str] = date_time[1].split(':')
                    if hours_minutes_seconds[0] == hours_minutes[0] and hours_minutes_seconds[1] == hours_minutes[1]:
                        break

                playsound.playsound(file_path)

            else:
                print('Please enter valid input...')

        except ValueError:
            print('Please enter a valid time...')
            continue

        except playsound.PlaysoundException:
            print('Please enter a valid file path...')
            exit()

        except KeyboardInterrupt:
            print(exit_message)
            exit()


if __name__ == '__main__':
    main()
