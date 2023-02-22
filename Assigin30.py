# Asuku  CIS 101  November 2022  Assignment 30
# This function will ask the person's First and Last name, then ask, how many credit they took. 
# Those information will put on the list.
# By using the list from the personal information, this program will check which class status they are.
def function ():
  while True:
    print("Enter your information Name and credit hours in the formatIf you would like to quit, input 'q' >>>")
    inList = input("'First Name', 'Last Name', crHrs: ")
    if inList[0] == 'q':
      break
    if len(inList)==3 and type(inList[0])==str and\
      type(inList[1])==str and type(inList[2])==int:
      credit = inList[2]
      if 0 <int(credit):
        if int(credit) < 30:
          status = 'Freshman'
        elif 30 <= int(credit) and int(credit) <60:
          status = 'Sophomore'
        elif 60 <= int(credit)  and int(credit) < 90:
          status = 'Junior'
        elif int(credit) >= 90:
          status = 'Senior'
        print('Hello '+inList[0]+' '+inList[1]+'!! Now, your status is ' + status +'.')
      else:
        print ('Sorry, your input is incorrect, please try again')

