
# cook your dish here
# Problem URL - https://www.codechef.com/problems/ADVITIYA1

# cook your dish here

ADVITIYA_DATES = [16, 17, 18]

def decideParticipantStatus(date, status=None):
  """Decides the participant visiting date is same as one of the advitiya fest dates

    Args:
      date (int): The visiting date of a participant
      status (:obj:`bool`, optional): Optional parameter
    
    Returns:
      bool: True if the participant visiting date is on the advitiya fest dates otherwise false
      
  """
  if date in ADVITIYA_DATES:
    return True
  else:
    return False

if __name__ == "__main__":
  visitingDate = int(input())
  mehulStatus = decideParticipantStatus(visitingDate)
  if(mehulStatus):
    print("ADVITIYA")
  else:
    print("WAITING FOR ADVITIYA")
  
