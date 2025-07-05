#Welcomer
print("""

░█████╗░░█████╗░░█████╗░███████╗██████╗░████████╗░█████╗░███╗░░██╗░█████╗░███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔══██╗████╗░██║██╔══██╗██╔════╝
███████║██║░░╚═╝██║░░╚═╝█████╗░░██████╔╝░░░██║░░░███████║██╔██╗██║██║░░╚═╝█████╗░░
██╔══██║██║░░██╗██║░░██╗██╔══╝░░██╔═══╝░░░░██║░░░██╔══██║██║╚████║██║░░██╗██╔══╝░░
██║░░██║╚█████╔╝╚█████╔╝███████╗██║░░░░░░░░██║░░░██║░░██║██║░╚███║╚█████╔╝███████╗
╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝
""")
print("Welcome to the university admissions office")
specialty = input("Choose mathematics, chemistry : ")
# Enter major IF
if specialty.lower() == "mathematics" or specialty.lower() == "chemistry":
  grades = int(input("What is your high school GPA? : "))
# Enter GPA IF
  if grades >= 90:
    print(f"\nGreet! You have been accepted into the major {specialty}")
  elif grades >= 75:
    print("\nYour result is being reviewed. Please wait.")
  elif grades >= 50:
    print("\nYour result is being reviewed. Please wait.")
  elif grades <= 50:
    print(f"\nSorry, You have been rejected for the major {specialty}")
# ENDING CODE and ENDING ( Error Codes )
  else:
    print("\nError! Inviled Number.")
else:
  print(f"\nError! This {specialty} is not available")
