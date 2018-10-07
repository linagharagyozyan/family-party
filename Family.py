import datetime
now = datetime.datetime.now()
class familyMember(object):
    def __init__(self, first_name, last_name,role,birthday,phone,job,school_university):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.birthday = birthday
        self.age = now.year - self.birthday.year
        self.phone = phone
        self.job = job
        self.school_university = school_university

    def getStatus(self):
        print self.role

    def getRelationto(self, person):
        print self.role, "and", person.role

    def checkBirthday(self):
        if now.month == self.birthday.month and now.day == self.birthday.day:
            return True

        else:
            return False

    def printInfo(self):
        print "\n""Info", "\n""Name: ", self.first_name, "\n" \
        "Surname: ", self.last_name, "\n", "Status: ",\
            self.role,"\n""Birthday: ", self.birthday, "\n""Age: ", self.age,"\n""Phone number: ",\
            self.phone, "\n""Job: ", self.job, "\n""University/School: ", self.school_university


class family:
    def __init__(self,address, telephone_number,family_name):
        self.address = address
        self.telephone_number = telephone_number
        self.family_name = family_name
        self.members = []

    def addMember(self, member):
        return self.members.append(member)

    def printMember(self):
        for k in self.members:
            print k

    def printInfo(self):
        print "\n""Family Info","\n""Address: ", self.address, "\n""Phone number: ",self.telephone_number,\
            "\n" "Family name: ", self.family_name

class pet:
    def __init__(self,name, type, age):
        self.name = name
        self.type = type
        self.age = age

    def voice(self):
        print "Haf-haf"

class birthdayParty:
    def __init__(self,member):
        self.birthdayPerson = member
        self.invited = []
        self.place = []
        self.date = []
        self.hour = []
        self.expenses = []

    def setDate(self,date):
        return self.date.append(date)

    def getDate(self):
        for k in self.date:
            return k

    def setHoure(self,hour):
        return self.hour.append(hour)

    def getHour(self):
        for k in self.hour:
            return k

    def invite(self,person):
        return self.invited.append(person)

    def getGuests(self):
        print "Guests for", self.birthdayPerson.first_name,"'s birthday party"
        for k in self.invited:
            print k
        print "Number of guests", "|",len(self.invited),"|"

    def setPartyPlace(self, place):
            return self.place.append(place)

    def getPartyPlace(self):
        for k in self.place:
            print k

    def changePlace(self,new_place):
        for place in self.place:
            self.place.remove(place)
            self.place.append(new_place)

    def setPriceForEach(self,price):
        return self.expenses.append(price)

    def totalExpeanceCalc(self):
        for k in self.expenses:
            print "Total expenses for ",len(self.invited),"people is",len(self.invited)*k

    def writeInvitationLetter(self,person):
        print "Dear", person, "\n""I am going to be", self.birthdayPerson.age, "on", self.birthdayPerson.birthday,\
            ". I have decided to celebrate my birthday.",\
            "\n""Hope you will be present on my birthday party. See party details bellow.",\
            "\n","Date: ",party1.getDate(),"\n""Hour: ",party1.getHour(),"\n","Place: ",party1.place

    def partyInfo(self):
        print "\n""<Party details>" "\n", "Birthday celebrant: ", \
            self.birthdayPerson.first_name, self.birthdayPerson.last_name,"\n" "Date: ", self.getDate(), \
            "\n","Time: ", self.getHour(),"\n" "Invited people: ", self.invited, "-->",len(self.invited),"people",\
            "\n","Place: ", self.place





member1 = familyMember("Lina", "Gharagyozyan","Daughter",datetime.date(2000,4,1),"+3442424234","N/A","AUA")
member2 = familyMember("Vahe", "Gharagyozyan","Son",datetime.date(2002,4,5),"+343333234","N/A","school33")
member3 = familyMember("Karen", "Gharagyozyan","Father",datetime.date(1988,4,1),"+3442424234","/..","N/A")
member4 = familyMember("Lilit", "Grigoryan","Mother",datetime.date(1988,3,4),"+3442424234","N/A",".")

pet1 = pet("Roma","Dog",3)
#pet1.voice()


family1 = family("Artashisyan","34141414","Gharagyozyan")
family1.addMember(member1)
family1.addMember(member2)
family1.addMember(member3)
family1.addMember(member4)
family1.printInfo()
#member1.getRelationto(member3)

party1 = birthdayParty(member1)
party1.setDate(datetime.date(2018,10,7))
party1.setHoure(datetime.time(18,30))
party1.invite("Erik")
party1.invite("Sarkis")
party1.invite("Iren")


party1.getGuests()
party1.setPriceForEach(30000)
party1.totalExpeanceCalc()

party1.setPartyPlace("Pub 11")
party1.changePlace("El Sky Bar")
party1.partyInfo()
party1.writeInvitationLetter("Erik")
#member1.getStatus()