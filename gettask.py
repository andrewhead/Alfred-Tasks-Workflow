#! /usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import logging
import datetime
import config
import argparse


logging.basicConfig(level=logging.INFO, format="%(message)s")


def get_task(tasks, hour, minute):

    target_hour = hour
    target_minute = minute - (minute % 30)  # Tasks are listed at 30-min. intervals
    target_timestamp = "%d:%02d" % (target_hour, target_minute)

    for timestamp, task in tasks:
        if timestamp == target_timestamp:
            if len(task.strip()) > 0:
                return task

    return "Nothing scheduled!  Proceed at will."


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Get the task for a time")
    parser.add_argument('--time', help="HH:MM-style time.  If not provided, get task for current time.")
    args = parser.parse_args()

    tasksfilename = config.get_option('tasksfile')
    tasks = []
    with open(tasksfilename) as tfile:
        for l in tfile.readlines():
            toks = l.split(',', 1)
            if len(toks) > 1:
                tasks.append((toks[0], toks[1]))

    if args.time is not None:
        hours, mins = [int(tok) for tok in args.time.split(':')]
    else:
        now = datetime.datetime.now()
        hours, mins = now.hour, now.minute

    print get_task(tasks, hours, mins)
