import json

EDUCATION_PROMPT = "prompt"

SKILLS_PROMPT = ""

PREVIOUS_EXPERIENCE_PROMPT = ""

def engineering_prompt(resume, job_description, section):
  """ Produce a prompt for an LLM to generate a resume section that matches the given job description"""
  prompt = "temporary prompt"
  if section == "Education":
    prompt = "Given the following resume: "+ resume + "write an Education section that includes the degree type, B.S., M.S. as well the university the years they attended and the location of that university" 
  elif section == "Skills":
    pass
  elif section == "Professional Experience":
    pass
  elif section == "Projects":
    pass
  # add more sections here

  return prompt # SHOULD BE JSON