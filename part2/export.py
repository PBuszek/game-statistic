import reports
from printing import *

def export_get_most_played(a):
    with open('export_reports.txt', 'a') as out:
        out.write(str(a) + "\n")

def export_sum_sold(a):
    with open('export_reports.txt', 'a') as out:
        out.write(str(a) + "\n")

def export_get_selling_avg(a):
    with open('export_reports.txt', 'a') as out:
        out.write(str(a) + "\n")

def export_get_game(a):
    with open('export_reports.txt', 'a') as out:
        out.write(str(a) + "\n")
