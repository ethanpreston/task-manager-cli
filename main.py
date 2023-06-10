import argparse
from actions import (
    add,
    delete,
    describe,
    categorize,
    list_category,
    list_all,
    complete,
    clear_completed,
    edit_due_date,
    edit_priority
)

# Set up parser for the command line interface
parser = argparse.ArgumentParser(description="Task Manager to help you organize your to-do lists")
parser.add_argument('action', help='Enter which action you would like to execute')
parser.add_argument('-t', '--task', default="", help='Specify which task you would like to add')
parser.add_argument('-c', '--category', default=None, help='Specify the category you are trying to reference')
parser.add_argument('-d', '--due_date', default=None, help='Specify the relevant due date for the task')
parser.add_argument('-p', '--priority', default=None, help='Specify the relevant priority of the task [1-10]')
args = parser.parse_args()

if args.action == 'add':
    add(args.task, args.due_date, args.priority, args.category, 0)
elif args.action == 'delete':
    delete(args.task)
elif args.action == 'describe':
    describe(args.task)
elif args.action == 'categorize':
    categorize(args.task, args.category)
elif args.action == 'edit':
    if args.category:
        categorize(args.task, args.category)
    elif args.due_date:
        edit_due_date(args.task, args.due_date)
    elif args.priority:
        edit_priority(args.task, args.priority)
elif args.action == 'list':
    if args.category:
        list_category(args.category)
    else:
        list_all()
elif args.action == 'complete':
    complete(args.task)
elif args.action == 'clear_completed':
    clear_completed()
else:
    parser.print_help()
