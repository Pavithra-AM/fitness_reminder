from django.shortcuts import render
from django.http import JsonResponse
import random

# Predefined reminders
REMINDERS = [
    "Take a 5-minute stretch break!",
    "Do 15 push-ups!",
    "Drink water!",
    "Go for a 10-minute walk!",
    "Try deep breathing for 2 minutes!"
]

# A global list to store activity logs (for demonstration purposes only)
# For production, use a database to store logs.
activity_log = []

# Home page view
def generate_reminder(request):
    context = {
        'reminder': "Click 'Generate New Reminder' to start.",
        'activity_log': activity_log
    }
    return render(request, 'reminder/home.html', context)

# API to get a new reminder
def get_new_reminder(request):
    new_reminder = random.choice(REMINDERS)
    activity_log.append(new_reminder)  # Log the generated reminder
    return JsonResponse({'reminder': new_reminder})
'''
limit the activities
from django.shortcuts import render
from django.http import JsonResponse
import random

# Predefined reminders
REMINDERS = [
    "Take a 5-minute stretch break!",
    "Do 15 push-ups!",
    "Drink water!",
    "Go for a 10-minute walk!",
    "Try deep breathing for 2 minutes!"
]

# Global list for activity log
activity_log = []
LOG_LIMIT = 5  # Maximum number of log entries

# Home page view
def generate_reminder(request):
    context = {
        'reminder': "Click 'Generate New Reminder' to start.",
        'activity_log': activity_log
    }
    return render(request, 'reminder/home.html', context)

# API to get a new reminder
def get_new_reminder(request):
    new_reminder = random.choice(REMINDERS)
    activity_log.append(new_reminder)  # Add new reminder to the log

    # Limit the activity log size
    if len(activity_log) > LOG_LIMIT:
        activity_log.pop(0)  # Remove the oldest entry if log exceeds the limit

    return JsonResponse({'reminder': new_reminder})
'''