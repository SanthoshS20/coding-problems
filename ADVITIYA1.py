
# cook your dish here
# Problem URL - https://www.codechef.com/problems/ADVITIYA1

# cook your dish here

# DOC STRING PYTHON
# https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
# https://www.datacamp.com/tutorial/docstrings-python

ADVITIYA_DATES = [16, 17, 18]

def decide_participant_status(date):
  """Decides the participant visiting date is same as one of the advitiya fest dates

    Args:
      date (int): The visiting date of a participant
    
    Returns:
      bool: True if the participant visiting date is on the advitiya fest dates otherwise false
      
  """
  return (date in ADVITIYA_DATES)


if __name__ == "__main__":
  visitingDate = int(input())
  mehulStatus = decide_participant_status(visitingDate)
  if(mehulStatus):
    print("ADVITIYA")
  else:
    print("WAITING FOR ADVITIYA")
  
