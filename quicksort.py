"""
This version of the quicksort algorithm sorts
employee objects by its data fields.
"""

class Quicksort:

    def quicksort(emp_list, sort_by, low, high):
        if high <= low:
            return

        low_high_index = Quicksort.partition(emp_list, sort_by, low, high)

        Quicksort.quicksort(emp_list, sort_by, low, low_high_index)
        Quicksort.quicksort(emp_list, sort_by, low_high_index + 1, high)


    def partition(emp_list, sort_by, low, high):

        mid = (low + high) // 2
        pivot = emp_list[mid]
        done = False

        while not done:

            while Quicksort.compare(sort_by, emp_list[low], pivot):
                low = low + 1

            while Quicksort.compare(sort_by, pivot, emp_list[high]):
                high = high - 1

            if high <= low:
                done = True
                
            else:
                Quicksort.swap(emp_list, low, high)
                low = low + 1
                high = high - 1

        return high

    def compare(sort_by, emp_1, emp_2):

        if sort_by == 'name':

            n1 = Quicksort.name_reformat(emp_1["name"])
            n2 = Quicksort.name_reformat(emp_2["name"])
            
            res = n1 < n2

        elif sort_by == 'id':

            res = emp_1["id"] < emp_2["id"]

        elif sort_by == 'title':

            res = emp_1["title"] < emp_2["title"]

        elif sort_by == 'date':

            #Reformat dates for comparison.
            hd1 = Quicksort.date_reformat(emp_1["hire_date"])
            hd2 = Quicksort.date_reformat(emp_2["hire_date"])

            res = hd1 < hd2

        return res

    #Reformat name for comparison.
    def name_reformat(name):

        name = name.lower()
        comma = name.find(',')
        space = name.find(' ')
        first = name[space+1:]
        last = name[:comma]
        return f'{last}{first}'

    #Reformat date for comparison.
    def date_reformat(date):
        return f'{date[6:]}/{date[0:2]}/{date[3:5]}'
        
    #Swap values.
    def swap(emp_list, low, high):
        temp = emp_list[low]
        emp_list[low] = emp_list[high]
        emp_list[high] = temp
