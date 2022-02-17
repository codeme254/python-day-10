#functions with output
# we have the following types of functions
# normal functions with no input
# functions that allow us to give an input
# another type of function is the one with output, it uses the return keyword


# DOCSTRINGS
# little pieces of documentation in our python functions
#use three quotation marks to write the documetation
# docstrings can also be used for commenting
def format_name(f_name, l_name):
    """Takes first and last name and formats them to title case"""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("dennis", "OTWOMA")
print(formated_string)

# days in moth coding exercise
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if month > 12 and month < 1:
      return "invalid month"
  elif is_leap(year) and month == 2:
      return 29
  return month_days[month-1]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)



    