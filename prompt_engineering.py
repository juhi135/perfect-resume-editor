import json

EDUCATION_PROMPT = "prompt"

SKILLS_PROMPT = ""

PREVIOUS_EXPERIENCE_PROMPT = ""

def engineering_prompt(resume, job_description, section):
  """ Produce a prompt for an LLM to generate a resume section that matches the given job description"""
  prompt = "temporary prompt"
  if section == "Education":
    pass
  elif section == "Skills":
    pass
  elif section == "Professional Experience":
    pass
  elif section == "Projects":
    pass
  # add more sections here

  return prompt