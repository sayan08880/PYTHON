def leep_year(year) :
    if(year % 4 == 0) :
        if(year % 100 != 0) or (year % 400 == 0):
            print(f"{year} IS LEEP YEAR")
        else :
            print(f"{year} IS NOT LEEP YEAR")
    else :
        print(f"{year} IS NOT LEEP YEAR")


year = int(input("ENTER THE YEAR : "))
leep_year(year)

