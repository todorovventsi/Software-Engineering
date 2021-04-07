class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


all_emails = []

email_info = input()
while not email_info == "Stop":
    s, r, c = email_info.split()
    current_email = Email(s, r, c)
    all_emails.append(current_email)

    email_info = input()

send_emails = [int(index) for index in input().split(", ")]

for index in send_emails:
    email = all_emails[index]
    email.send()

for email in all_emails:
    print(email.get_info())
