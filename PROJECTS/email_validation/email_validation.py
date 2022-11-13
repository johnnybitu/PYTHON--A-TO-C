Email = input("provide your email :")
k = 0
d = 0
j =0


if len(Email)>= 6 :

    if Email[0].isalpha():

        if ("@" in Email) and (Email.count("@")==1):



            if (Email[-4]==".") ^ (Email[-3]==".") :


                for  i in Email:

                    if i ==i.isspace():

                        k = 1

                    elif i.isalpha():

                        if i == i.upper():

                            j = 1

                    elif i.isdigit():

                        continue

                    elif i == "_" or i =="." or i =="@":

                        
                        continue

                    else:

                        d = 1

                if k ==1 or j ==1 or d == 1:

                    print("wrong email ")
                else:
                    print("you have provided write email")

                    
            else:

                print("wrong email")

        else:
            print('wrong email address')

    else:
        print('wrong email ')
else :
    print("provide a correct email addresss")