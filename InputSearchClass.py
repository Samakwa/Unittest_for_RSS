import re



def check_emailAddress(Email_Address):
    ''' Rule: <host name>@<provider name>.<DNS type>  '''
    match = re.search(r'(^\w+\.?\w+)@(\w+\.\w+$)', Email_Address)
    if match:
        '''print "Email Address:", match.group(0),
        print "Host part:", match.group(1),
        print "Domain part:", match.group(2), '''
        return True
    else:
        return False





def check_Name(Name):
    ''' Rule: Starts with [A-Z] the multiple occurrences of [a-z]. '''
    match = re.search(r'^[A-z][a-z]+$', Name)
    if match:
        #print match.group(0),
        return True
    else:
        return False




def check_organisation(organ):

    match = re.search(r'(^[A-Z][a-z]+) ([A-Z][a-z]+)$', organ)
    if match:
        '''print "Organisation:", match.group(0),
        '''
        return True
    else:
        return False


def check_pass1(password1):

    match = re.search(r'(^[A-Z][a-z]+) ([A-Z][a-z]+)$', password1)
    if match:
        #print match.group(0),
        return True
    else:
        return False

def check_pass2(password2):
    ''' Rule: Same with password1  '''
    match = re.search(r'(^[A-Z][a-z]+) ([A-Z][a-z]+)$', password2)
    if match:
        #print match.group(0),
        return True
    else:
        return False



def check_state(state):
    ''' Rule: Short form of states in US.  '''
    match = re.search(r'[A-Z]{2}', state)
    if match:
        #print match.group(0),
        return True
    else:
        return False

def check_county(county):
    ''' Rule: Name of US counties.  '''
    match = re.search(r'^[A-Z][a-z]+) ([A-Z][a-z]+)$', county)
    if match:
        #print match.group(0),
        return True
    else:
        return False
def check_phoneNumber(Contact_Number):

    match = re.search(r'\d{3}-\d{7}', Contact_Number)
    if match:
        #print match.group(0),
        return True
    else:
        return False

