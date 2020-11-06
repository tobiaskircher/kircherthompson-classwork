class Member():
    def __init__(self,my_surname,my_first_name,my_annual_fee):
        self.surname = my_surname
        self.firstname = my_first_name
        self.annualfee = my_annual_fee
    #endprocedure

#endclass

class JuniorMember(Member):
    def __init__(self,my_surname,my_first_name,my_annual_fee,my_date_of_birth):
        super().__init__(my_surname,my_first_name,my_annual_fee)
        self.dateofbirth = my_date_of_birth
    #end procedure

#endclass

member1 = Member("Mason","Harry",30)
junior1 = JuniorMember("Mason","Larry",25,"12/12/2004")

print(junior1.annualfee)
