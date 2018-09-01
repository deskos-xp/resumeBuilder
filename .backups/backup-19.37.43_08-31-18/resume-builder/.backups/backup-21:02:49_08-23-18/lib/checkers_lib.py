#! /usr/bin/env python3
import ipaddress
import os,sys,string,re
class checkers:
    def __init__(self):
        pass

class checkers_email:
    def __init__(self):
        pass

    def verify_if_address(self,address):
        try:
            ip=ipaddress.ip_address(address)
            return ip.compressed
        except:
            return False

    def verify_domain(self,domain):
        validDomainChar=string.ascii_letters+string.digits+'.-'
        if '.' in domain:
            if domain[0] == '.':
                return domain,False
            if domain[-1] == '.':
                return domain,False
            if domain[0] == '[' and domain[-1] == ']':
                state=self.verify_if_address(domain[1:-1])
                if state == False:
                    return False
            else:
                for char in domain:
                    if char not in validDomainChar:
                        return domain,False
            if domain[0] == '-':
                return domain,False
            if domain[-1] == '-':
                return domain,False
            return domain,True
        else:
            #if this is hit, then the email address
            #provided is a localone, and is basically useless for the resume
            if domain[0] == '[' and domain[-1] == ']':
                state=self.verify_if_address(domain[1:-1])
                if state == False:
                    return False
            else:
                for char in domain:
                    if char not in validDomainChar:
                        return domain,False
            if domain[0] == '-':
                return domain,False
            if domain[-1] == '-':
                return domain,False
            return domain,True
    def comment_check(self,address):
        comments=re.split(r'(\([abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\s]*\))',address)
        comments=[i for i in comments if i != '']
        for seg in comments[1:-1]:
            if ('(' in seg and ')' in seg ) or ( '(' in seg or ')' in seg ):
                return address,False
        return address,True


    def verify_localPart(self,address):
        restricted='(),;:<>@[]\\"'
        validLocalChar=string.ascii_letters+string.digits+"!#$%&'*+_?^_~{}|~."
        if address[0] == '.':
            return address,False
        if address[-1] == '.':
            return address,False

        if address[0] != '"' and address[-1] != '"':
            #unquoted addresses pass through here
            if '..' in address:
                return address,False
            if self.comment_check(address)[1] == True:
                validLocalChar+="()"
            for char in address:
                if char not in validLocalChar:
                    return address,False
        else:
            for num,char in enumerate(address[1:-1]):
                if char not in validLocalChar and char not in restricted:
                    return address,False
            ver3=self.comment_check(address[1:-1])
            if ver3[1] == False:
                return address,False

            for chars in re.split(r'\\"',address[1:-1]):
                if '"' in chars:
                    return address,False

            for chars in re.split(r'\\\\',address[1:-1]):
                if '\\' in chars:
                    return address,False
        #need to match comments, and get their offsets 
        
        return address,True
    def correct_email(self,address):
        if '@' in address:
            address_0=address.split('@')
            if len(address_0) > 2:
                domain=address_0[-1]
                localPart='@'.join(address_0[0:-1])
            else:
                localPart=address_0[0]
                domain=address_0[1]
            ver=self.verify_domain(domain)
            if ver[1] == True:
                verL=self.verify_localPart(localPart)
                if verL[1] == True:
                    print(address,verL,ver)
            else:
                pass
        else:
            print(None)

if __name__ == "__main__":
    addresses=['avalon@mail.com',
            'avalon@.mail.com',
            'ava@ms',
            'ava@ms.com.',
            'ava@0mail.com',
            'ava@-0mail.com',
            'avaloon@0mail.com-',
            'avalon@0mail{}.com',
            'ava@[12.12.12.12]',
            'ava@[mozart.com',
            '"ava..a"@mail.com',
            'ava..a@mail.com',
            'ava{}@mail.com',
            'ava()@mail.com',
            '"ava@"@mail.com',
            "ava\"a@mail.com",
            '"ava""@mail.com',
            '"ava\\\\"@mail.com',
            '"avalon\""@mail.com',
            "(test)mail@mail.com",
            "mail(test)@mail.com",
            'ma(test)il@mail.com',
            '"vitality(test)"@mail.com',
            ]
    c=checkers_email()
    for email in addresses:
        c.correct_email(email)
