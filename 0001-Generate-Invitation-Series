import uuid

class generateInvitationSeries:
    def __init__(self):
        self.list = []

    def generate(self, generate_number):
        for each_uuid in range(generate_number):
            id = str(uuid.uuid1())
            self.list.append(id)
        return True
    """def printLists(self):
        for each_uuid in self.list:
            print each_uuid
        return True"""
    def saveFile(self, str):
        File = open(str, "w")
        list = [line+"\n" for line in self.list]
        File.writelines(list)
        File.close()

#FOLLOWING TESTS
test = generateInvitationSeries()
test.generate(200)
#test.printLists()
test.saveFile("InvitationSeries.txt")
