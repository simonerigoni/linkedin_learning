# Set an alarm
# python set_an_alarm.py


import time
import sched
import winsound


def set_alarm(alarm_time, audio_filepath, message):
    '''
    Set an alarm that will be triggered at the given time showing the given message

    Arguments:
        alarm_time (str): time to trigger the alarm
        audio_filepath (str): filepath for the audiofile to be used for the aalarm
        message (str): message to show when the alarm is triggered

    Returns
        None
    '''
    alarm = sched.scheduler(time.time, time.sleep)
    alarm.enterabs(alarm_time, 1, winsound.PlaySound, argument = (audio_filepath, winsound.SND_FILENAME))
    alarm.enterabs(alarm_time, 1, print, argument = (message, ))
    print('Alarm set for ', time.asctime(time.localtime(alarm_time)))
    alarm.run()


if __name__ == '__main__':
    set_alarm(time.time() + 1, 'Alarm05.wav', 'Wake up!')