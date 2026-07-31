class Member:
    def show_status(self):
        return f"{self.name}: {self.status}"


class PremiumMember(Member):
    pass


member = PremiumMember()
member.name = "Mia"
member.status = "active"
print(member.show_status())
